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
import itertools
from mbed_cloud.subscribe.observer import Observer


def dict_to_frozen(d):
    """Expands a dictionary into a keyable frozen set

    :param d: dictionary (of strings or lists)
    :returns: cartesian product of list parts
    """
    to_product = []
    static = []
    for key, values in sorted(d.items()):
        if isinstance(values, (list, tuple, set)):
            to_product.append(tuple((key, v) for v in values))
        else:
            static.append((key, values))
    new_keys = (
        ((*static, *items) for items in itertools.product(*to_product))
        if to_product else [static]
    )
    return [frozenset(sorted(new_key)) for new_key in new_keys]


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
        return item

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
    _manager = None
    _routes = None
    _optional_filters = None

    def get_routing_keys(self):
        return self._route_keys

    def get_extra_keys(self):
        return self._optional_filters

    @property
    def observer(self):
        return self._observer

    def filter_notification(self, data):
        # a further level of filtering for this channel
        for k, v in (self._optional_filters or {}).items():
            print('optional filter', k, v, data.get(k))
            if data.get(k) not in v:
                print('optional filter rejecting', k, v, data.get(k))
                return False
        return True

    def notify(self, data):
        if self.filter_notification(data):
            self.observer.notify(data)

    def start(self, manager, connect_api_instance, observer):
        self._manager = manager
        self._api = connect_api_instance
        self._observer = observer

    def ensure_started(self):
        pass

    def ensure_stopped(self):
        self.observer.cancel()
        self._manager.remove_routes(self.get_routing_keys())


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
    def __init__(self, connect_api):
        super(SubscriptionsManager, self).__init__()
        self.watch_keys = set()
        self.connect_api = connect_api

    def subscribe(self, subscription_channel, **observer_params):
        observer = Observer(**observer_params)
        subscription_channel.start(self, self.connect_api, observer)
        keys = subscription_channel.get_routing_keys()
        [self.watch_keys.add(k_v[0]) for key in keys for k_v in key]
        print('now watching', self.watch_keys)
        return self.get_or_create_routes(keys, subscription_channel).observer

    def notify(self, data):
        for channel_name, items in data.items():
            for item in items:
                # inject the channel name to the data, for a flat structure
                data = dict(item)
                data.update(dict(channel=channel_name))

                # pluck keys we care about
                route_keys = {key_name: data[key_name] for key_name in self.watch_keys if key_name in data}
                for route in dict_to_frozen(route_keys):
                    subscriber = self.get_route_item(route)
                    if subscriber is not None:
                        subscriber.notify(data)

    # def unsubscribe_all(self):
    #     # DO BULK UNSUBSCRIBE ON SERVER?
    #     for route, sub_channel in self._routes.items():
    #         sub_channel.cancel()
