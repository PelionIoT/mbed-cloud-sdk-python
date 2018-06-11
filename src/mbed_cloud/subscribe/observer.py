# --------------------------------------------------------------------------
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
"""Observer"""
import functools
import logging
import queue
import threading

from mbed_cloud.subscribe.async_wrapper import AsyncWrapper

LOG = logging.getLogger(__name__)


class NoMoreNotifications(Exception):
    """Raised as a sentinel when a stream is terminated"""

    pass


class Observer(object):
    """An async stream generator (Future1, Future2, ... FutureN)

    This system should abstract async concepts to the end application
    so that native async logic can be used if available -

    awaitables/futures/callbacks

    or blocking behaviour on these
    """

    sentinel = NoMoreNotifications()

    def __init__(self, filters=None, queue_size=0, once=False, provider=None, timeout=None):
        """Observer

        An iterable that manufactures results or promises for a stream of data
        Observer[1..n] gives promises for data stream [1..n] and fulfills them in that order

        :param filters: Additional key-value pairs to whitelist inbound notifications
        :param queue_size: sets internal notification queue max length
        :param once: only retrieve one item
        :param provider:
        :param timeout:
        """
        # a notification storage queue that will grow if the user does not consume
        # inbound data, up to the queue size (after which, new data will be discarded)
        # this could be replaced with asyncio.Queue in py3
        self._notifications = queue.Queue(maxsize=queue_size)
        self._once = once
        self._once_done = False
        self._timeout = timeout
        self._filters = filters
        self._lock = threading.Lock()

        # a queue of internally waitable objects
        self._waitables = queue.Queue()

        # provider is passed straight to the ConcurrentCall abstraction
        # if you are using asyncio you can pass your current event loop here and receive Futures
        # (although underneath this will still use an executor, until such time
        # as the library fully supports Py3 asyncio)
        self._async_wrapper_class = AsyncWrapper
        self._provider = provider

        # callbacks, if you want those instead
        self._callbacks = []

        self._latest_item = None
        self._iter_count = 0
        self._notify_count = 0
        self._subscription_started = None
        self._cancelled = False

    @property
    def queue(self):
        """Direct access to the internal notification queue"""
        return self._notifications

    def __iter__(self):
        """Iterator"""
        return self

    def __next__(self):
        """Generates abstracted waitables (a new subscriber)

        They will be fulfilled in the order they were created,
        matching the order of new inbound notifications
        """
        waitable = queue.Queue(maxsize=1)
        getter = functools.partial(waitable.get, timeout=self._timeout)
        self._latest_item = self._async_wrapper_class(
            func=getter,
            concurrency_provider=self._provider
        )
        with self._lock:
            try:
                # get latest notification
                data = self._notifications.get_nowait()
            except queue.Empty:
                # store the consumer
                self._waitables.put(waitable)
                LOG.debug('no data for new consumer')
            else:
                # if we have a notification, pass it to the consumer immediately
                waitable.put_nowait(data)
                LOG.debug('new consumer taking next data immediately')
        return self._latest_item

    def next(self):
        """Next item in sequence (Python 2 compatibility)"""
        return self.__next__()

    def notify(self, data):
        """Notify this observer that data has arrived"""
        LOG.debug('notify received: %s', data)
        self._notify_count += 1
        if self._cancelled:
            LOG.debug('notify skipping due to `cancelled`')
            return self
        if self._once_done and self._once:
            LOG.debug('notify skipping due to `once`')
            return self
        with self._lock:
            try:
                # notify next consumer immediately
                self._waitables.get_nowait().put_nowait(data)
                LOG.debug('found a consumer, notifying')
            except queue.Empty:
                # store the notification
                try:
                    self._notifications.put_nowait(data)
                    LOG.debug('no consumers, queueing data')
                except queue.Full:
                    LOG.warning('notification queue full - discarding new data')

        # callbacks are sent straight away
        # bombproofing should be handled by individual callbacks
        for callback in self._callbacks:
            LOG.debug('callback: %s', callback)
            callback(data)
        self._once_done = True
        return self

    @property
    def notify_count(self):
        """Number of notifications received"""
        return self._notify_count

    def cancel(self):
        """Cancels the observer

        No more notifications will be passed on
        """
        LOG.debug('cancelling %s', self)
        self._cancelled = True
        self.clear_callbacks()  # not strictly necessary, but may release references
        while True:
            try:
                self._waitables.get_nowait().put_nowait(self.sentinel)
            except queue.Empty:
                break

    def add_callback(self, fn):
        """Register a callback, triggered when new data arrives

        As an alternative to callbacks, consider use of
        Futures or AsyncResults e.g. from `.next().defer()`
        """
        self._callbacks.append(fn)
        return self

    def remove_callback(self, fn):
        """Remove a registered callback"""
        self._callbacks.remove(fn)
        return self

    def clear_callbacks(self):
        """Remove all callbacks"""
        self._callbacks[:] = []
        return self
