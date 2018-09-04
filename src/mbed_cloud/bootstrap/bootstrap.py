# ---------------------------------------------------------------------------
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
"""Public API for Bootstrap API."""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud.core import BaseAPI
from mbed_cloud.core import BaseObject

from mbed_cloud.decorators import catch_exceptions

from mbed_cloud.pagination import PaginatedResponse

# Import backend API
import mbed_cloud._backends.connector_bootstrap as bootstrap
from mbed_cloud._backends.connector_bootstrap import models
from mbed_cloud._backends.connector_bootstrap.rest import ApiException as BootstrapAPIException

LOG = logging.getLogger(__name__)


class BootstrapAPI(BaseAPI):
    """API reference for the Bootstrap API."""

    api_structure = {bootstrap: [bootstrap.PreSharedKeysApi]}

    @catch_exceptions(BootstrapAPIException)
    def add_psk(self, **kwargs):
        """Add"""
        api = self._get_api(bootstrap.PreSharedKeysApi)
        item = PreSharedKey._create_request_map(kwargs)
        item = models.PreSharedKey(**item)
        api.upload_pre_shared_key(item)
        return PreSharedKey(item)

    @catch_exceptions(BootstrapAPIException)
    def get_psk(self, endpoint_name, **kwargs):
        """Get"""
        api = self._get_api(bootstrap.PreSharedKeysApi)
        return PreSharedKey(api.get_pre_shared_key(endpoint_name=endpoint_name))

    @catch_exceptions(BootstrapAPIException)
    def list_psks(self, **kwargs):
        """List"""
        api = self._get_api(bootstrap.PreSharedKeysApi)
        return PaginatedResponse(api.list_pre_shared_keys, lwrap_type=PreSharedKey, **kwargs)

    @catch_exceptions(BootstrapAPIException)
    def delete_psk(self, endpoint_name, **kwargs):
        """Delete"""
        api = self._get_api(bootstrap.PreSharedKeysApi)
        return api.delete_pre_shared_key(endpoint_name=endpoint_name)


class PreSharedKey(BaseObject):
    """Describes device object from the catalog.

    For more information about such keys,
    have a look at
    https://cloud.mbed.com/docs/latest/connecting/mbed-client-lite-security-considerations.html"
    """

    @staticmethod
    def _get_attributes_map():
        return {
            'endpoint_name': 'endpoint_name',
            'secret_hex': 'secret_hex',
            'created_at': 'created_at',
        }

    @property
    def endpoint_name(self):
        """The endpoint_name of this PreSharedKey.

        Endpoint name is the unique ID of the pre-shared key.
        16-64 printable (non-control) ASCII characters.
        It also must be globally unique.
        Consider using vendor-MAC-ID-device-model.
        For example "myEndpoint.host.com"

        :param endpoint_name: The endpoint_name of this PreSharedKey.
        :type: str
        """
        return self._endpoint_name

    @property
    def secret_hex(self):
        """The secret_hex of this PreSharedKey.

        The secret of the pre-shared key in HEX format.
        - It is not case sensitive; 4a is same as 4A
        - It is allowed with or without 0x in the beginning.
        - The minimum length of the secret is 128 bits and max 512 bits.

        For example "4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a"

        :return: The secret_hex of this PreSharedKey.
        :rtype: str
        """
        return self._secret_hex

    @property
    def created_at(self):
        """Gets the created_at of this PreSharedKey.

        The date-time (RFC3339) when this pre-shared key was uploaded to Mbed Cloud.

        :return: The created_at of this PreSharedKey.
        :rtype: datetime
        """
        return self._created_at
