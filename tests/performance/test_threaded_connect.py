from mbed_cloud.connect import ConnectAPI
from mbed_cloud._backends.mds import NotificationsApi

from tests.common import BaseCase

import os
import threading
from multiprocessing.pool import ThreadPool
import unittest
import time
import random


def worker(start, api_key, results):
    print('hi')
    start.wait()  # let's all start at the same time
    print('go')
    api = ConnectAPI(dict(api_key=api_key))
    time.sleep(random.triangular(0.1, 0.2, 0.5))
    codegen_layer = api._get_api(NotificationsApi)
    key_set = codegen_layer.api_client.configuration.api_key['Authorization']
    print('get/set %r %r' % (api_key, key_set))
    results.append(key_set)


@unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
class Test(BaseCase):
    """Checks for #499 in which multiple concurrent calls somehow use the wrong config

    This was historically caused by `TypeWithDefault` from swagger codegen which tries to
    make config objects into module-wide singletons.
    """
    def test_concurrent_config(self):
        n = 50
        so_many_threads = ThreadPool(processes=n//2)
        start = threading.Event()
        results = []

        for i in range(n):
            so_many_threads.apply_async(worker, args=(start, str(i), results))
        so_many_threads.close()  # no more submissions
        time.sleep(1.0)  # wait for threads to get set up. we'd like a thundering herd.
        # (not as clean as managing threads ourselves)
        start.set()  # start!
        so_many_threads.join()  # wait for all tasks to complete

        failures = [i for i in range(n) if results.count(str(i)) != 1]
        print(results)
        self.assertFalse(failures)
