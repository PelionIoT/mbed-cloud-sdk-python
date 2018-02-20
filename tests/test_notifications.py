import mock

from tests.common import BaseCase
from mbed_cloud import ConnectAPI
from mbed_cloud.exceptions import CloudUnhandledError


class Test(BaseCase):
    def test_autostart_enabled(self):
        with mock.patch('mbed_cloud._backends.mds.apis.device_requests_api.DeviceRequestsApi.v2_device_requests_device_idasync_idasync_id_post') as mk:
            a = ConnectAPI(dict(autostart_notification_thread=True))
            self.assertFalse(a.has_active_notification_thread)
            a.get_resource_value_async('abc123', '/3/4/5')
            self.assertTrue(a.has_active_notification_thread)

    def test_autostart_disabled(self):
        with mock.patch('mbed_cloud._backends.mds.apis.device_requests_api.DeviceRequestsApi.v2_device_requests_device_idasync_idasync_id_post') as mk:
            a = ConnectAPI(dict(autostart_notification_thread=False))
            self.assertFalse(a.has_active_notification_thread)
            with self.assertRaises(CloudUnhandledError) as e:
                a.get_resource_value_async('abc123', '/3/4/5')
            self.assertFalse(a.has_active_notification_thread)
            self.assertIn('notifications thread', str(e.exception))
