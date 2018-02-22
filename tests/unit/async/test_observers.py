import itertools
import logging
import random
import six
import threading
import time

from mbed_cloud.subscribe import subscribe

from tests.common import BaseCase


class Test(BaseCase):
    def test_subscribe_first(self):
        obs = subscribe.Observer()
        a = obs.next()
        b = obs.next()
        obs.notify('a')
        obs.notify('b')
        obs.notify('c')
        self.assertNotEqual(a, b)
        self.assertEqual(a.block(), 'a')
        self.assertEqual(b.block(), 'b')

    def test_notify_first(self):
        obs = subscribe.Observer()
        obs.notify('a')
        obs.notify('b')
        obs.notify('c')
        a = obs.next()
        b = obs.next()
        self.assertNotEqual(a, b)
        self.assertEqual(a.block(), 'a')
        self.assertEqual(b.block(), 'b')

    def test_interleaved(self):
        obs = subscribe.Observer()
        obs.notify('a')
        a = obs.next()
        b = obs.next()
        c = obs.next()
        obs.notify('b')
        d = obs.next()
        obs.notify('c')
        obs.notify('d')
        obs.notify('e')
        e = obs.next()
        self.assertEqual(a.block(), 'a')
        self.assertEqual(b.block(), 'b')
        self.assertEqual(c.block(), 'c')
        self.assertEqual(d.block(), 'd')
        self.assertEqual(e.block(), 'e')

    def test_stream(self):
        """Looping over the observer with iteration"""
        obs = subscribe.Observer()
        n = 7
        # we stream some new values
        for i in range(n):
            obs.notify(dict(i=i))
        # and we can read from them asynchronously
        items = []
        for new_item in itertools.islice(obs, 0, n-1):
            items.append(new_item.block().get('i'))
        self.assertEqual(items, list(range(6)))

    def test_threaded_stream(self):
        """Behaviour in threaded environment"""
        obs = subscribe.Observer()
        n = 12
        start = threading.Event()
        sleepy = lambda: random.randrange(1, 3) / 1000.0

        def add_values():
            start.wait()
            for i in range(n):
                obs.notify(dict(a_key=i))
                time.sleep(sleepy())

        add = threading.Thread(target=add_values)
        add.daemon = True
        add.start()

        def read_values(result):
            start.wait()
            # finite iteration of infinite generator
            for new_item in itertools.islice(obs, 0, n - 1):
                result.append(new_item.block().get('a_key'))
                time.sleep(sleepy())

        results = []
        read = threading.Thread(target=read_values, args=(results,))
        read.daemon = True
        read.start()

        start.set()
        add.join()
        read.join()

        # the sequence of values from all the subscribers
        # should be in the same order as the data was added
        self.assertEqual(results, list(range(n-1)))

    def test_callback(self):
        """Callback is triggered on notification"""
        x = dict(a=1)

        def incr(n):
            x['a'] += n

        obs = subscribe.Observer()
        obs.add_callback(incr)
        obs.notify(3)

        self.assertEqual(x, dict(a=4))

    def test_callback_add_remove_clear(self):
        """Callbacks can be added and removed"""
        f = lambda: 5
        g = lambda: 6
        obs = subscribe.Observer()
        obs.add_callback(f)
        obs.add_callback(g)

        obs.remove_callback(f)
        self.assertEqual(obs._callbacks, [g])

        obs.clear_callbacks()
        self.assertEqual(obs._callbacks, [])

    def test_overflow(self):
        """Inbound queue overflows"""
        obs = subscribe.Observer(queue_size=1)
        obs.notify(1)
        if six.PY3:
            with self.assertLogs(level=logging.WARNING):
                obs.notify(1)
        obs.notify(1)
        self.assertTrue(obs.next().defer().get(0.05))

        # The second waiter will never resolve because the queue was too short
        waiter = obs.next().defer()
        waiter.wait(0.05)
        self.assertFalse(waiter.ready())
