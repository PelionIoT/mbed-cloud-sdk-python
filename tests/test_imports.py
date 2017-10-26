from tests.common import BaseCase
from mbed_cloud import BaseAPI
import urllib3


class TestImports(BaseCase):
    """A simple test for validating coverage"""

    def test_run(self):
        from mbed_cloud import account_management
        from mbed_cloud import certificates
        from mbed_cloud import connect
        from mbed_cloud import device_directory
        from mbed_cloud import update
        from mbed_cloud import _version

    def test_config(self):
        from mbed_cloud import config
        self.assertIn('https', config.get('host'))

    def test_config_insecure(self):
        from mbed_cloud import config
        old = config.get('host')
        try:
            config['host'] = 'http://insecure.invalidhost'
            with self.assertRaises(ValueError):
                BaseAPI()
        finally:
            config['host'] = old

    def test_config_default(self):
        from mbed_cloud import config
        old = config.pop('host')
        try:
            api = BaseAPI()
            self.assertIn('api.us-east-1', config.get('host'))
        finally:
            config['host'] = old

    def test_config_invalid_host(self):
        from mbed_cloud import config
        old = config.pop('host')
        try:
            # an invalid host
            config['host'] = 'https://0.0.0.0'
            from mbed_cloud import connect
            with self.assertRaises(urllib3.exceptions.MaxRetryError):
                connect.ConnectAPI().list_connected_devices().data
        finally:
            config['host'] = old
