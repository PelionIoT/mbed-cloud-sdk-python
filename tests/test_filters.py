import datetime
import unittest

from tests.common import BaseCase
from mbed_cloud.device_directory import Device
from mbed_cloud import BaseAPI
from mbed_cloud import CloudValueError

simple_filter = {
    'created_at': {
        '$gte': datetime.datetime(2017, 1, 1),
        '$lte': datetime.datetime(2017, 12, 31),
   },
}

many_types_filter = {
    'banana': {
        'eq': 'yellow',
        '$gte': datetime.datetime(2017, 1, 1),
    },
    'apple': 'green',
    'size': {
        'gte': 5,
    },
    'on': True,
    'off': False,
    'nill': None,
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
            {u'filter': 'created_at__gte=2017-01-01T00%253A00%253A00Z&created_at__lte=2017-12-31T00%253A00%253A00Z'},
            filter=simple_filter
        )

    def test_simple_plural_valid(self):
        # FIXME: why are we allowed to use `filter` or `filters`? too permissive.
        self._run(
            {u'filter': 'created_at__gte=2017-01-01T00%253A00%253A00Z&created_at__lte=2017-12-31T00%253A00%253A00Z'},
            # note plural 'filters' phrase
            filters=simple_filter
        )

    def test_noencode(self):
        self._run(
            {
                'apple__eq': 'green', 'banana__eq': 'yellow', 'banana__gte': '2017-01-01T00:00:00Z',
                'nill__eq': None, 'off__eq': False, 'on__eq': True, 'size__gte': 5,
             },
            filters=many_types_filter,
            encode=False
        )

    @unittest.expectedFailure
    def test_encode(self):
        # FIXME: Update team needs this to pass as defined below.
        self._run(
            {'filter': 'apple=green&banana=yellow&banana__gte=2017-01-01T00:00:00Z&nill=None&off=False&on=True&size__gte=5'},
            filters=many_types_filter,
            encode=True
        )

    @unittest.expectedFailure
    def test_simple_empty(self):
        # FIXME: stupidity
        filters = {}
        self._run({'filters': {}}, filter=filters)

    def test_simple_plural_empty(self):
        filters = {}
        self._run({'filters': {}}, filters=filters)

    def test_simple_unknown_field(self):
        # we are highly permissive about filtering on unknown fields
        filters = {
            'nuthing': {'$gte': datetime.datetime(2017, 1, 1),
                        '$lte': datetime.datetime(2017, 12, 31)
                        }
        }
        self._run(
            {u'filter': 'nuthing__gte=2017-01-01T00%253A00%253A00Z&nuthing__lte=2017-12-31T00%253A00%253A00Z'},
            filters=filters
        )

    def test_simple_known_field_remap(self):
        # 'alias' -> 'endpoint_name'
        filters = {
            'alias': {'$eq': 5}
        }
        self._run({u'filter': 'endpoint_name=5'}, filters=filters)

    @unittest.expectedFailure
    def test_custom_fields(self):
        # FIXME: Update team needs this to pass as defined below.
        # custom fields are an explicit thing...
        filters = {
            'custom_attributes': many_types_filter
        }
        self._run({u'filter': (
            'custom_attributes__apple=green'
            '&custom_attributes__banana=yellow'
            '&custom_attributes__banana__gte=2017-01-01T00:00:00Z'
            '&custom_attributes__nill=None'
            '&custom_attributes__off=False'
            '&custom_attributes__on=True'
            '&custom_attributes__size__gte=5'
        )}, filters=filters)
