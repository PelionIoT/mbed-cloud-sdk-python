import os
import sys
import shlex
import platform
import subprocess
import traceback
import unittest

import requests

from mbed_cloud.tests.common import BaseCase

docker_image = os.environ.get(
    'TESTRUNNER_DOCKER_IMAGE',
    '104059736540.dkr.ecr.us-west-2.amazonaws.com/mbed/sdk-testrunner'
)


def have_docker_image(image):
    cmd = 'docker images -q %s' % image
    try:
        output = subprocess.check_output(shlex.split(cmd))
    except subprocess.CalledProcessError as e:
        traceback.print_exc()
        return False
    return bool(output)


@unittest.skipIf(not have_docker_image(docker_image), 'missing docker image %s' % docker_image)
class TestWithRPC(BaseCase):

    @classmethod
    def setUpClass(cls):
        cmd = 'docker pull %s' % docker_image
        subprocess.check_call(shlex.split(cmd))

    def setUp(self):
        exe = sys.executable
        target = os.path.join(os.path.dirname(__file__), 'server.py')
        self.process = subprocess.Popen(args=[exe, target], universal_newlines=True)
        if self.process.poll():
            raise Exception('test server failed to start: %s' % self.process.stdout)

        # check the host route from inside the docker container
        routes = subprocess.check_output('docker run --rm --net=host {image} route'.format(
            image=docker_image
        ))
        for routing in routes.splitlines():
            if routing.lower().startswith('default'):
                self.host = routing.split()[1]
                break
        if not self.host:
            raise Exception('no host address determined')

        try:
            # ping the server to make sure it's up
            response = requests.get('http://127.0.0.1:5000/_init')
            response.raise_for_status()
        except Exception as exception:
            print('welp, couldnt get the server on 127.0.0.1, maybe docker will have better luck. %s' % exception)

    def test_run(self):
        # this is in lieu of having a docker-compose...
        version = platform.python_version()
        results_file = os.path.join(os.path.expanduser('~'), 'rpc_results', version)

        cmd = shlex.split(
            'docker run --rm --net=host --name=testrunner_container'
            ' -e "TEST_SERVER_URL=http://{host}:5000"'  # where our SDK server is located
            ' -e "TEST_FIXTURES_DIR=fixtures"'          # host-relative path to fixtures mountpoint
            ' -v {fixtures}:/runner/test_fixtures'      # configure the fixtures mountpoint
            ' -v {results}:/runner/results'             # configure the results mountpoint
            ' {image}'.format(
                image=docker_image,
                host=self.host,
                fixtures=os.path.join(os.path.dirname(__file__), 'fixtures'),
                results=results_file,
            )
        )
        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as e:
            if e.returncode > 0:
                # polite re-raise
                self.fail('remote testrunner sequence failed. results should be at: %s' % results_file)
            raise
        finally:
            subprocess.Popen('docker kill testrunner_container')

    def tearDown(self):
        if self.process.poll():
            raise Exception('test server has exited prematurely')
        self.process.kill()
