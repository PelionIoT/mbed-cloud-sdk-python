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
import six
if six.PY3:
    import asyncio


class ConcurrentCall(object):
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
        return (
            asyncio.ensure_future(self.func(*args, **kwargs), loop=self.concurrency_provider)
            if self.is_asyncio else self.concurrency_provider.apply_async(self.func, args, kwargs)
        )

    def block(self, *args, **kwargs):
        """Call the wrapped function in a blocking fashion - returns the result of the function call

        :param args:
        :param kwargs:
        :return: result of function call
        """
        return (
            self.concurrency_provider.run_until_complete(self.defer(*args, **kwargs))
            if self.is_asyncio else self.func(*args, **kwargs)
        )
