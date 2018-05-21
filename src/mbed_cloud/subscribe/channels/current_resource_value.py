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
from mbed_cloud.subscribe.subscribe import expand_dict_as_keys

from mbed_cloud import tlv
from mbed_cloud import utils

import logging

LOG = logging.getLogger(__name__)


class CurrentResourceValue(ChannelSubscription):
    """Triggers on response to a request for a current resource value"""

    def __init__(self, device_id, resource_path, **extra_filters):
        """Triggers on response to a request for a current resource value

        .. warning:: This functionality is considered experimental;
           the interface may change in future releases

        :param device_id: a device identifier
        :param resource_path: a resource path
        :param extra_filters:
        """
        super(CurrentResourceValue, self).__init__()
        self.device_id = device_id
        self.resource_path = resource_path

        # each request is unique
        self.async_id = utils.new_async_id()
        LOG.debug('new async id: %s', self.async_id)

        self._route_keys = expand_dict_as_keys(dict(
            id=self.async_id,
            channel=ChannelIdentifiers.async_responses,
        ))
        self._optional_filters = {}
        self._optional_filters.update(extra_filters)
        self._optional_filter_keys = expand_dict_as_keys(self._optional_filters)

    def start(self):
        """Start the channel"""
        # observers for this channel only need to wait for one value
        self._observer_params.update(dict(once=True))
        super(CurrentResourceValue, self).start()
        self._api.ensure_notifications_thread()
        self._api._mds_rpc_post(
            device_id=self.device_id,
            method='GET',
            uri=self.resource_path,
            async_id=self.async_id,
            _wrap_with_consumer=False,
        )

    def _notify(self, data):
        """Notify this channel of inbound data"""
        payload = tlv.decode(
            payload=data.get('payload'),
            content_type=data.get('ct'),
            decode_b64=True
        )
        super(CurrentResourceValue, self)._notify(payload)
        # after one response, close the channel
        self.ensure_stopped()
