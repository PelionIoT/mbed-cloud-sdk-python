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
"""Example showing basic usage of the webhook functionality."""
from mbed_cloud import ConnectAPI
import time

BUTTON_RESOURCE = "/5002/0/1"


def _main():
    api = ConnectAPI()
    devices = api.list_connected_devices().data
    if len(devices) == 0:
        raise Exception("No endpints registered. Aborting")
    # Delete device subscriptions
    api.delete_device_subscriptions(devices[0].id)
    # First register to webhook
    api.update_webhook("http://python.requestcatcher.com/")
    time.sleep(2)
    api.add_resource_subscription(devices[0].id, BUTTON_RESOURCE)
    while True:
        print("Webhook registered. Listening to button updates for 10 seconds...")

        time.sleep(10)
        break

    api.delete_webhook()
    print("Deregistered and unsubscribed from all resources. Exiting.")


if __name__ == '__main__':
    _main()
