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
from mbed_cloud.core import BaseAPI
from mbed_cloud.core import BaseObject
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud.pagination import PaginatedResponse

# Import backend API
import mbed_cloud._backends.connector_ca as cert
from mbed_cloud._backends.connector_ca.rest import ApiException as CaApiException
import mbed_cloud._backends.iam as iam
from mbed_cloud._backends.iam.rest import ApiException as IamApiException


class CertificatesAPI(BaseAPI):
    """Certificates API reference."""

    api_structure = {
        cert: [cert.DeveloperCertificateApi, cert.ServerCredentialsApi],
        iam: [iam.AccountAdminApi, iam.DeveloperApi],
    }

    def __init__(self, params=None):
        """Initialise the certificates API, optionally passing in overriding config."""
        super(CertificatesAPI, self).__init__(params)
        self.auth = self.api_clients[cert].configuration.api_key['Authorization']

    @catch_exceptions(IamApiException)
    def list_certificates(self, **kwargs):
        """List certificates registered to organisation.

        Currently returns partially populated certificates. To obtain the full certificate object:
        `[get_certificate(certificate_id=cert['id']) for cert in list_certificates]`

        :param int limit: The number of certificates to retrieve.
        :param str order: The ordering direction, ascending (asc) or
            descending (desc).
        :param str after: Get certificates after/starting at given `certificate_id`.
        :param dict filters: Dictionary of filters to apply: type (eq), expire (eq), owner (eq)
        :return: list of :py:class:`Certificate` objects
        :rtype: Certificate
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, Certificate)
        if "service__eq" in kwargs:
            if kwargs["service__eq"] == CertificateType.bootstrap:
                pass
            elif kwargs["service__eq"] == CertificateType.developer:
                kwargs["device_execution_mode__eq"] = 1
                kwargs.pop("service__eq")
            elif kwargs["service__eq"] == CertificateType.lwm2m:
                pass
            else:
                raise CloudValueError(
                    "Incorrect value for CertificateType filter: %s" % (kwargs["service__eq"])
                )
        owner = kwargs.pop('owner_id__eq', None)
        if owner is not None:
            kwargs['owner__eq'] = owner
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
            dev_cert = dev_api.v3_developer_certificates_muuid_get(certificate.id, self.auth)
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
        kwargs['name'] = name
        api = self._get_api(cert.DeveloperCertificateApi)
        certificate = Certificate._create_request_map(kwargs)

        # just pull the fields we care about
        subset = cert.DeveloperCertificateRequestData.attribute_map
        certificate = {k: v for k, v in certificate.items() if k in subset}

        body = cert.DeveloperCertificateRequestData(**certificate)
        dev_cert = api.v3_developer_certificates_post(self.auth, body)
        return self.get_certificate(dev_cert.id)

    @catch_exceptions(IamApiException)
    def update_certificate(self, certificate_id, **kwargs):
        """Update a certificate.

        :param str certificate_id: The certificate id (Required)
        :param str certificate_data: X509.v3 trusted certificate in PEM format.
        :param str signature: Base64 encoded signature of the account ID
            signed by the certificate to be uploaded. Available only for bootstrap and lwm2m types.
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
            "updated_at": "updated_at",
            "issuer": "issuer",
            "subject": "subject",
            "validity": "validity",
            "owner_id": "owner_id",
            "server_uri": "server_uri",
            "server_certificate": "server_certificate",
            "header_file": "security_file_content",
            "developer_certificate": "developer_certificate",
            "developer_private_key": "developer_private_key",
            "enrollment_mode": "enrollment_mode",
            "signature": "signature",
        }

    @classmethod
    def _create_request_map(cls, input_map):
        """Create request map."""
        mapped = super(Certificate, cls)._create_request_map(input_map)
        if mapped.get('service') == CertificateType.developer:
            mapped['service'] = CertificateType.bootstrap
        return mapped

    @property
    def status(self):
        """The status of the certificate.

        :return: The status of this certificate.
        :rtype: str
        """
        return self._status

    @property
    def signature(self):
        """The signature of the certificate.

        :return: The signature of this certificate.
        :rtype: str
        """
        return self._signature

    @property
    def enrollment_mode(self):
        """The enrollment_mode of the certificate.

        :return: The enrollment_mode of this certificate.
        :rtype: str
        """
        return self._enrollment_mode or False  # FIXME: is this the correct default?

    @property
    def description(self):
        """Human readable description of this certificate.

        :return: The description of this certificate.
        :rtype: str
        """
        return self._description

    @property
    def device_mode(self):
        """The device mode

        :rtype: str
        """
        return self._device_mode

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
    def updated_at(self):
        """Update UTC time RFC3339.

        :rtype: datetime
        """
        return self._updated_at

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
