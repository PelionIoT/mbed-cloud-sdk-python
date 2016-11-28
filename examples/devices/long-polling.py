"""Example setting up long-polling on a device."""
import time

from mbed_cloud_sdk.devices import DeviceAPI

BUTTON_RESOURCE = "/3200/0/5501"


def _run_synchronized():
    api = DeviceAPI()
    api.start_long_polling()
    endpoints = api.list_endpoints()
    if not endpoints:
        raise Exception("No endpoints registered. Aborting")

    current_value = None
    while True:
        # Will get the resource value for button and block the thread whilst doing it
        # See the async example for details on what the 'sync' flag does in the background.
        # Note this will raise a AsyncError if something goes wrong, which we're not catching
        # here for simplicity.
        new_value = api.get_resource_value(endpoints[0].name, BUTTON_RESOURCE, sync=True)

        # Print new value to user, if it has changed.
        if new_value != current_value:
            print("Current value: %r" % (new_value,))

            # Save new current value
            current_value = new_value


def _run_async():
    api = DeviceAPI()
    api.start_long_polling()
    endpoints = api.list_endpoints()
    if not endpoints:
        raise Exception("No endpoints registered. Aborting")

    current_value = None
    while True:
        async_resp = api.get_resource_value(endpoints[0].name, BUTTON_RESOURCE)

        # Busy wait - block the thread and wait for the response to finish.
        while not async_resp.is_done():
            time.sleep(0.1)

        # Check if we have a async error response, and abort if it is.
        if async_resp.error():
            raise Exception("Got async error response: %r" % async_resp.error())

        # Get the value from the async response, as we know it's done and it's not
        # an error.
        new_value = async_resp.get_value()

        # Print new value to user, if it has changed.
        if current_value != new_value:
            print("Current value: %r" % (new_value,))

            # Save new current value
            current_value = new_value

if __name__ == "__main__":
    # These two methods are doing the same, but one is showing the behaviour of the
    # 'sync' flag to `get_resource`, and the `run_async` shows how you can have
    # a bit more fine grained control.
    _run_synchronized()
    # _run_async()
