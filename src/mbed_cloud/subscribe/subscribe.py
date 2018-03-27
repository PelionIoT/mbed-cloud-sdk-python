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
"""Subscriptions

This higher-level-abstraction aims to get the user code quickly from
defining a subscription, to acting on the data received

# callbacks
def callback(x):
    print(x)

connect_api.subscribe(device_state_changes(device_id=a)).add_callback(blah)

# blocking calls with filters
channel = connect_api.subscribe(device_state_changes(device_id=, state='deregistered'))
for result in channel:
    print(result.block())

# deferred in python3
for my_future in connect_api.subscribe(device_state_changes(device_id=None)):
    await my_future

# deferred in python2
for my_async_result in connect_api.subscribe(device_state_changes(device_id=None)):
    print(my_async_result.get())

# independently using a separate queue
q = Queue.Queue()
connect_api.subscribe(device_state_changes(device_id=None)).add_callback(q.put)
while True:
    print(q.get())
"""
import itertools
import logging
import threading


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
    """Routing Conflict"""

    pass


class RoutingBase(object):
    """Two-level routing

    Level one - matches permanent keys
    Level two - optional keys
    """

    def __init__(self):
        """Routes"""
        self._routes = {}
        self._lock = threading.Lock()
        self._any_key = '_any_'

    def get_route_item(self, route):
        """Get item attached to this route"""
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
                        routes,
                        sub_routes
                    )
                )

            # so assuming there were no conflicts, loop a second time to do the insertions
            for route in routes:
                nested = self._routes.setdefault(route, {})
                for sub_route in sub_routes:
                    nested.setdefault(sub_route, item)
        return item

    def remove_routes(self, routes):
        """Removes matching routes"""
        with self._lock:
            for r in routes:
                self._routes.pop(r)
                logging.debug('removed route %s', r)

    def list_all(self):
        """All routes"""
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
        """Subscriptions Manager"""
        super(SubscriptionsManager, self).__init__()
        self.watch_keys = set()
        self.connect_api = connect_api

    @property
    def channels(self):
        """Shorthand for available channel classes"""
        # TODO(useability review. Other patterns/best practises)
        # should the channels be instantiated directly on the Manager already?
        from mbed_cloud.subscribe import channels
        return channels

    def get_channel(self, subscription_channel, **observer_params):
        """Get or start the requested channel"""
        keys = subscription_channel.get_routing_keys()
        extras = subscription_channel.get_extra_keys()
        [self.watch_keys.add(k_v[0]) for key in keys for k_v in key]
        channel = self.get_or_create_routes(subscription_channel, keys, extras)
        channel._configure(self, self.connect_api, observer_params)
        return channel

    def subscribe(self, subscription_channel, **observer_params):
        """Subscribe to a channel

        This adds a channel to the router, configures it, starts it, and returns its observer
        """
        return self.get_channel(subscription_channel, **observer_params).ensure_started().observer
    __call__ = subscribe

    def notify(self, data):
        """Notify subscribers that data was received"""
        logging.debug('notified: %s', data)
        try:
            for channel_name, items in data.items():
                for item in items or []:
                    # inject the channel name to the data, for a flat structure
                    item = dict(item)
                    item.update(dict(channel=channel_name))

                    # pluck keys we care about
                    plucked = {
                        key_name: item[key_name]
                        for key_name in self.watch_keys if key_name in item
                    }
                    route_keys = expand_dict_as_keys(plucked)
                    for route in route_keys:
                        sub_channels = self.get_route_item(route) or {}
                        logging.debug('subscribed channels: %s', sub_channels)
                        if not sub_channels:
                            logging.debug(
                                'no subscribers.\nkey %s\nroutes: %s',
                                route,
                                self._routes
                            )
                            logging.debug(
                                'plucked params: %s\nwatched: %s',
                                plucked,
                                self.watch_keys
                            )
                        for sub_channel in sub_channels.values():
                            logging.debug('dispatch: %s', item)
                            sub_channel.notify(item)
        except Exception:  # noqa
            logging.exception('Subscription notification failed')

    def unsubscribe_all(self):
        """Unsubscribes all channels"""
        for channel in self.list_all():
            channel.ensure_stopped()
        self.connect_api.stop_notifications()
