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
"""Webhooks"""
from mbed_cloud.core import BaseObject


class Webhook(BaseObject):
    """Describes webhook object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "url": "url",
            "headers": "headers",
        }

    @property
    def url(self):
        """Get the URL of this Webhook.

        The URL to which the notifications are sent.
        We recommend that you serve this URL over HTTPS.

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._url

    @property
    def headers(self):
        """Get the headers of this Webhook.

        Headers (key/value) that are sent with the notification. Optional.

        :return: The headers of this Webhook.
        :rtype: dict(str, str)
        """
        return self._headers
