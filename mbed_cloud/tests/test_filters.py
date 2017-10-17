import datetime
import unittest

from mbed_cloud.tests.common import BaseCase
from mbed_cloud.device_directory import Device
from mbed_cloud import BaseAPI
from mbed_cloud import CloudValueError


class TestFilters(BaseCase):
    """Check filters"""

    @classmethod
    def setUpClass(cls):
        cls.api = BaseAPI()

    def _run(self, expected, **kwargs):
        outcome = self.api._verify_filters(kwargs, Device, True)
        self.assertEqual(outcome, expected)

    def test_simple_invalid(self):
        with self.assertRaises(CloudValueError):
            self._run(None, filters=1337)

    def test_simple_valid(self):
        filters = {
            'created_at': {'$gte': datetime.datetime(2017, 1, 1),
                           '$lte': datetime.datetime(2017, 12, 31)
                           }
        }
        self._run(
            {u'filter': 'created_at__lte=2017-12-31T00%253A00%253A00Z&created_at__gte=2017-01-01T00%253A00%253A00Z'},
            filter=filters
        )

    def test_simple_plural_valid(self):
        filters = {
            'created_at': {'$gte': datetime.datetime(2017, 1, 1),
                           '$lte': datetime.datetime(2017, 12, 31)
                           }
        }
        self._run(
            {u'filter': 'created_at__lte=2017-12-31T00%253A00%253A00Z&created_at__gte=2017-01-01T00%253A00%253A00Z'},
            filters=filters
        )

    @unittest.expectedFailure
    def test_simple_empty(self):
        # FIXME: why are we allowed to use `filter` or `filters`? too permissive.
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
            {u'filter': 'nuthing__lte=2017-12-31T00%253A00%253A00Z&nuthing__gte=2017-01-01T00%253A00%253A00Z'},
            filters=filters
        )

    def test_simple_known_field_remap(self):
        # 'alias' -> 'endpoint_name'
        filters = {
            'alias': {'$eq': 5}
        }
        self._run({u'filter': 'endpoint_name=5'}, filters=filters)
