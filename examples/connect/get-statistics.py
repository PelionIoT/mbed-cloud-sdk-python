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
"""Example showing basic usage of getting device statistics."""
from datetime import datetime
from mbed_cloud.connect import ConnectAPI


def _main():
    api = ConnectAPI()
    header = "Get statistics from the last 30 days in 1 day interval"
    print("%s\n%s" % (header, len(header) * "-"))
    for metric in api.get_metrics(interval="1d", period="30d"):
        print(metric)

    header = "Get statistics from the last 2 days in 3 hours interval"
    print("%s\n%s" % (header, len(header) * "-"))
    for metric in api.get_metrics(interval="3h", period="2d"):
        print(metric)

    header = "Get statistics from 1 March 2017 to 1 April 2017"
    print("%s\n%s" % (header, len(header) * "-"))
    start = datetime(2017, 3, 1, 0, 0, 0)
    end = datetime(2017, 4, 1, 0, 0, 0)
    for metric in api.get_metrics(interval="1d", start=start, end=end):
        print(metric)


if __name__ == "__main__":
    _main()
