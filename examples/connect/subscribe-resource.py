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
from mbed_cloud.connect import ConnectAPI

BUTTON_RESOURCE = "/5002/0/1"
WRITEABLE_RESOURCE = "/5001/0/1"


def _main():
    api = ConnectAPI()
    api.start_notifications()
    devices = api.list_connected_devices().data
    if not devices:
        raise Exception("No connected devices registered. Aborting")

    # Synchronously get the initial/current value of the resource
    value = api.get_resource_value(devices[0].id, BUTTON_RESOURCE)

    # Register a subscription for new values
    api.set_resource_value(device_id=devices[0].id,
                           resource_path=WRITEABLE_RESOURCE,
                           resource_value='10')

    queue = api.add_resource_subscription(devices[0].id, BUTTON_RESOURCE)
    while True:
        # Print the current value
        print("Current value: %r" % (value,))

        # Get a new value, using the subscriptions
        value = queue.get(timeout=30)


if __name__ == "__main__":
    _main()
