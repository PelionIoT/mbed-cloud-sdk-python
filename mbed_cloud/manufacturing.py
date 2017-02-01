# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""API reference for manufacturing components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import config
from mbed_cloud.decorators import catch_exceptions

# Import backend APIs
import mbed_cloud._backends.factory_tool as factory_tool
import mbed_cloud._backends.factory_tool.rest as FactoryApiException
import mbed_cloud._backends.production_line_certificates as production_line_certificates
import mbed_cloud._backends.production_line_certificates.rest as ProductionLineApiException
import mbed_cloud._backends.provisioning_certificate as provisioning_certificate
import mbed_cloud._backends.provisioning_certificate.rest as ProvisioningApiException

LOG = logging.getLogger(__name__)


class ManufacturingAPI(BaseAPI):
    """Describing the public update API.

    Exposing functionality from the following underlying services:

    - Production line certificates
    - Provisioning certificate
    - Factory tool download
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(ManufacturingAPI, self).__init__(params)

        # Set the api_key for the requests
        self.factory_tool = self._init_api(factory_tool)
        self.provisioning_certificate = self._init_api(provisioning_certificate)
        self.production_line_certificates = self._init_api(production_line_certificates)

        # This API is a bit weird, so create the "authorization" string
        self.auth = "Bearer %s" % (config.get("api_key"),)

    @catch_exceptions(FactoryApiException)
    def factory_tool_versions(self):
        """Get a list of downloadable Factory Tool versions.

        - mbed Cloud user role must be Administrator.
        - mbed Cloud account must have Factory Tool downloads enabled
        """
        api = self.factory_tool.DefaultApi()
        return api.downloads_mbed_factory_provisioning_package_info_get()

    @catch_exceptions(FactoryApiException)
    def factory_tool_download(self, os):
        """Return a specific Factory Tool package in a ZIP archive.

        - mbed Cloud user role must be Administrator.
        - mbed Cloud account must have Factory Tool downloads enabled.

        :param os: Operating System. Either "Windows" or "Linux".
        :return: file binary
        """
        api = self.factory_tool.DefaultApi()
        return api.downloads_mbed_factory_provisioning_package_get(os)

    @catch_exceptions(ProvisioningApiException)
    def get_provisioning_certificate(self):
        """Get the provisioning certificate registered to organisation.

        :return: Provisioning certificate object
        """
        api = self.provisioning_certificate.DefaultApi()
        return api.v3_provisioning_certificate_get(self.auth)

    @catch_exceptions(ProductionLineApiException)
    def list_production_line_certificates(self):
        """Get list of production line certificates associated with the organisation.

        :return: List of production line certificates
        """
        api = self.production_line_certificates.DefaultApi()
        return api.v3_production_line_certificates_get(self.auth).data

    @catch_exceptions(ProductionLineApiException)
    def get_production_line_certificate(self, certificate_muuid):
        """Get production certificate with provided mUUID.

        :param certificate_muuid: the mUUID of the requested certificate (str)
        :return: Production line certificate object
        """
        api = self.production_line_certificates.DefaultApi()
        return api.v3_production_line_certificates_muuid_get(self.auth, certificate_muuid)

    @catch_exceptions(ProductionLineApiException)
    def delete_production_line_certificate(self, certificate_muuid):
        """Delete production certificate with provided mUUID.

        :param certificate_muuid: the mUUID of the requested certificate (str)
        :return: void
        """
        api = self.production_line_certificates.DefaultApi()
        api.v3_production_line_certificates_muuid_delete(self.auth, certificate_muuid)
        return

    def rename_production_line_certificate(self, certificate_muuid, new_name):
        """Rename the production line certificate with provided mUUID.

        :param certificate_muuid: the mUUID of the production line certificate to rename (str)
        :param new_name: the new name of the production line certificate (str)
        :return: the new production line certificate object.
        """
        api = self.production_line_certificates.DefaultApi()
        body = self.production_line_certificates.Body1(comment=new_name)
        api.v3_production_line_certificates_muuid_put(self.auth, certificate_muuid, body)
