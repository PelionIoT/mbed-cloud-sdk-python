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
"""Example showing basic usage of Statistics API."""
from datetime import datetime
from mbed_cloud.statistics import StatisticsAPI


def _main():
    api = StatisticsAPI()
    start = datetime(2017, 3, 1, 0, 0, 0)
    end = datetime(2017, 4, 1, 0, 0, 0)
    header = "Get statistics from the last 30 days in 1 day interval"
    print("%s\n%s" % (header, len(header) * "-"))
    for metric in api.get_metric(None, None, None, "30d", "1d"):
        print(metric)

    header = "Get statistics from the last 2 days in 3 hours interval"
    print("%s\n%s" % (header, len(header) * "-"))
    for metric in api.get_metric(None, None, None, "2d", "3h"):
        print(metric)

    header = "Get statistics from 1 March 2017 to 1 April 2017"
    print("%s\n%s" % (header, len(header) * "-"))
    for metric in api.get_metric(None, start, end, None, "1d"):
        print(metric)


if __name__ == "__main__":
    _main()
