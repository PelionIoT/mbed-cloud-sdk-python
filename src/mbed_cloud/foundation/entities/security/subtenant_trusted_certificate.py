"""
.. warning::
    SubtenantTrustedCertificate should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SubtenantTrustedCertificate
==============================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`SubtenantTrustedCertificate.create`
- :meth:`SubtenantTrustedCertificate.delete`
- :meth:`SubtenantTrustedCertificate.get_developer_certificate_info`
- :meth:`SubtenantTrustedCertificate.read`
- :meth:`SubtenantTrustedCertificate.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    subtenant_trusted_certificates = pelion_dm_sdk.foundation.subtenant_trusted_certificate()

How to import SubtenantTrustedCertificate directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SubtenantTrustedCertificate

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SubtenantTrustedCertificate(Entity):
    """Represents the `SubtenantTrustedCertificate` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "account_id",
        "certificate",
        "certificate_fingerprint",
        "created_at",
        "description",
        "device_execution_mode",
        "enrollment_mode",
        "id",
        "is_developer_certificate",
        "issuer",
        "name",
        "owner_id",
        "service",
        "status",
        "subject",
        "updated_at",
        "valid",
        "validity",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        certificate=None,
        certificate_fingerprint=None,
        created_at=None,
        description=None,
        device_execution_mode=None,
        enrollment_mode=None,
        id=None,
        is_developer_certificate=None,
        issuer=None,
        name=None,
        owner_id=None,
        service=None,
        status=None,
        subject=None,
        updated_at=None,
        valid=None,
        validity=None,
    ):
        """Creates a local `SubtenantTrustedCertificate` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: (Required) The ID of the account.
        :type account_id: str
        :param certificate: (Required) X509.v3 trusted certificate in PEM format.
        :type certificate: str
        :param certificate_fingerprint: A SHA-256 fingerprint of the certificate.
        :type certificate_fingerprint: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Human readable description of this certificate.
        :type description: str
        :param device_execution_mode: Device execution mode where 1 means a developer certificate.
        :type device_execution_mode: int
        :param enrollment_mode: If true, signature is not required. Default value false.
        :type enrollment_mode: bool
        :param id: (Required) Entity ID.
        :type id: str
        :param is_developer_certificate: Whether or not this certificate is a developer certificate.
        :type is_developer_certificate: bool
        :param issuer: Issuer of the certificate.
        :type issuer: str
        :param name: (Required) Certificate name.
        :type name: str
        :param owner_id: The ID of the owner.
        :type owner_id: str
        :param service: (Required) Service name where the certificate is used.
        :type service: str
        :param status: Status of the certificate.
        :type status: str
        :param subject: Subject of the certificate.
        :type subject: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param valid: This read-only flag indicates whether the certificate is valid or
            not.
        :type valid: bool
        :param validity: Expiration time in UTC formatted as RFC3339.
        :type validity: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._certificate = fields.StringField(value=certificate)
        self._certificate_fingerprint = fields.StringField(value=certificate_fingerprint)
        self._created_at = fields.DateTimeField(value=created_at)
        self._description = fields.StringField(value=description)
        self._device_execution_mode = fields.IntegerField(value=device_execution_mode)
        self._enrollment_mode = fields.BooleanField(value=enrollment_mode)
        self._id = fields.StringField(value=id)
        self._is_developer_certificate = fields.BooleanField(value=is_developer_certificate)
        self._issuer = fields.StringField(value=issuer)
        self._name = fields.StringField(value=name)
        self._owner_id = fields.StringField(value=owner_id)
        self._service = fields.StringField(value=service, enum=enums.SubtenantTrustedCertificateServiceEnum)
        self._status = fields.StringField(value=status, enum=enums.SubtenantTrustedCertificateStatusEnum)
        self._subject = fields.StringField(value=subject)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._valid = fields.BooleanField(value=valid)
        self._validity = fields.DateTimeField(value=validity)

    @property
    def account_id(self):
        """The ID of the account.

        This field must be set when creating a new SubtenantTrustedCertificate Entity.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """Set value of `account_id`

        :param value: value to set
        :type value: str
        """

        self._account_id.set(value)

    @property
    def certificate(self):
        """X509.v3 trusted certificate in PEM format.

        This field must be set when creating a new SubtenantTrustedCertificate Entity.
        
        api example: '-----BEGIN CERTIFICATE----- ... -----END CERTIFICATE-----'
        
        :rtype: str
        """

        return self._certificate.value

    @certificate.setter
    def certificate(self, value):
        """Set value of `certificate`

        :param value: value to set
        :type value: str
        """

        self._certificate.set(value)

    @property
    def certificate_fingerprint(self):
        """A SHA-256 fingerprint of the certificate.
        
        api example: 'a10fb2c8ba90e6de927bd0ae391dcc38f6115685de2d7024712af37ead0608f1'
        
        :rtype: str
        """

        return self._certificate_fingerprint.value

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def description(self):
        """Human readable description of this certificate.
        
        api example: 'Certificate created by me.'
        
        :rtype: str
        """

        return self._description.value

    @description.setter
    def description(self, value):
        """Set value of `description`

        :param value: value to set
        :type value: str
        """

        self._description.set(value)

    @property
    def device_execution_mode(self):
        """Device execution mode where 1 means a developer certificate.
        
        api example: 1
        
        :rtype: int
        """

        return self._device_execution_mode.value

    @property
    def enrollment_mode(self):
        """If true, signature is not required. Default value false.
        
        :rtype: bool
        """

        return self._enrollment_mode.value

    @enrollment_mode.setter
    def enrollment_mode(self, value):
        """Set value of `enrollment_mode`

        :param value: value to set
        :type value: bool
        """

        self._enrollment_mode.set(value)

    @property
    def id(self):
        """Entity ID.

        This field must be set when updating or deleting an existing SubtenantTrustedCertificate Entity.
        
        api example: '01619571d01d0242ac12000600000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        self._id.set(value)

    @property
    def is_developer_certificate(self):
        """Whether or not this certificate is a developer certificate.
        
        api example: True
        
        :rtype: bool
        """

        from mbed_cloud.foundation._custom_methods import is_developer_certificate_getter

        return is_developer_certificate_getter(self=self)

    @property
    def issuer(self):
        """Issuer of the certificate.
        
        api example: 'CN=issuer'
        
        :rtype: str
        """

        return self._issuer.value

    @property
    def name(self):
        """Certificate name.

        This field must be set when creating a new SubtenantTrustedCertificate Entity.
        
        api example: 'My certificate'
        
        :rtype: str
        """

        return self._name.value

    @name.setter
    def name(self, value):
        """Set value of `name`

        :param value: value to set
        :type value: str
        """

        self._name.set(value)

    @property
    def owner_id(self):
        """The ID of the owner.
        
        api example: '01619571dad80242ac12000600000000'
        
        :rtype: str
        """

        return self._owner_id.value

    @property
    def service(self):
        """Service name where the certificate is used.

        This field must be set when creating a new SubtenantTrustedCertificate Entity.
        
        :rtype: str
        """

        return self._service.value

    @service.setter
    def service(self, value):
        """Set value of `service`

        :param value: value to set
        :type value: str
        """

        self._service.set(value)

    @property
    def status(self):
        """Status of the certificate.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """

        return self._status.value

    @status.setter
    def status(self, value):
        """Set value of `status`

        :param value: value to set
        :type value: str
        """

        self._status.set(value)

    @property
    def subject(self):
        """Subject of the certificate.
        
        api example: 'CN=subject'
        
        :rtype: str
        """

        return self._subject.value

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @property
    def valid(self):
        """This read-only flag indicates whether the certificate is valid or not.
        
        api example: True
        
        :rtype: bool
        """

        return self._valid.value

    @property
    def validity(self):
        """Expiration time in UTC formatted as RFC3339.
        
        api example: '2038-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._validity.value

    def create(self):
        """Upload new trusted certificate.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/trusted-certificates>`_.
        
        :rtype: SubtenantTrustedCertificate
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._certificate.value_set:
            body_params["certificate"] = self._certificate.to_api()
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._enrollment_mode.value_set:
            body_params["enrollment_mode"] = self._enrollment_mode.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        if self._service.value_set:
            body_params["service"] = self._service.to_api()
        if self._status.value_set:
            body_params["status"] = self._status.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account_id}/trusted-certificates",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api()},
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete trusted certificate by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/trusted-certificates/{cert_id}>`_.
        
        :rtype: SubtenantTrustedCertificate
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account_id}/trusted-certificates/{cert_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "cert_id": self._id.to_api()},
            unpack=self,
        )

    def get_developer_certificate_info(self):
        """Fetch an existing developer certificate to connect to the bootstrap server.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/developer-certificates/{developerCertificateId}>`_.
        
        :rtype: DeveloperCertificate
        """

        from mbed_cloud.foundation import DeveloperCertificate

        return self._client.call_api(
            method="get",
            path="/v3/developer-certificates/{developerCertificateId}",
            content_type="application/json",
            path_params={"developerCertificateId": self._id.to_api()},
            unpack=DeveloperCertificate,
        )

    def read(self):
        """Get trusted certificate by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/trusted-certificates/{cert_id}>`_.
        
        :rtype: SubtenantTrustedCertificate
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/trusted-certificates/{cert_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "cert_id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Update trusted certificate.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/trusted-certificates/{cert_id}>`_.
        
        :rtype: SubtenantTrustedCertificate
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._certificate.value_set:
            body_params["certificate"] = self._certificate.to_api()
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._enrollment_mode.value_set:
            body_params["enrollment_mode"] = self._enrollment_mode.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        if self._service.value_set:
            body_params["service"] = self._service.to_api()
        if self._status.value_set:
            body_params["status"] = self._status.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/accounts/{account_id}/trusted-certificates/{cert_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "cert_id": self._id.to_api()},
            body_params=body_params,
            unpack=self,
        )
