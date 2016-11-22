import unittest, mock
from mbed_cloud_sdk.devices.connector import ConnectorAPI

class TestConnector(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestConnector, self).__init__(*args, **kwargs)
        self.api = ConnectorAPI()

    @mock.patch('mbed_cloud_sdk._backends.mds.EndpointsApi.v2_endpoints_get')
    def test_list_endpoints(self, c):
        self.api.list_endpoints()
        c.assert_called_once_with()

    @mock.patch('mbed_cloud_sdk._backends.mds.SubscriptionsApi.v2_subscriptions_put')
    def test_pre_subscribe(self, c):
        self.api.pre_subscribe('endpoint_foo', '/some/path')
        c.assert_called_once_with(mock.ANY)

if __name__ == '__main__':
    unittest.main()
