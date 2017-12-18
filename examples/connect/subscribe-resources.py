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
"""Example showing basic usage of device resource subscriptions."""

from mbed_cloud import ConnectAPI
import time

INCRIMENTAL_RESOURCE = "/5002/0/1"
VOLTAGE_RESOURCE = "/3316/0/5700"
CURRENT_RESOURCE = "/3317/0/5700"
POWER_RESOURCE = "/3328/0/5700"


def _callback_fn(device_id, path, value):
    print("callback path: %r value: %r" % (path, value))


def _main():
    api = ConnectAPI()
    api.start_notifications()
    devices = api.list_connected_devices().data
    if not devices:
        raise Exception("No connected devices registered. Aborting")
    device_id = "015e9a938ff100000000000100100019"
    api.delete_device_subscriptions(device_id)
    api.list_presubscriptions()

    api.add_resource_subscription_async(device_id, INCRIMENTAL_RESOURCE, _callback_fn)
    api.add_resource_subscription_async(device_id, VOLTAGE_RESOURCE, _callback_fn)
    api.add_resource_subscription_async(device_id, CURRENT_RESOURCE, _callback_fn)
    api.add_resource_subscription_async(device_id, POWER_RESOURCE, _callback_fn)
    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    _main()
