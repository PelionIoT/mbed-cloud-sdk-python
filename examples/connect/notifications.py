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
"""Example setting up notifications on a device."""
import time

from mbed_cloud.connect import ConnectAPI

BUTTON_RESOURCE = "/5002/0/1"


def _run_synchronized():
    api = ConnectAPI()
    api.start_notifications()
    devices = api.list_connected_devices()
    if not devices:
        raise Exception("No devices registered. Aborting")

    current_value = None
    while True:
        # Will get the resource value for button and block the thread whilst doing it
        # See the async example for details on what the 'sync' flag does in the background.
        # Note this will raise a CloudAsyncError if something goes wrong, which we're not catching
        # here for simplicity.
        new_value = api.get_resource_value(devices[0].id, BUTTON_RESOURCE)

        # Print new value to user, if it has changed.
        if new_value != current_value:
            print("Current value: %r" % (new_value,))

            # Save new current value
            current_value = new_value


def _run_async():
    api = ConnectAPI()
    api.start_notifications()
    devices = api.list_connected_devices()
    if not devices:
        raise Exception("No devices registered. Aborting")

    current_value = None
    while True:
        async_resp = api.get_resource_value_async(devices[0].id, BUTTON_RESOURCE)

        # Busy wait - block the thread and wait for the response to finish.
        while not async_resp.is_done:
            time.sleep(0.1)

        # Check if we have a async error response, and abort if it is.
        if async_resp.error:
            raise Exception("Got async error response: %r" % async_resp.error)

        # Get the value from the async response, as we know it's done and it's not
        # an error.
        new_value = async_resp.value

        # Print new value to user, if it has changed.
        if current_value != new_value:
            print("Current value: %r" % (new_value,))

            # Save new current value
            current_value = new_value


if __name__ == "__main__":
    # These two methods are doing the same, but one is showing the behaviour of the
    # 'sync' flag to `get_resource`, and the `run_async` shows how you can have
    # a bit more fine grained control.
    _run_synchronized()
    # _run_async()
