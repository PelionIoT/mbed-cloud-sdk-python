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
"""Example showing creating and deleting devices in device catalog."""
from mbed_cloud.devices import DeviceAPI
import random
import string


def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _main():
    api = DeviceAPI()

    # Create a new device
    print("Creating new device...")
    device = {
        "mechanism": "connector",
        "provision_key": _id_generator(12)
    }
    new_device = api.add_device(**device)
    print("Successfully created device with device_id: %r" % new_device.device_id)

    # Update device
    updated_device = api.update_device(new_device.id,
                                       provision_key=_id_generator(12),
                                       mechanism=new_device.mechanism)
    assert new_device.provision_key != updated_device.provision_key

    # Delete the device
    print("Attempting to delete device from catalog...")
    api.delete_device(new_device.device_id)
    print("Successfully deleted device (ID: %r)" % new_device.device_id)


if __name__ == "__main__":
    _main()
