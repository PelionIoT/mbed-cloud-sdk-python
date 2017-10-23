import datetime

from tests.common import BaseCase
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud.connect import ConnectAPI
from mbed_cloud.connect import Metric

start = datetime.datetime(year=2017, month=6, day=15)
end = datetime.datetime(year=2017, month=6, day=20)


class TestMetrics(BaseCase):

    @classmethod
    def setUpClass(cls):
        cls.api = ConnectAPI()
        # some arbitrary period
        cls.metrics = cls.api.list_metrics(
            start=start,
            end=end,
        )

    def test_verify_arguments(self):
        kwargs = dict(irrelevant=5)
        with self.assertRaises(CloudValueError) as e:
            self.api._verify_arguments(interval='1d', kwargs=kwargs)
        self.assertIn('period is not specified', e.exception.message)

    def test_verify_arguments_interval_invalid(self):
        kwargs = dict(period='3h')
        with self.assertRaises(CloudValueError) as e:
            self.api._verify_arguments(interval='1dog', kwargs=kwargs)
        self.assertIn('interval is incorrect', e.exception.message)

    def test_verify_arguments_period(self):
        kwargs = dict(period='3h')
        self.api._verify_arguments(interval='1d', kwargs=kwargs)
        self.assertEqual({'period': '3h'}, kwargs)

    def test_verify_arguments_period_invalid(self):
        kwargs = dict(period='3horses')
        with self.assertRaises(CloudValueError) as e:
            self.api._verify_arguments(interval='1d', kwargs=kwargs)
        self.assertIn('period is incorrect', e.exception.message)

    def test_verify_arguments_start(self):
        kwargs = dict(period=5, start=start)
        with self.assertRaises(CloudValueError) as e:
            self.api._verify_arguments(interval='1d', kwargs=kwargs)
        self.assertIn('end is required', e.exception.message)

    def test_verify_arguments_end(self):
        kwargs = dict(period=5, end=end)
        with self.assertRaises(CloudValueError) as e:
            self.api._verify_arguments(interval='1d', kwargs=kwargs)
        self.assertIn('start is required', e.exception.message)

    def test_metrics(self):
        props = Metric._get_attributes_map()
        inverse_props = {v: k for k, v in props.items()}
        a_metric = Metric(inverse_props)
        parts = {prop: getattr(a_metric, prop) for prop in props}
        self.assertEqual(parts['successful_bootstraps'], 'successful_bootstraps')

    def test_metrics_map_include(self):
        included = Metric._map_includes(['handshakes'])
        self.assertEqual('handshakes_successful', included)
