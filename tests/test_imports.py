from mbed_cloud import BaseAPI
from mbed_cloud import config
from mbed_cloud import connect
from tests.common import BaseCase
import multiprocessing
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
        ok = multiprocessing.Event()
        p = multiprocessing.Process(target=execute_connect, args=(ok,))
        p.start()
        p.join()
        self.assertTrue(ok.is_set())


def execute_connect(completion_event):
    # FIXME: this is suboptimal but necessary due to
    # use of singletons and other oddities by the codegen SDK backend
    # i.e. you cannot change api host in a single process
    api = connect.ConnectAPI(dict(host='https://0.0.0.0'))
    try:
        api.list_connected_devices().data
    except urllib3.exceptions.MaxRetryError:
        completion_event.set()
