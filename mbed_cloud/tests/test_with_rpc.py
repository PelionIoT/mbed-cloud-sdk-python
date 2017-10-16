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
        cmd = [exe, target]
        print('running: %s' % cmd)
        self.process = subprocess.Popen(args=cmd, universal_newlines=True)
        if self.process.poll():
            raise Exception('test server failed to start: %s' % self.process.stdout)

        # check the host route from inside the docker container
        cmd=shlex.split(
            'docker run --rm --net=host {image} route'.format(
                image=docker_image
            )
        )
        routes = subprocess.check_output(cmd)
        print('routes table:\n%s' % routes)
        for routing in routes.splitlines():
            if routing.lower().startswith('default'):
                self.host = routing.split()[1]
                break
        if not self.host:
            raise Exception('no host address determined')
        if self.host.startswith('ip'):
            self.host = self.host[3:].strip('.').replace('-', '.')

        cmd = """ifconfig lxcbr0 | awk '/inet addr/{split($2,a,":"); print a[2]}'"""
        try:
            address = subprocess.check_output(args=cmd, shell=True)
        except Exception as exception:
            print('didnt see an lxcbr0 interface', exception)
        else:
            if address:
                self.host = address
        print('determined host address to be: "%s"' % self.host)

        try:
            # ping the server to make sure it's up
            response = requests.get('http://127.0.0.1:5000/_init')
            response.raise_for_status()
        except Exception as exception:
            print('welp, couldnt get the server on 127.0.0.1, maybe docker will have better luck. %s' % exception)
            print(subprocess.check_output(shlex.split('ps -aux')))
            print(subprocess.check_output(shlex.split('netstat -aon')))
            raise
        else:
            print('looks like the server is ok')

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

    def tearDown(self):
        if self.process.poll():
            raise Exception('test server has exited prematurely')
        self.process.kill()
