# coding=utf8

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
from mbed_cloud.subscribe.channels.channel import ChannelIdentifiers
from mbed_cloud.subscribe.channels.channel import ChannelSubscription
from mbed_cloud.subscribe.channels.channel import FirstValue

from mbed_cloud.subscribe.subscribe import expand_dict_as_keys

from mbed_cloud import tlv
from mbed_cloud import utils

import logging
import threading

# module-level lock to attempt to protect presubscriptions list
_presub_lock = threading.Lock()

LOG = logging.getLogger(__name__)


class ResourceValues(ChannelSubscription):
    """Triggers when a resource's value changes"""

    def __init__(
            self,
            device_id=None,
            resource_path=None,
            first_value=FirstValue.on_value_update,
            **extra_filters
    ):
        """Triggers when a resource's value changes

        .. warning:: This functionality is considered experimental;
           the interface may change in future releases

        :param device_id: device identifier, (or list thereof), optionally ending with wildcard *
        :param resource_path: resource path, (or list thereof), optionally ending with wildcard *
        :param first_value: mode for adjusting immediacy of subscribed values
        :param extra_filters: other local key-value filters
        """
        super(ResourceValues, self).__init__()

        self.device_ids = [str(d) for d in utils.ensure_listable(device_id) if d]
        self.resource_paths = [str(p) for p in utils.ensure_listable(resource_path) if p]
        # TODO(endpoint_type) support needs the endpoint_type or identifier in presub api response
        # self.endpoint_type

        self._immediacy = first_value
        self._presubscription_registry = None  # type: PreSubscriptionRegistry

        # for filtering inbound notifications (with wildcards)
        self._local_filters = {}

        # for configuring the router (which has no wildcard behaviour)
        self._route_seeds = {
            'channel': ChannelIdentifiers.notifications,
        }

        # turn our parameters into a presubscriptions-compatible list (one device id per entry)
        # note: pluralised 'resource_paths'
        self._sdk_presub_params = [
            {
                k: v for k, v in dict(
                    device_id=d,
                    resource_paths=self.resource_paths
                ).items() if v
            }
            # API will not accept an empty pre-subscription, default wildcard match-all
            for d in self.device_ids or ["*"]
        ]

        # api sends back different field names on the notification channel so remap them before
        # putting them in the routing table
        for api_key_name, values in dict(ep=self.device_ids, path=self.resource_paths).items():
            has_wildcards = any(self._is_wildcard(v) for v in values if v)
            for to_validate in values:
                if to_validate is None:
                    continue
                if not self._validate_wildcard(to_validate):
                    raise ValueError(
                        'Wildcards can only be used at the end of values: "%s"' % (to_validate,)
                    )
                # local filters recreate behaviour of server-side wildcard filter, but are not
                # routable (can't look them up in a dictionary)
                # routable filters are for explicit key-value pairs
                if has_wildcards:
                    self._local_filters.setdefault(api_key_name, []).append(to_validate)
                else:
                    self._route_seeds.setdefault(api_key_name, []).append(to_validate)
        self._route_keys = expand_dict_as_keys(self._route_seeds)

        self._optional_filters = {}
        self._optional_filters.update(extra_filters)
        self._optional_filter_keys = expand_dict_as_keys(self._optional_filters)

        self.add_filter_function(self._wildcard_filter)

    def _wildcard_filter(self, data):
        # custom local filtering based on wildcard string matches for each field
        for required_key, any_required_values in self._local_filters.items():
            value = data.get(required_key)
            if value is None:
                # the filter key is missing from the data
                return False
            for required_value in any_required_values:
                if self._wildcard_match(str(value), required_value):
                    break
            else:
                # no match from optional list: this data is not a match
                return False
        # every key has at least one matching value
        return True

    def _wildcard_match(self, candidate, expression):
        return candidate.startswith(expression[:-1])

    def _validate_wildcard(self, item):
        return '*' not in item[:-1]

    def _is_wildcard(self, item):
        return item.endswith('*')

    def _pattern_match(self, item, pattern):
        """Determine whether the item supplied is matched by the pattern."""
        if pattern.endswith('*'):
            return item.startswith(pattern[:-1])
        else:
            return item == pattern

    def _matching_device_resources(self):
        device_resource_pairs = []
        devices = self._api.list_connected_devices()
        LOG.debug('found %s connected device(s)', len(devices))
        for device in devices:
            if self.device_ids and not any(
                self._pattern_match(device.id, filter_id) for filter_id in self.device_ids
            ):
                continue
            resources = self._api.list_resources(device.id)
            LOG.debug('found %s resource(s) on device %s', len(resources), device.id)
            for live_device_resource in resources:
                # Don't subscribe to resources which are not observable
                if not live_device_resource.observable:
                    continue
                # If a wildcard matches then subscribe, default to wildcard match-all
                for filter_path in self.resource_paths or ["*"]:
                    if self._pattern_match(live_device_resource.path, filter_path):
                        # if we reach this point, we have matched this resource
                        device_resource_pairs.append((device.id, live_device_resource.path))
                        break
        return device_resource_pairs

    def _subscribe_all_matching(self):
        device_resource_pairs = self._matching_device_resources()
        device_subscription_count = len(device_resource_pairs)
        if not device_subscription_count:
            LOG.warning('no matching devices and resources found, unable to auto-subscribe')
        elif device_subscription_count > 49:
            LOG.warning(
                'auto-subscribing to a significant number of resources (%s), '
                'this may take some time',
                device_subscription_count
            )
        else:
            LOG.debug('auto-subscribing to %s resources', device_subscription_count)
        for device, resource_path in device_resource_pairs:
            self._api._add_subscription(device, resource_path)

    def _unsubscribe_all_matching(self):
        device_resource_pairs = self._matching_device_resources()
        LOG.debug('removing subscriptions from %s resources', len(device_resource_pairs))
        for device, resource_path in device_resource_pairs:
            self._api._delete_subscription(device, resource_path)

    @property
    def _presubs(self):
        if not self._presubscription_registry:
            self._presubscription_registry = PreSubscriptionRegistry(self._api)
        return self._presubscription_registry

    def start(self):
        """Start the channel"""
        super(ResourceValues, self).start()
        self._api.ensure_notifications_thread()
        self._presubs.add(self._sdk_presub_params)
        if self._immediacy == FirstValue.on_value_update:
            self._subscribe_all_matching()

    def _notify(self, data):
        decoded = {}
        decoded.update(data)
        decoded['payload'] = tlv.decode(
            payload=data.get('payload'),
            content_type=data.get('ct'),
            decode_b64=True
        )
        for k, v in dict(ep='device_id', path='resource_path').items():
            if k in decoded:
                decoded[v] = decoded.pop(k, None)
        super(ResourceValues, self)._notify(decoded)

    def stop(self):
        """Stop the channel"""
        self._presubs.remove(self._sdk_presub_params)
        if self._immediacy == FirstValue.on_value_update:
            self._unsubscribe_all_matching()
        super(ResourceValues, self).stop()


class PreSubscriptionRegistry(object):
    """A registry representing the presubscription JSON array of objects"""

    def __init__(self, api):
        """New registry instance"""
        self.api = api
        self.current = []

    def load_from_cloud(self):
        """Sync - read"""
        self.current = [
            {k: v for k, v in p.to_dict().items() if v is not None}
            for p in self.api.list_presubscriptions()
        ]

    def save_to_cloud(self):
        """Sync - write"""
        self.api.update_presubscriptions(self.current)

    def add(self, items):
        """Add entry to global presubs list"""
        with _presub_lock:
            self.load_from_cloud()
            for entry in utils.ensure_listable(items):
                # add new entries, but only if they're unique
                if entry not in self.current:
                    self.current.append(entry)
            self.save_to_cloud()

    def remove(self, items):
        """Remove entry from global presubs list"""
        with _presub_lock:
            self.load_from_cloud()
            for entry in utils.ensure_listable(items):
                # remove all matching entries
                while entry in self.current:
                    self.current.remove(entry)
            self.save_to_cloud()
