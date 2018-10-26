# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Example showing basic usage of getting device statistics."""
from datetime import datetime
from mbed_cloud import ConnectAPI


def _main():
    api = ConnectAPI()
    header = "Get statistics from the last 30 days in 1 day interval"
    print("%s\n%s" % (header, len(header) * "-"))
    metrics = list(api.list_metrics(interval="1d", period="30d"))
    for idx, metric in enumerate(metrics):
        print(metric)

    header = "Get statistics from the last 2 days in 3 hours interval"
    print("%s\n%s" % (header, len(header) * "-"))
    metrics = list(api.list_metrics(interval="3h", period="2d"))
    for idx, metric in enumerate(metrics):
        print(metric)

    header = "Get statistics from 1 March 2017 to 1 April 2017"
    print("%s\n%s" % (header, len(header) * "-"))
    start = datetime(2018, 3, 1, 0, 0, 0)
    end = datetime(2018, 4, 1, 0, 0, 0)
    metrics = list(api.list_metrics(interval="1d", start=start, end=end))
    for idx, metric in enumerate(metrics):
        print(metric)

# 2018-03-01T00:00Z'), ('end', '2018-04-01T00:00Z

if __name__ == "__main__":
    _main()
