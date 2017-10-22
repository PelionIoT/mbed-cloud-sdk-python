import pytest
from mbed_cloud.tlv.tests import test_common

from mbed_cloud.connect import ConnectAPI


@pytest.mark.integration
class TestIntegration(test_common.BaseCase):
    def test_real_connection(self):
        api = ConnectAPI()
        api.start_notifications()
        devices = api.list_connected_devices().data
        device = devices[0]
        print(device)
        path = "/3/0"
        result = api.get_resource_value(device.id, path)
        self.assertEqual(result['11']['0'], 0)
        self.assertEqual(result['18'], 'dev_hardware_version')
        self.assertEqual(result['17'], 'dev_device_type')
