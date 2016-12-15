"""Example showing devices from device query service."""
from mbed_cloud.devices import DeviceAPI
import urllib
import urlparse
import uuid


def _print_filters(filters):
    filters_str = []
    for idx, f in enumerate(filters):
        name = f.name
        filters = urlparse.parse_qs(urllib.unquote(f.query))
        s = "%d) %s\n%s\n" % (idx + 1, f.name, "-" * len(name))
        s += "\n".join(["%s=%s" % (k, ", ".join(v)) for k, v in filters.iteritems()])
        filters_str.append(s)
    print("\n\n".join(filters_str))


def _main():
    api = DeviceAPI()

    # Pretty print all the registered filters
    filters = api.list_filters()
    _print_filters(filters)

    # Create a new filter
    new_filter = api.create_filter("test_filter", {'device_id': str(uuid.uuid4())})
    print("Created new filter: %r" % (new_filter.name))

    # Delete same filter
    api.delete_filter(new_filter.query_id)
    print("Deleted newly created filter")

    # Create more complex filter
    new_c_filter = api.create_filter("complex_test_filter", {
        'device_id': str(uuid.uuid4()),
        'auto_update': True,
        'state': 'bootstrapped',
        'device_class': 'embedded',
        'serial_number': '1234',
        'vendor_id': 'ARM',
        'description': 'Loreum ipsum',
        'device_name': 'DeviceName'
    }, {
        'customA': 'SomethingA',
        'customB': 'Something B'
    })

    # And delete that too
    api.delete_filter(new_c_filter.query_id)

if __name__ == "__main__":
    _main()
