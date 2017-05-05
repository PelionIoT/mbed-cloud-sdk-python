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
"""Example showing devices from device catalog."""
from mbed_cloud.device_directory import DeviceDirectoryAPI


def _print_device(idx, d):
    print("%d) %s | %s | %s" % (idx, d.id, d.state, d.created_at))


def _main():
    api = DeviceDirectoryAPI()

    # List all devices, ordering by the most recently created first.
    for idx, d in enumerate(api.list_devices(order='desc', limit=10)):
        _print_device(idx + 1, d)

    print("\n" + "-" * 30 + "\n")

    # Now only list the devices that are registered.
    filters = {
        'state': { '$eq': "deregistered" }
    }
    registered = api.list_devices(order='desc', limit=10, filters=filters)
    for idx, d in enumerate(registered):
        _print_device(idx + 1, d)


if __name__ == "__main__":
    _main()
