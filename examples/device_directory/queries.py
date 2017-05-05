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
from mbed_cloud.device_directory import DeviceDirectoryAPI
import random
import string
import urllib
import urlparse
import uuid

def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _main():
    api = DeviceDirectoryAPI()

    # Pretty print all the registered queries
    for idx, e in enumerate(api.list_queries(limit=5)):
        print(e)

    # Create a new query
    new_query = api.add_query("test_filter", {'device_id': { '$eq' : str(uuid.uuid4())}})
    print("\nCreated new query: %r" % (new_query.name))

    # Delete same query
    api.delete_query(new_query.id)
    print("Deleted newly created query")

    # Create more complex query
    print("Creating complex query")
    new_c_query = api.add_query("complex_test_query %s" % _id_generator(), {
        'device_id': { '$eq': str(uuid.uuid4())},
        'auto_update': { '$eq': True },
        'state': { '$eq': 'bootstrapped' },
        'device_class': { '$eq': 'embedded' },
        'serial_number': { '$eq': '1234' },
        'vendor_id': { '$eq': 'ARM' },
        'description': { '$eq': 'Loreum ipsum' },
        'device_name': { '$eq': 'DeviceName' },
        'custom_attributes': {
            'customA': { '$eq': 'SomethingA' },
            'customB': { '$eq': 'Something B' }
        }
    })

    # Manually get it
    gf = api.get_query(new_c_query.id)
    print("Got query %r using 'get'" % gf.name)
    # Update the query
    gf.filter['serial_number']['$eq'] = '12345'
    updated_gf = api.update_query(
        query_id=gf.id,
        name=gf.name,
        filter=gf.filter
    )
    # Check it was successful
    assert updated_gf.filter['serial_number']['$eq'] == '12345'
    print ("Updated query with new serial number")

    # And delete that too
    api.delete_query(new_c_query.id)
    print("Deleted complex query")


if __name__ == "__main__":
    _main()
