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
from mbed_cloud.subscribe.channels.channel import _API_CHANNELS
from mbed_cloud.subscribe.channels.channel import ChannelSubscription
from mbed_cloud.subscribe.subscribe import expand_dict_as_keys


class ResourceValueChanges(ChannelSubscription):
    """Triggers when a resource's value changes"""

    def __init__(self, device_id, resource_path, **extra_filters):
        """Channel"""
        raise NotImplementedError('coming soon™')
        self.device_id = device_id
        self.resource_path = resource_path

        self._route_keys = expand_dict_as_keys(dict(
            device_id=device_id,
            resource_path=resource_path,
            channel=_API_CHANNELS.notifications,
        ))
        self._optional_filters = {}
        self._optional_filters.update(extra_filters)
        self._optional_filter_keys = expand_dict_as_keys(self._optional_filters)

    def start(self):
        """Start the channel"""
        super(ResourceValueChanges, self).start()
        self._api.ensure_notifications_thread()
        self._api._add_subscription(
            self.device_id,
            self.resource_path,
        )

    def stop(self):
        """Stop the channel"""
        self._api._delete_subscription(
            self.device_id,
            self.resource_path,
        )
        super(ResourceValueChanges, self).stop()
