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
from mbed_cloud.logging import LoggingAPI


def _print_log(idx, l):
    print("%d) %s | %s\n%s\n" % (idx, l.date_time, l.device_log_id, l.description))


def _main():
    api = LoggingAPI()
    logs = api.list_device_logs(limit=5, order='desc')

    for log, idx in logs.iteritems():
        _print_log(idx + 1, log)

    print("-" * 30 + "\n")

    filters = {
        'device_id': str(logs.data[0].device_id),
    }
    device_logs = api.list_device_logs(limit=5, filters=filters)
    for device_log, idx in device_logs.iteritems():
        _print_log(idx + 1, device_log)


if __name__ == "__main__":
    _main()
