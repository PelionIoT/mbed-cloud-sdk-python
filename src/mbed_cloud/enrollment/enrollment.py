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
"""Public API for Enrollment API."""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud.core import BaseAPI
from mbed_cloud.core import BaseObject
from mbed_cloud.pagination import PaginatedResponse

from mbed_cloud.decorators import catch_exceptions

# Import backend API
import mbed_cloud._backends.enrollment as enrollment
from mbed_cloud._backends.enrollment import models
from mbed_cloud._backends.enrollment.rest import ApiException as EnrollmentAPIException

LOG = logging.getLogger(__name__)


class EnrollmentAPI(BaseAPI):
    """API reference for the Enrollment API."""

    api_structure = {enrollment: [enrollment.PublicAPIApi]}

    @catch_exceptions(EnrollmentAPIException)
    def add_enrollment_claim(self, **kwargs):
        """Add"""
        api = self._get_api(enrollment.PublicAPIApi)
        item = EnrollmentClaim._create_request_map(kwargs)
        item = models.EnrollmentIdentity(**item)
        return EnrollmentClaim(api.create_device_enrollment(item))

    @catch_exceptions(EnrollmentAPIException)
    def get_enrollment_claim(self, id, **kwargs):
        """Get"""
        api = self._get_api(enrollment.PublicAPIApi)
        return EnrollmentClaim(api.get_device_enrollment(id=id))

    @catch_exceptions(EnrollmentAPIException)
    def list_enrollment_claims(self, **kwargs):
        """List"""
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, EnrollmentClaim)
        api = self._get_api(enrollment.PublicAPIApi)
        return PaginatedResponse(
            api.get_device_enrollments,
            lwrap_type=EnrollmentClaim,
            **kwargs
        )

    @catch_exceptions(EnrollmentAPIException)
    def delete_enrollment_claim(self, id, **kwargs):
        """Delete"""
        api = self._get_api(enrollment.PublicAPIApi)
        return api.delete_device_enrollment(id=id)


class EnrollmentClaim(BaseObject):
    """Describes device object from the catalog."""

    @staticmethod
    def _get_attributes_map():
        return {
            "account_id": "account_id",
            "claimed_at": "claimed_at",
            "created_at": "created_at",
            "device_id": "enrolled_device_id",
            "claim_id": "enrollment_identity",
            "expires_at": "expires_at",
            "id": "id",
        }

    @property
    def account_id(self):
        """Gets the account_id of this EnrollmentIdentity.

        :return: The account_id of this EnrollmentIdentity.
        :rtype: str
        """
        return self._account_id

    @property
    def claimed_at(self):
        """Gets the claimed_at of this EnrollmentIdentity.

        The time of claiming the device to be assigned to the account.

        :return: The claimed_at of this EnrollmentIdentity.
        :rtype: datetime
        """
        return self._claimed_at

    @property
    def created_at(self):
        """Gets the created_at of this EnrollmentIdentity.

        The time of the enrollment identity creation.

        :return: The created_at of this EnrollmentIdentity.
        :rtype: datetime
        """
        return self._created_at

    @property
    def device_id(self):
        """Gets the enrolled_device_id of this EnrollmentIdentity.

        Enrolled device internal ID

        :return: The enrolled_device_id of this EnrollmentIdentity.
        :rtype: str
        """
        return self._device_id

    @property
    def claim_id(self):
        """Gets the claim_id of this EnrollmentIdentity.

        Enrollment identity.

        :return: The claim_id of this EnrollmentIdentity.
        :rtype: str
        """
        return self._claim_id

    @property
    def expires_at(self):
        """Gets the expires_at of this EnrollmentIdentity.

        The enrollment claim expiration time. If the device does not connect to Mbed Cloud
        before the expiration, the claim is removed without a separate notice

        :return: The expires_at of this EnrollmentIdentity.
        :rtype: datetime
        """
        return self._expires_at

    @property
    def id(self):
        """Gets the id of this EnrollmentIdentity.

        Enrollment identity internal id

        :return: The id of this EnrollmentIdentity.
        :rtype: str
        """
        return self._id
