from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud.subscribe import channels

from tests.common import BaseCase

import mock
import six

from multiprocessing.pool import ThreadPool

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
                dict(ep='A', original_ep='test_original_ep')
            ]
        })

        result = future_a.get(timeout=2)
        self.assertDictContainsSubset(dict(device_id="A", alias="test_original_ep"), result)

        # just because one observer (`a`) is ready, does not mean another (`c`) is.
        result = future_c.get(timeout=2)
        self.assertDictContainsSubset(dict(device_id="A", alias="test_original_ep"), result)

        self.assertFalse(future_b.ready())

    def test_subscribe_custom_threadpool(self):
        subs = SubscriptionsManager(mock.MagicMock())
        custom_threads = ThreadPool(processes=1)
        observer_a = subs.subscribe(
            channels.DeviceStateChanges(device_id='A'),
            provider=custom_threads
        )
        with mock.patch.object(custom_threads, 'apply_async') as custom:
            observer_a.next().defer()
            observer_a.next().defer()
            # prove that we used the threadpool we provided
            self.assertEqual(custom_threads.apply_async.call_count, 2)

    def test_notify_registration_expiry(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer = subs.subscribe(channels.DeviceStateChanges())
        future = observer.next().defer()

        subs.notify({
            channels.ChannelIdentifiers.registrations_expired: [
                "device_id_test"
            ]
        })

        output = future.get(timeout=2)
        self.assertEqual(output, {"device_id": "device_id_test", "channel": "registrations_expired"})

    def test_notify_de_registrations(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer = subs.subscribe(channels.DeviceStateChanges())
        future = observer.next().defer()

        subs.notify({
            channels.ChannelIdentifiers.de_registrations: [
                "device_id_test"
            ]
        })

        output = future.get(timeout=2)
        self.assertEqual(output, {"device_id": "device_id_test", "channel": "de_registrations"})

    def test_notify_registration(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer = subs.subscribe(channels.DeviceStateChanges())
        future = observer.next().defer()

        subs.notify({
            channels.ChannelIdentifiers.registrations: [
                {
                    "ep": "test_endpoint_name",
                    "original_ep": "test_original_ep",
                    "ept": "test_ept",
                    "q": "test_q",
                    "resources": [{
                        "path": "test_path",
                        "if": "test_if",
                        "rt": "test_rt",
                        "ct": "test_ct",
                        "obs": "test_obs"
                    }]
                }
            ]
        })

        output = future.get(timeout=2)

        self.assertEqual(output, {
            "channel": "registrations",
            "device_id": "test_endpoint_name",
            "alias": "test_original_ep",
            "device_type": "test_ept",
            "queue_mode": "test_q",
            "resources": [{
                "path": "test_path",
                "type": "test_rt",
                "content_type": "test_ct",
                "observable": "test_obs"
            }]
        })

    def test_notify_reg_updates(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer = subs.subscribe(channels.DeviceStateChanges())
        future = observer.next().defer()

        subs.notify({
            channels.ChannelIdentifiers.reg_updates: [
                {
                    "ep": "test_endpoint_name",
                    "original_ep": "test_original_ep",
                    "ept": "test_ept",
                    "q": "test_q",
                    "resources": [{
                        "path": "test_path",
                        "if": "test_if",
                        "rt": "test_rt",
                        "ct": "test_ct",
                        "obs": "test_obs"
                    }]
                }
            ]
        })

        output = future.get(timeout=2)

        self.assertEqual(output, {
            "channel": "reg_updates",
            "device_id": "test_endpoint_name",
            "alias": "test_original_ep",
            "device_type": "test_ept",
            "queue_mode": "test_q",
            "resources": [{
                "path": "test_path",
                "type": "test_rt",
                "content_type": "test_ct",
                "observable": "test_obs"
            }]
        })

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
                dict(a=1, b=2, ep=d.id),
                dict(a=1, b=2, ep='A'),
                dict(a=1, b=2, ep='B'),
            ]
        })
        r = observer.next().block(timeout=2)
        self.assertTrue(r)

    @unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
    def test_registration_notifications(self):
        """Test a all registration notifications in a single message"""
        from mbed_cloud.connect import ConnectAPI
        device_id = "015f3850a657000000000001001002ab"
        api = ConnectAPI()
        registrations_observer = api.subscribe(api.subscribe.channels.DeviceStateChanges(
            device_id=device_id,
            channel=channels.ChannelIdentifiers.registrations),
            provider = False)
        de_registrations_observer = api.subscribe(api.subscribe.channels.DeviceStateChanges(
            device_id=device_id,
            channel=channels.ChannelIdentifiers.de_registrations))
        reg_updates_observer = api.subscribe(api.subscribe.channels.DeviceStateChanges(
            device_id=device_id,
            channel=channels.ChannelIdentifiers.reg_updates))
        registrations_expired_observer = api.subscribe(api.subscribe.channels.DeviceStateChanges(
            device_id=device_id,
            channel=channels.ChannelIdentifiers.registrations_expired))
        # cheat, waiting takes too long
        example_data = {
            "registrations": [{
                "q": False,
                "original-ep": "my-device-123",
                "ept": "Light",
                "resources": [{
                    "path": "/sen/light",
                    "ct": "text/plain",
                    "obs": True,
                    "rt": "light_sensor",
                    "if": "sensor"
                }],
                "ep": device_id
            }],
            "reg_updates": [{
                "q": False,
                "original-ep": "my-device-123",
                "ept": "Light",
                "resources": [{
                    "path": "/sen/light",
                    "ct": "text/plain",
                    "obs": True,
                    "rt": "light_sensor",
                    "if": "sensor"
                }],
                "ep": device_id
            }],
            "async_responses": [{
                "ct": "text/plain",
                "payload": "My4zMQ==",
                "max-age": "60",
                "id": "9e3c96b8-c4d7-496a-ab90-cc732b9b560e",
                "error": "TIMEOUT",
                "status": 200
            }],
            "notifications": [{
                "path": "/sen/light",
                "ct": "text/plain",
                "payload": "My4zMQ==",
                "max-age": "60",
                "ep": device_id
            }],
            "de_registrations": [device_id],
            "registrations_expired": [device_id],
        }

        # from pprint import pprint
        api.subscribe.notify(example_data)
        # r = registrations_observer.next().block(timeout=2)
        # pprint(r)
        # r = de_registrations_observer.next().block(timeout=2)
        # pprint(r)
        # r = reg_updates_observer.next().block(timeout=2)
        # pprint(r)
        # r = registrations_expired_observer.next().block(timeout=2)
        # pprint(r)

        self.assertEqual(registrations_observer.next().block(timeout=2),
                         {
                             'alias': None,
                             'channel': 'registrations',
                             'device_id': '015f3850a657000000000001001002ab',
                             'device_type': 'Light',
                             'queue_mode': False,
                             'resources': [{'content_type': 'text/plain',
                                            'observable': True,
                                            'path': '/sen/light',
                                            'type': 'light_sensor'}]})
        self.assertEqual(de_registrations_observer.next().block(timeout=2),
                         {'channel': 'de_registrations', 'device_id': '015f3850a657000000000001001002ab'})
        self.assertEqual(reg_updates_observer.next().block(timeout=2),
                         {'alias': None,
                          'channel': 'reg_updates',
                          'device_id': '015f3850a657000000000001001002ab',
                          'device_type': 'Light',
                          'queue_mode': False,
                          'resources': [{'content_type': 'text/plain',
                                         'observable': True,
                                         'path': '/sen/light',
                                         'type': 'light_sensor'}]})
        self.assertEqual(registrations_expired_observer.next().block(timeout=2),
                         {'channel': 'registrations_expired',
                          'device_id': '015f3850a657000000000001001002ab'})

    @unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
    def test_observer_timeout(self):
        """Test that the observer timeouts"""
        from mbed_cloud.connect import ConnectAPI
        api = ConnectAPI()
        observer = api.subscribe(api.subscribe.channels.DeviceStateChanges(device_id=123456))
        with self.assertRaises(TimeoutError) as timeout_error:
            observer.next().block(timeout=2)
        self.assertEqual(str(timeout_error.exception), "No data received after 2.0 seconds.")
