"""
.. warning::
    ApiKey should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: ApiKey
=========================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`ApiKey.create`
- :meth:`ApiKey.delete`
- :meth:`ApiKey.list`
- :meth:`ApiKey.me`
- :meth:`ApiKey.read`
- :meth:`ApiKey.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    api_keys = pelion_dm_sdk.foundation.api_key()

How to import ApiKey directly:

.. code-block:: python
    
    from mbed_cloud.foundation import ApiKey

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class ApiKey(Entity):
    """Represents the `ApiKey` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "created_at",
        "creation_time",
        "id",
        "key",
        "last_login_time",
        "name",
        "owner",
        "status",
        "updated_at",
    ]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        created_at=None,
        creation_time=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `ApiKey` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: The ID of the account.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: The timestamp of the API key creation in the storage, in
            milliseconds.
        :type creation_time: int
        :param id: (Required) The ID of the API key.
        :type id: str
        :param key: The API key.
        :type key: str
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: int
        :param name: (Required) The display name for the API key.
        :type name: str
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: str
        :param status: The status of the API key.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._creation_time = fields.IntegerField(value=creation_time)
        self._id = fields.StringField(value=id)
        self._key = fields.StringField(value=key)
        self._last_login_time = fields.IntegerField(value=last_login_time)
        self._name = fields.StringField(value=name)
        self._owner = fields.StringField(value=owner)
        self._status = fields.StringField(value=status, enum=enums.ApiKeyStatusEnum)
        self._updated_at = fields.DateTimeField(value=updated_at)

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
    def creation_time(self):
        """The timestamp of the API key creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """

        return self._creation_time.value

    @creation_time.setter
    def creation_time(self, value):
        """Set value of `creation_time`

        :param value: value to set
        :type value: int
        """

        self._creation_time.set(value)

    @property
    def id(self):
        """The ID of the API key.

        This field must be set when updating or deleting an existing ApiKey Entity.
        
        api example: '01619571f7020242ac12000600000000'
        
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
    def key(self):
        """The API key.
        
        api example: 'ak_1MDE2MTk1NzFmNmU4MDI0MmFjMTIwMDA2MDAwMDAwMDA01619571f7020242ac120006000000
            00'
        
        :rtype: str
        """

        return self._key.value

    @key.setter
    def key(self, value):
        """Set value of `key`

        :param value: value to set
        :type value: str
        """

        self._key.set(value)

    @property
    def last_login_time(self):
        """The timestamp of the latest API key usage, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """

        return self._last_login_time.value

    @last_login_time.setter
    def last_login_time(self, value):
        """Set value of `last_login_time`

        :param value: value to set
        :type value: int
        """

        self._last_login_time.set(value)

    @property
    def name(self):
        """The display name for the API key.

        This field must be set when creating a new ApiKey Entity.
        
        api example: 'API key gorgon'
        
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
    def owner(self):
        """The owner of this API key, who is the creator by default.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """

        return self._owner.value

    @owner.setter
    def owner(self, value):
        """Set value of `owner`

        :param value: value to set
        :type value: str
        """

        self._owner.set(value)

    @property
    def status(self):
        """The status of the API key.
        
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

    def create(self):
        """Create a new API key.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/api-keys
        
        :rtype: ApiKey
        """

        return self._client.call_api(
            method="post",
            path="/v3/api-keys",
            body_params={
                "name": self._name.to_api(),
                "owner": self._owner.to_api(),
                "status": self._status.to_api(),
            },
            unpack=self,
        )

    def delete(self):
        """Delete API key.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/api-keys/{apikey_id}
        
        :rtype: ApiKey
        """

        return self._client.call_api(
            method="delete",
            path="/v3/api-keys/{apikey_id}",
            path_params={"apikey_id": self._id.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get all API keys

        **API Filters**

        The following filters are supported by the API when listing ApiKey entities:

        +-------+------+------+------+------+------+------+------+
        | Field | eq   | neq  | gte  | lte  | in   | nin  | like |
        +=======+======+======+======+======+======+======+======+
        | key   | Y    |      |      |      |      |      |      |
        +-------+------+------+------+------+------+------+------+
        | owner | Y    |      |      |      |      |      |      |
        +-------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import ApiKey
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("key", "eq", <filter value>)
            for api_key in ApiKey().list(filter=api_filter):
                print(api_key.key)
        
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
        :rtype: mbed_cloud.pagination.PaginatedResponse(ApiKey)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import ApiKey
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(
                filter_definition=filter, field_renames=ApiKey._renames_to_api
            )
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = ApiKey._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=ApiKey,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def me(self):
        """Get API key details.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/api-keys/me
        
        :rtype: ApiKey
        """

        return self._client.call_api(method="get", path="/v3/api-keys/me", unpack=self)

    def _paginate_list(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get all API keys
        
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
            order, enum=enums.ApiKeyOrderEnum
        ).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get", path="/v3/api-keys", query_params=query_params, unpack=False
        )

    def read(self):
        """Get API key details.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/api-keys/{apikey_id}
        
        :rtype: ApiKey
        """

        return self._client.call_api(
            method="get",
            path="/v3/api-keys/{apikey_id}",
            path_params={"apikey_id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Update API key details.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/api-keys/{apikey_id}
        
        :rtype: ApiKey
        """

        return self._client.call_api(
            method="put",
            path="/v3/api-keys/{apikey_id}",
            path_params={"apikey_id": self._id.to_api()},
            body_params={
                "name": self._name.to_api(),
                "owner": self._owner.to_api(),
                "status": self._status.to_api(),
            },
            unpack=self,
        )
