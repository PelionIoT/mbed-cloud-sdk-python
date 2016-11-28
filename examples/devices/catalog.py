"""Example showing devices from device catalog."""
from mbed_cloud_sdk.devices import DevicesAPI


def _main():
    api = DevicesAPI()
    devices = api.list_devices()
    print(len(devices))

if __name__ == "__main__":
    _main()
