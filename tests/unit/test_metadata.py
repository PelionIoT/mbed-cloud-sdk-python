from tests.common import BaseCase
from mbed_cloud.device_directory import DeviceDirectoryAPI
from mbed_cloud.core import ApiMetadata

import mock


class TestFilters(BaseCase):
    """Check filters"""

    @classmethod
    def setUpClass(cls):
        cls.api = DeviceDirectoryAPI()
        with mock.patch('urllib3.PoolManager.request') as mocked:
            mocked.return_value = mock.MagicMock()
            mocked.return_value.status = 200
            mocked.return_value.data = '{"data":[{"a":1}]}'.encode()
            cls.devices = cls.api.list_devices(filter=dict(state='registered')).next()

    def test_meta(self):
        # exercise all the getters for metadata objects
        meta = self.api.get_last_api_metadata()
        props = (
            'url',
            'method',
            'status_code',
            'date',
            'headers',
            'request_id',
            'error_message',
        )
        parts = {prop: getattr(meta, prop, None) for prop in props}
        self.assertEqual(parts['method'], 'GET')
        self.assertIn('200', repr(meta))
        as_dict = meta.to_dict()
        for prop in props:
            self.assertIn(prop, as_dict)

    def test_meta_exception(self):
        # check what happens if an exception is passed to the metadata object
        msg = 'just a test'
        exception = Exception(msg)
        exception.status = 5
        exception.body = 'the body'
        meta = ApiMetadata('http://not.real', 'GET', exception=exception)
        self.assertEqual(meta.error_message, msg)

