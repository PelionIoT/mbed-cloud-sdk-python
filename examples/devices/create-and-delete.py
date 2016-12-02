"""Example showing creating and deleting devices in device catalog."""
from mbed_cloud_sdk.devices import DeviceAPI
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
    new_device = api.create_device(**device)
    print("Successfully created device with device_id: %r" % new_device.device_id)

    # Delete the device
    print("Attempting to delete device from catalog...")
    api.delete_device(new_device.device_id)
    print("Successfully deleted device (ID: %r)" % new_device.device_id)

if __name__ == "__main__":
    _main()
