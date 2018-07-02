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
from mbed_cloud._backends import billing
from mbed_cloud._backends.billing import models
from mbed_cloud._backends.billing.rest import ApiException as BillingAPIException

LOG = logging.getLogger(__name__)


class BillingAPI(BaseAPI):
    """API reference for the Billing API."""

    api_structure = {billing: [billing.DefaultApi]}

    @catch_exceptions(BillingAPIException)
    def get_quota_remaining(self):
        """Get the available firmware update quota"""
        api = self._get_api(billing.DefaultApi)
        quota = api.get_service_package_quota().get('quota')
        return None if quota is None else int(quota)

    @catch_exceptions(BillingAPIException)
    def get_quota_history(self, **kwargs):
        """Get your quota usage history"""
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, Package)
        api = self._get_api(billing.DefaultApi)
        # TODO: handle missing 'include' parameter for getting total count
        return PaginatedResponse(
            api.get_service_package_quota_history,
            lwrap_type=QuotaHistory,
            **kwargs
        )

    @catch_exceptions(BillingAPIException)
    def get_packages(self, **kwargs):
        """Get all service packages"""
        api = self._get_api(billing.DefaultApi)
        return api.get_service_packages()

    @catch_exceptions(BillingAPIException)
    def get_report_overview(self, file_path, month, **kwargs):
        """Downloads a report overview"""
        api = self._get_api(billing.DefaultApi)
        return api.get_billing_report(month)


class QuotaHistory(BaseObject):
    """An audit history entry for billing entities"""

    @staticmethod
    def _get_attributes_map():
        return dict(
            id='id',
            added_at='added',
            amount='amount',
            reason='reason',
            reservation='reservation',
            service_package='service_package',
        )

    @property
    def id(self):
        return self._id

    @property
    def added_at(self):
        return self._added_at

    @property
    def amount(self):
        return self._amount

    @property
    def reason(self):
        return self._reason

    @property
    def reservation(self):
        return self._reservation

    @property
    def service_package(self):
        return self._service_package


class Package(BaseObject):
    """A billing package"""

    @staticmethod
    def _get_attributes_map():
        return dict(
            created_at='created',
            modified_at='modified',
            starts_at='starts_time',
            expires_at='expires',
            ends_at='end_time',
            grace_period='grace_period',
            firmware_update_count='firmware_update_count',
            reason='reason',
            previous_id='previous_id',
            next_id='next_id',
        )

    @property
    def created_at(self):
        return self._created_at

    @property
    def modified_at(self):
        return self._modified_at

    @property
    def starts_at(self):
        return self._starts_at

    @property
    def expires_at(self):
        return self._expires_at

    @property
    def ends_at(self):
        return self._ends_at

    @property
    def grace_period(self):
        return self._grace_period

    @property
    def reason(self):
        return self._reason

    @property
    def previous_id(self):
        return self._previous_id

    @property
    def next_id(self):
        return self._next_id

    @property
    def firmware_update_count(self):
        return self._firmware_update_count

