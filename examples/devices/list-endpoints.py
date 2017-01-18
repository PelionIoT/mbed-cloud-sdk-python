"""Example: listing endpoints and their resources using Device API."""
from mbed_cloud.devices import DeviceAPI


def _main():
    api = DeviceAPI()

    for device, idx in api.list_connected_devices().iteritems():
        resources = api.list_resources(device.id)

        # Print endpoint name header
        header = device.id
        print(header)
        print(len(header) * "-")

        for r in resources:
            print("\t- %s (%s / Observable: %s)" % (r.uri, r.name if r.name else "-", r.observable))

        # Space between endpoints
        print("")

if __name__ == "__main__":
    _main()
