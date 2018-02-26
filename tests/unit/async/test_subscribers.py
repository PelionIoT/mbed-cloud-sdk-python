from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud.subscribe import channels

from tests.common import BaseCase
import logging

logging.basicConfig(level=logging.DEBUG)


class Test(BaseCase):
    def test_subscribe(self):
        subs = SubscriptionsManager(None)
        observer_a = subs.subscribe(channels.DeviceStateChanges(device_id='A'))
        observer_b = subs.subscribe(channels.DeviceStateChanges(device_id='B'))
        observer_c = subs.subscribe(channels.DeviceStateChanges())

        self.assertIsNot(observer_a, observer_b)
        self.assertIsNot(observer_b, observer_c)

        future_a = observer_a.next().defer()
        future_b = observer_b.next().defer()
        future_c = observer_c.next().defer()

        self.assertIsNot(future_a, future_b)
        self.assertIsNot(future_b, future_c)

        subs.notify({
            channels._API_CHANNELS.reg_updates: [
                dict(a=1, b=2, device_id='A')
            ]
        })
        result = future_a.get(timeout=2)
        self.assertDictContainsSubset(dict(a=1, b=2), result)

        self.assertFalse(future_b.ready())

        self.assertTrue(future_c.ready())
        result = future_c.get()
        self.assertEqual(result, dict(a=1, b=2))
