import functools
import logging
import queue
import warnings

from mbed_cloud.subscribe.subscribe import SubscriptionsManager
from mbed_cloud.subscribe.util import ConcurrentCall


class Observer(object):
    """Basically an async stream

    This system should abstract async concepts to the end application
    so that native async logic can be used if available -

    awaitables/futures/callbacks

    or blocking behaviour on these
    """
    # module-level singleton, with that django-familiar feel
    objects = SubscriptionsManager()

    def __init__(self, filters=None, queue_size=0, once=False, provider=None, timeout=None):

        # a notification storage queue that will grow if the user does not consume
        # inbound data, up to the queue size (after which, new data will be discarded)
        # this could be replaced with asyncio.Queue in py3
        self._notifications = queue.Queue(maxsize=queue_size)
        self._once = once
        self._once_done = False
        self._timeout = timeout
        self._filters = filters

        # a queue of internally waitable objects
        self._waitables = queue.Queue()

        # provider is passed straight to the ConcurrentCall abstraction
        # if you are using asyncio you can pass your current event loop here and receive Futures
        # (although underneath this will still use an executor, until such time
        # as the library fully supports Py3 asyncio)
        self._provider = provider

        # callbacks, if you want those instead
        self._callbacks = []

        self._latest_item = None
        self._iter_count = 0
        self._subscription_started = None

    def __iter__(self):
        return self

    def __next__(self):
        """Generates abstracted waitables (a new subscriber)

        They will be fulfilled in the order they were created,
        matching the order of new inbound notifications
        """
        waitable = queue.Queue(maxsize=1)
        getter = functools.partial(waitable.get, timeout=self._timeout)
        self._latest_item = ConcurrentCall(
            func=getter,
            concurrency_provider=self._provider
        )
        try:
            # get latest notification
            data = self._notifications.get_nowait()
        except queue.Empty:
            # store the consumer
            self._waitables.put(waitable)
        else:
            # if we have a notification, pass it to the consumer immediately
            waitable.put_nowait(data)
        return self._latest_item

    def next(self):
        """Next item in sequence (Python 2 compatibility)"""
        return self.__next__()

    def filter_notification(self, data):
        """Given some data, return True if this Observer should trigger"""
        return True

    def notify(self, data):
        """Notify this observer that data has arrived"""
        logging.debug('notify received: %s', data)
        if self._once_done and self._once:
            logging.debug('notify skipping due to `once`')
            return self
        if self.filter_notification(data):
            try:
                # notify next consumer immediately
                self._waitables.get_nowait().put_nowait(data)
                logging.debug('found a consumer, notifying')
            except queue.Empty:
                # store the notification
                logging.debug('no consumers, queueing data')
                try:
                    self._notifications.put_nowait(data)
                except queue.Full:
                    logging.warn('notification queue full - discarding new data')

            # callbacks are sent straight away
            # bombproofing should be handled by individual callbacks
            for callback in self._callbacks:
                logging.debug('callback: %s', callback)
                callback(data)
            self._once_done = True
        return self

    def add_callback(self, fn):
        """Register a callback, triggered when new data arrives"""
        warnings.warn('Instead of callbacks, consider using Futures or AsyncResults')
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