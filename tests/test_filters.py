import datetime
import unittest

from tests.common import BaseCase
from mbed_cloud.device_directory import Device, DeviceDirectoryAPI
from mbed_cloud import BaseAPI
from mbed_cloud import CloudValueError
from unittest import mock


class MockResponseObject:
    """Response to return when mocking request calls."""
    status = 200
    reason = None
    data = b''


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
        filters = {
            'created_at': {'$gte': datetime.datetime(2017, 1, 1),
                           '$lte': datetime.datetime(2017, 12, 31)
                           }
        }
        self._run(
            {u'filter': 'created_at__gte=2017-01-01T00:00:00Z&created_at__lte=2017-12-31T00:00:00Z'},
            filter=filters
        )

    def test_encoding_is_not_over_applied(self):
        filters = {
            'updated_at': {'$gte': datetime.datetime(2017, 1, 1),
                           '$lte': datetime.datetime(2017, 12, 31)}
        }

        expected_filter = 'updated_at__gte=2017-01-01T00:00:00Z&updated_at__lte=2017-12-31T00:00:00Z'
        self._run({u'filter': expected_filter}, filters=filters)

        # Instantiate the device directory API with mocked request call
        device_directory = DeviceDirectoryAPI()
        device_directory.api_client.rest_client.pool_manager.request = mock.MagicMock(return_value=MockResponseObject())
        mocked_device_directory_request = device_directory.api_client.rest_client.pool_manager.request

        # Call the device directory API and assert that the filtering is correct
        device_directory.list_devices(filters=filters)
        request_call_args, request_call_kwargs = mocked_device_directory_request.call_args
        self.assertEqual(request_call_kwargs['fields'][0][0], 'filter')
        self.assertEqual(request_call_kwargs['fields'][0][1], expected_filter)

    def test_simple_plural_valid(self):
        filters = {
            'created_at': {'$gte': datetime.datetime(2017, 1, 1),
                           '$lte': datetime.datetime(2017, 12, 31)
                           }
        }
        self._run(
            {u'filter': 'created_at__gte=2017-01-01T00:00:00Z&created_at__lte=2017-12-31T00:00:00Z'},
            filters=filters
        )

    def test_simple_noencode(self):
        filters = {
            'banana': {'eq': 'yellow'},
            'apple': 'green',
        }
        self._run(
            {u'apple__eq': 'green', u'banana__eq': 'yellow'},
            filters=filters,
            encode=False
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
            {u'filter': 'nuthing__gte=2017-01-01T00:00:00Z&nuthing__lte=2017-12-31T00:00:00Z'},
            filters=filters
        )

    def test_simple_known_field_remap(self):
        # 'alias' -> 'endpoint_name'
        filters = {
            'alias': {'$eq': 5}
        }
        self._run({u'filter': 'endpoint_name=5'}, filters=filters)
