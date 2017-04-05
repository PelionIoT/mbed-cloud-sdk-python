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
"""Example: listing endpoints and their resources using Device API."""
from mbed_cloud.devices import DeviceAPI


def _main():
    api = DeviceAPI()

    for device in api.list_connected_devices():
        resources = api.list_resources(device.id)

        # Print endpoint name header
        header = device.id
        print(header)
        print(len(header) * "-")

        for r in resources:
            print("\t- %s (%s / Observable: %s)" % (r.uri, r.name if r.name else "-", r.observable))

        # Space between endpoints
        print("")


if __name__ == "__main__":
    _main()
