import datetime

from tests.common import BaseCase
from mbed_cloud.device_directory import Device
from mbed_cloud.core import BaseAPI
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud.filters import OP
import json

simple_filter = {
    'created_at': {
        OP.GTE: datetime.datetime(2017, 1, 1),
        OP.LTE: datetime.datetime(2017, 12, 31),
   },
}

many_types_filter = {
    'last_deployment': {
        OP.EQ: 'yellow',
        '$gte': datetime.datetime(2017, 1, 1),
    },
    'vendor_id': 'green',
    'device_execution_mode': {
        'gte': 5,
    },
    'state': True,
    'name': False,
    'firmware_checksum': None,
}


class TestFilters(BaseCase):

    @classmethod
    def setUpClass(cls):
        cls.api = BaseAPI()

    def _run(self, expected, encode=True, **kwargs):
        outcome = self.api._verify_filters(kwargs, Device, encode)
        self.assertEqual(expected, outcome)

    def test_simple_invalid(self):
        with self.assertRaises(CloudValueError):
            self._run(None, filters=1337)

    def test_simple_valid(self):
        self._run(
            {u'filter': 'created_at__gte=2017-01-01T00%3A00%3A00Z&created_at__lte=2017-12-31T00%3A00%3A00Z'},
            filter=simple_filter
        )

    def test_simple_plural_valid(self):
        # FIXME: why are we allowed to use `filter` or `filters`? too permissive.
        self._run(
            {u'filter': 'created_at__gte=2017-01-01T00%3A00%3A00Z&created_at__lte=2017-12-31T00%3A00%3A00Z'},
            # note plural 'filters' phrase
            filters=simple_filter
        )

    def test_noencode(self):
        self._run(
            {
                'vendor_id__eq': 'green', 'deployment__eq': 'yellow', 'deployment__gte': '2017-01-01T00:00:00Z',
                'firmware_checksum__eq': None, 'name__eq': False, 'state__eq': True, 'device_execution_mode__gte': 5,
            },
            filters=many_types_filter,
            encode=False
        )

    def test_encode(self):
        this_filter = {'device_class': 'red & "yellow", <green>'}
        this_filter.update(many_types_filter)
        self._run(
            {'filter': (
                'deployment=yellow'
                '&deployment__gte=2017-01-01T00%3A00%3A00Z'
                '&device_class=red+%26+%22yellow%22%2C+%3Cgreen%3E'
                '&device_execution_mode__gte=5'
                '&firmware_checksum=None'
                '&name=False'
                '&state=True'
                '&vendor_id=green'
            )},
            filters=this_filter,
            encode=True
        )

    def test_simple_empty(self):
        filters = {}
        self._run({}, filter=filters)

    def test_simple_plural_empty(self):
        filters = {}
        self._run({}, filters=filters)

    def test_empty_with_other_params(self):
        # noop for non-filter fields
        filters = {}
        self._run(dict(sort=5, order=6, other='yes'), filter=filters, sort=5, order=6, other='yes')

    def test_simple_unknown_field(self):
        filters = {
            'nuthing': {'$gte': datetime.datetime(2017, 1, 1),
                        '$lte': datetime.datetime(2017, 12, 31)
            }
        }
        with self.assertRaises(CloudValueError):
            self._run(
                {
                    u'filter': 'nuthing__gte=2017-01-01T00%3A00%3A00Z&nuthing__lte=2017-12-31T00%3A00%3A00Z',
                    'other_stuff': None
                },
                filters=filters,
                other_stuff=None
            )

    def test_simple_known_field_remap(self):
        # 'alias' -> 'endpoint_name'
        filters = {
            'alias': {'$eq': 5}
        }
        self._run({u'filter': 'endpoint_name=5'}, filters=filters)

    def test_dont_mutate_my_stuff(self):
        # a direct call to the filter generator, checking that the input kwargs dictionary
        # is not modified by the call
        kwargs = dict(
            filters={
                'alias': {'$eq': 5}
            },
            other_thing={
                5: [6, 7, 8]
            }
        )
        before = json.dumps(kwargs)
        result = self.api._verify_filters(kwargs, Device, True)
        self.assertEqual(dict(filter='endpoint_name=5', other_thing={5: [6, 7, 8]}), result)
        self.assertEqual(before, json.dumps(kwargs))

    def test_custom_fields(self):
        filters = {
            'custom_attributes': many_types_filter,
            'name': 'red & yellow'
        }
        self.maxDiff = 1e5
        self._run({u'filter': (
                'custom_attributes__device_execution_mode__gte=5'
                '&custom_attributes__firmware_checksum=None'
                '&custom_attributes__last_deployment=yellow'
                '&custom_attributes__last_deployment__gte=2017-01-01T00%3A00%3A00Z'
                '&custom_attributes__name=False'
                '&custom_attributes__state=True'
                '&custom_attributes__vendor_id=green'
                '&name=red+%26+yellow'
            ),
            'other_stuff': 'yes'
        }, filters=filters, other_stuff='yes')
