# ---------------------------------------------------------------------------
# Pelion Device Management SDK
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
"""Example: listing devices events."""
from mbed_cloud import DeviceDirectoryAPI


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
