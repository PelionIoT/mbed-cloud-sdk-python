"""API reference for manufacturing components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI
from mbed_cloud_sdk import config
from mbed_cloud_sdk.decorators import catch_exceptions

# Import backend API
import mbed_cloud_sdk._backends.factory_tool as factory_tool
import mbed_cloud_sdk._backends.factory_tool.rest as ApiException

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
        factory_tool.configuration.api_key['Authorization'] = config.get("api_key")
        factory_tool.configuration.api_key_prefix['Authorization'] = 'Bearer'

        # Override host, if defined
        if config.get("host"):
            factory_tool.configuration.host = config.get("host")

    @catch_exceptions(ApiException)
    def versions(self):
        """Get a list of downloadable Factory Tool versions.

        - mbed Cloud user role must be Administrator.
        - mbed Cloud account must have Factory Tool downloads enabled
        """
        api = factory_tool.DefaultApi()
        return api.downloads_mbed_factory_provisioning_package_info_get()

    @catch_exceptions(ApiException)
    def download(self, os):
        """Return a specific Factory Tool package in a ZIP archive.

        - mbed Cloud user role must be Administrator.
        - mbed Cloud account must have Factory Tool downloads enabled.

        :param os: Operating System. Either "Windows" or "Linux".
        :returns: file binary
        """
        api = factory_tool.DefaultApi()
        return api.downloads_mbed_factory_provisioning_package_get(os)
