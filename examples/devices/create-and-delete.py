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
