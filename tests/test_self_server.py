import subprocess
import os
import requests
from tests.common import BaseCase


class Test(BaseCase):

    def setUp(self):
        server_path = os.path.join(self._project_root_dir, 'tests')
        self.server = subprocess.Popen(
            ['python', 'server2.py'], cwd=server_path, stderr=subprocess.STDOUT
        )

    def test(self):
        server_addr = 'http://127.0.0.1:5000'

        self.assertIsNone(self.server.poll())

        self.assertEqual(requests.get(server_addr + '/ping').text, 'pong')

        self.assertEqual(requests.get(server_addr).json(), [
            'AccountManagementAPI',
            'DeviceDirectoryAPI',
            'UpdateAPI',
            'test_stub',
            'CertificatesAPI',
            'ConnectAPI'
        ])

        response = requests.post(server_addr + '/test_stub', json=dict(more=0))
        response.raise_for_status()
        idee = response.text
        self.assertTrue(idee)

        response = requests.get(server_addr + '/test_stub')
        response.raise_for_status()
        self.assertEqual(response.json()[0], idee)

        response = requests.get(server_addr + '/test_stub/%s' % idee)
        response.raise_for_status()
        result = response.json()
        self.assertIn('success', result)
        self.assertIn('exception', result)
        self.assertIn('api_name', result)

        response = requests.post(server_addr + '/test_stub/%s/success' % idee, json=dict(extra=1))
        response.raise_for_status()
        self.assertEquals(response.json(), dict(more=0, extra=1, success=True))

        response = requests.post(server_addr + '/test_stub/%s/exception' % idee)
        with self.assertRaises(requests.HTTPError):
            response.raise_for_status()
        result = response.json()
        self.assertEquals(result.get('message'), 'just a test')
        self.assertIn('traceback', result)

        response = requests.get(server_addr + '/in/val/id/_url')
        self.assertEqual(404, response.status_code)

        response = requests.post(server_addr + '/test_stub/%s/invalid_method' % idee)
        with self.assertRaises(requests.HTTPError):
            response.raise_for_status()
        self.assertIn('no such method', response.json().get('message').lower())

        response = requests.post(server_addr + '/test_stub/invalid_id/invalid_method')
        print(response.text)
        with self.assertRaises(requests.HTTPError):
            response.raise_for_status()
        self.assertIn('no such instance', response.json().get('message').lower())

        response = requests.delete(server_addr + '/test_stub/%s' % idee)
        response.raise_for_status()
        self.assertEqual(response.json(), True)

        response = requests.get(server_addr + '/test_stub/%s' % idee)
        self.assertEqual(404, response.status_code)

    def tearDown(self):
        self.server.kill()
