import mbed_cloud
from mbed_cloud.core import BaseAPI
from mbed_cloud import utils
from mbed_cloud.configuration import Config
from mbed_cloud import configuration
from mbed_cloud import ConnectAPI
from mbed_cloud._backends.mds.apis.endpoints_api import EndpointsApi
from tests.common import BaseCase


import json
import logging
import mock
import os
import queue
import shutil
import tempfile

from logging import Handler


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
        api = ConnectAPI(dict(api_key='fake_key', host='invalid'))
        with mock.patch('urllib3.PoolManager.request') as mocked:
            mocked.side_effect = RuntimeError
            with self.assertRaises(RuntimeError):
                api.list_connected_devices().next()

    def test_config_singleton(self):
        # check two different api configs don't clobber each other
        a = ConnectAPI(dict(api_key='apple'))
        b = ConnectAPI(dict(api_key='banana'))
        api_key = EndpointsApi
        self.assertEqual(a.apis[api_key].api_client.configuration.api_key, {'Authorization': 'apple'})
        self.assertEqual(b.apis[api_key].api_client.configuration.api_key, {'Authorization': 'banana'})

    def test_logging(self):
        q = queue.Queue()

        class FakeLogHandler(Handler):
            def emit(self, record):
                q.put(record)

        top_logger = logging.getLogger(mbed_cloud.__name__)
        logging.getLogger('mbed_cloud.utils').addHandler(FakeLogHandler(level=logging.DEBUG))

        top_logger.setLevel(level=logging.INFO)  # enables >'INFO' (but our config should have got there first anyway)
        utils.logging_check()  # this iterates all log levels, and should include up to 'INFO'
        levels_seen = {log.levelname for log in list(q.queue)}
        self.assertIn('INFO', levels_seen)
        self.assertNotIn('DEBUG', levels_seen)

        q.queue.clear()
        top_logger.setLevel(level=logging.DEBUG)  # explicitly enable >'DEBUG' at top level
        utils.logging_check()  # this iterates all log levels, and should now include up to 'DEBUG'
        levels_seen = {log.levelname for log in list(q.queue)}
        self.assertIn('INFO', levels_seen)  # check that module-level log config has cascaded
        self.assertIn('DEBUG', levels_seen)  # check that module-level log config has cascaded


class TempConf(object):
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        self.temp_dir = tempfile.mkdtemp(prefix='mbed_sdk_test')
        temp_path = self.temp_dir + 'conf.json'
        with open(temp_path, 'w') as fh:
            json.dump(self.data, fh)
        os.environ['MBED_CLOUD_SDK_CONFIG'] = temp_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        os.environ.pop('MBED_CLOUD_SDK_CONFIG', None)


class TestConfigSources(BaseCase):
    dummy_key = 'ak_1234567'
    dummy_host = 'https://dummy_host_url'

    def setUp(self):
        self.host = os.environ.pop(configuration.ENVVAR_API_HOST, '')
        self.key = os.environ.pop(configuration.ENVVAR_API_KEY, '')

    def tearDown(self):
        os.environ.setdefault(configuration.ENVVAR_API_HOST, self.host)
        os.environ.setdefault(configuration.ENVVAR_API_KEY, self.key)

    def test_no_config_file_default(self):
        with TempConf(dict(api_key=self.dummy_key)):
            # when we get a config object, force it not to look at existing paths (to see what it defaults to)
            with mock.patch.object(Config, attribute='paths') as mocked:
                mocked.return_value = [os.environ.get("MBED_CLOUD_SDK_CONFIG")]
                a = ConnectAPI(dict(api_key=self.dummy_key))
            self.assertIn('api.us-east-1', a.apis[EndpointsApi].api_client.configuration.host)

    def test_config_file_from_env(self):
        # fully define a config at a custom location, and verify it is loaded
        with TempConf(dict(api_key=self.dummy_key, host=self.dummy_host)):
            c = Config()
            self.assertEqual(self.dummy_key, c.get('api_key'))
            self.assertIn('dummy_host_url', c['host'])

            # verify custom config reaches the internal api
            a = ConnectAPI()
            self.assertIn(self.dummy_key, str(a.apis[EndpointsApi].api_client.configuration.api_key))

    def test_config_from_envvar(self):
        # fully define a config at a custom location
        # as well as setting config through environment
        with TempConf(dict(api_key='not this one', host=self.dummy_host)):
            os.environ.setdefault(configuration.ENVVAR_API_KEY, self.dummy_key)

            c = Config()
            self.assertEqual(self.dummy_key, c.get('api_key'))
            self.assertIn('dummy_host_url', c['host'])

            # verify custom config reaches the internal api
            a = ConnectAPI()
            self.assertIn(self.dummy_key, str(a.apis[EndpointsApi].api_client.configuration.api_key))
