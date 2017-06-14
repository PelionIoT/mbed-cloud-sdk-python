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
from mbed_cloud import BaseAPI
from mbed_cloud import BaseObject
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud import PaginatedResponse

# Import backend API

import mbed_cloud._backends.connector_ca as cert
from mbed_cloud._backends.connector_ca.rest import ApiException
import mbed_cloud._backends.iam as iam


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

        :param int limit: The number of logs to retrieve.
        :param str order: The ordering direction, ascending (asc) or
            descending (desc).
        :param str after: Get logs after/starting at given `device_log_id`.
        :param dict filters: Dictionary of filters to apply: type (eq), expire (eq), owner (eq)
        :return: list of :py:class:`DeviceLog` objects
        :rtype: Certificate
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        if "type__eq" in kwargs:
            if kwargs["type__eq"] == CertificateType.bootstrap:
                kwargs["service__eq"] = CertificateType.bootstrap
                kwargs["device_execution_mode__eq"] = 0
            elif kwargs["type__eq"] == CertificateType.developer:
                kwargs["device_execution_mode__eq"] = 1
            elif kwargs["type__eq"] == CertificateType.lwm2m:
                kwargs["service__eq"] = CertificateType.lwm2m
                kwargs["device_execution_mode__eq"] = 0
            else:
                raise CloudValueError("Incorrect filter 'type': %s" % (kwargs["type__eq"]))
            del kwargs["type__eq"]
        api = self.iam.AccountAdminApi()
        return PaginatedResponse(api.get_all_certificates, lwrap_type=Certificate, **kwargs)

    @catch_exceptions(ApiException)
    def get_certificate(self, certificate_id):
        """Get certificate by id.

        :param str certificate_id: The certificate id (Required)
        :returns: Certificate object
        :rtype: Certificate
        """
        api = self.iam.AccountAdminApi()
        certificate = Certificate(api.get_certificate(certificate_id))
        self._extend_certificate(certificate)
        return certificate

    def _extend_certificate(self, certificate):
        # extend certificate with developer_certificate properties
        if certificate.type == CertificateType.developer:
            dev_api = self.cert.DeveloperCertificateApi()
            dev_cert = dev_api.v3_developer_certificates_id_get(certificate.id, self.auth)
            certificate.update_attributes(dev_cert)

    @catch_exceptions(ApiException)
    def delete_certificate(self, certificate_id):
        """Delete a certificate.

        :param str certificate_id: The certificate id (Required)
        :returns: void
        """
        api = self.iam.AccountAdminApi()
        api.delete_certificate(certificate_id)
        return

    @catch_exceptions(ApiException)
    def add_certificate(self, name, type, **kwargs):
        """Add a new certificate.

        :param str name: name of the certificate (Required)
        :param str type: type of the certificate (Required)
        :param str certificate: X509.v3 trusted certificate in PEM format.
            Required for types lwm2m and bootstrap.
        :param str signature: Base64 encoded signature of the account ID
            signed by the certificate to be uploaded.
            Signature must be hashed with SHA256. Required for types lwm2m and bootstrap.
        :param str status: Status of the certificate.
            Allowed values: "ACTIVE" | "INACTIVE".
        :param str description: Human readable description of this certificate,
            not longer than 500 characters.
        :returns: Certificate object
        :rtype: Certificate
        """
        kwargs.update({'name': name})
        if type == CertificateType.developer:
            api = self.cert.DeveloperCertificateApi()
            certificate = Certificate.create_request_map(kwargs)
            body = cert.DeveloperCertificateRequestData(**certificate)
            dev_cert = api.v3_developer_certificates_post(self.auth, body)
            return self.get_certificate(dev_cert.id)
        else:
            api = self.iam.AccountAdminApi()
            kwargs["service"] = type
            certificate = Certificate.create_request_map(kwargs)
            body = iam.TrustedCertificateReq(**certificate)
            return api.add_certificate(body)

    @catch_exceptions(ApiException)
    def update_certificate(self, certificate_id, **kwargs):
        """Update a certificate.

        :param str certificate_id: The certificate id (Required)
        :param str certificate: X509.v3 trusted certificate in PEM format.
            Required for types lwm2m and bootstrap.
        :param str signature: Base64 encoded signature of the account ID
            signed by the certificate to be uploaded.
        :param str status: Status of the certificate.
            Allowed values: "ACTIVE" | "INACTIVE".
        :param str description: Human readable description of this certificate,
            not longer than 500 characters.
        :returns: Certificate object
        :rtype: Certificate
        """
        api = self.iam.AccountAdminApi()
        cert = Certificate.create_request_map(kwargs)
        body = iam.TrustedCertificateReq(**cert)
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


class Certificate(BaseObject):
    """Describes device certificate object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "id": "id",
            "name": "name",
            "description": "description",
            "type": "device_execution_mode",
            "service": "service",
            "status": "status",
            "account_id": "account_id",
            "certificate_data": "certificate",
            "created_at": "created_at",
            "issuer": "issuer",
            "subject": "subject",
            "validity": "validity",
            "owner_id": "owner_id",
            "server_uri": "server_uri",
            "server_certificate": "server_certificate",
            "header_file": "security_file_content",
            "developer_certificate": "developer_certificate",
            "developer_private_key": "developer_private_key"
        }

    @property
    def status(self):
        """The status of the certificate.

        :return: The status of this certificate.
        :rtype: str
        """
        return self._status

    @property
    def description(self):
        """Human readable description of this certificate.

        :return: The description of this certificate.
        :rtype: str
        """
        return self._description

    @property
    def certificate_data(self):
        """X509.v3 trusted certificate data in PEM format.

        :return: The certificate data.
        :rtype: str
        """
        return self._certificate_data

    @property
    def issuer(self):
        """Issuer of the certificate.

        :return: The issuer of this certificate.
        :rtype: str
        """
        return self._issuer

    @property
    def type(self):
        """Certificate type.

        :return: The type of the certificate.
        :rtype: CertificateType
        """
        if self._type == 1:
            return CertificateType.developer
        elif self._service == CertificateType.bootstrap:
            return CertificateType.bootstrap
        else:
            return CertificateType.lwm2m

    @property
    def created_at(self):
        """Creation UTC time RFC3339.

        :rtype: datetime
        """
        return self._created_at

    @property
    def subject(self):
        """Subject of the certificate.

        :return: The subject of this certificate.
        :rtype: str
        """
        return self._subject

    @property
    def account_id(self):
        """The UUID of the account.

        :rtype: str
        """
        return self._account_id

    @property
    def validity(self):
        """Expiration time in UTC formatted as RFC3339.

        :return: The validity of this certificate.
        :rtype: datetime
        """
        return self._validity

    @property
    def owner_id(self):
        """The UUID of the owner.

        :rtype: str
        """
        return self._owner_id

    @property
    def id(self):
        """ID of this certificate.

        :return: The id of this certificate.
        :rtype: str
        """
        return self._id

    @property
    def name(self):
        """Certificate name.

        :return: The name of this certificate.
        :rtype: str
        """
        return self._name

    @property
    def header_file(self):
        """The content of the `security.c` file that is flashed into the device

        to provide the security credentials.
        :rtype: str
        """
        return self._header_file

    @property
    def developer_certificate(self):
        """The PEM format X.509 developer certificate.

        :rtype: str
        """
        return self._developer_certificate

    @property
    def server_uri(self):
        """The URI to which the client needs to connect to.

        :rtype: str
        """
        return self._server_uri

    @property
    def developer_private_key(self):
        """The PEM format developer private key associated to the certificate.

        :rtype: str
        """
        return self._developer_private_key

    @property
    def server_certificate(self):
        """The PEM format X.509 server certificate that is used to validate

        the server certificate that is received during the TLS/DTLS handshake.

        :rtype: str
        """
        return self._server_certificate
