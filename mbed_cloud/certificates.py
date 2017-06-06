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
"""Reference API for certificates component."""
from __future__ import absolute_import
from __future__ import unicode_literals

# Import common functions and exceptions from frontend API
from builtins import str
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

# Import backend API

import mbed_cloud._backends.connector_ca as cert
from mbed_cloud._backends.connector_ca.models import DeveloperCertificateResponseData
from mbed_cloud._backends.connector_ca.rest import ApiException
import mbed_cloud._backends.iam as iam
from mbed_cloud._backends.iam.models import TrustedCertificateResp


class CertificatesAPI(BaseAPI):
    """Certificates API reference."""

    def __init__(self, params={}):
        """Initialise the certificates API, optionally passing in overriding config."""
        super(CertificatesAPI, self).__init__(params)

        # Set the api_key for the requests
        self.cert = self._init_api(cert)
        self.iam = self._init_api(iam)
        self.auth = self.cert.configuration.api_key['Authorization']

    @catch_exceptions(ApiException)
    def list_certificates(self, **kwargs):
        """List certificates registered to organisation.

        :param int limit: (Optional) The number of logs to retrieve.
        :param str order: (Optional) The ordering direction, ascending (asc) or
            descending (desc).
        :param str after: (Optional) Get logs after/starting at given `device_log_id`.
        :param dict filters: (Optional) Dictionary of filters to apply.
        :return: list of :py:class:`DeviceLog` objects
        :rtype: Certificate
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        api = self.iam.AccountAdminApi()
        return PaginatedResponse(api.get_all_certificates, lwrap_type=Certificate, **kwargs)

    @catch_exceptions(ApiException)
    def get_certificate(self, certificate_id):
        """Get certificate by id.

        :param str certificate_id: The certificate id.
        :returns: Certificate object
        :rtype: Certificate
        """
        api = self.iam.AccountAdminApi()
        certificate = Certificate(api.get_certificate(certificate_id))
        self._extend_certificate(certificate)
        return certificate
        # return Certificate(api.get_certificate(certificate_id))

    def _extend_certificate(self, certificate):
        # extend certificate with developer_certificate properties
        if certificate.type == CertificateType.developer:
            dev_api = self.cert.DeveloperCertificateApi()
            dev_cert = dev_api.v3_developer_certificates_id_get(certificate.id, self.auth)
            certificate.update_certificate(dev_cert.__dict__)

    @catch_exceptions(ApiException)
    def delete_certificate(self, certificate_id):
        """Delete a certificate.

        :param str certificate_id: The certificate id.
        :returns: void
        """
        api = self.iam.AccountAdminApi()
        api.delete_certificate(certificate_id)
        return

    @catch_exceptions(ApiException)
    def add_certificate(self, name, type, **kwargs):
        """Add a new certificate.

        :param str name: name of the certificate.
        :param str type: type of the certificate.
        :param str certificate: (Optional) X509.v3 trusted certificate in PEM format.
            Required for types lwm2m and bootstrap.
        :param str signature: (Optional) Base64 encoded signature of the account ID
            signed by the certificate to be uploaded.
            Signature must be hashed with SHA256. Required for types lwm2m and bootstrap.
        :param str status: (Optional) Status of the certificate.
            Allowed values: "ACTIVE" | "INACTIVE".
        :param str description: (Optional) Human readable description of this certificate,
            not longer than 500 characters.
        :returns: Certificate object
        :rtype: Certificate
        """
        kwargs.update({'name': name})
        if type == CertificateType.developer:
            api = self.cert.DeveloperCertificateApi()
            body = cert.DeveloperCertificateRequestData(**kwargs)
            dev_cert = api.v3_developer_certificates_post(self.auth, body)
            return self.get_certificate(dev_cert.id)
        else:
            api = self.iam.AccountAdminApi()
            kwargs["service"] = type
            body = iam.TrustedCertificateReq(**kwargs)
            return api.add_certificate(body)

    @catch_exceptions(ApiException)
    def update_certificate(self, certificate_id, **kwargs):
        """Update a certificate.

        :param str certificate_id: The certificate id.
        :param str certificate: (Optional) X509.v3 trusted certificate in PEM format.
            Required for types lwm2m and bootstrap.
        :param str signature: (Optional) Base64 encoded signature of the account ID
            signed by the certificate to be uploaded.
        :param str status: (Optional) Status of the certificate.
            Allowed values: "ACTIVE" | "INACTIVE".
        :param str description: (Optional) Human readable description of this certificate,
            not longer than 500 characters.
        :returns: Certificate object
        :rtype: Certificate
        """
        api = self.iam.AccountAdminApi()
        body = iam.TrustedCertificateReq(**kwargs)
        certificate = Certificate(api.update_certificate(certificate_id, body))
        return self.get_certificate(certificate.id)


class Enumeration(set):
    """Enumeration class."""

    def __getattr__(self, name):
        """Get attribute. Return name of the attribute."""
        if name in self:
            return name
        raise AttributeError

    def __setattr__(self, name, value):
        """Set attribute. Method not allowed. Raises RuntimeError."""
        raise RuntimeError("Cannot override values in Enum")

    def __delattr__(self, name):
        """Delete attribute. Method not allowed. Raises RuntimeError."""
        raise RuntimeError("Cannot delete values from Enum")


CertificateType = Enumeration(["developer", "bootstrap", "lwm2m"])


class Certificate(TrustedCertificateResp, DeveloperCertificateResponseData):
    """Describes device certificate object."""

    def __init__(self, certificate_obj):
        """Override __init__ and allow passing in backend object.

        :param object certificate_obj: Certificate object..
        """
        super(Certificate, self).__init__(**certificate_obj.to_dict())
        if self.device_execution_mode == 1:
            self._type = CertificateType.developer
        elif self.service == CertificateType.bootstrap:
            self._type = CertificateType.bootstrap
        else:
            self._type = CertificateType.lwm2m

    def update_certificate(self, dev_certificate):
        """Update certificate with attributes from developer certificate.

        :param dict dev_certificate: Developer certificate dictionary.
        """
        self.__dict__.update(dev_certificate)

    @property
    def type(self):
        """Get the type of this certificate.

        :return: The type of the certificate.
        :rtype: CertificateType
        """
        return self._type

    def to_dict(self):
        """Convert Certificate to dictionary"""
        # List of properties to be excluded from dict
        deletes = ('creation_time_millis', 'device_execution_mode', 'etag', 'object', 'service')
        d = super(Certificate, self).to_dict()
        d["type"] = self._type
        # Remove keys from dictionary if they exist
        for key in deletes:
            d.pop(key, None)
        return d

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())
