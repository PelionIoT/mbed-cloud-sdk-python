"""Reference API for development component."""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI
from mbed_cloud_sdk import config
from mbed_cloud_sdk.decorators import catch_exceptions

# Import backend API
import mbed_cloud_sdk._backends.developer_certificate as cert
import mbed_cloud_sdk._backends.developer_certificate.rest as ApiException

LOG = logging.getLogger(__name__)


class DevelopmentAPI(BaseAPI):
    """Describing the public development API.

    Exposing functionality from the following underlying services:
    - Developer certificate
    """

    def __init__(self, params={}):
        """Initialise the development API, optionally passing in overriding config."""
        super(DevelopmentAPI, self).__init__(params)

        # Set the api_key for the requests
        cert.configuration.api_key['Authorization'] = config.get("api_key")
        cert.configuration.api_key_prefix['Authorization'] = 'Bearer'

        # Override host, if defined
        if config.get("host"):
            cert.configuration.host = config.get("host")

        # This API is a bit weird, so create the "authorization" string
        self.auth = "Bearer %s" % (config.get("api_key"),)

    @catch_exceptions(ApiException)
    def get_certificate(self):
        """Get current certificate registered to organisation.

        Returns an object with details on when certificate was created and the
        public key.

        If no certificate is registered, this function returns `None`.

        :return: Object with public key and created date if found, or `None` if
            no certificate is registered.
        """
        api = cert.DefaultApi()
        resp = api.v3_developer_certificate_get(self.auth)

        # Return None if the cert object is empty
        if resp.id:
            return resp
        return None

    @catch_exceptions(ApiException)
    def revoke_certificate(self):
        """Revoke/delete the organisation certificate, if found.

        If not found/registered, we do nothing.

        :return: void
        """
        api = cert.DefaultApi()
        return api.v3_developer_certificate_delete(self.auth)

    @catch_exceptions(ApiException)
    def create_certificate(self, public_key):
        """Create and register a new organisation certificate.

        Registeres a new certificate to the organisation, using the provided
        public key. If a certificate is already registered (and not revoked) an
        exception indication a conflict will be raised.

        :param public_key: NIST P-256 Elliptic Curve public key, base64 encoded.
        :return: The newly created certificate (created date, public key, ...)
        """
        api = cert.DefaultApi()

        body = cert.Body()
        body.pub_key = public_key

        return api.v3_developer_certificate_post(self.auth, body)
