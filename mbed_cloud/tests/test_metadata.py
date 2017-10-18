from mbed_cloud.tests.common import BaseCase
from mbed_cloud.device_directory import DeviceDirectoryAPI


class TestFilters(BaseCase):
    """Check filters"""

    @classmethod
    def setUpClass(cls):
        cls.api = DeviceDirectoryAPI()
        cls.api.list_devices(filter=dict(connected=True))

    def test_meta(self):
        meta = self.api.get_last_api_metadata()
        props = (
            'url',
            'method',
            'status_code',
            'date',
            'headers',
            'request_id',
            'object',
            'etag',
            'error_message',
        )
        # exercise all the getters
        parts = {prop: getattr(meta, prop) for prop in props}
        self.assertEqual(parts['method'], 'GET')
        self.assertEqual(parts['object'], 'list')
        as_dict = meta.to_dict()
        for prop in props:
            self.assertIn(prop, as_dict)
