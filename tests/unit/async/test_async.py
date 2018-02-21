import six
import unittest
import uuid
from multiprocessing import pool
from mbed_cloud.subscribe import util

from tests.common import BaseCase

Thing = util.ConcurrentCall


class AsyncBase(BaseCase):
    abstract = True
    thing = None
    unique_string = None
    target = None

    test_delay = 0.02

    def setUp(self):
        self.unique_string = str(uuid.uuid4())

    def check_result(self, result):
        self.assertEqual(result, self.unique_string * 2)

    def get_async(self):
        return self.thing.defer(self.unique_string, delay=self.test_delay)

    def get_async_value(self, defer):
        raise NotImplementedError()

    def test_sync(self):
        self.check_result(self.thing.block(self.unique_string, delay=self.test_delay))

    def test_async(self):
        defer = self.get_async()
        result = self.get_async_value(defer)
        self.check_result(result)


@unittest.skipIf(not six.PY2, 'not currently running with python2 interpreter')
class Test2(AsyncBase):
    @classmethod
    def setUpClass(cls):
        super(Test2, cls).setUpClass()
        from tests.unit.async.b_call import slow
        cls.thing = Thing(func=slow)

    def get_async_value(self, defer):
        return defer.get()


class Test2CustomLoop(Test2):
    @classmethod
    def setUpClass(cls):
        super(Test2CustomLoop, cls).setUpClass()
        from tests.unit.async.b_call import slow
        tp = pool.ThreadPool(processes=1)
        cls.thing = Thing(func=slow, concurrency_provider=tp)


@unittest.skipIf(not six.PY3, 'not currently running with python3 interpreter')
class Test3(AsyncBase):
    loop = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        import asyncio
        from tests.unit.async import slow
        cls.target = slow
        cls.loop = asyncio.get_event_loop()
        cls.thing = Thing(func=cls.target)

    def get_async_value(self, defer):
        return self.loop.run_until_complete(defer)


class Test3CustomLoop(Test3):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        import asyncio
        cls.loop = asyncio.new_event_loop()
        cls.thing = Thing(concurrency_provider=cls.loop, func=cls.target)


class Test3CustomWrongLoop(Test3CustomLoop):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # silly us, we used a different loop compared to our testing code! this won't work.
        cls.thing = Thing(concurrency_provider=None, func=cls.target)

    def test_async(self):
        with self.assertRaises(ValueError):
            super().test_async()


class Test3DoesThreadsToo(Test3):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # if we wanted to, we could make our Thing use ThreadPools in python3.
        from tests.unit.async.b_call import slow
        cls.target = slow
        tp = pool.ThreadPool(processes=1)
        cls.thing = Thing(concurrency_provider=tp, func=cls.target)

    def get_async_value(self, defer):
        return defer.get()


# remove Base from keyspace so it's not picked up in test discovery
del AsyncBase
