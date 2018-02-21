from six.moves import queue
import warnings
from mbed_cloud.subscribe.util import ConcurrentCall
"""
usages


mbed_cloud
connectAPI.subscribe.device_state_changes(device_id=a).add_callback(blah).wait()

while true:
    connectAPI.subscribe.device_state_changes(device_id=a, state=deregistered).wait()

<python3>
for my_future in connectAPI.subscribe.device_state_changes(device_id=None):
    await my_future

<python2>
for my_tpe in connectAPI.subscribe.device_state_changes(device_id=None):
    my_tpe.get()


if you want to put stuff in a queue:
q = Queue.Queue()
connectAPI.subscribe.device_state_changes(device_id=None).add_callback(q.put)
while True:
    q.get()


"""


class IterQueue(queue.Queue):
    _sentinel = object()
    def __iter__(self):
        return iter(self.get, self.sentinel)

    def __next__(self):
        return self.get()

    def next(self):
        """Next item in sequence (Python 2 compatibility)"""
        return self.__next__()

    def close(self):
        self.put(self._sentinel)


class SubscriptionsManager(object):
    """Abstracts channels for userland

    We have four channels for device state

    One channel for resource subscriptions/presubscriptions

    One for getting current resource value

    This system should abstract the mapping between available API channels
    and watchers/observers that expose awaitables/futures/callbacks to the
    end application

    If that involves creating a new actual subscription, then do it
    """

    class SIGNALS:
        DEVICE_STATE_CHANGES='DEVICE_STATE_CHANGES'
        RESOURCE_VALUE_CURRENT='RESOURCE_VALUE_CURRENT'
        RESOURCE_VALUE_CHANGES='RESOURCE_VALUE_CHANGES'

    def __init__(self):
        self._routing = {}
        self._observers = []

    def routing_key(self, signal_key, **filter_keys):
        return [signal_key] + sorted(list(set(filter_keys)))

    def get_or_create_route(self, signal_key, **filter_keys):
        key = self.routing_key(signal_key, **filter_keys)
        return self._routing.setdefault(key, None)

    def get_or_create_observer(self, signal_key, **filter_keys):
        # ensure_notifications_started ?!?
        existing = self.get_or_create_route(signal_key, data)
        if existing:
            return existing
        if self.signal_key == self.SIGNALS.DEVICE_STATE_CHANGES:
            # no need to create a subscription
            # but we do need
            pass

    def list_all(self):
        return self._observers[:]

    def unsubscribe_all(self):
        # DO UNSUBSCRIBE ON SERVER
        for observer in self._observers:
            observer
        pass

    def device_state_changes(self, device_id=None, **params):
        pass

    def resource_value_current(self, device_id, resource_path, **params):
        pass

    def resource_value_changes(self, **params):
        pass


class Observer(object):
    """Basically an async stream

    This system should abstract async concepts to the end application
    so that native async logic can be used if available -

    awaitables/futures/callbacks

    or blocking behaviour on these
    """
    # module-level singleton, with that django-familiar feel
    objects = SubscriptionsManager()

    def __init__(self, signal_key=None, filters=None, queue_size=0, once=False, provider=None, timeout=None):

        # a backing queue that will grow if the user does not consume
        # inbound data
        # this could be replaced with asyncio.Queue in py3
        self._queue = IterQueue(maxsize=queue_size)
        self._once = once
        self._timeout = timeout

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

    @property
    def queue(self):
        """The raw iterable queue behind this observer"""
        return self._queue

    @property
    def latest_item(self):
        """The most recent item read from the queue"""
        return self._latest_item

    def _start_subscription(self):
        """Actually do a subscription, if there isn't one already"""
        if not self._subscription_started:
            # DO SOMETHING
            self._subscription_started = True
        return self

    def pull_from_queue(self, **kwargs):
        return self._queue.next()

    def __iter__(self):
        return self

    def __next__(self):
        self._latest_item = ConcurrentCall(func=, concurrency_provider=self._provider)
        return self._latest_item

    def next(self):
        """Next item in sequence (Python 2 compatibility)"""
        return self.__next__()

    def filter_notification(self, data):
        return True

    def notify(self, data):
        """Notify this observer that data has arrived"""
        if self.filter_notification(data):
            self._queue.put_nowait(data)
            if self._once:
                self._queue.close()

            # callbacks are sent straight away
            # bombproofing should be handled by individual callbacks
            for callback in self._callbacks:
                callback(data)
        return self

    def add_callback(self, fn):
        """Register a callback, triggered when new data arrives"""
        warnings.warn('Instead of callbacks, consider using Futures')
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
