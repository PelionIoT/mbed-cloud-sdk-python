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
"""Example showing devices from device catalog."""
from mbed_cloud import DeviceDirectoryAPI


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
        'state': {'$eq': "deregistered"}
    }
    registered = api.list_devices(order='desc', limit=10, filters=filters)
    for idx, d in enumerate(registered):
        _print_device(idx + 1, d)


if __name__ == "__main__":
    _main()
