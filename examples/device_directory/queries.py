# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Example showing devices from device query service."""
from mbed_cloud import DeviceDirectoryAPI
import random
import string
import uuid


def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _main():
    api = DeviceDirectoryAPI()

    # Pretty print all the registered queries
    for idx, e in enumerate(api.list_queries(limit=5)):
        print(e)

    # Create a new query
    new_query = api.add_query("test_filter", {'device_id': {'$eq': str(uuid.uuid4())}})
    print("\nCreated new query: %r" % (new_query.name))

    # Delete same query
    api.delete_query(new_query.id)
    print("Deleted newly created query")

    # Create more complex query
    print("Creating complex query")
    new_c_query = api.add_query("complex_test_query %s" % _id_generator(), {
        'device_id': {'$eq': str(uuid.uuid4())},
        'auto_update': {'$eq': True},
        'state': {'$eq': 'bootstrapped'},
        'device_class': {'$eq': 'embedded'},
        'serial_number': {'$eq': '1234'},
        'vendor_id': {'$eq': 'Arm'},
        'description': {'$eq': 'Loreum ipsum'},
        'device_name': {'$eq': 'DeviceName'},
        'custom_attributes': {
            'customA': {'$eq': 'SomethingA'},
            'customB': {'$eq': 'Something B'}
        }
    })

    # Manually get it
    gf = api.get_query(new_c_query.id)
    print("Got query %r using 'get'" % gf.name)
    # Update the query
    new_filter_dict = gf.filter
    new_filter_dict['serial_number']['$eq'] = '12345'
    updated_gf = api.update_query(
        query_id=gf.id,
        name=gf.name,
        filter=new_filter_dict
    )
    # Check it was successful
    assert updated_gf.filter['serial_number']['$eq'] == '12345'
    print("Updated query with new serial number")

    # Find device using query object
    print("Find devices that are matching the created query")
    devicesResponse = api.list_devices(filters=updated_gf.filter)
    # Print all devices that are matching provided query
    print(list(devicesResponse))

    # And delete that too
    api.delete_query(new_c_query.id)
    print("Deleted complex query")


if __name__ == "__main__":
    _main()
