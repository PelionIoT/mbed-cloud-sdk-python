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
"""Example showing devices from device query service."""
from mbed_cloud.devices import DeviceAPI
import random
import string
import urllib
import urlparse
import uuid


def _print_queries(queries, start_idx=0):
    queries_str = []
    for idx, f in enumerate(queries):
        queries_str.append(_str_query(f, idx=start_idx + idx + 1))
    print("\n\n".join(queries_str))


def _parse_query_qs(f):
    qs = urlparse.parse_qs(urllib.unquote(f.query))
    return {key: ", ".join(value) for (key, value) in qs.iteritems()}


def _str_query(f, idx):
    name = f.name
    queries = _parse_query_qs(f)
    s = "%d) %s\n%s\n" % (idx, f.name, "-" * len(name))
    s += "\n".join(["%s = %s" % (k, v) for k, v in queries.iteritems()])
    return s


def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _main():
    api = DeviceAPI()

    # Pretty print all the registered queries
    for idx, e in enumerate(api.list_queries(limit=5)):
        print(_str_query(e, idx))

    # Create a new query
    new_query = api.add_query("test_filter", {'device_id': str(uuid.uuid4())})
    print("\nCreated new query: %r" % (new_query.name))

    # Delete same query
    api.delete_query(new_query.id)
    print("Deleted newly created query")

    # Create more complex query
    print("Creating complex query")
    new_c_query = api.add_query("complex_test_query %s" % _id_generator(), {
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
    gf = api.get_query(new_c_query.id)
    print("Got query %r using 'get'" % gf.name)

    # Update the query
    q = _parse_query_qs(gf)
    q['serial_number'] = '12345'
    updated_gf = api.update_query(
        query_id=gf.id,
        name=gf.name,
        query=q
    )
    # Check it was successful
    assert _parse_query_qs(gf)['serial_number'] == '1234'
    assert _parse_query_qs(updated_gf)['serial_number'] == '12345'
    print ("Updated query with new serial number")

    # And delete that too
    api.delete_query(new_c_query.id)
    print("Deleted complex query")


if __name__ == "__main__":
    _main()
