"""
.. warning::
    TrustedCertificate should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: TrustedCertificate
=====================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`TrustedCertificate.create`
- :meth:`TrustedCertificate.delete`
- :meth:`TrustedCertificate.get_developer_certificate_info`
- :meth:`TrustedCertificate.list`
- :meth:`TrustedCertificate.read`
- :meth:`TrustedCertificate.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    trusted_certificates = pelion_dm_sdk.foundation.trusted_certificate()

How to import TrustedCertificate directly:

.. code-block:: python
    
    from mbed_cloud.foundation import TrustedCertificate

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class TrustedCertificate(Entity):
    """Represents the `TrustedCertificate` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
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
        """Creates a local `TrustedCertificate` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: The ID of the account.
        :type account_id: str
        :param certificate: (Required) X509.v3 trusted certificate in PEM format.
        :type certificate: str
        :param certificate_fingerprint: A SHA-256 fingerprint of the certificate.
        :type certificate_fingerprint: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Human readable description of this certificate.
        :type description: str
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
        :param service: (Required) Service name where the certificate is to be used.
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
        self._device_execution_mode = fields.IntegerField(value=None)
        self._enrollment_mode = fields.BooleanField(value=enrollment_mode)
        self._id = fields.StringField(value=id)
        self._is_developer_certificate = fields.BooleanField(value=is_developer_certificate)
        self._issuer = fields.StringField(value=issuer)
        self._name = fields.StringField(value=name)
        self._owner_id = fields.StringField(value=owner_id)
        self._service = fields.StringField(
            value=service, enum=enums.TrustedCertificateServiceEnum
        )
        self._status = fields.StringField(
            value=status, enum=enums.TrustedCertificateStatusEnum
        )
        self._subject = fields.StringField(value=subject)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._valid = fields.BooleanField(value=valid)
        self._validity = fields.DateTimeField(value=validity)

    @property
    def account_id(self):
        """The ID of the account.
        
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

        This field must be set when creating a new TrustedCertificate Entity.
        
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

    @certificate_fingerprint.setter
    def certificate_fingerprint(self, value):
        """Set value of `certificate_fingerprint`

        :param value: value to set
        :type value: str
        """

        self._certificate_fingerprint.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """Set value of `created_at`

        :param value: value to set
        :type value: datetime
        """

        self._created_at.set(value)

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

        This field must be set when updating or deleting an existing TrustedCertificate Entity.
        
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

        return is_developer_certificate_getter(
            self=self, field=self._is_developer_certificate
        )

    @is_developer_certificate.setter
    def is_developer_certificate(self, value):
        """Set value of `is_developer_certificate`

        :param value: value to set
        :type value: bool
        """

        from mbed_cloud.foundation._custom_methods import is_developer_certificate_setter

        is_developer_certificate_setter(
            self=self, field=self._is_developer_certificate, value=value
        )

    @property
    def issuer(self):
        """Issuer of the certificate.
        
        api example: 'CN=issuer'
        
        :rtype: str
        """

        return self._issuer.value

    @issuer.setter
    def issuer(self, value):
        """Set value of `issuer`

        :param value: value to set
        :type value: str
        """

        self._issuer.set(value)

    @property
    def name(self):
        """Certificate name.

        This field must be set when creating a new TrustedCertificate Entity.
        
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

    @owner_id.setter
    def owner_id(self, value):
        """Set value of `owner_id`

        :param value: value to set
        :type value: str
        """

        self._owner_id.set(value)

    @property
    def service(self):
        """Service name where the certificate is to be used.

        This field must be set when creating a new TrustedCertificate Entity.
        
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

    @subject.setter
    def subject(self, value):
        """Set value of `subject`

        :param value: value to set
        :type value: str
        """

        self._subject.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """Set value of `updated_at`

        :param value: value to set
        :type value: datetime
        """

        self._updated_at.set(value)

    @property
    def valid(self):
        """This read-only flag indicates whether the certificate is valid or not.
        
        api example: True
        
        :rtype: bool
        """

        return self._valid.value

    @valid.setter
    def valid(self, value):
        """Set value of `valid`

        :param value: value to set
        :type value: bool
        """

        self._valid.set(value)

    @property
    def validity(self):
        """Expiration time in UTC formatted as RFC3339.
        
        api example: '2038-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._validity.value

    @validity.setter
    def validity(self, value):
        """Set value of `validity`

        :param value: value to set
        :type value: datetime
        """

        self._validity.set(value)

    def create(self):
        """Upload a new trusted certificate.

        .. _REST API Documentation: https://os.mbed.com/search/?q=Service+API+References+/v3/trusted-certificates
        
        :rtype: TrustedCertificate
        """

        return self._client.call_api(
            method="post",
            path="/v3/trusted-certificates",
            body_params={
                "certificate": self._certificate.to_api(),
                "description": self._description.to_api(),
                "enrollment_mode": self._enrollment_mode.to_api(),
                "name": self._name.to_api(),
                "service": self._service.to_api(),
                "status": self._status.to_api(),
            },
            unpack=self,
        )

    def delete(self):
        """Delete a trusted certificate by ID.

        .. _REST API Documentation: https://os.mbed.com/search/?q=Service+API+References+/v3/trusted-certificates/{cert_id}
        
        :rtype: TrustedCertificate
        """

        return self._client.call_api(
            method="delete",
            path="/v3/trusted-certificates/{cert_id}",
            path_params={"cert_id": self._id.to_api()},
            unpack=self,
        )

    def get_developer_certificate_info(self):
        """Fetch an existing developer certificate to connect to the bootstrap server.

        .. _REST API Documentation: https://os.mbed.com/search/?q=Service+API+References+/v3/developer-certificates/{developerCertificateId}
        
        :rtype: DeveloperCertificate
        """

        from mbed_cloud.foundation import DeveloperCertificate

        return self._client.call_api(
            method="get",
            path="/v3/developer-certificates/{developerCertificateId}",
            path_params={"developerCertificateId": self._id.to_api()},
            unpack=DeveloperCertificate,
        )

    def list(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get all trusted certificates.

        .. _REST API Documentation: https://os.mbed.com/search/?q=Service+API+References+/v3/trusted-certificates

        **API Filters**

        The following filters are supported by the API when listing TrustedCertificate entities:

        +-----------------------+------+------+------+------+------+------+------+
        | Field                 | eq   | neq  | gte  | lte  | in   | nin  | like |
        +=======================+======+======+======+======+======+======+======+
        | device_execution_mode | Y    | Y    |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | enrollment_mode       | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | expire                | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | issuer                |      |      |      |      |      |      | Y    |
        +-----------------------+------+------+------+------+------+------+------+
        | name                  | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | owner                 | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | service               | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | status                | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | subject               |      |      |      |      |      |      | Y    |
        +-----------------------+------+------+------+------+------+------+------+
        | valid                 | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import TrustedCertificate
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("device_execution_mode", "eq", <filter value>)
            for trusted_certificate in TrustedCertificate().list(filter=api_filter):
                print(trusted_certificate.device_execution_mode)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000), default is 50.
        :type page_size: int
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(TrustedCertificate)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import TrustedCertificate
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(
                filter_definition=filter, field_renames=TrustedCertificate._renames_to_api
            )
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = TrustedCertificate._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=TrustedCertificate,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get all trusted certificates.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(
            order, enum=enums.TrustedCertificateOrderEnum
        ).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/trusted-certificates",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get trusted certificate by ID.

        .. _REST API Documentation: https://os.mbed.com/search/?q=Service+API+References+/v3/trusted-certificates/{cert_id}
        
        :rtype: TrustedCertificate
        """

        return self._client.call_api(
            method="get",
            path="/v3/trusted-certificates/{cert_id}",
            path_params={"cert_id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Update trusted certificate.

        .. _REST API Documentation: https://os.mbed.com/search/?q=Service+API+References+/v3/trusted-certificates/{cert_id}
        
        :rtype: TrustedCertificate
        """

        return self._client.call_api(
            method="put",
            path="/v3/trusted-certificates/{cert_id}",
            body_params={
                "certificate": self._certificate.to_api(),
                "description": self._description.to_api(),
                "enrollment_mode": self._enrollment_mode.to_api(),
                "name": self._name.to_api(),
                "service": self._service.to_api(),
                "status": self._status.to_api(),
            },
            path_params={"cert_id": self._id.to_api()},
            unpack=self,
        )
