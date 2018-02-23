import six
import unittest
import uuid
from multiprocessing import pool
from mbed_cloud.subscribe.async_wrapper import AsyncWrapper

from tests.common import BaseCase


class AsyncBase(BaseCase):
    abstract = True
    AsyncWrapper = None
    unique_string = None
    target = None

    test_delay = 0.02

    def setUp(self):
        self.unique_string = str(uuid.uuid4())[:3]

    def check_result(self, result):
        self.assertEqual(self.unique_string * 2, result)

    def get_async(self):
        return self.AsyncWrapper.defer(self.unique_string, delay=self.test_delay)

    def get_async_value(self, defer):
        """This is done differently in 2/3"""
        raise NotImplementedError()

    def test_sync(self):
        self.check_result(self.AsyncWrapper.block(self.unique_string, delay=self.test_delay))

    def test_async(self):
        defer = self.get_async()
        result = self.get_async_value(defer)
        self.check_result(result)


@unittest.skipIf(not six.PY2, 'Need Python 2 interpreter for this test')
class Test2(AsyncBase):
    def setUp(self):
        super(Test2, self).setUp()
        from tests.unit.async.b_call import slow
        self.AsyncWrapper = AsyncWrapper(func=slow)

    def get_async_value(self, defer):
        return defer.get()


class Test2CustomLoop(Test2):
    def setUp(self):
        super(Test2CustomLoop, self).setUp()
        from tests.unit.async.b_call import slow
        tp = pool.ThreadPool(processes=1)
        self.AsyncWrapper = AsyncWrapper(concurrency_provider=tp, func=slow)


@unittest.skipIf(not six.PY3, 'Need Python 3 interpreter for this test')
class Test3(AsyncBase):
    loop = None

    def setUp(self):
        super().setUp()
        import asyncio
        from tests.unit.async.a_call import slow
        self.target = slow
        self.loop = asyncio.get_event_loop()
        self.AsyncWrapper = AsyncWrapper(concurrency_provider=self.loop, func=self.target)

    def get_async_value(self, defer):
        return self.loop.run_until_complete(defer)


class Test3Executor(Test3):
    # use a Python3 event loop, but a blocking function underneath
    def setUp(self):
        super().setUp()
        import asyncio
        from tests.unit.async.b_call import slow
        self.target = slow
        self.loop = asyncio.get_event_loop()
        self.AsyncWrapper = AsyncWrapper(concurrency_provider=self.loop, func=self.target)


class Test3CustomLoop(Test3):
    def setUp(self):
        super().setUp()
        import asyncio
        self.loop = asyncio.new_event_loop()
        self.AsyncWrapper = AsyncWrapper(concurrency_provider=self.loop, func=self.target)


class Test3CustomWrongLoop(Test3CustomLoop):
    def setUp(self):
        super().setUp()
        import asyncio
        # silly us, we used a different loop compared to our testing code! this won't work.
        self.AsyncWrapper = AsyncWrapper(concurrency_provider=asyncio.new_event_loop(), func=self.target)

    def test_async(self):
        with self.assertRaises(ValueError):
            super().test_async()


class Test3DoesThreadsToo(Test3):
    def setUp(self):
        super().setUp()
        # if we wanted to, we could make our AsyncWrapper use ThreadPools in python3.
        from tests.unit.async.b_call import slow
        self.target = slow
        tp = pool.ThreadPool(processes=1)
        self.AsyncWrapper = AsyncWrapper(concurrency_provider=tp, func=self.target)

    def get_async_value(self, defer):
        return defer.get()


# remove Base from keyspace so it's not picked up in test discovery
del AsyncBase
