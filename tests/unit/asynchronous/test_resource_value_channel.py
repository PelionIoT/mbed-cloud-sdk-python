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
        self.assertEqual({'channel': 'notifications', 'ep': ['AB']}, channel._route_seeds)

        channel = channels.ResourceValues(device_id=['A', 'B'])
        self.assertEqual({'channel': 'notifications', 'ep': ['A', 'B']}, channel._route_seeds)

        channel = channels.ResourceValues(device_id='AB*')
        self.assertEqual({'channel': 'notifications'}, channel._route_seeds)

        channel = channels.ResourceValues(device_id='A', resource_path='/3/0/1/*')
        self.assertEqual({'channel': 'notifications', 'ep': ['A']}, channel._route_seeds)
        self.assertEqual({'path': ['/3/0/1/*']}, channel._local_filters)

        channel = channels.ResourceValues(device_id=['a*', 'b'], resource_path=['/3/0/1/*', '4/*'])
        self.assertEqual({'channel': 'notifications'}, channel._route_seeds)
        self.assertEqual({'ep': ['a*', 'b'], 'path': ['/3/0/1/*', '4/*']}, channel._local_filters)

    def test_wildcards(self):
        # subscription to wildcard value should be triggered when receiving specific value
        device_id1 = 'ABCDEF'
        device_id2 = 'ABC123'
        subs = SubscriptionsManager(mock.MagicMock())

        # channels
        A = subs.channels.ResourceValues(device_id=device_id1, resource_path=999)
        B = subs.channels.ResourceValues(device_id='ABCD*')
        C = subs.channels.ResourceValues(device_id='ABC*', resource_path=5)
        D = subs.channels.ResourceValues(device_id=device_id1, custom_attr='x')
        E = subs.channels.ResourceValues(device_id='*')
        F = subs.channels.ResourceValues(resource_path=[4, 5, 6, 7])

        # set names for clarity of logging
        A.name = 'A'
        B.name = 'B'
        C.name = 'C'
        D.name = 'D'
        E.name = 'E'
        F.name = 'F'

        sequence = [A, B, C, D, E, F]

        # set up the channels
        for channel in sequence:
            subs.subscribe(channel)

        # notification payloads
        notifications = [
            # device id matches ALL but doesn't match A, C, F because of resource paths, D due to custom attr
            ({'ep': device_id1}, (B, E)),
            # device id matches ALL but doesn't match A because of resource paths, D due to custom attr
            ({'ep': device_id1, 'path': '5'}, (B, C, E, F)),
            # should work as above
            ({'ep': device_id1, 'path': '5', 'unexpected': 'extra'}, (B, C, E, F)),
            # only matches D due to custom attr, E due to having any device id
            ({'ep': device_id1, 'custom_attr': 'x'}, (B, D, E)),
            # matches C and F due to resource path
            ({'ep': device_id2, 'path': '5'}, (C, E, F)),
            # should not trigger anything
            ({'endpoint': device_id1, 'custom_attr': 'x'}, tuple()),
        ]

        # trigger one-by-one
        for notification, expected_triggers in notifications:
            triggered = subs.notify({
                channels.ChannelIdentifiers.notifications: [notification]
            })
            expected_names = [c.name for c in expected_triggers]
            actual_names = [c.name for c in triggered]
            self.assertEqual(sorted(expected_names), sorted(actual_names))

        # trigger in one go
        triggered = subs.notify({
            channels.ChannelIdentifiers.notifications: [n[0] for n in notifications]
        })
        all_expected_channels = [c.name for n in notifications for c in n[1]]
        actual_names = [c.name for c in triggered]
        self.assertEqual(sorted(all_expected_channels), sorted(actual_names))

        self.assertEqual(8, B.observer.notify_count)
        self.assertEqual(2, D.observer.notify_count)

    def test_payload(self):
        # subscription to wildcard value should be triggered when receiving specific value
        device_id1 = 'ABCD_E'
        subs = SubscriptionsManager(mock.MagicMock())
        observer_a = subs.subscribe(channels.ResourceValues(device_id=device_id1, resource_path='/10255/0/4'))

        subs.notify({
            channels.ChannelIdentifiers.notifications: [
                {
                    "ct": "application/vnd.oma.lwm2m+tlv",
                    "ep": device_id1,
                    "max-age": 0,
                    "path": "/10255/0/4",
                    "payload": "iAsLSAAIAAAAAAAAAAA=",
                    'unexpected': 'extra',
                },
            ],
        })

        self.assertEqual(1, observer_a.notify_count)
        received_payload = observer_a.next().block(1)

        self.assertEqual(
            received_payload,
            {
                'ct': 'application/vnd.oma.lwm2m+tlv',
                'device_id': device_id1,
                'max-age': 0,
                'resource_path': '/10255/0/4',
                'payload': {'11': {'0': 0}},
                'channel': 'notifications',
                'unexpected': 'extra',
            }
        )

    def test_parameters_as_lists(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer_a = subs.subscribe(channels.ResourceValues(device_id='a', resource_path=['a', 'b']))
        observer_b = subs.subscribe(channels.ResourceValues(device_id=['x', 'y'], resource_path=['a', 'b']))
        subs.notify({
            channels.ChannelIdentifiers.notifications: [
                # should trigger A
                {'ep': 'a', 'path': 'a'},
                # should trigger A
                {'ep': 'a', 'path': 'b'},
                # should trigger B
                {'ep': 'x', 'path': 'b'},
            ]
        })

        self.assertEqual(2, observer_a.notify_count)
        self.assertEqual(1, observer_b.notify_count)

    @BaseCase._skip_in_ci
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


class FakeDevice(object):
    def __init__(self, device_id):
        self.id = device_id

class FakeResource(object):
    def __init__(self, observable, path):
        self.observable = observable
        self.path = path
        
        
class FakeConnectAPI(object):

    def list_connected_devices(self):
        return [FakeDevice("Device1"), FakeDevice("Device2"), FakeDevice("Device3"), FakeDevice("Excluded")]

    def list_resources(self, unused):
        return [FakeResource(False, '/3/0/13'),
                FakeResource(True, '/3/0/21'),
                FakeResource(False, '/3/0/18'),
                FakeResource(True, '/3/0/17'),
                FakeResource(True, '/3/0/2'),
                FakeResource(False, '/3/0/1'),
                FakeResource(False, '/3/0/0'),
                FakeResource(False, '/35011'),
                FakeResource(True, '/35011/0'),
                FakeResource(True, '/35011/0/27002'),
                FakeResource(False, '/10252/0/9'),
                FakeResource(True, '/10252/0/5'),
                FakeResource(False, '/10252/0/3'),
                FakeResource(True, '/10252/0/2'),
                FakeResource(False, '/10252/0/1')]


class TestMatchingDeviceResources(BaseCase):

    def test_observable_single(self):
        channel = channels.ResourceValues(
            device_id="Device1",
            resource_path="/10252/0/3")
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual([], channel._matching_device_resources(), "The specified resource was not observable")

    def test_observable_list(self):
        channel = channels.ResourceValues(
            device_id="Device1",
            resource_path=["/10252/0/1", "/10252/0/5"])
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual([('Device1', '/10252/0/5')],
                         channel._matching_device_resources(),
                         "Only the observable resources in the specified list, on Device1 should be returned")

    def test_observable_pattern(self):
        channel = channels.ResourceValues(
            device_id="Device1",
            resource_path="/10252/0/*")
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual(
            [('Device1', '/10252/0/5'), ('Device1', '/10252/0/2')],
            channel._matching_device_resources(),
            "Only the observable resources beginning '/10252/0/' on Device1 should be returned")

    def test_wildcard_resource(self):
        channel = channels.ResourceValues(
            device_id="Device1",
            resource_path="/35011/0*")
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual(
            [('Device1', '/35011/0'), ('Device1', '/35011/0/27002')],
            channel._matching_device_resources(),
            "'/35011/0*' should match all resource beginning '/35011/0'")

    def test_list_device(self):
        channel = channels.ResourceValues(
            device_id=["Device1", "Device2"],
            resource_path="/10252/0/5")
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual(
            [('Device1', '/10252/0/5'), ('Device2', '/10252/0/5')],
            channel._matching_device_resources(),
            "Defining devices as a list should explicitly match device IDs")

    def test_wildcard_device(self):
        channel = channels.ResourceValues(
            # device_id=["Device1", "Device2"],
            device_id="Device*",
            resource_path="/10252/0/5")
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual(
            [('Device1', '/10252/0/5'), ('Device2', '/10252/0/5'), ('Device3', '/10252/0/5')],
            channel._matching_device_resources(),
            "'Device*' should not match all devices starting with 'Device'")

    def test_device_no_match(self):
        channel = channels.ResourceValues(
            device_id="Device",
            resource_path="*")
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual([], channel._matching_device_resources(), "'Device' should not match any devices")

    def test_multiple_matches(self):
        channel = channels.ResourceValues(
            device_id=["Device1", "Device*"],
            resource_path=["/35011/0", "/35011*"])
        # Mock the Connect API to return connected devices and available resources
        channel._api = mock.Mock().method.return_value = FakeConnectAPI()

        self.assertEqual([('Device1', '/35011/0'), ('Device1', '/35011/0/27002'), ('Device2', '/35011/0'),
                          ('Device2', '/35011/0/27002'), ('Device3', '/35011/0'), ('Device3', '/35011/0/27002')],
                         channel._matching_device_resources(),
                         "Each Device and resource path should be listed once")
