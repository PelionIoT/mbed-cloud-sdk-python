# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

"""Cross-version toolkit for concurrency concepts"""
from builtins import object
from multiprocessing.pool import ThreadPool
import functools
import six
if six.PY3:
    import asyncio


class ConcurrentCall(object):
    """Wraps a potentially asynchronous function to provide a consistent API
    """

    def __init__(self, func=None, concurrency_provider=None):
        """Creates a wrapper for a potentially asynchronous function

        :param func: blocking call, asyncio coroutine or future
        :param concurrency_provider: ThreadPool or asyncio BaseEventLoop
                                    or None: default ThreadPool
                                    or False: default EventLoop
        """
        self.func = func
        self.concurrency_provider = (
            concurrency_provider or
            asyncio.get_event_loop() if six.PY3 and concurrency_provider is False else ThreadPool(processes=1)
        )
        self.is_asyncio_provider = six.PY3 and not isinstance(self.concurrency_provider, ThreadPool)
        self.is_awaitable = self.is_asyncio_provider and (
            isinstance(self.func, asyncio.Future) or
            asyncio.iscoroutinefunction(self.func) or
            asyncio.iscoroutine(self.func)
        )

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
        func_partial = functools.partial(self.func, *args, **kwargs)
        return (
            asyncio.ensure_future(func_partial(), loop=self.concurrency_provider)
            if self.is_awaitable else (
                self.concurrency_provider.run_in_executor(func=self.func, executor=None)
                if self.is_asyncio_provider else (
                    self.concurrency_provider.apply_async(self.func)
                )
            )
        )

    def block(self, *args, **kwargs):
        """Call the wrapped function in a blocking fashion - returns the result of the function call

        :param args:
        :param kwargs:
        :return: result of function call
        """
        return (
            self.concurrency_provider.run_until_complete(self.defer(*args, **kwargs))
            if self.is_asyncio_provider else self.func(*args, **kwargs)
        )
