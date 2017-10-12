from mbed_cloud.tests.common import BaseCase
import os
import sys
import shlex
import subprocess


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
        cmd = shlex.split('docker run --rm --net="host" -p 5000:5000 -e "SERVER_URL=http://10.0.75.1:5000" mbed/sdk-testrunner')
        subprocess.call(cmd)

    def tearDown(self):
        if self.process.poll():
            raise subprocess.CalledProcessError('server exited prematurely')
        self.process.kill()
