from tests.common import BaseCase
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
        api = BaseAPI()
        self.assertIn('https', api.config.get('host'))

    def test_config_set_user_config(self):
        key = 'test_key'
        config = {'api_key': key}
        api = BaseAPI(config)
        self.assertIn(key, api.config.get('api_key'))

