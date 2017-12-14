import os
import sys
import shlex
import platform
import subprocess
import traceback
import unittest

import requests
from requests.adapters import HTTPAdapter

from tests.common import BaseCase


docker_image = os.environ.get(
    'TESTRUNNER_DOCKER_IMAGE',
    '104059736540.dkr.ecr.us-west-2.amazonaws.com/mbed/sdk-testrunner:master'
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
        try:
            subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            if 'docker login' in e.output:
                raise unittest.SkipTest('missing docker login')
            raise

    def setUp(self):
        exe = sys.executable
        target = os.path.join(os.path.dirname(__file__), 'server.py')
        cmd = [exe, '-m', 'coverage', 'run', target]
        print('running: %s' % cmd)
        self.process = subprocess.Popen(args=cmd, universal_newlines=True)
        if self.process.poll():
            raise Exception('test server failed to start: %s' % self.process.stdout)

        # check the host route from inside the docker container
        cmd = shlex.split(
            'docker run --rm --net=host {image} route'.format(
                image=docker_image
            )
        )
        routes = subprocess.check_output(args=cmd, universal_newlines=True)
        for routing in routes.splitlines():
            if routing.lower().startswith('default'):
                self.host = routing.split()[1]
                break
        if not self.host:
            print('routes table:\n%s' % routes)
            raise Exception('no host address determined')
        if self.host.startswith('ip'):
            self.host = self.host[3:].strip('.').replace('-', '.')

        cmd = """ifconfig lxcbr0 | awk '/inet addr/{split($2,a,":"); print a[2]}'"""
        try:
            address = subprocess.check_output(args=cmd, shell=True, universal_newlines=True)
        except Exception as exception:
            print('didnt see an lxcbr0 interface', exception)
        else:
            if address:
                self.host = address.strip()
        print('determined host address to be: "%s"' % self.host)

        try:
            # ping the server to make sure it's up (don't use _init, may not be idempotent)
            s = requests.Session()
            s.mount('htt', adapter=HTTPAdapter(max_retries=5))
            response = s.get('http://127.0.0.1:5000/invalid_url', timeout=(15, 15))
            # we expect to receive 404, any other failure is bad news (200 OK is unlikely)
            if response.status_code != 404:
                response.raise_for_status()
        except Exception:
            print('could not reach local test server.')
            print(subprocess.check_output(shlex.split('ps -aux')))
            print(subprocess.check_output(shlex.split('netstat -aon')))
            raise
        else:
            print('looks like the server is ok')

    def test_run(self):
        version = 'py%s%s' % platform.python_version_tuple()[:2]  # build a directory that matches tox's {envvar}
        results_dir = os.path.abspath(
            os.getenv('TESTRUNNER_OUTPUT_DIR', os.path.join(os.path.expanduser('~'), 'rpc_results', version))
        )
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        fixtures_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'fixtures')
        )

        cmd = shlex.split(
            'docker run --rm --net=host --name=testrunner_container'
            ' -e "TEST_SERVER_URL=http://{host}:5000"'  # where our SDK server is located
            ' -e "TEST_FIXTURES_DIR={fixtures}"'        # host-relative path to fixtures mountpoint
            ' -v {fixtures}:/runner/test_fixtures'      # configure the fixtures mountpoint
            ' -v {results}:/runner/results'             # configure the results mountpoint
            ' {image}'.format(
                image=docker_image,
                host=self.host,
                fixtures=fixtures_path,
                results=results_dir,
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
        # graceful shutdown
        requests.get('http://localhost:5000/_bye')
        self.process.wait()
