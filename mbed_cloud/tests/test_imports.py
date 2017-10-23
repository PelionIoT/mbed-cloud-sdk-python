from mbed_cloud.tests.common import BaseCase
from mbed_cloud import BaseAPI


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
            api = BaseAPI()
            self.assertEqual(None, config.get('host'))
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

