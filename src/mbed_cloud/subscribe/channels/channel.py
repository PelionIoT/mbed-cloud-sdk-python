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
"""A Channels API module"""
import logging

from mbed_cloud.subscribe.observer import Observer

LOG = logging.getLogger(__name__)


class ChannelIdentifiers(object):
    """API channels

    Internal Mbed Cloud channel identifiers
    """

    notifications = 'notifications'
    async_responses = 'async_responses'
    registrations = 'registrations'
    de_registrations = 'de_registrations'
    reg_updates = 'reg_updates'
    registrations_expired = 'registrations_expired'


class FirstValue(object):
    """Container for 'first value' modes

    'First value' refers to how soon after requesting a subscription
    the first resource value is fetched.

    There is a tradeoff in terms of performance/api calls/device power usage
    """

    # waits for a device to send re-register message. one api call. long wait.
    on_registration = 'on_registration'

    # sets up subscriptions on existing live resources. many api calls. medium wait.
    on_value_update = 'on_value_update'

    # TODO(first value immediate):
    # explicitly requests value update from each matching resource. many api calls. immediate.
    # immediately='immediately'


class ChannelSubscription(object):
    """Represents a subscription to a channel

    In pub/sub terms, this is one channel of notifications.

    In mbed terms, this may be a Presubscription or a Subscription.
    There could be multiple references to a single mbed channel (e.g. `notifications`),
    with multiple receiving channels applying different filters, on the server or client-side.
    """

    def __init__(self, *args, **kwargs):
        """New Channel Subscription Instance"""
        self._active = False
        self._api = None  # type: mbed_cloud.connect.ConnectAPI
        self._filter_func = None
        self._filters = []
        self._manager = None  # type: mbed_cloud.subscribe.SubscriptionsManager
        self._observer = None
        self._observer_class = Observer
        self._observer_params = None
        self._optional_filters = None
        self._route_keys = None
        self.add_filter_function(self._filter_optional_keys)
        self.name = None
        super(ChannelSubscription, self).__init__()

    def get_routing_keys(self):
        """Primary, mandatory routing keys (list of hashables)"""
        return self._route_keys

    def add_filter_function(self, func):
        """Adds a function for local notification filtering"""
        self._filters.append(func)
        return self

    @property
    def active(self):
        """Channel currently active"""
        return self._active

    @property
    def observer(self):
        """The Observer instance for this channel

        Each channel has one observer, which is notified whenever new
        data is received by the channel. Observers can then notify
        multiple listeners/futures in downstream code.
        """
        return self._observer

    def _filter_optional_keys(self, data):
        """Filtering for this channel, based on key-value matching"""
        for filter_key, filter_value in (self._optional_filters or {}).items():
            data_value = data.get(filter_key)
            LOG.debug(
                'optional keys filter %s: %s (%s)',
                filter_key, filter_value, data_value
            )
            if data_value is None or data_value != filter_value:
                LOG.debug(
                    'optional keys filter rejecting %s: %s (%s)',
                    filter_key, filter_value, data_value
                )
                return False
        return True

    def _notify(self, data):
        self.observer.notify(data)

    def notify(self, data):
        """Notify this channel of inbound data"""
        for filter_function in self._filters:
            if not filter_function(data):
                return False
        self._notify(data)
        return True

    def __enter__(self):
        """Enter"""
        return self.ensure_started()

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit"""
        return self.ensure_stopped()

    def __repr__(self):
        """String representation"""
        return '<%s %s>' % (self.__class__.__name__, self.name or self._route_keys)

    def start(self):
        """Base method for starting the channel"""
        pass

    def stop(self):
        """Base method for stopping the channel"""
        pass

    def _configure(self, manager, connect_api_instance, observer_params):
        """Configure behind-the-scenes settings for the channel

        These are required in addition to the parameters provided
        on instantiation
        """
        self._manager = manager
        self._api = connect_api_instance
        self._observer_params = self._observer_params or {}
        self._observer_params.update(observer_params)

    def ensure_started(self):
        """Idempotent channel start"""
        if self.active:
            return self
        self._observer = self._observer_class(**self._observer_params)
        self.start()
        self._active = True
        return self

    def ensure_stopped(self):
        """Idempotent channel stop"""
        if not self.active:
            return self
        self.stop()
        self.observer.cancel()
        self._manager.remove_routes(self, self.get_routing_keys())
        self._active = False
        return self
