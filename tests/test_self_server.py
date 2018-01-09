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
        server_path = os.path.join('tests', 'server2.py')
        cls.server = subprocess.Popen(
            ['python', server_path], cwd=cls._project_root_dir, stderr=subprocess.STDOUT
        )

    @property
    def idee(self):
        return self.instance[0]

    def test_a(self):
        # ping server
        self.assertIsNone(self.server.poll())

        self.assertEqual(requests.get(server_addr + '/ping').json(), 'pong')

    def test_a2(self):
        # list methods
        self.assertEqual(requests.get(server_addr).json(), [
            'AccountManagementAPI',
            'DeviceDirectoryAPI',
            'UpdateAPI',
            'test_stub',
            'CertificatesAPI',
            'ConnectAPI'
        ])

    def test_b(self):
        # create an instance
        response = requests.post(server_addr + '/test_stub', json=dict(more=0))
        response.raise_for_status()
        self.instance.append(response.json())
        self.assertTrue(self.idee)

    def test_c(self):
        # read instance list
        response = requests.get(server_addr + '/test_stub')
        response.raise_for_status()
        self.assertEqual(response.json()[0], self.idee)

    def test_d(self):
        # read instance
        response = requests.get(server_addr + '/test_stub/%s' % self.idee)
        response.raise_for_status()
        result = response.json()
        self.assertIn('success', result)
        self.assertIn('exception', result)
        self.assertIn('api_name', result)

    def test_e(self):
        # call a method
        response = requests.post(server_addr + '/test_stub/%s/success' % self.idee, json=dict(extra=1))
        response.raise_for_status()
        self.assertEquals(response.json(), dict(more=0, extra=1, success=True))

    def test_f(self):
        # call a failing method
        response = requests.post(server_addr + '/test_stub/%s/exception' % self.idee)
        with self.assertRaises(requests.HTTPError):
            response.raise_for_status()
        result = response.json()
        self.assertEquals(result.get('message'), 'just a test')
        self.assertIn('traceback', result)

    def test_g(self):
        # invalid url
        response = requests.get(server_addr + '/in/val/id/_url')
        self.assertEqual(404, response.status_code)

    def test_h(self):
        # invalid method
        response = requests.post(server_addr + '/test_stub/%s/invalid_method' % self.idee)
        with self.assertRaises(requests.HTTPError):
            response.raise_for_status()
        self.assertIn('no such method', response.json().get('message').lower())

    def test_i(self):
        # invalid instance
        response = requests.post(server_addr + '/test_stub/invalid_id/invalid_method')
        print(response.text)
        with self.assertRaises(requests.HTTPError):
            response.raise_for_status()
        self.assertIn('no such instance', response.json().get('message').lower())

    def test_j(self):
        # delete instance
        response = requests.delete(server_addr + '/test_stub/%s' % self.idee)
        response.raise_for_status()
        self.assertEqual(response.json(), True)

        response = requests.get(server_addr + '/test_stub/%s' % self.idee)
        self.assertEqual(404, response.status_code)

    def test_k(self):
        response = requests.put(server_addr + '/shutdown')
        response.raise_for_status()
        for i in range(10):
            time.sleep(0.01)
            result = self.server.poll()
            if result is not None:
                break
        self.assertEqual(result, 0)

    @classmethod
    def tearDownClass(cls):
        cls.server.kill()
