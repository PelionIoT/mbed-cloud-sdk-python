from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud.subscribe import channels
from mbed_cloud.connect import ConnectAPI

from tests.common import BaseCase

import mock

import os
import unittest


class Test(BaseCase):
    def test_invalid_wildcard(self):
        # can't have a wildcard in anything other than last character
        with self.assertRaises(ValueError):
            channels.ResourceValues(device_id='A*B*', resource_path=5)

        with self.assertRaises(ValueError):
            channels.ResourceValues(resource_path=['1', '**/'])

    def test_valid_wildcard(self):
        channel = channels.ResourceValues(device_id='AB')
        self.assertEqual({'channel': 'notifications', 'endpoint-name': ['AB']}, channel._route_seeds)

        channel = channels.ResourceValues(device_id=['A', 'B'])
        self.assertEqual({'channel': 'notifications', 'endpoint-name': ['A', 'B']}, channel._route_seeds)

        channel = channels.ResourceValues(device_id='AB*')
        self.assertEqual({'channel': 'notifications'}, channel._route_seeds)

        channel = channels.ResourceValues(device_id='A', resource_path='/3/0/1/*')
        self.assertEqual({'channel': 'notifications', 'endpoint-name': ['A']}, channel._route_seeds)
        self.assertEqual({'resource-path': ['/3/0/1/*']}, channel._local_filters)

        channel = channels.ResourceValues(device_id=['a*', 'b'], resource_path=['/3/0/1/*', '4/*'])
        self.assertEqual({'channel': 'notifications'}, channel._route_seeds)
        self.assertEqual({'endpoint-name': ['a*', 'b'], 'resource-path': ['/3/0/1/*', '4/*']}, channel._local_filters)

    def test_wildcards(self):
        # subscription to wildcard value should be triggered when receiving specific value
        device_id1 = 'ABCD_E'
        device_id2 = 'ABCD_F'
        subs = SubscriptionsManager(mock.MagicMock())
        observer_a = subs.subscribe(channels.ResourceValues(device_id=device_id1, resource_path=5))
        observer_b = subs.subscribe(channels.ResourceValues(device_id=device_id2, resource_path=5))
        observer_c = subs.subscribe(channels.ResourceValues(device_id='ABCD*', resource_path=5))
        observer_d = subs.subscribe(channels.ResourceValues(device_id=device_id1, custom_attr='x'))

        subs.notify({
            channels.ChannelIdentifiers.notifications: [
                # should trigger B and C (matches B, wildcard matches C)
                {'unexpected': 'extra', 'endpoint-name': device_id2, 'resource-path': '5'},
                # should only trigger D (resource_path is different)
                {'unexpected': 'extra', 'endpoint-name': device_id1, 'resource-path': '2'},
                # should trigger D (matches device id 1, custom attr)
                {'endpoint-name': device_id1, 'custom_attr': 'x'},
            ]
        })

        self.assertEqual(0, observer_a.notify_count)
        self.assertEqual(1, observer_b.notify_count)
        self.assertEqual(1, observer_c.notify_count)
        self.assertEqual(2, observer_d.notify_count)

    def test_parameters_as_lists(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer_a = subs.subscribe(channels.ResourceValues(device_id='a', resource_path=['a', 'b']))
        observer_b = subs.subscribe(channels.ResourceValues(device_id=['x', 'y'], resource_path=['a', 'b']))
        subs.notify({
            channels.ChannelIdentifiers.notifications: [
                # should trigger A
                {'endpoint-name': 'a', 'resource-path': 'a'},
                # should trigger A
                {'endpoint-name': 'a', 'resource-path': 'b'},
                # should trigger B
                {'endpoint-name': 'x', 'resource-path': 'b'},
            ]
        })

        self.assertEqual(2, observer_a.notify_count)
        self.assertEqual(1, observer_b.notify_count)

    @unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
    def test_live_device_state_change(self):
        api = ConnectAPI()
        api.delete_presubscriptions()
        d = api.list_connected_devices().first()
        api.delete_device_subscriptions(d.id)
        channel = channels.ResourceValues(device_id=d.id, resource_path=['/3/0/*'])
        observer = api.subscribe(channel)
        # don't actually care about notifications, we want to see subscriptions
        current_subs = api.list_device_subscriptions(d.id)
        self.assertGreaterEqual(len(current_subs), 3)
        for path in current_subs:
            self.assertIn('/3/0', path)

        channel.stop()
        current_subs = api.list_device_subscriptions(d.id)
        self.assertIsNone(None, current_subs)
