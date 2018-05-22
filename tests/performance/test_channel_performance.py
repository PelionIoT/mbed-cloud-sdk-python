from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud.subscribe import channels

from tests.common import BaseCase

import inspect
import mock
import os
import timeit
import unittest


def bench(n):
    """Just a benchmarking function for relative expected performance"""
    items = [x for x in range(n)]
    return sum([x ** 2 for x in items])


@unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
class Test(BaseCase):
    @classmethod
    def setUpClass(cls):
        setup = inspect.getsource(bench)
        number = 500
        cls.bench = timeit.timeit(stmt='bench(1000)', setup=setup, number=number) / number

    def test_routing_performance(self):
        subs = SubscriptionsManager(mock.MagicMock())
        sample_id = 42
        sample = None
        # register a bunch of subscribers
        for i in range(1000):
            subs.subscribe(channels.ResourceValues(device_id=i))
            obs = subs.subscribe(channels.ResourceValues(device_id=i, resource_path=['/3/0/*', '/4/0/1']))
            if i == sample_id:
                sample = obs
            subs.subscribe(channels.ResourceValues(**{'device_id': i, str(i): 'abc'}))

        notification_count = 33
        start = timeit.default_timer()
        for i in range(notification_count):
            subs.notify({'notifications': [{'endpoint-name': str(42), 'resource-path': '/3/0/1'}]})
            subs.notify({'notifications': [{'endpoint-name': str(42), 'resource-path': '/3/1'}]})
            subs.notify({'notifications': [{'endpoint-name': str(5), 'resource-path': '/3/1'}]})
        stop = timeit.default_timer()
        duration = stop - start
        self.assertEqual(notification_count, sample.notify_count)

        # mildly contrived, but for cross-machine consistency we need
        # to use a benchmark to compare the lookup performance with
        self.assertLess(duration, 100 * self.bench)
