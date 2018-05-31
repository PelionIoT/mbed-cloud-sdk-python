from mbed_cloud import ConnectAPI

from tests.common import BaseCase

import os
import threading
import unittest


def worker(id, start, api, device, total):
    print('new worker', id)
    start.wait()
    for i in range(total):
        value = api.get_resource_value(device_id=device.id, resource_path='/3/0/1')
        print('%6s\t%6s\t%s' % (id, i, value))


@unittest.skipIf(os.environ.get('CI'), 'Do not run in CI')
class Test(BaseCase):
    def test(self):
        api = ConnectAPI()
        device = api.list_connected_devices().first()
        start = threading.Event()
        threads = []
        for i in range(20):
            t = threading.Thread(target=worker, args=(i, start, api, device, 100))
            t.daemon = True
            t.start()
            threads.append(t)
        start.set()
        [t.join() for t in threads]
