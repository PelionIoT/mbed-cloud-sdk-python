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


