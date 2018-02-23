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
import threading
from mbed_cloud.subscribe.observer import Observer


class RoutingBase(object):
    def __init__(self):
        self._routes = {}
        self._lock = threading.Lock()

    def get_route_item(self, route):
        return self._routes.get(route)

    def get_or_create_routes(self, routes, item):
        """Stores a new item in route map

        Unless that exact route already exists - then returns existing item
        or partial route exists - then error
        """
        with self._lock:
            if any(route in self._routes for route in routes):
                new_routes = set(routes)
                overlap = new_routes.intersection(set(self._routes))
                if overlap == new_routes and len({self._routes[k] for k in overlap}) == 1:
                    # if they are all the same item, we can return that item from cache!
                    return self._routes[routes[0]]
                # otherwise, something weird is going on. can't mix and match routes:
                raise ValueError('route(s) already exist: %s' % (overlap,))

            [self._routes.setdefault(r, item) for r in routes]

    def remove_routes(self, routes):
        with self._lock:
            [self._routes.pop(r) for r in routes]

    def list_all(self):
        return list(set(self._routes.values()))




class ChannelSubscription(object):
    """Represents a subscription to a channel

    (In mbed terms, this may be a Presubscription or a Subscription)
    """
    _api = None
    _observer = None
    _routes = None

    def _get_routing_keys(self, **filter_keys):
        # TODO: expand lists
        return frozenset(sorted(list(filter_keys.items())))

    @property
    def observer(self):
        return self._observer

    def filter_notification(self):
        pass

    def notify(self, data):
        if self.filter_notification(data):
            self.observer.notify(data)

    def start(self, subs_controller, connect_api_instance, observer_params=None):
        self._subs_controller = subs_controller
        self._api = connect_api_instance
        observer_params = observer_params or {}
        self._observer = Observer(**observer_params)

    def ensure_started(self):
        pass

    def ensure_stopped(self):
        self.observer.cancel()


class ResourceValueCurrent(ChannelSubscription):
    def __init__(self, device_id, resource_path, **extra_filters):
        self.get_or_create_observer(
            self.CHANNELS.async_responses,
            device_id=device_id,
            resource_path=resource_path,
            **extra_filters
        )

    def ensure_started(self):
        """Start the channel (Idempotent)"""
        super(ResourceValueCurrent, self).ensure_started()
        self.connect_api_instance._add_subscription(
            device_id,
            resource
        )

    def ensure_stopped(self):
        """Stop the channel (Idempotent)"""
        self.connect_api_instance._delete_subscription(
            device_id,
            resource
        )
        super(ResourceValueCurrent, self).ensure_stopped()


class ResourceValueChanges(ChannelSubscription):
    def __init__(self, device_id, resource_path, **extra_filters):
        self.get_or_create_observer(
            self.CHANNELS.notifications,
            device_id=device_id,
            resource_path=resource_path,
            **extra_filters
        )

    def ensure_started(self):
        """Start the channel (Idempotent)"""
        super(ResourceValueChanges, self).ensure_started()
        self.connect_api_instance._add_subscription(
            device_id,
            resource
        )

    def ensure_stopped(self):
        """Stop the channel (Idempotent)"""
        self.connect_api_instance._delete_subscription(
            device_id,
            resource
        )
        super(ResourceValueChanges, self).ensure_stopped()


class DeviceStateChanges(ChannelSubscription):
    def __init__(self, device_id=None, **extra_filters):
        filters = {}
        if device_id:
            filters['device_id'] = device_id
        self.get_or_create_observer(
            self.CHANNELS.async_responses,
            **filters,
            **extra_filters
        )

    def ensure_started(self):
        """Start the channel (Idempotent)"""
        super(DeviceStateChanges, self).ensure_started()
        self.connect_api_instance._add_subscription(
            device_id,
            resource
        )

    def ensure_stopped(self):
        """Stop the channel (Idempotent)"""
        self.connect_api_instance._delete_subscription(
            device_id,
            resource
        )
        super(DeviceStateChanges, self).ensure_stopped()


class SubscriptionsManager(SubscriptionsManagerBase):


    class SIGNALS:
        DEVICE_STATE_CHANGES = 'DEVICE_STATE_CHANGES'
        RESOURCE_VALUE_CURRENT = 'RESOURCE_VALUE_CURRENT'
        RESOURCE_VALUE_CHANGES = 'RESOURCE_VALUE_CHANGES'

    class CHANNELS:
        notifications = 'notifications'
        async_responses = 'async_responses'
        registrations = 'registrations'
        de_registrations = 'de_registrations'
        reg_updates = 'reg_updates'
        registrations_expired = 'registrations_expired'

    channel_configs = {
        SIGNALS.DEVICE_STATE_CHANGES: dict(channels=[''], remote_filters=[]),
        SIGNALS.RESOURCE_VALUE_CURRENT: dict(channels=[''], remote_filters=['device_id', 'resource_path']),
        SIGNALS.RESOURCE_VALUE_CHANGES: dict(channels=['notifications'], remote_filters=['device_id', 'resource_path']),
    }

    def device_state_changes(self, device_id=None, **extra_filters):
        filters = {}
        if device_id:
            filters['device_id'] = device_id
        self.get_or_create_observer(
            self.CHANNELS.async_responses,
            **filters,
            **extra_filters
        )

    def resource_value_current(self, device_id, resource_path, **extra_filters):
        self.get_or_create_observer(
            self.CHANNELS.async_responses,
            device_id=device_id,
            resource_path=resource_path,
            **extra_filters
        )

    def resource_value_changes(self, device_id, resource_path, **extra_filters):
        self.get_or_create_observer(
            self.CHANNELS.notifications,
            device_id=device_id,
            resource_path=resource_path,
            **extra_filters
        )


class SubscriptionsManager(RoutingBase):
    """Tracks pub/sub state

    We have four channels for device state

    One channel for resource subscriptions/presubscriptions

    One for getting current resource value

    Some channels map to one logical channel - e.g. four device state channels
    Some channels are further filtered locally before notifying Observers

    This system should abstract the mapping between available API channels
    and observers that expose awaitables/futures/callbacks to the
    end application
    """

    def __init__(self):
        super(SubscriptionsManagerBase, self).__init__()
        self._routes.update(dict(
            notifications='notifications',
            async_responses='async_responses',
            registrations='registrations',
            de_registrations='de_registrations',
            reg_updates='reg_updates',
            registrations_expired='registrations_expired',
        ))

    def routing_key(self, **filter_keys):
        return frozenset(sorted(list(filter_keys.items())))

    def notify(self, data):
        for channel_name, items in data.items():
            for item in items:

    def unsubscribe_all(self):
        # DO BULK UNSUBSCRIBE ON SERVER?
        for observer in self._observers:
            observer.cancel()
        pass
