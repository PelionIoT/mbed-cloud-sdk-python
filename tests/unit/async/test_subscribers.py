from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud.subscribe import channels

from tests.common import BaseCase

import mock
import os
import time
import unittest


class Test(BaseCase):
    def test_subscribe(self):
        subs = SubscriptionsManager(mock.MagicMock())
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

        # a valid, but irrelevant channel
        subs.notify({
            channels.ChannelIdentifiers.async_responses: [
                dict(a=1, b=2, device_id='A')
            ]
        })
        time.sleep(0.01)
        self.assertFalse(future_a.ready())
        self.assertFalse(future_b.ready())
        self.assertFalse(future_c.ready())

        # a valid channel, relevant for DeviceState
        subs.notify({
            channels.ChannelIdentifiers.reg_updates: [
                dict(a=1, b=2, device_id='A')
            ]
        })

        result = future_a.get(timeout=2)
        self.assertDictContainsSubset(dict(a=1, b=2), result)

        self.assertFalse(future_b.ready())

        # possible race condition, so an unreliable check.
        # just because one observer (`a`) is ready, does not mean another (`c`) is.
        # self.assertTrue(future_c.ready())
        result = future_c.get()
        self.assertDictContainsSubset(dict(a=1, b=2), result)

    def test_subscribe_custom_threadpool(self):
        subs = SubscriptionsManager(mock.MagicMock())
        fake_threads = mock.MagicMock()
        fake_threads.apply_async.return_value = 42
        observer_a = subs.subscribe(
            channels.DeviceStateChanges(device_id='A'),
            provider=fake_threads
        )
        # with a custom threadpool with only two processes, we'll time out on any call
        # because there are no threads available
        self.assertEqual(observer_a.next().defer(), 42)

    @unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
    def test_live_create_and_cleanup(self):
        # integration - ResourceValueCurrent cleans up
        from mbed_cloud.connect import ConnectAPI
        api = ConnectAPI()
        d = api.list_connected_devices().first()
        r = api.subscribe(api.subscribe.channels.ResourceValues(
            device_id=d.id,
            resource_path='/3/0/0',
        )).next().block(timeout=2)
        self.assertTrue(r)

        # wait for notifications to be stopped
        api.stop_notifications()

        # check that the routing table is cleaned up
        for i in range(10):
            time.sleep(0.01)
            if not api.subscribe.list_all():
                break
        else:
            self.fail('Routing table not empty')

    @unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
    def test_live_device_state_change(self):
        # integration - DeviceStateChanges local filter
        from mbed_cloud.connect import ConnectAPI
        api = ConnectAPI()
        d = api.list_connected_devices().first()
        observer = api.subscribe(api.subscribe.channels.DeviceStateChanges(device_id=d.id))
        # cheat, waiting takes too long
        api.subscribe.notify({
            channels.ChannelIdentifiers.reg_updates: [
                dict(a=1, b=2, device_id=d.id),
                dict(a=1, b=2, device_id='A'),
                dict(a=1, b=2, device_id='B'),
            ]
        })
        r = observer.next().block(timeout=2)
        self.assertTrue(r)
