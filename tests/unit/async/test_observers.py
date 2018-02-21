import six
import unittest
import uuid
from multiprocessing import pool
from mbed_cloud.subscribe import util
from mbed_cloud.subscribe import subscribe
import itertools
from tests.common import BaseCase

Thing = util.ConcurrentCall


class Test(BaseCase):
    def setUp(self):
        self.unique_string = str(uuid.uuid4())

    def test_register(self):
        obs = subscribe.Observer()

        conc_thing1 = obs.next()
        deferred1 = conc_thing1.defer()
        # in threadpool land we have 'ready'
        self.assertFalse(deferred1.ready())

        conc_thing2 = obs.next()
        deferred2 = conc_thing2.defer()
        self.assertFalse(deferred2.ready())

        # these aren't the same observers. Maybe they should be
        self.assertNotEqual(conc_thing1, conc_thing2)

        obs.notify(dict(x=1))
        self.assertFalse(deferred2.ready())
        print(conc_thing1)
        print(conc_thing2.block())
        self.assertEqual(deferred1.wait(), dict(x=1))
        self.assertEqual(deferred2.wait(), dict(x=1))


    def test_push_pull(self):
        obs = subscribe.Observer()
        n = 7
        print(len(range(n)))
        # now we stream some new values
        for i in range(n):
            obs.notify(dict(i=i))
        # and we can read from them asynchronously
        items = []
        for new_item in itertools.islice(obs, 0, n-1):
            items.append(new_item.block().get('i'))
        self.assertEqual(items, list(range(6)))
