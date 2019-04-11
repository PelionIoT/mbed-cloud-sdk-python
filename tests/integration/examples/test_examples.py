from mbed_cloud.exceptions import CloudApiException
from tests.common import BaseCase

import unittest


@BaseCase._skip_in_ci
class TestExamples(BaseCase):

    @unittest.skip('cannot demonstrate pip in test suite')
    def test_install(self):
        """
        # an example: initial setup
        pip install mbed-cloud-sdk
        # end of example
        """
        pass

    def test_legacy_listing_resources(self):
        # an example: legacy listing resources
        from mbed_cloud import BillingAPI

        billing_api = BillingAPI()
        for quota_history in billing_api.get_quota_history():
            print("Quota change reason: %s, delta: %s" % (quota_history.reason, quota_history.delta))
        # end of example

    def test_legacy_get_resources(self):
        # an example: legacy get resource
        from mbed_cloud import BillingAPI

        billing_api = BillingAPI()
        print("Quota remaining: %s" % billing_api.get_quota_remaining())
        # end of example

    def test_configuration(self):
        with self.assertRaises(CloudApiException):
            # an example: configuring the SDK
            from mbed_cloud import AccountManagementAPI
            config = dict(api_key='ak_1234abc')
            # alternatively, configuration can be loaded from json files or environment variables
            # if the host is not the default Mbed Cloud, it needs to be specified
            config['host'] = 'https://custom-mbed-cloud-host.com'
            # create an instance of one of the SDK modules
            api = AccountManagementAPI(params=config)
            # do something with the SDK
            print(api.get_account())
            # end of example

    def test_list_connected(self):
        # an example: list devices in mbed cloud
        from mbed_cloud import ConnectAPI
        api = ConnectAPI()

        # Print all devices
        for device in api.list_connected_devices(order='asc', max_results=900):
            print(device.id, device.state)
        # end of example

    def test_list_disconnected(self):
        # an example: list deregistered devices in mbed cloud
        from mbed_cloud import DeviceDirectoryAPI
        api = DeviceDirectoryAPI()

        # Print all devices
        for device in api.list_devices(filter=dict(state='deregistered'), order='asc', max_results=900):
            print(device.id, device.state)
        # end of example

    def test_subscribe_resources(self):
        import logging
        logging.basicConfig(level=logging.DEBUG)
        # an example: subscribing to resource value changes
        # creates an Observer listening to resource value changes for devices
        # whose id starts with `016` and resource paths start with `/3/0/`
        from mbed_cloud import ConnectAPI
        api = ConnectAPI()
        # prepare a channel
        channel = api.subscribe.channels.ResourceValues(device_id='016*', resource_path='/3/0/*')
        # start listening for updates
        observer = api.subscribe(channel)
        # on the first update for the channel, block for the specified timeout
        print(observer.next().block(timeout=120000))
        # end of example

    def test_subscribe_device_state(self):
        # an example: subscribing to device state changes
        # creates an Observer listening to device state changes for devices
        # whose id starts with `016`
        from mbed_cloud import ConnectAPI
        api = ConnectAPI()
        # prepare a channel
        channel = api.subscribe.channels.DeviceStateChanges(
            device_id='016*',
            # here, `channel` refers to the filterable device state received from
            # the notification system
            channel=[
                api.subscribe.channels.ChannelIdentifiers.registrations,
                api.subscribe.channels.ChannelIdentifiers.registrations_expired
            ]
        )
        # start listening for updates
        observer = api.subscribe(channel)
        # on the first update for the channel, block for the specified timeout
        print(observer.next().block(timeout=120000))
        # end of example
