"""Examples for SDK Documentation that can be run to test they are working"""

from tests.common import BaseCase


@BaseCase._skip_in_ci
class TestExamples(BaseCase):

    def test_get_and_set_resource_value(self):
        # an example: get and set a resource value
        from mbed_cloud.foundation import Device
        from mbed_cloud import ApiFilter
        from mbed_cloud.foundation.enums import DeviceStateEnum
        from mbed_cloud import ConnectAPI

        # Use the Foundation interface to find a registered device.
        api_filter = ApiFilter()
        api_filter.add_filter("state", "eq", DeviceStateEnum.REGISTERED)
        device = Device().list(max_results=2, filter=api_filter).next()

        # Use the Legacy interface for find resources
        connect_api = ConnectAPI()

        # Find an observable resource
        for resource in connect_api.list_resources(device.id):
            if resource.observable:
                break

        # Set a resource value
        connect_api.set_resource_value(device.id, resource.path, "12")

        # Get a resource value
        value = connect_api.get_resource_value(device.id, resource.path)
        print("Device %s, path %s, current value: %s" %(device.id, resource.path, value))
        # end of example

        connect_api.stop_notifications()

    def test_subscribe(self):
        # an example: subscribe to resource values
        from mbed_cloud import ConnectAPI

        # Create an instance of the Connect API
        connect_api = ConnectAPI()

        # Configure a subscription to receive resource value changes on all devices
        channel = connect_api.subscribe.channels.ResourceValues(device_id="*")

        # Contact Pelion Device Management to actually make the configured subscription
        observer = connect_api.subscribe(channel)

        # Print the subscription notifications received
        while True:
            print(observer.next().block())

        # end of example
            break

        connect_api.subscribe.unsubscribe_all()
