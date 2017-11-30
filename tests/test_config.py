from mbed_cloud import BaseAPI
from mbed_cloud import connect
from mbed_cloud._backends.mds.apis.endpoints_api import EndpointsApi
from tests.common import BaseCase
import urllib3


class Test(BaseCase):
    def test_config_default(self):
        # check host default from codegen is set to production
        api = EndpointsApi()
        self.assertIn('api.us-east-1', api.api_client.configuration.host)

    def test_config_set_user_config(self):
        # check top-level config setter
        key = 'test_key'
        config = {'api_key': key}
        api = BaseAPI(config)
        self.assertIn(key, api.config.get('api_key'))

    def test_unicode_config(self):
        # host format validation - check trailing slash trimmed
        uft8_host = 'http://\xf0\x9f\x8c\x90.example.com/'
        if hasattr(str, 'decode'):
            # in python2, convert to unicode
            uft8_host = uft8_host.decode('utf8')
        api = BaseAPI(dict(host=uft8_host))
        self.assertEqual('http://\xf0\x9f\x8c\x90.example.com', api.config.get('host'))

    def test_config_invalid_host(self):
        # regression check - give a sane error for invalid hosts
        api = connect.ConnectAPI(dict(host='https://0.0.0.0'))
        with self.assertRaises(urllib3.exceptions.MaxRetryError):
            api.list_connected_devices().data

    def test_config_singleton(self):
        # check two different api configs don't clobber each other
        a = connect.ConnectAPI(dict(api_key='apple'))
        b = connect.ConnectAPI(dict(api_key='banana'))
        api_key = EndpointsApi
        self.assertNotEqual(
            a.apis[api_key].api_client.configuration.api_key,
            b.apis[api_key].api_client.configuration.api_key
        )
