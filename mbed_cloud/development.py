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
"""Reference API for development component."""
from __future__ import absolute_import

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions

# Import backend API
import mbed_cloud._backends.developer_certificate as cert
from mbed_cloud._backends.developer_certificate.models import DeveloperCertificate
import mbed_cloud._backends.developer_certificate.rest as ApiException


class DevelopmentAPI(BaseAPI):
    """Development / developer certificate API reference.

    This module covers functionality for the development/prototyping phase of
    your project. By creating and deploying development certificates the
    developer is able to very easily connect the device to the cloud in a
    secure manner.

    Please do note that each organisation/account only have one active
    certificate at a time. As a consequence, if you do delete an already active
    development certificate please make sure it's not activly in use and that
    you know what you're doing.
    """

    def __init__(self, params={}):
        """Initialise the development API, optionally passing in overriding config."""
        super(DevelopmentAPI, self).__init__(params)

        # Set the api_key for the requests
        self.cert = self._init_api(cert)
        self.auth = self.cert.configuration.api_key['Authorization']

    @catch_exceptions(ApiException)
    def get_certificate(self):
        """Get current certificate registered to organisation.

        Returns an object with details on when certificate was created and the
        public key.

        If no certificate is registered, this function returns `None`.

        :return: Object with public key and created date if found,
            or `None` if no certificate is registered.
        :rtype: Certificate
        """
        api = self.cert.DefaultApi()
        resp = api.v3_developer_certificate_get(self.auth)

        # Return None if the cert object is empty
        if resp.id:
            return Certificate(resp)
        return None

    @catch_exceptions(ApiException)
    def delete_certificate(self):
        """Delete the organisation certificate, if found.

        If not found/registered, we do nothing.

        :return: void
        """
        api = self.cert.DefaultApi()
        api.v3_developer_certificate_delete(self.auth)
        return

    @catch_exceptions(ApiException)
    def add_certificate(self, public_key):
        """Register a new organisation certificate.

        Registeres a new certificate to the organisation, using the provided
        public key. If a certificate is already registered (and not deleted) an
        exception indication a conflict will be raised.

        :param public_key: NIST P-256 Elliptic Curve public key, base64 encoded.
        :return: The newly created certificate object
        :rtype: Certificate
        """
        api = self.cert.DefaultApi()

        body = cert.Body()
        body.pub_key = public_key

        return Certificate(api.v3_developer_certificate_post(self.auth, body))


class Certificate(DeveloperCertificate):
    """Describes device certificate object."""

    def __init__(self, developer_certificate_obj):
        """Override __init__ and allow passing in backend object."""
        super(Certificate, self).__init__(**developer_certificate_obj.to_dict())
