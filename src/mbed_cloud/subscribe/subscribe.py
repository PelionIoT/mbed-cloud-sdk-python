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
from mbed_cloud import utils

LOG = logging.getLogger(__name__)


def expand_dict_as_keys(d):
    """Expands a dictionary into a list of immutables with cartesian product

    :param d: dictionary (of strings or lists)
    :returns: cartesian product of list parts
    """
    to_product = []
    for key, values in sorted(d.items()):
        # if we sort the inputs here, itertools.product will keep a stable sort order for us later
        key_values = sorted([(key, v) for v in utils.ensure_listable(values) if v is not None])
        if key_values:
            to_product.append(key_values)
    return list(itertools.product(*to_product))


class RoutingBase(object):
    """Routes unique inbound keys

    to matching lists of items
    """

    def __init__(self):
        """Routes"""
        self._routes = {}

    def get_route_items(self, route):
        """Get items attached to this route"""
        return list(self._routes.get(route, []))

    def create_route(self, item, routes):
        """Stores a new item in routing map"""
        for route in routes:
            self._routes.setdefault(route, set()).add(item)
        return item

    def remove_routes(self, item, routes):
        """Removes item from matching routes"""
        for route in routes:
            items = self._routes.get(route)
            try:
                items.remove(item)
                LOG.debug('removed item from route %s', route)
            except ValueError:
                pass
            if not items:
                self._routes.pop(route)
                LOG.debug('removed route %s', route)

    def list_all(self):
        """All items"""
        return list(set(
            item for items in self._routes.values() for item in items
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
        # watch keys are unique sets of keys that we will attempt to extract from inbound items
        self.watch_keys.add(frozenset({k_v[0] for key in keys for k_v in key}))
        self.create_route(subscription_channel, keys)
        subscription_channel._configure(self, self.connect_api, observer_params)
        return subscription_channel

    def subscribe(self, subscription_channel, **observer_params):
        """Subscribe to a channel

        This adds a channel to the router, configures it, starts it, and returns its observer
        """
        return self.get_channel(subscription_channel, **observer_params).ensure_started().observer
    __call__ = subscribe

    def _notify(self, item):
        """Route inbound items to individual channels"""
        for key_set in self.watch_keys:
            # only pluck keys if they exist
            plucked = {
                key_name: item[key_name]
                for key_name in key_set if key_name in item
            }
            route_keys = expand_dict_as_keys(plucked)
            for route in route_keys:
                channels = self.get_route_items(route) or {}
                logging.debug('subscribed channels: %s', channels)
                if not channels:
                    logging.debug(
                        'no subscribers for message.\nkey %s\nroutes: %s',
                        route,
                        self._routes
                    )
                for channel in channels:
                    logging.debug('routing dispatch: %s', item)
                    channel.notify(item)

    def notify(self, data):
        """Notify subscribers that data was received"""
        for channel_name, items in data.items():
            for item in items or []:
                LOG.debug('notified: %s', item)
                try:
                    # inject the channel name to the data (so channels can filter on it)
                    item = dict(item)
                    item['channel'] = channel_name
                    self._notify(item)
                except Exception:  # noqa
                    LOG.exception('Subscription notification failed')

    def unsubscribe_all(self):
        """Unsubscribes all channels"""
        for channel in self.list_all():
            channel.ensure_stopped()
        self.connect_api.stop_notifications()
