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
        return PreSharedKey(api.upload_a_pre_shared_key(item))

    @catch_exceptions(BootstrapAPIException)
    def get_psk(self, id, **kwargs):
        """Get"""
        api = self._get_api(bootstrap.PreSharedKeysApi)
        return PreSharedKey(api.get_a_pre_shared_key(id=id))

    @catch_exceptions(BootstrapAPIException)
    def delete_psk(self, id, **kwargs):
        """Delete"""
        api = self._get_api(bootstrap.PreSharedKeysApi)
        return api.delete_a_pre_shared_key(id=id)


class PreSharedKey(BaseObject):
    """Describes device object from the catalog."""

    @staticmethod
    def _get_attributes_map():
        return {
            'endpoint_name': 'endpoint_name',
            'secret_hex': 'secret_hex',
        }

    @property
    def endpoint_name(self):
        """The endpoint_name of this PreSharedKey.

        Endpoint name is the unique ID of the pre-shared key.
        16-64 printable (non-control) ASCII characters.

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

        :return: The secret_hex of this PreSharedKey.
        :rtype: str
        """
        return self._secret_hex
