from mbed_cloud import BaseAPI
from mbed_cloud import config
from mbed_cloud import connect
from tests.common import BaseCase
import urllib3
import imp


class TestImports(BaseCase):
    """A simple test for validating coverage"""

    def test_run(self):
        from mbed_cloud import account_management
        from mbed_cloud import certificates
        from mbed_cloud import connect
        from mbed_cloud import device_directory
        from mbed_cloud import update
        from mbed_cloud import _version


class TestConfig(BaseCase):

    def test_base_config(self):
        self.assertIn('https', config.get('host'))

    def test_config_insecure(self):
        with self.assertRaises(ValueError):
            BaseAPI(dict(host='http://insecure.invalidhost'))

    def test_config_default(self):
        default_host = config.pop('host')
        try:
            api = BaseAPI()
            self.assertIn('api.us-east-1', api.config.get('host'))
        finally:
            config['host'] = default_host

    def test_config_invalid_host(self):
        default_host = config.get('host')
        try:
            api = connect.ConnectAPI(dict(host='https://0.0.0.0'))
            with self.assertRaises(urllib3.exceptions.MaxRetryError):
                api.list_connected_devices().data
        finally:
            # reset the mds configuration singleton x_x
            # FIXME!!!
            imp.reload(connect)
            from mbed_cloud._backends.mds.configuration import Configuration
            c = Configuration()
            c.host = default_host
            api.apis[:] = []
