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
import logging


def expand_dict_as_keys(d):
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
        (tuple(static + list(items)) for items in itertools.product(*to_product))
        if to_product else [static]
    )
    return [tuple(sorted(new_key)) for new_key in new_keys]


class RoutingConflict(KeyError):
    pass


class RoutingBase(object):
    """Two-level routing

    Level one - matches permanent keys
    Level two - optional keys
    """
    def __init__(self):
        self._routes = {}
        self._lock = threading.Lock()
        self._any_key = '_any_'

    def get_route_item(self, route):
        return self._routes.get(route)

    def get_or_create_routes(self, item, routes, sub_routes=None):
        """Stores a new item in routing map

        Unless that exact route already exists - then returns existing item
        or partial route exists - then error
        """
        sub_routes = sub_routes or [self._any_key]
        with self._lock:
            # check for existing exact matches
            # FIXME: use a top-level memoisation for performance (but invalidation is tricky)
            # or take a copy and only modify it if no conflicts (also yuk?)
            unique_conflicts = set()
            for route in routes:
                nested = self._routes.get(route, {})
                for sub_route in sub_routes:
                    existing = nested.get(sub_route)
                    unique_conflicts.add(existing)

            if len(unique_conflicts) == 1:
                if unique_conflicts != {None}:
                    return unique_conflicts.pop()
            else:
                raise RoutingConflict(
                    '%s/%s matched multiple different existing entries' % (
                        route,
                        sub_route
                    )
                )

            for route in routes:
                nested = self._routes.setdefault(route, {})
                for sub_route in sub_routes:
                    nested.setdefault(sub_route, item)
        return item

    def remove_routes(self, routes):
        with self._lock:
            [self._routes.pop(r) for r in routes]

    def list_all(self):
        return list(set(
            sub_route for route in self._routes.values() for sub_route in route.values()
        ))


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

    @property
    def channels(self):
        # TODO: useability review. Other patterns/best practises
        # should the channels be instantiated directly on the Manager already?
        from mbed_cloud.subscribe import channels
        return channels

    def get_channel(self, subscription_channel, **observer_params):
        keys = subscription_channel.get_routing_keys()
        extras = subscription_channel.get_extra_keys()
        [self.watch_keys.add(k_v[0]) for key in keys for k_v in key]
        channel = self.get_or_create_routes(subscription_channel, keys, extras)
        channel.configure(self, self.connect_api, observer_params)
        return channel

    def subscribe(self, subscription_channel, **observer_params):
        return self.get_channel(subscription_channel, **observer_params).ensure_started().observer
    __call__ = subscribe

    def notify(self, data):
        try:
            for channel_name, items in data.items():
                for item in items:
                    # inject the channel name to the data, for a flat structure
                    data = dict(item)
                    data.update(dict(channel=channel_name))

                    # pluck keys we care about
                    route_keys = expand_dict_as_keys({key_name: data[key_name] for key_name in self.watch_keys if key_name in data})
                    for route in route_keys:
                        subscribers = self.get_route_item(route)
                        if subscribers:
                            for subscriber in subscribers.values():
                                subscriber.notify(data)
        except Exception:  # noqa
            logging.exception('Subscription notification failed')

    # def unsubscribe_all(self):
    #     # DO BULK UNSUBSCRIBE ON SERVER?
    #     for route, sub_channel in self._routes.items():
    #         sub_channel.cancel()
