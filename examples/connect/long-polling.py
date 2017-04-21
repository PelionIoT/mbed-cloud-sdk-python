# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Example setting up long-polling on a device."""
import time

from mbed_cloud.connect import ConnectAPI

BUTTON_RESOURCE = "/5002/0/1"


def _run_synchronized():
    api = ConnectAPI()
    api.start_notifications()
    devices = list(api.list_connected_devices())
    if not devices:
        raise Exception("No devices registered. Aborting")

    current_value = None
    while True:
        # Will get the resource value for button and block the thread whilst doing it
        # See the async example for details on what the 'sync' flag does in the background.
        # Note this will raise a CloudAsyncError if something goes wrong, which we're not catching
        # here for simplicity.
        new_value = api.get_resource_value(devices[0].id, BUTTON_RESOURCE)

        # Print new value to user, if it has changed.
        if new_value != current_value:
            print("Current value: %r" % (new_value,))

            # Save new current value
            current_value = new_value


def _run_async():
    api = ConnectAPI()
    api.start_notifications()
    devices = list(api.list_connected_devices())
    if not devices:
        raise Exception("No devices registered. Aborting")

    current_value = None
    while True:
        async_resp = api.get_resource_value_async(devices[0].id, BUTTON_RESOURCE)

        # Busy wait - block the thread and wait for the response to finish.
        while not async_resp.is_done:
            time.sleep(0.1)

        # Check if we have a async error response, and abort if it is.
        if async_resp.error:
            raise Exception("Got async error response: %r" % async_resp.error)

        # Get the value from the async response, as we know it's done and it's not
        # an error.
        new_value = async_resp.value

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
