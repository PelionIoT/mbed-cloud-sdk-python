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
"""Presubscriptions"""
from mbed_cloud.core import BaseObject


class Presubscription(BaseObject):
    """Presubscription data object"""

    @staticmethod
    def _get_attributes_map():
        return {
            'device_id': 'endpoint-name',
            'device_type': 'endpoint-type',
            'resource_paths': 'resource-path',
        }

    @property
    def device_id(self):
        """The Device ID

        :return: The URL of this Webhook.
        :rtype: str
        """
        return self._device_id

    @property
    def device_type(self):
        """Device type of this Presubscription.

        :return: The URL of this Webhook.
        :rtype: str
        """
        return self._device_type

    @property
    def resource_paths(self):
        """Resource paths of this Presubscription.

        :return: The URL of this Webhook.
        :rtype: list[str]
        """
        return self._resource_paths
