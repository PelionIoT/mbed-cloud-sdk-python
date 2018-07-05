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
import datetime
import json
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud.core import BaseAPI
from mbed_cloud.core import BaseObject
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.pagination import PaginatedResponse
from mbed_cloud.utils import ensure_listable

# Import backend API
from mbed_cloud._backends import billing
from mbed_cloud._backends.billing.rest import ApiException as BillingAPIException

LOG = logging.getLogger(__name__)

PACKAGE_STATES = ('pending', 'active', 'previous')


class BillingAPI(BaseAPI):
    """API reference for the Billing API."""

    api_structure = {billing: [billing.DefaultApi]}

    @catch_exceptions(BillingAPIException)
    def get_quota_remaining(self):
        """Get the remaining value"""
        api = self._get_api(billing.DefaultApi)
        quota = api.get_service_package_quota()
        return None if quota is None else int(quota.quota)

    @catch_exceptions(BillingAPIException)
    def get_quota_history(self, **kwargs):
        """Get quota usage history"""
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, ServicePackage)
        api = self._get_api(billing.DefaultApi)
        return PaginatedResponse(
            api.get_service_package_quota_history,
            lwrap_type=QuotaHistory,
            **kwargs
        )

    @catch_exceptions(BillingAPIException)
    def get_service_packages(self):
        """Get all service packages"""
        api = self._get_api(billing.DefaultApi)
        package_response = api.get_service_packages()
        packages = []
        for state in PACKAGE_STATES:
            # iterate states in order
            items = getattr(package_response, state) or []
            for item in ensure_listable(items):
                params = item.to_dict()
                params['state'] = state
                packages.append(ServicePackage(params))
        return packages

    @catch_exceptions(BillingAPIException)
    def get_report_overview(self, month, file_path):
        """Downloads a report overview

        :param month: month as datetime instance, or string in YYYY-MM format
        :type month: str or datetime
        :param str file_path: location to store output file
        :return: outcome
        :rtype: True or None
        """
        if isinstance(month, datetime.datetime):
            month = '%s-%02d' % (month.year, month.day)
        api = self._get_api(billing.DefaultApi)
        response = api.get_billing_report(month=month)

        if response:
            content = api.api_client.sanitize_for_serialization(response.to_dict())
            with open(file_path, 'w') as fh:
                fh.write(
                    json.dumps(
                        content,
                        sort_keys=True,
                        indent=2,
                    )
                )
        return True if response else None


class QuotaHistory(BaseObject):
    """An audit history entry for billing entities"""

    @staticmethod
    def _get_attributes_map():
        return dict(
            id='id',
            created_at='added',
            delta='amount',
            reason='reason',
            reservation='reservation',
            service_package='service_package',
        )

    @property
    def id(self):
        """The id of this QuotaHistory"""
        return self._id

    @property
    def created_at(self):
        """The time this entry was created"""
        return self._created_at

    @property
    def delta(self):
        """The change in remaining value, at the time this entry was created

        Negative values mean the remaining amount has been reduced
        for example, a reservation caused by starting a campaign
        """
        return self._delta

    @property
    def reason(self):
        """The reason this entry was created"""
        return self._reason

    @property
    def reservation(self):
        """The campaign reservation that this entry refers to"""
        return self._reservation

    @property
    def service_package(self):
        """The service package that this entry refers to"""
        return self._service_package


class ServicePackage(BaseObject):
    """A billing package"""

    @staticmethod
    def _get_attributes_map():
        return dict(
            id='id',
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
            state='state',
        )

    @property
    def id(self):
        """The id of this package"""
        return self._id

    @property
    def created_at(self):
        """The creation datetime of this package"""
        return self._created_at

    @property
    def modified_at(self):
        """The modification datetime of this package"""
        return self._modified_at

    @property
    def starts_at(self):
        """The start datetime of this package"""
        return self._starts_at

    @property
    def expires_at(self):
        """The expiry datetime of this package"""
        return self._expires_at

    @property
    def ends_at(self):
        """The end datetime of this package"""
        return self._ends_at

    @property
    def grace_period(self):
        """Period after package ending in which existing update campaigns continue to function"""
        return self._grace_period

    @property
    def reason(self):
        """The reason for package ending"""
        return self._reason

    @property
    def previous_id(self):
        """The previous package in the sequence"""
        return self._previous_id

    @property
    def next_id(self):
        """The next package in the sequence"""
        return self._next_id

    @property
    def firmware_update_count(self):
        """The firmware update count"""
        return self._firmware_update_count

    @property
    def state(self):
        """The state"""
        return self._state
