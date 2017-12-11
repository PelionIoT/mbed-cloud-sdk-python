from tests.common import BaseCase

from mbed_cloud import ConnectAPI


class TestIntegration(BaseCase):
    def test_real_connection(self):
        api = ConnectAPI()
        print('got a connect api')
        api.start_notifications()
        print('listing devices...')
        devices = api.list_connected_devices().data
        print('listed devices')
        for d in devices:
            print(d.bootstrapped_timestamp, d.id)
            # print(vars(d))
        device = devices[0]
        path = "/3/0"
        result = api.get_resource_value(device.id, path)
        self.assertEqual(result['11']['0'], 0)
        self.assertEqual(result['18'], 'dev_hardware_version')
        self.assertEqual(result['17'], 'dev_device_type')
