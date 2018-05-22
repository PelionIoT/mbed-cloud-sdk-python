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

    def start(self):
        """Start the channel"""
        super(DeviceStateChanges, self).start()
        # n.b. No true start/stop implementation as DeviceState is permanently subscribed
        self._api.ensure_notifications_thread()
