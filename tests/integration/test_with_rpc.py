import os
import sys
import shlex
import platform
import subprocess
import time
import traceback
import unittest

from threading import Timer

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from tests.common import BaseCase

from mbed_cloud.configuration import Config


docker_image = os.environ.get(
    'TESTRUNNER_DOCKER_IMAGE',
    '104059736540.dkr.ecr.us-west-2.amazonaws.com/mbed/sdk-testrunner:master'
)


def timeout_check_output(timeout=5, process=None, _or_fail=True, *args, **kwargs):
    process = process or subprocess.Popen(
        *args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        **kwargs
    )

    stdout = '<no output collected>'
    now = time.time()

    def killer():
        # called by timer thread to terminate process
        process.timed_out = time.time() - now
        process.kill()

    timer = Timer(timeout, killer)
    timer.start()
    try:
        stdout, stderr = process.communicate()
    finally:
        timer.cancel()
    status_code = process.poll()
    if _or_fail and status_code != 0:
        timed_out = getattr(process, 'timed_out', '')
        raise subprocess.CalledProcessError(
            status_code,
            (timed_out and '<TIMED OUT (%.2fs)>\'' % timed_out) + str(kwargs.get('args', args)),
            output=stdout
        )
    return stdout


def have_docker_image(image):
    cmd = 'docker images -q %s' % image
    try:
        output = timeout_check_output(args=shlex.split(cmd))
    except (subprocess.CalledProcessError, OSError):
        traceback.print_exc()
        return False
    return bool(output)


def find_host_address_potentials(image):
    potentials = ['127.0.0.1', '', '10.0.75.1']

    # check the host route from inside the docker container
    cmd = shlex.split(
        'docker run --rm --net=host {image} route'.format(
            image=image
        )
    )
    # routes = subprocess.check_output(args=cmd, universal_newlines=True)
    routes = timeout_check_output(args=cmd)
    for routing in routes.splitlines():
        if routing.lower().startswith('default'):
            host = routing.split()[1]
            if host.startswith('ip'):
                host = host[3:].strip('.').replace('-', '.')
            potentials.append(host)

    if platform.system().lower() == 'linux':
        cmd = """ifconfig lxcbr0 | awk '/inet addr/{split($2,a,":"); print a[2]}'"""
        try:
            address = timeout_check_output(args=cmd, shell=True)
            if address:
                potentials.append(address.strip())
        except Exception as exception:
            print('didnt see an lxcbr0 interface:', exception)

    if not potentials:
        raise Exception('did not find any potential addresses inside docker')
    return list(reversed(sorted(potentials)))


def find_test_server_host(image, potentials):
    for potential in potentials:
        cmd = shlex.split(
            'docker run --rm --net=host {image} wget -T 2 -t 3 http://{host}:5000/ping'.format(
                image=image,
                host=potential
            )
        )
        try:
            print('checking for sdk server at: %r' % (potential,))
            timeout_check_output(args=cmd)
            break
        except Exception as e:
            print('this address did not work: %r - %s' % (potential, e))
    else:
        raise Exception('Did not find working address inside docker. Potentials: %s' % (potentials,))
    return potential


def new_server_process(coverage=True):
    exe = sys.executable
    target = os.path.join(os.path.dirname(__file__), 'server.py')
    cmd = [exe, '-u']
    if coverage:
        cmd.extend(['-m', 'coverage', 'run'])
    cmd.append(target)
    process = subprocess.Popen(args=cmd, universal_newlines=True)
    try:
        # ping the server to make sure it's up
        test_server_local_address = 'http://127.0.0.1:5000'
        url = '%s/ping' % test_server_local_address
        s = requests.Session()
        s.mount(url, adapter=HTTPAdapter(max_retries=Retry(total=20, connect=5, read=15, backoff_factor=0.5)))
        response = s.get(url, timeout=(15, 15))
        response.raise_for_status()
    except Exception as e:
        print('could not reach test server locally: %s\n%s' % (cmd, e))
        print('server status', process.poll(), process.pid)
        print(timeout_check_output(args=shlex.split('ps -aux')))
        print(timeout_check_output(args=shlex.split('netstat -aon')))
        raise
    else:
        print('SDK test server is running locally on %s' % (test_server_local_address,))
    return process


@unittest.skipIf(not have_docker_image(docker_image), 'missing docker image %s' % docker_image)
class TestWithRPC(BaseCase):

    host = None
    process = None

    @classmethod
    def setUpClass(cls):
        cmd = 'docker pull %s' % docker_image
        try:
            timeout_check_output(timeout=120, args=shlex.split(cmd))
        except subprocess.CalledProcessError as e:
            if 'docker login' in e.output:
                raise unittest.SkipTest('missing docker login')
            raise

    def setUp(self):
        self.process = new_server_process()
        self.host = find_test_server_host(docker_image, find_host_address_potentials(docker_image))
        config = Config()
        print("RPC test ready:\n\tserver: %s\n\tcloud host: %r\n\tapi key: '***%s'\n\timage: %s" % (
            self.host,
            config.get('host', 'default'),
            config.get('api_key', 'default')[-5:],
            docker_image,
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
            print(timeout_check_output(timeout=600, args=cmd, _or_fail=True))
        except subprocess.CalledProcessError:
            self.fail('remote testrunner sequence failed. results should be at: %s' % results_dir)

    def tearDown(self):
        # graceful shutdown
        requests.post('http://localhost:5000/shutdown')
        timeout_check_output(process=self.process)
