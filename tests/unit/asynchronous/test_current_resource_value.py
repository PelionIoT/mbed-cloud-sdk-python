from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud.subscribe import channels
from mbed_cloud.connect import ConnectAPI

from tests.common import BaseCase

import mock

import os
import unittest


class Test(BaseCase):

    def test_current_resource_value(self):
        device_id1 = 'ABCD_E'
        device_id2 = 'ABCD_F'
        resource_path = '/3/4/5'
        subs = SubscriptionsManager(mock.MagicMock())
        channel_a = channels.CurrentResourceValue(device_id=device_id1, resource_path=resource_path)
        observer_a = subs.subscribe(channel_a)
        channel_b = channels.CurrentResourceValue(device_id=device_id2, resource_path=resource_path)
        observer_b = subs.subscribe(channel_b)

        subs.notify({
            channels.ChannelIdentifiers.async_responses: [
                {'id': channel_a.async_id},
                {'id': 'unlikely'},
            ]
        })

        self.assertEqual(1, observer_a.notify_count)
        self.assertEqual(0, observer_b.notify_count)

    @unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
    def test_live_device_state_change(self):
        api = ConnectAPI()
        d = api.list_connected_devices().first()
        api.delete_device_subscriptions(d.id)

        # request the `manufacturer` field
        channel = channels.CurrentResourceValue(device_id=d.id, resource_path='/3/0/0')
        observer = api.subscribe(channel)
        value = observer.next().block(timeout=2)
        # should be, in this case, TLV
        self.assertEqual(b'6465765f6d616e756661637475726572', value)
