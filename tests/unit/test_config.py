from mbed_cloud.core import BaseAPI
from mbed_cloud.configuration import Config
from mbed_cloud import ConnectAPI
from mbed_cloud._backends.mds.apis.endpoints_api import EndpointsApi
from tests.common import BaseCase

import json
import tempfile
import os
import shutil
import urllib3


class TestConfigObj(BaseCase):
    def test_config_default_codegen(self):
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
        api = ConnectAPI(dict(host='https://0.0.0.0'))
        with self.assertRaises(urllib3.exceptions.MaxRetryError):
            api.list_connected_devices().next()

    def test_config_singleton(self):
        # check two different api configs don't clobber each other
        a = ConnectAPI(dict(api_key='apple'))
        b = ConnectAPI(dict(api_key='banana'))
        api_key = EndpointsApi
        self.assertEqual(a.apis[api_key].api_client.configuration.api_key, {'Authorization': 'apple'})
        self.assertEqual(b.apis[api_key].api_client.configuration.api_key, {'Authorization': 'banana'})


class TestConfigSources(BaseCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists('.mbed_cloud_config.json'):
            os.rename('.mbed_cloud_config.json', '.mbed_cloud_config.jsonx')
        cls.dummy_key = 'dummy-api-key'

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('.mbed_cloud_config.jsonx'):
            os.rename('.mbed_cloud_config.jsonx', '.mbed_cloud_config.json')

    def test_no_config_default(self):
        a = ConnectAPI(dict(api_key=self.dummy_key))
        self.assertIn('api.us-east-1', a.apis[EndpointsApi].api_client.configuration.host)

    def test_config_env(self):
        try:
            temp_dir = tempfile.mkdtemp(prefix='mbed_sdk_test')
            temp_path = temp_dir + 'conf.json'
            with open(temp_path, 'w') as fh:
                json.dump(dict(api_key=self.dummy_key, host='https://dummy_host_url'), fh)
            os.environ['MBED_CLOUD_SDK_CONFIG'] = temp_path
            c = Config()
            self.assertEqual(self.dummy_key, c.get('api_key'))
            self.assertIn('dummy_host_url', c['host'])
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
            os.environ.pop('MBED_CLOUD_SDK_CONFIG', None)
