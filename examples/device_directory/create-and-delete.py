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
"""Example showing creating and deleting devices in device catalog."""
from mbed_cloud.device_directory import DeviceDirectoryAPI
import random
import string


def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _main():
    api = DeviceDirectoryAPI()

    # Create a new device
    print("Creating new device...")
    device = {
        "certificate_issuer_id": _id_generator(12),
        "certificate_fingerprint": _id_generator(12)
    }
    new_device = api.add_device(**device)
    print("Successfully created device with id: %r" % new_device.id)

    # Update device
    updated_device = api.update_device(new_device.id,
                                       certificate_fingerprint=new_device.certificate_fingerprint,
                                       certificate_issuer_id=_id_generator(12))

    # Delete the device
    print("Attempting to delete device from catalog...")
    api.delete_device(updated_device.id)
    print("Successfully deleted device (ID: %r)" % updated_device.id)


if __name__ == "__main__":
    _main()
