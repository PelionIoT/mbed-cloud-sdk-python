"""Cross-version toolkit for concurrency concepts
"""
import six
from multiprocessing.pool import ThreadPool
if six.PY3:
    import asyncio


class ConcurrentCall:
    def __init__(self, func=None, concurrency_provider=None):
        """Wraps a potentially asynchronous function to provide a consistent API
        :param func: blocking call, asyncio coroutine or future
        :param concurrency_provider: ThreadPool or asyncio BaseEventLoop
        """
        self.func = func
        self.concurrency_provider = (
            concurrency_provider or
            asyncio.get_event_loop() if six.PY3 else ThreadPool(processes=1)
        )
        self.is_asyncio = not isinstance(self.concurrency_provider, ThreadPool)

    def defer(self, *args, **kwargs):
        """Initialise a deferred call to the function - returns an asynchronous object.
        The calling code will need to check for the result at a later time.

        In Python 2 - an AsyncResult
            (https://docs.python.org/2/library/multiprocessing.html#multiprocessing.pool.AsyncResult)

        In Python 3 - a Future
            (https://docs.python.org/3/library/asyncio-task.html#future)

        :param args:
        :param kwargs:
        :return:
        """
        if self.is_asyncio:
            return asyncio.ensure_future(self.func(*args, **kwargs), loop=self.concurrency_provider)
        return self.concurrency_provider.apply_async(self.func, args, kwargs)

    def block(self, *args, **kwargs):
        """Call the wrapped function in a blocking fashion - returns the result of the function call

        :param args:
        :param kwargs:
        :return: result of function call
        """
        if self.is_asyncio:
            promise = self.promise(*args, **kwargs)
            return self.concurrency_provider.run_until_complete(promise)
        # alternatively, to force using the threadpool in py2, self.promise(f,*,**).get() (but this seems wasteful)
        return self.func(*args, **kwargs)
