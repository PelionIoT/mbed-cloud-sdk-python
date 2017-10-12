from mbed_cloud.tests.common import BaseCase
import os
import sys
import shlex
import subprocess
import traceback
import unittest

docker_image = 'mbed/sdk-testrunner:latest'


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
    image = "mbed/sdk-testrunner"

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        exe = sys.executable
        target = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'tests', 'server.py')
        self.process = subprocess.Popen(args=[exe, target])

    def test_run(self):
        results_file = 'file://results/results.html'
        cmd = shlex.split(
            'docker run --rm --net="host"'
            ' -p 5000:5000'
            ' -e "SERVER_URL=http://10.0.75.1:5000"'
            ' -v results:/runner/results'
            ' %s' % docker_image
        )
        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as e:
            if e.returncode > 0:
                # polite re-raise
                self.fail('remote testrunner sequence failed: %s' % results_file)
            raise

    def tearDown(self):
        if self.process.poll():
            raise subprocess.CalledProcessError('server exited prematurely')
        self.process.kill()
