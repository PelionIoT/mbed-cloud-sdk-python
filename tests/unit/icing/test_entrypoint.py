from tests.common import BaseCase


class Test(BaseCase):
    def test_getting_started(self):
        # an example: subscribing to device state changes
        from mbed_cloud import MbedCloud
        from mbed_cloud import channels
        api_key = 'abcd1234'
        # cloak
        api_key = None
        # uncloak
        mbed = MbedCloud(api_key=api_key)
        # cloak
        with self.assertRaises(TimeoutError):
            # uncloak
            print(mbed.subscribe(channels.DeviceStateChanges()).next().block(timeout=0.1))
        # end of example
