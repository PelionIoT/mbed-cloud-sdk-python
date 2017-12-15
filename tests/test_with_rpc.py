import os
import sys
import shlex
import platform
import subprocess
import time
import traceback
import unittest

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

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


def find_host_address_potentials(image):
    potentials = ['127.0.0.1', '']

    # check the host route from inside the docker container
    cmd = shlex.split(
        'docker run --rm --net=host {image} route'.format(
            image=image
        )
    )
    routes = subprocess.check_output(args=cmd, universal_newlines=True)
    for routing in routes.splitlines():
        if routing.lower().startswith('default'):
            host = routing.split()[1]
            if host.startswith('ip'):
                host = host[3:].strip('.').replace('-', '.')
            potentials.append(host)
            # break

    if platform.system().lower() == 'linux':
        cmd = """ifconfig lxcbr0 | awk '/inet addr/{split($2,a,":"); print a[2]}'"""
        try:
            address = subprocess.check_output(args=cmd, shell=True, universal_newlines=True)
            if address:
                potentials.append(address.strip())
        except Exception as exception:
            print('didnt see an lxcbr0 interface:', exception)

    if not potentials:
        raise Exception('did not find any potential addresses inside docker')
    return potentials


def find_test_server_host(image, potentials):
    for potential in potentials:
        cmd = shlex.split(
            'docker run --rm --net=host {image} wget http://{host}:5000/ping'.format(
                image=image,
                host=potential
            )
        )
        try:
            subprocess.check_output(args=cmd, stderr=subprocess.STDOUT, universal_newlines=True)
            break
        except Exception as e:
            print('this address did not work: %s - %s' % (potential, e))
    else:
        raise Exception('Did not find working address inside docker. Potentials: %s' % (potentials,))
    print('determined host to be:', potential)
    return potential


@unittest.skipIf(not have_docker_image(docker_image), 'missing docker image %s' % docker_image)
class TestWithRPC(BaseCase):

    host = None

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
        cmd = [exe, '-u', '-m', 'coverage', 'run', target]
        self.process = subprocess.Popen(args=cmd, universal_newlines=True)
        time.sleep(0.5)
        try:
            # ping the server to make sure it's up
            test_server_local_address = 'http://127.0.0.1:5000'
            url = '%s/ping' % test_server_local_address
            s = requests.Session()
            s.mount(url, adapter=HTTPAdapter(max_retries=Retry(total=20, connect=5, read=15, backoff_factor=0.4)))
            response = s.get(url, timeout=(15, 15))
            response.raise_for_status()
        except Exception as e:
            print('could not reach test server locally: %s\n%s' % (cmd, e))
            print('server status', self.process.poll(), self.process.pid)
            print(subprocess.check_output(shlex.split('ps -aux'), universal_newlines=True))
            print(subprocess.check_output(shlex.split('netstat -aon'), universal_newlines=True))
            raise
        else:
            print('sdk test server is running locally on %s' % (test_server_local_address,))
        self.host = find_test_server_host(docker_image, find_host_address_potentials(docker_image))
        print('rpc testrun ready - host: %r key: ***%s' % (
            os.getenv('MBED_CLOUD_API_HOST', 'default'),
            os.getenv('MBED_CLOUD_API_KEY', 'default')[-7:]
        ))

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
            subprocess.check_output(cmd, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            if e.returncode > 0:
                # polite re-raise
                self.fail('remote testrunner sequence failed. results should be at: %s' % results_dir)
            raise

    def tearDown(self):
        # graceful shutdown
        requests.get('http://localhost:5000/_bye')
        self.process.wait()
