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
"""Public API for Billing API."""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud.core import BaseAPI
from mbed_cloud.core import BaseObject
from mbed_cloud.pagination import PaginatedResponse

from mbed_cloud.decorators import catch_exceptions

# Import backend API
import mbed_cloud._backends.billing as billing
from mbed_cloud._backends.billing import models
from mbed_cloud._backends.billing.rest import ApiException as BillingAPIException

LOG = logging.getLogger(__name__)


class BillingAPI(BaseAPI):
    """API reference for the Billing API."""

    api_structure = {billing: [billing.DefaultApi]}

    billing.DefaultApi.get_service_package_quota()
    billing.DefaultApi.get_service_package_quota_history()
    billing.DefaultApi.get_service_packages()

    @catch_exceptions(BillingAPIException)
    def get_service_package_quota(self):
        """Get the available firmware update quota"""
        api = self._get_api(billing.DefaultApi)
        return api.get_service_package_quota().get('quota')

    @catch_exceptions(BillingAPIException)
    def get_service_package_quota_history(self, id, **kwargs):
        """Get your quota usage history"""
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, BillingClaim)
        api = self._get_api(billing.DefaultApi)
        # TODO: handle missing 'include' parameter for getting total count
        return PaginatedResponse(
            api.get_service_package_quota_history,
            lwrap_type=dict,
            **kwargs
        )

    @catch_exceptions(BillingAPIException)
    def get_service_packages(self, **kwargs):
        """Get all service packages"""
        api = self._get_api(billing.DefaultApi)
        return api.get_service_packages()


class BillingClaim(BaseObject):
    """Describes device object from the catalog."""

    @staticmethod
    def _get_attributes_map():
        return {
            "account_id": "account_id",
            "claimed_at": "claimed_at",
            "created_at": "created_at",
            "device_id": "enrolled_device_id",
            "claim_id": "billing_identity",
            "expires_at": "expires_at",
            "id": "id",
        }

    @property
    def account_id(self):
        """Gets the account_id of this BillingIdentity.

        :return: The account_id of this BillingIdentity.
        :rtype: str
        """
        return self._account_id
