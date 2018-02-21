import unittest
import uuid
from mbed_cloud.subscribe import util
from mbed_cloud.subscribe import subscribe
import itertools
from tests.common import BaseCase

Thing = util.ConcurrentCall


class Test(BaseCase):
    def setUp(self):
        self.unique_string = str(uuid.uuid4())

    def test_ordered(self):
        obs = subscribe.Observer()

        # one notification
        obs.notify('a')

        # two awaitables
        a = obs.next()
        b = obs.next()
        self.assertNotEqual(a, b)

        # three notifications
        obs.notify('b')
        c = obs.next()
        print(a, b, c)
        self.assertEqual(a.block(), 'a')

        # FIXME : ----------->
        # got this far.... and it doesn't work
        # needs more coffee

        # self.assertEqual(b.block(), 'b')
        #
        # # another awaitable
        # c = obs.next()


    @unittest.skip('this one is for unordered consumption')
    def test_unordered(self):
        """Trying future tasks"""
        obs = subscribe.Observer()

        conc_thing1 = obs.next()
        deferred1 = conc_thing1.defer()
        # in threadpool land we have 'ready'
        self.assertFalse(deferred1.ready())

        conc_thing2 = obs.next()
        deferred2 = conc_thing2.defer()
        self.assertFalse(deferred2.ready())

        # nothing has been removed from the queue, so these are referring to the same threads
        self.assertEqual(conc_thing1, conc_thing2)

        # and the 'defer' are the same defers
        self.assertEqual(deferred1, deferred2)

        obs.notify(dict(x=1))
        obs.notify(dict(x=2))
        obs.notify(dict(x=3))
        self.assertEqual(deferred1.get(), dict(x=1))
        self.assertEqual(deferred1.get(), dict(x=1))
        with self.assertRaises(RuntimeError):
            self.assertEqual(conc_thing1.block(), dict(x=2))

        conc_thing3 = obs.next()
        self.assertEqual(conc_thing3.defer().get(), dict(x=2))
        self.assertNotEqual(conc_thing1, conc_thing3)

        for thing in obs:
            self.assertEqual(thing.block(), dict(x=3))
            break

    @unittest.skip('this one is for unordered consumption')
    def test_push_pull(self):
        """Looping over the observer"""
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
