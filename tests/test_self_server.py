import subprocess
import os
import requests
import time
from tests.common import BaseCase

server_addr = 'http://127.0.0.1:5000'


class Test(BaseCase):
    server = None
    instance = []

    @classmethod
    def setUpClass(cls):
        server_path = os.path.join('tests', 'server.py')
        cls.server = subprocess.Popen(
            ['python', server_path], cwd=cls._project_root_dir, stderr=subprocess.STDOUT
        )

    @property
    def idee(self):
        return self.instance[0]

    def test_ping_pong(self):
        self.assertIsNone(self.server.poll())
        self.assertEqual(requests.get(server_addr + '/ping', timeout=(15, 15)).json(), 'pong')

    def test_shutdown(self):
        response = requests.post(server_addr + '/shutdown')
        response.raise_for_status()
        for _ in range(50):
            time.sleep(0.02)
            result = self.server.poll()
            if result is not None:
                break
        self.assertEqual(result, 0)

    @classmethod
    def tearDownClass(cls):
        cls.server.kill()
