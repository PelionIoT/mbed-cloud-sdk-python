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
    """API reference for the Enrollment API.
    """

    api_structure = {enrollment: [enrollment.PublicAPIApi]}

    @catch_exceptions(EnrollmentAPIException)
    def add_enrollment_claim(self, **kwargs):
        """Add"""
        api = self._get_api(enrollment.PublicAPIApi)
        item = EnrollmentClaim._create_request_map(kwargs)
        item = models.EnrollmentIdentity(**item)
        return EnrollmentClaim(api.v3_device_enrollments_post(item))

    @catch_exceptions(EnrollmentAPIException)
    def get_enrollment_claim(self, claim_id, **kwargs):
        """Get"""
        api = self._get_api(enrollment.PublicAPIApi)
        return EnrollmentClaim(api.v3_device_enrollments_id_get(id=claim_id))

    @catch_exceptions(EnrollmentAPIException)
    def list_enrollment_claims(self, **kwargs):
        """List"""
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, EnrollmentClaim)
        api = self._get_api(enrollment.PublicAPIApi)
        return PaginatedResponse(api.v3_device_enrollments_get, lwrap_type=EnrollmentClaim, **kwargs)

    @catch_exceptions(EnrollmentAPIException)
    def delete_enrollment_claim(self, claim_id, **kwargs):
        """Delete"""
        api = self._get_api(enrollment.PublicAPIApi)
        return api.v3_device_enrollments_id_delete(id=claim_id)


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
    @BaseObject._pass_through(models.EnrollmentIdentity.account_id)
    def account_id(self):
        pass

    @property
    @BaseObject._pass_through(models.EnrollmentIdentity.claimed_at)
    def claimed_at(self):
        pass

    @property
    @BaseObject._pass_through(models.EnrollmentIdentity.created_at)
    def created_at(self):
        pass

    @property
    @BaseObject._pass_through(models.EnrollmentIdentity.enrolled_device_id)
    def device_id(self):
        pass

    @property
    @BaseObject._pass_through(models.EnrollmentIdentity.enrollment_identity)
    def claim_id(self):
        pass

    @property
    @BaseObject._pass_through(models.EnrollmentIdentity.expires_at)
    def expires_at(self):
        pass

    @property
    @BaseObject._pass_through(models.EnrollmentIdentity.id)
    def id(self):
        pass
