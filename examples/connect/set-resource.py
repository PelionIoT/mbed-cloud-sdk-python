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
from mbed_cloud.connect import ConnectAPI

WRITEABLE_RESOURCE = "/5001/0/1"


def _main():
    api = ConnectAPI()
    # calling start_notifications is required for getting/setting resource synchronously
    api.start_notifications()
    devices = list(api.list_connected_devices())
    if not devices:
        raise Exception("No connected devices registered. Aborting")

    # Synchronously get the initial/current value of the resource
    value = api.get_resource_value(devices[0].id, WRITEABLE_RESOURCE)
    print("Current value: %r" % (value,))

    # Set Resource value. Resource needs to have type == "writable_resource"
    api.set_resource_value(device_id=devices[0].id,
                           resource_path=WRITEABLE_RESOURCE,
                           resource_value=10)

    # Synchronously get the current value of the resource
    value = api.get_resource_value(devices[0].id, WRITEABLE_RESOURCE)
    print("Current value: %r" % (value,))


if __name__ == "__main__":
    _main()
