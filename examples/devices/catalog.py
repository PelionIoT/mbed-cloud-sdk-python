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
from mbed_cloud.devices import DeviceAPI


def _print_device(idx, d):
    print("%d) %s | %s | %s" % (idx, d.device_id, d.state, d.created_at))


def _main():
    api = DeviceAPI()

    # List all devices, ordering by the most recently created first.
    for d, idx in api.list_devices(order='desc', limit=10).iteritems():
        _print_device(idx + 1, d)

    print("\n" + "-" * 30 + "\n")

    # Now only list the devices that are registered.
    filters = {
        'state': 'registered'
    }
    registered = api.list_devices(order='desc', limit=10, filters=filters)
    for d, idx in registered.iteritems():
        _print_device(idx + 1, d)

if __name__ == "__main__":
    _main()
