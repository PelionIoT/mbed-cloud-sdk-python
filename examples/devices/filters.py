"""Example showing devices from device query service."""
from mbed_cloud.devices import DeviceAPI
import random
import string
import urllib
import urlparse
import uuid


def _print_filters(filters, start_idx=0):
    filters_str = []
    for idx, f in enumerate(filters):
        filters_str.append(_str_filter(f, idx=start_idx + idx + 1))
    print("\n\n".join(filters_str))


def _parse_filter_qs(f):
    qs = urlparse.parse_qs(urllib.unquote(f.query))
    return {key: ", ".join(value) for (key, value) in qs.iteritems()}


def _str_filter(f, idx):
    name = f.name
    filters = _parse_filter_qs(f)
    s = "%d) %s\n%s\n" % (idx, f.name, "-" * len(name))
    s += "\n".join(["%s = %s" % (k, v) for k, v in filters.iteritems()])
    return s


def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _main():
    api = DeviceAPI()

    # Pretty print all the registered filters
    for e, idx in api.list_filters(limit=5).iteritems():
        print(_str_filter(e, idx))

    # Create a new filter
    new_filter = api.add_filter("test_filter", {'device_id': str(uuid.uuid4())})
    print("\nCreated new filter: %r" % (new_filter.name))

    # Delete same filter
    api.delete_filter(new_filter.query_id)
    print("Deleted newly created filter")

    # Create more complex filter
    print("Creating complex filter")
    new_c_filter = api.add_filter("complex_test_filter %s" % _id_generator(), {
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

    # Manually get it
    gf = api.get_filter(new_c_filter.id)
    print("Got filter %r using 'get'" % gf.name)

    # Update the filter
    q = _parse_filter_qs(gf)
    q['serial_number'] = '12345'
    updated_gf = api.update_filter(
        filter_id=gf.id,
        name=gf.name,
        query=q
    )
    # Check it was successful
    assert _parse_filter_qs(gf)['serial_number'] == '1234'
    assert _parse_filter_qs(updated_gf)['serial_number'] == '12345'
    print ("Updated filter with new serial number")

    # And delete that too
    api.delete_filter(new_c_filter.query_id)
    print("Deleted complex filter")

if __name__ == "__main__":
    _main()
