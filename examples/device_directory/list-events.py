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
"""Example: listing devices events."""
from mbed_cloud.device_directory import DeviceDirectoryAPI


def _print_event(idx, l):
    print("%d) %s | %s\n%s\n" % (idx, l.date_time, l.id, l.description))


def _main():
    api = DeviceDirectoryAPI()
    events = list(api.list_device_events(limit=5, order='desc'))

    for idx, event in enumerate(events):
        _print_event(idx + 1, event)

    print("-" * 30 + "\n")

    filters = {
        'id': str(events[0].id),
    }
    device_events = api.list_device_events(limit=5, filters=filters)
    for idx, device_event in enumerate(device_events):
        _print_event(idx + 1, device_event)


if __name__ == "__main__":
    _main()
