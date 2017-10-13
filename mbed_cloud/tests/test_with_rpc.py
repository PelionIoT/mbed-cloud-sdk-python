import os
import sys
import shlex
import platform
import subprocess
import traceback
import unittest

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
        self.process = subprocess.Popen(args=[exe, target])

    def test_run(self):
        # this is in lieu of having a docker-compose...
        results_file = 'file://results/results.html'
        version = platform.python_version()
        cmd = shlex.split(
            'docker run --rm --net="host"'
            ' -p 5000:5000'
            ' -e "TEST_SERVER_URL=http://10.0.75.1:5000"'
            ' -e "TEST_FIXTURES_DIR=fixtures"'
            ' -v {fixtures}:/runner/test_fixtures'
            ' -v {results}:/runner/results'
            ' {images}'.format(
                images=docker_image,
                fixtures=os.path.join(os.path.dirname(__file__), 'fixtures'),
                results=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'results', version),
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
            raise subprocess.CalledProcessError('server exited prematurely')
        self.process.kill()
