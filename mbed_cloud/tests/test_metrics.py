import datetime

from mbed_cloud.tests.common import BaseCase
from mbed_cloud.connect import ConnectAPI
from mbed_cloud.connect import Metric


class TestMetrics(BaseCase):
    """Check filters"""

    @classmethod
    def setUpClass(cls):
        cls.api = ConnectAPI()
        # some arbitrary period
        cls.metrics = cls.api.list_metrics(
            start=datetime.datetime(year=2017, month=6, day=15),
            end=datetime.datetime(year=2017, month=6, day=20),
        )

    def test_metrics(self):
        metrics = list(self.metrics)
        # 5 days with interval of 1 day
        self.assertEqual(len(metrics), 5)
        a_metric = metrics[-1]
        props = Metric._get_attributes_map()
        # exercise all the getters
        parts = {prop: getattr(a_metric, prop) for prop in props}
        self.assertEqual(parts['handshakes'], 0)
