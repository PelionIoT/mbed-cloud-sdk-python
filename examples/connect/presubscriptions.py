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
"""Example showing basic usage of device presubscriptions."""
from mbed_cloud.connect import ConnectAPI


def _main():
    api = ConnectAPI()
    devices = api.list_connected_devices()
    if not devices:
        raise Exception("No connected devices registered. Aborting")

    # get list of presubscriptions
    presubscriptions = api.list_presubscriptions()
    print("List of presubscriptions: %r" % presubscriptions)
    device_id = devices[0].id
    # Get list of resources on a device
    resources = api.list_resources(device_id)
    # Get observable resource
    resource_uri = filter(lambda r: r.observable, resources)[0].path
    # Set new presubscription
    api.update_presubscriptions([
        {
            "device_id": device_id,
            "resource_paths": [resource_uri]
        }
    ])
    # Subscription will be automatically set when a device with this id and resource path
    # will be connected

    # List presubscriptions
    presubscriptions = api.list_presubscriptions()
    print("List of presubscriptions after adding new presubscription: %r" % presubscriptions)
    # Delete presubscription
    api.delete_presubscriptions()
    presubscriptions = api.list_presubscriptions()
    print("List of presubscriptions after deleting all presubscriptions: %r" % presubscriptions)


if __name__ == "__main__":
    _main()
