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
from __future__ import absolute_import

from mbed_cloud.subscribe.channels.channel import ChannelIdentifiers
from mbed_cloud.subscribe.channels.channel import ChannelSubscription

from mbed_cloud.subscribe.subscribe import expand_dict_as_keys


class DeviceStateChanges(ChannelSubscription):
    """Triggers on changes to registration state of devices"""

    def __init__(self, device_id=None, **extra_filters):
        """Triggers on changes to registration state of devices

        .. warning:: This functionality is considered experimental;
           the interface may change in future releases

        :param device_id: a device identifier
        :param extra_filters: additional filters e.g. dict(channel=API_CHANNELS.registrations)
        """
        super(DeviceStateChanges, self).__init__()
        self._route_keys = expand_dict_as_keys(dict(
            channel=[
                ChannelIdentifiers.de_registrations,
                ChannelIdentifiers.reg_updates,
                ChannelIdentifiers.registrations_expired,
                ChannelIdentifiers.registrations,
            ],
        ))
        self._optional_filters = {}
        if device_id is not None:
            self._optional_filters['device_id'] = device_id
        self._optional_filters.update(extra_filters)

    @staticmethod
    def _map_resource_data(resource_data):
        attribute_map = {
            "path": "path",
            "rt": "type",
            "ct": "content_type",
            "obs": "observable"
        }

        new_items = map(
            lambda item: (item[1], resource_data.get(item[0], None)),
            attribute_map.items()
        )

        return dict(new_items)

    @staticmethod
    def _map_endpoint_data(endpoint_data):
        attribute_map = {
            "ep": "device_id",
            "original_ep": "alias",
            "ept": "device_type",
            "q": "queue_mode",
            "channel": "channel"
        }

        output = dict(map(
            lambda item: (item[1], endpoint_data.get(item[0], None)),
            attribute_map.items()
        ))

        output["resources"] = list(map(
            DeviceStateChanges._map_resource_data, endpoint_data.get("resources", [])
        ))

        return output

    def start(self):
        """Start the channel"""
        super(DeviceStateChanges, self).start()
        # n.b. No true start/stop implementation as DeviceState is permanently subscribed
        self._api.ensure_notifications_thread()

    def notify(self, data):
        """Notify this channel of inbound data"""
        string_channels = {
            ChannelIdentifiers.de_registrations,
            ChannelIdentifiers.registrations_expired
        }

        if data['channel'] in string_channels:
            message = {'device_id': data["value"], 'channel': data["channel"]}
        else:
            message = DeviceStateChanges._map_endpoint_data(data)

        return super(DeviceStateChanges, self).notify(message)
