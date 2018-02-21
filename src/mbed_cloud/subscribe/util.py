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
import threading
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
        self._func = func
        self._concurrency_provider = (
            concurrency_provider or
            asyncio.get_event_loop() if six.PY3 and concurrency_provider is False else ThreadPool(processes=1)
        )
        self._is_asyncio_provider = six.PY3 and not isinstance(self._concurrency_provider, ThreadPool)
        self._is_awaitable = self._is_asyncio_provider and (
                isinstance(self._func, asyncio.Future) or
                asyncio.iscoroutinefunction(self._func) or
                asyncio.iscoroutine(self._func)
        )
        self._deferable = None
        self._blocked = None

        self._lock = threading.Lock()

    def defer(self, *args, **kwargs):
        """Initialise a deferred call to the function - returns an asynchronous object.

        The calling code will need to check for the result at a later time.

        In Python 2/3 - an AsyncResult
            (https://docs.python.org/2/library/multiprocessing.html#multiprocessing.pool.AsyncResult)

        In Python 3 - a Future
            (https://docs.python.org/3/library/asyncio-task.html#future)

        :param args:
        :param kwargs:
        :return:
        """
        if self._blocked:
            raise RuntimeError('Already activated this deferred call by blocking on it')
        with self._lock:
            if not self._deferable:
                func_partial = functools.partial(self._func, *args, **kwargs)

                # we are either:
                # - pure asyncio
                # - asyncio but with blocking function
                # - not asyncio, use threadpool
                self._deferable = (
                    asyncio.ensure_future(func_partial(), loop=self._concurrency_provider)
                    if self._is_awaitable else (
                        self._concurrency_provider.run_in_executor(func=self._func, executor=None)
                        if self._is_asyncio_provider else (
                            self._concurrency_provider.apply_async(self._func)
                        )
                    )
                )
        return self._deferable

    def block(self, *args, **kwargs):
        """Call the wrapped function in a blocking fashion - returns the result of the function call

        :param args:
        :param kwargs:
        :return: result of function call
        """
        if self._deferable:
            raise RuntimeError('Already activated this call by deferring it')
        with self._lock:
            if not hasattr(self, '_result'):
                self._result = (
                    self._concurrency_provider.run_until_complete(self.defer(*args, **kwargs))
                    if self._is_asyncio_provider else self._func(*args, **kwargs)
                )
            self._blocked = True
        return self._result
