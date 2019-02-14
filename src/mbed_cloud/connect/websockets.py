# --------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2019 Arm Limited
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
"""Websockets"""
from mbed_cloud.core import BaseObject


class Websocket(BaseObject):
    """Describes websocket object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "channel_id": "channel_id",
            "status": "status",
            "queue_size": "queue_size",
        }

    @property
    def channel_id(self):
        """Get the channel_id of this Websocket.

        Unique identifier of the channel.

        :return: The channel_id of this Websocket.
        :rtype: str
        """
        return self._channel_id

    @property
    def status(self):
        """Get the status of this Websocket.

        Channel status will be 'connected' when the channel has an active WebSocket bound to it.
        The state will be 'disconnected' when either the channel or the WebSocket bound to it is closed.

        :return: The status of this Websocket.
        :rtype: str
        """
        return self._status

    @property
    def queue_size(self):
        """Get the queue_size of this Websocket.

        Headers (key/value) that are sent with the notification. Optional.

        :return: The queue_size of this Websocket.
        :rtype: int
        """
        return self._queue_size
