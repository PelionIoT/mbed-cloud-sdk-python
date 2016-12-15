"""Example showing devices from device catalog."""
from mbed_cloud.devices import DeviceAPI


def _print_device(idx, d):
    print("%d) %s | %s | %s" % (idx, d.device_id, d.state, d.created_at))


def _main():
    api = DeviceAPI()

    # List all devices, ordering by the most recently created first.
    devices = api.list_devices(order='desc', limit=10)
    for idx, d in enumerate(devices):
        _print_device(idx + 1, d)

    print("\n" + "-" * 30 + "\n")

    # Now only list the devices that are registered.
    filters = {
        'state': 'registered'
    }
    registered = api.list_devices(order='desc', limit=10, filters=filters)
    for idx, d in enumerate(registered):
        _print_device(idx + 1, d)

if __name__ == "__main__":
    _main()
