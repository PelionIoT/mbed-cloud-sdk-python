"""Example showing basic usage of device resource subscriptions."""
from mbed_cloud.devices import DeviceAPI

BUTTON_RESOURCE = "/3200/0/5501"


def _main():
    api = DeviceAPI()
    api.start_long_polling()
    devices = api.list_connected_devices().as_list()
    if not devices:
        raise Exception("No connected devices registered. Aborting")

    # Synchronously get the initial/current value of the resource
    value = api.get_resource_value(devices[0].id, BUTTON_RESOURCE)

    # Register a subscription for new values
    queue = api.add_subscription(devices[0].id, BUTTON_RESOURCE)
    while True:
        # Print the current value
        print("Current value: %r" % (value,))

        # Get a new value, using the subscriptions
        value = queue.get(timeout=30)

if __name__ == "__main__":
    _main()
