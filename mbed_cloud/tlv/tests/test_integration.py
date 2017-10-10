import unittest
from mbed_cloud.tlv.tests import test_common
from mbed_cloud.tlv.decode import maybe_decode_payload

from mbed_cloud.connect import ConnectAPI
import time

no_integration_tests = False

@unittest.skipIf(no_integration_tests, 'no integration tests')
class TestIntegration(test_common.BaseCase):
    def test_real_connection(self):
        api = ConnectAPI()
        api.start_notifications()
        devices = api.list_connected_devices().data

        device = devices[0]
        print(device)
        print('')
        path = "/3/0"

        current_value = None
        for i in range(2):

            async_resp = api.get_resource_value_async(device.id, path)
            print(vars(async_resp))

            # Busy wait - block the thread and wait for the response to finish.
            while not async_resp.is_done:
                time.sleep(0.1)

            # Check if we have a async error response, and abort if it is.
            if async_resp.error:
                continue
                raise Exception("Got async error response: %r" % async_resp.error)
            print('result', vars(async_resp))
            break
        else:
            self.fail('didnt get a good async response')

