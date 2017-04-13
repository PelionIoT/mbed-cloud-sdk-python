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
"""Example showing basic usage of device resource subscriptions."""
from mbed_cloud.devices import DeviceAPI

BUTTON_RESOURCE = "/5002/0/1"


def _main():
    api = DeviceAPI()
    api.start_notifications()
    devices = list(api.list_connected_devices())
    if not devices:
        raise Exception("No connected devices registered. Aborting")

    # Synchronously get the initial/current value of the resource
    value = api.get_resource_value(devices[0].id, BUTTON_RESOURCE)

    # Register a subscription for new values
    queue = api.add_resource_subscription(devices[0].id, BUTTON_RESOURCE)
    while True:
        # Print the current value
        print("Current value: %r" % (value,))

        # Get a new value, using the subscriptions
        value = queue.get(timeout=30)


if __name__ == "__main__":
    _main()
