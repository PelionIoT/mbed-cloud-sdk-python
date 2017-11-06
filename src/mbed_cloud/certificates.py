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
from mbed_cloud._backends.connector_ca.rest import ApiException as CaApiException
import mbed_cloud._backends.iam as iam
from mbed_cloud._backends.iam.rest import ApiException as IamApiException


class CertificatesAPI(BaseAPI):
    """Certificates API reference."""

    def __init__(self, params=None):
        """Initialise the certificates API, optionally passing in overriding config."""
        super(CertificatesAPI, self).__init__(params)

        # Set the api_key for the requests
        cert_api_client = self._init_api(cert, [cert.DeveloperCertificateApi,
                                                cert.ServerCredentialsApi])
        self._init_api(iam, [iam.AccountAdminApi, iam.DeveloperApi])
        self.auth = cert_api_client.configuration.api_key['Authorization']

    @catch_exceptions(IamApiException)
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
        kwargs = self._verify_filters(kwargs, Certificate)

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
        api = self._get_api(iam.DeveloperApi)
        return PaginatedResponse(api.get_all_certificates, lwrap_type=Certificate, **kwargs)

    @catch_exceptions(CaApiException, IamApiException)
    def get_certificate(self, certificate_id):
        """Get certificate by id.

        :param str certificate_id: The certificate id (Required)
        :returns: Certificate object
        :rtype: Certificate
        """
        api = self._get_api(iam.DeveloperApi)
        certificate = Certificate(api.get_certificate(certificate_id))
        self._extend_certificate(certificate)
        return certificate

    def _extend_certificate(self, certificate):
        # extend certificate with developer_certificate properties
        if certificate.type == CertificateType.developer:
            dev_api = self._get_api(cert.DeveloperCertificateApi)
            dev_cert = dev_api.v3_developer_certificates_id_get(certificate.id, self.auth)
            certificate.update_attributes(dev_cert)
        elif certificate.type == CertificateType.bootstrap:
            server_api = self._get_api(cert.ServerCredentialsApi)
            credentials = server_api.v3_server_credentials_bootstrap_get(self.auth)
            certificate.update_attributes(credentials)
        elif certificate.type == CertificateType.lwm2m:
            server_api = self._get_api(cert.ServerCredentialsApi)
            credentials = server_api.v3_server_credentials_lwm2m_get(self.auth)
            certificate.update_attributes(credentials)

    @catch_exceptions(IamApiException)
    def delete_certificate(self, certificate_id):
        """Delete a certificate.

        :param str certificate_id: The certificate id (Required)
        :returns: void
        """
        api = self._get_api(iam.DeveloperApi)
        api.delete_certificate(certificate_id)
        return

    @catch_exceptions(CaApiException, IamApiException)
    def add_certificate(self, name, type, certificate_data, signature, **kwargs):
        """Add a new BYOC certificate.

        :param str name: name of the certificate (Required)
        :param str type: type of the certificate. Values: lwm2m or bootstrap (Required)
        :param str certificate_data: X509.v3 trusted certificate in PEM format. (Required)
        :param str signature: Base64 encoded signature of the account ID
            signed by the certificate to be uploaded.
            Signature must be hashed with SHA256. (Required)
        :param str status: Status of the certificate.
            Allowed values: "ACTIVE" | "INACTIVE".
        :param str description: Human readable description of this certificate,
            not longer than 500 characters.
        :returns: Certificate object
        :rtype: Certificate
        """
        kwargs.update({'name': name})
        kwargs.update({'type': type})
        api = self._get_api(iam.AccountAdminApi)

        kwargs.update({'certificate_data': certificate_data})
        certificate = Certificate._create_request_map(kwargs)
        certificate.update({'signature': signature})
        body = iam.TrustedCertificateReq(**certificate)
        prod_cert = api.add_certificate(body)
        return self.get_certificate(prod_cert.id)

    @catch_exceptions(CaApiException, IamApiException)
    def add_developer_certificate(self, name, **kwargs):
        """Add a new developer certificate.

        :param str name: name of the certificate (Required)
        :param str description: Human readable description of this certificate,
            not longer than 500 characters.
        :returns: Certificate object
        :rtype: Certificate
        """
        kwargs.update({'name': name})
        api = self._get_api(cert.DeveloperCertificateApi)
        certificate = Certificate._create_request_map(kwargs)
        body = cert.DeveloperCertificateRequestData(**certificate)
        dev_cert = api.v3_developer_certificates_post(self.auth, body)
        return self.get_certificate(dev_cert.id)

    @catch_exceptions(IamApiException)
    def update_certificate(self, certificate_id, **kwargs):
        """Update a certificate.

        :param str certificate_id: The certificate id (Required)
        :param str certificate_data: X509.v3 trusted certificate in PEM format.
        :param str signature: Base64 encoded signature of the account ID
            signed by the certificate to be uploaded. Available only for bootstrap and lvm2m types.
        :param str type: type of the certificate. Values: lwm2m or bootstrap.
        :param str status: Status of the certificate.
            Allowed values: "ACTIVE" | "INACTIVE".
        :param str description: Human readable description of this certificate,
            not longer than 500 characters.
        :returns: Certificate object
        :rtype: Certificate
        """
        api = self._get_api(iam.DeveloperApi)
        cert = Certificate._create_request_map(kwargs)
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
            "type": "service",
            "device_mode": "device_execution_mode",
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
        if self._device_mode == 1 or self._type == CertificateType.developer:
            return CertificateType.developer
        elif self._type == CertificateType.bootstrap:
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

        to provide the security credentials. Set only for developer certificate.
        :rtype: str
        """
        return getattr(self, '_header_file', None)

    @property
    def developer_certificate(self):
        """The PEM format X.509 developer certificate.

        Set only for developer certificate.
        :rtype: str
        """
        return getattr(self, '_developer_certificate', None)

    @property
    def server_uri(self):
        """The URI to which the client needs to connect to.

        :rtype: str
        """
        return getattr(self, '_server_uri', None)

    @property
    def developer_private_key(self):
        """The PEM format developer private key associated with the certificate.

        Set only for developer certificate.
        :rtype: str
        """
        return getattr(self, '_developer_private_key', None)

    @property
    def server_certificate(self):
        """The PEM format X.509 server certificate that is used to validate

        the server certificate that is received during the TLS/DTLS handshake.

        :rtype: str
        """
        return getattr(self, '_server_certificate', None)
