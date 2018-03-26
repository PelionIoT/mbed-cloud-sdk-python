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
"""Channel"""
import logging
from mbed_cloud.subscribe.observer import Observer


class _API_CHANNELS(object):
    """API channels"""

    notifications = 'notifications'
    async_responses = 'async_responses'
    registrations = 'registrations'
    de_registrations = 'de_registrations'
    reg_updates = 'reg_updates'
    registrations_expired = 'registrations_expired'


class ChannelSubscription(object):
    """Represents a subscription to a channel

    In pub/sub terms, this is one channel of notifications.

    In mbed terms, this may be a Presubscription or a Subscription.
    There could be multiple references to a single mbed channel (e.g. `notifications`),
    with multiple receiving channels applying different filters, on the server or client-side.
    """

    _api = None  # type: mbed_cloud.connect.ConnectAPI
    _observer = None
    _observer_class = Observer
    _observer_params = None
    _manager = None
    _routes = None
    _optional_filters = None
    _optional_filter_keys = None
    _route_keys = None
    _active = False
    _filter_func = None

    def get_routing_keys(self):
        """Primary, mandatory routing keys (list of hashables)"""
        return self._route_keys

    def get_extra_keys(self):
        """Secondary, optional routing keys (list of hashables)"""
        return self._optional_filter_keys

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

    def filter_notification(self, data):
        """Filtering for this channel, based on key-value matching

        Subclasses can further extend or override this to provide
        custom behaviours e.g. filtering on timestamp ranges or other conditions
        """
        for k, v in (self._optional_filters or {}).items():
            logging.debug('optional filter %s: %s (%s)', k, v, data.get(k))
            if data.get(k) not in v:
                logging.debug('optional filter rejecting %s: %s (%s)', k, v, data.get(k))
                return False
        return self._filter_func(data) if self._filter_func else True

    def notify(self, data):
        """Notify this channel of inbound data"""
        if self.filter_notification(data):
            self.observer.notify(data)

    def __enter__(self):
        """Enter"""
        return self.ensure_started()

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit"""
        return self.ensure_stopped()

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
        self._manager.remove_routes(self.get_routing_keys())  # hmm - SoC?
        self._active = False
        return self
