"""
.. warning::
    IdentityProvider should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: IdentityProvider
===================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`IdentityProvider.create`
- :meth:`IdentityProvider.delete`
- :meth:`IdentityProvider.delete_service_provider_certificate`
- :meth:`IdentityProvider.generate_service_provider_certificate`
- :meth:`IdentityProvider.list`
- :meth:`IdentityProvider.read`
- :meth:`IdentityProvider.refresh_tokens`
- :meth:`IdentityProvider.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    identity_providers = pelion_dm_sdk.foundation.identity_provider()

How to import IdentityProvider directly:

.. code-block:: python
    
    from mbed_cloud.foundation import IdentityProvider

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class IdentityProvider(Entity):
    """Represents the `IdentityProvider` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "account_id",
        "created_at",
        "description",
        "id",
        "identity_provider_type",
        "is_default",
        "name",
        "saml2_attributes",
        "status",
        "updated_at",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {
        "type": "identity_provider_type",
    }

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {
        "identity_provider_type": "type",
    }

    def __init__(
        self,
        _client=None,
        account_id=None,
        created_at=None,
        description=None,
        id=None,
        identity_provider_type=None,
        is_default=None,
        name=None,
        saml2_attributes=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `IdentityProvider` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: The ID of the account the identity provider belongs to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Description for the identity provider.
        :type description: str
        :param id: (Required) Entity ID.
        :type id: str
        :param identity_provider_type: (Required) Identity provider type.
        :type identity_provider_type: str
        :param is_default: Flag indicating whether this is the global default identity
            provider.
        :type is_default: bool
        :param name: (Required) Name of the identity provider.
        :type name: str
        :param saml2_attributes: Represents SAML2 specific attributes in responses.
        :type saml2_attributes: dict
        :param status: Status of the identity provider.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._description = fields.StringField(value=description)
        self._id = fields.StringField(value=id)
        self._identity_provider_type = fields.StringField(
            value=identity_provider_type, enum=enums.IdentityProviderTypeEnum
        )
        self._is_default = fields.BooleanField(value=is_default)
        self._name = fields.StringField(value=name)
        self._saml2_attributes = fields.DictField(value=saml2_attributes)
        self._status = fields.StringField(value=status, enum=enums.IdentityProviderStatusEnum)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def account_id(self):
        """The ID of the account the identity provider belongs to.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._account_id.value

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def description(self):
        """Description for the identity provider.
        
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
    def id(self):
        """Entity ID.

        This field must be set when updating or deleting an existing IdentityProvider Entity.
        
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
    def identity_provider_type(self):
        """Identity provider type.

        This field must be set when creating a new IdentityProvider Entity.
        
        :rtype: str
        """

        return self._identity_provider_type.value

    @identity_provider_type.setter
    def identity_provider_type(self, value):
        """Set value of `identity_provider_type`

        :param value: value to set
        :type value: str
        """

        self._identity_provider_type.set(value)

    @property
    def is_default(self):
        """Flag indicating whether this is the global default identity provider.
        
        :rtype: bool
        """

        return self._is_default.value

    @property
    def name(self):
        """Name of the identity provider.

        This field must be set when creating a new IdentityProvider Entity.
        
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
    def saml2_attributes(self):
        """Represents SAML2 specific attributes in responses.
        
        :rtype: dict
        """

        return self._saml2_attributes.value

    @saml2_attributes.setter
    def saml2_attributes(self, value):
        """Set value of `saml2_attributes`

        :param value: value to set
        :type value: dict
        """

        self._saml2_attributes.set(value)

    @property
    def status(self):
        """Status of the identity provider.
        
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
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def create(self, discovery=None, oidc_attributes=None):
        """Create a new identity provider.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers>`_.
        
        :param discovery: Indicates that the OpenID Connect endpoints and keys should be set
            using the OpenID Connect Discovery mechanism. The following parameters
            are set automatically: * authorization_endpoint * token_endpoint *
            userinfo_endpoint * revocation_endpoint * jwks_uri * keys
        :type discovery: bool
        
        :param oidc_attributes: Represents OIDC specific attributes.
        :type oidc_attributes: mbed_cloud.foundation.entities.OidcRequest
        
        :rtype: IdentityProvider
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._identity_provider_type.value_set:
            body_params["type"] = self._identity_provider_type.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        # Method parameters are unconditionally sent even if set to None
        body_params["oidc_attributes"] = fields.DictField(oidc_attributes).to_api()
        if self._saml2_attributes.value_set:
            body_params["saml2_attributes"] = self._saml2_attributes.to_api()
        if self._status.value_set:
            body_params["status"] = self._status.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/identity-providers",
            content_type="application/json",
            body_params=body_params,
            query_params={"discovery": fields.BooleanField(discovery).to_api(),},
            unpack=self,
        )

    def delete(self):
        """Delete an identity provider by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers/{identity_provider_id}>`_.
        
        :rtype: IdentityProvider
        """

        return self._client.call_api(
            method="delete",
            path="/v3/identity-providers/{identity_provider_id}",
            content_type="application/json",
            path_params={"identity_provider_id": self._id.to_api(),},
            unpack=self,
        )

    def delete_service_provider_certificate(self):
        """Delete the service provider certificate.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers/{identity_provider_id}/delete-sp-certificate>`_.
        
        :rtype: IdentityProvider
        """

        return self._client.call_api(
            method="post",
            path="/v3/identity-providers/{identity_provider_id}/delete-sp-certificate",
            content_type="application/json",
            path_params={"identity_provider_id": self._id.to_api(),},
            unpack=self,
        )

    def generate_service_provider_certificate(self, algorithm=None, validity=None):
        """Generate a new service provider certificate.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers/{identity_provider_id}/generate-sp-certificate>`_.
        
        :param algorithm: The algorithm and its key size used for generating the certificate.
            Defaults to RSA2048.
        :type algorithm: str
        
        :param validity: Validity for the certificate in days.
        :type validity: int
        
        :rtype: IdentityProvider
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        # Method parameters are unconditionally sent even if set to None
        body_params["algorithm"] = fields.StringField(algorithm, enum=enums.IdentityProviderAlgorithmEnum).to_api()
        # Method parameters are unconditionally sent even if set to None
        body_params["validity"] = fields.IntegerField(validity).to_api()

        return self._client.call_api(
            method="post",
            path="/v3/identity-providers/{identity_provider_id}/generate-sp-certificate",
            content_type="application/json",
            body_params=body_params,
            path_params={"identity_provider_id": self._id.to_api(),},
            unpack=self,
        )

    def list(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get all identity providers.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers>`_.
        
        :param filter: Filtering when listing entities is not supported by the API for this
            entity.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000). Default 50.
        :type page_size: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(IdentityProvider)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import IdentityProvider
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=IdentityProvider._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = IdentityProvider._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=IdentityProvider,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get all identity providers.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param limit: The number of results to return (2-1000). Default 50.
        :type limit: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.IdentityProviderOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/identity-providers",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get identity provider.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers/{identity_provider_id}>`_.
        
        :rtype: IdentityProvider
        """

        return self._client.call_api(
            method="get",
            path="/v3/identity-providers/{identity_provider_id}",
            content_type="application/json",
            path_params={"identity_provider_id": self._id.to_api(),},
            unpack=self,
        )

    def refresh_tokens(self):
        """Refreshes the OIDC signing keys.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers/{identity_provider_id}/refresh-jwks>`_.
        
        :rtype: IdentityProvider
        """

        return self._client.call_api(
            method="post",
            path="/v3/identity-providers/{identity_provider_id}/refresh-jwks",
            content_type="application/json",
            path_params={"identity_provider_id": self._id.to_api(),},
            unpack=self,
        )

    def update(self, discovery=None, oidc_attributes=None):
        """Update an existing identity provider.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/identity-providers/{identity_provider_id}>`_.
        
        :param discovery: Indicates that the OpenID Connect endpoints and keys should be set
            using the OpenID Connect Discovery mechanism. The following parameters
            are set automatically: * authorization_endpoint * token_endpoint *
            userinfo_endpoint * revocation_endpoint * jwks_uri * keys
        :type discovery: bool
        
        :param oidc_attributes: Represents OIDC specific attributes.
        :type oidc_attributes: mbed_cloud.foundation.entities.OidcRequest
        
        :rtype: IdentityProvider
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._identity_provider_type.value_set:
            body_params["type"] = self._identity_provider_type.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        # Method parameters are unconditionally sent even if set to None
        body_params["oidc_attributes"] = fields.DictField(oidc_attributes).to_api()
        if self._saml2_attributes.value_set:
            body_params["saml2_attributes"] = self._saml2_attributes.to_api()
        if self._status.value_set:
            body_params["status"] = self._status.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/identity-providers/{identity_provider_id}",
            content_type="application/json",
            body_params=body_params,
            query_params={"discovery": fields.BooleanField(discovery).to_api(),},
            path_params={"identity_provider_id": self._id.to_api(),},
            unpack=self,
        )
