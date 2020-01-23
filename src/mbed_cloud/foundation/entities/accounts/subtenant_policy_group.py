"""
.. warning::
    SubtenantPolicyGroup should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SubtenantPolicyGroup
=======================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`SubtenantPolicyGroup.api_keys`
- :meth:`SubtenantPolicyGroup.create`
- :meth:`SubtenantPolicyGroup.delete`
- :meth:`SubtenantPolicyGroup.list`
- :meth:`SubtenantPolicyGroup.read`
- :meth:`SubtenantPolicyGroup.update`
- :meth:`SubtenantPolicyGroup.users`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    subtenant_policy_groups = pelion_dm_sdk.foundation.subtenant_policy_group()

How to import SubtenantPolicyGroup directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SubtenantPolicyGroup

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SubtenantPolicyGroup(Entity):
    """Represents the `SubtenantPolicyGroup` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["account_id", "apikey_count", "created_at", "id", "name", "updated_at", "user_count"]

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
        apikey_count=None,
        created_at=None,
        id=None,
        name=None,
        updated_at=None,
        user_count=None,
    ):
        """Creates a local `SubtenantPolicyGroup` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: (Required) The ID of the account this group belongs to.
        :type account_id: str
        :param apikey_count: The number of API keys in this group.
        :type apikey_count: int
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: (Required) The ID of the group.
        :type id: str
        :param name: (Required) The name of the group.
        :type name: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_count: The number of users in this group.
        :type user_count: int
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._apikey_count = fields.IntegerField(value=apikey_count)
        self._created_at = fields.DateTimeField(value=created_at)
        self._id = fields.StringField(value=id)
        self._name = fields.StringField(value=name)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._user_count = fields.IntegerField(value=user_count)

    @property
    def account_id(self):
        """The ID of the account this group belongs to.

        This field must be set when creating a new SubtenantPolicyGroup Entity.
        
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
    def apikey_count(self):
        """The number of API keys in this group.
        
        :rtype: int
        """

        return self._apikey_count.value

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def id(self):
        """The ID of the group.

        This field must be set when updating or deleting an existing SubtenantPolicyGroup Entity.
        
        api example: '01619571dec00242ac12000600000000'
        
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
    def name(self):
        """The name of the group.

        This field must be set when creating a new SubtenantPolicyGroup Entity.
        
        api example: 'Administrators'
        
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
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @property
    def user_count(self):
        """The number of users in this group.
        
        api example: 1
        
        :rtype: int
        """

        return self._user_count.value

    def api_keys(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get API keys in a group.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/policy-groups/{group_id}/api-keys>`_.
        
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
        :rtype: mbed_cloud.pagination.PaginatedResponse(SubtenantApiKey)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import SubtenantApiKey
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=SubtenantApiKey._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = SubtenantApiKey._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=SubtenantApiKey,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_api_keys,
        )

    def create(self, members=None):
        """Create a new group.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/policy-groups>`_.
        
        :param members: Represents arrays of user and API key IDs.
        :type members: dict
        
        :rtype: SubtenantPolicyGroup
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        # Method parameters are unconditionally sent even if set to None
        body_params["members"] = fields.DictField(members).to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account_id}/policy-groups",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(),},
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete a group.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/policy-groups/{group_id}>`_.
        
        :rtype: SubtenantPolicyGroup
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account_id}/policy-groups/{group_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "group_id": self._id.to_api(),},
            unpack=self,
        )

    def list(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get policy groups.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/policy-groups>`_.

        **API Filters**

        The following filters are supported by the API when listing SubtenantPolicyGroup entities:

        +-------+------+------+------+------+------+------+------+
        | Field | eq   | neq  | gte  | lte  | in   | nin  | like |
        +=======+======+======+======+======+======+======+======+
        | name  | Y    |      |      |      |      |      |      |
        +-------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import SubtenantPolicyGroup
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("name", "eq", <filter value>)
            for subtenant_policy_group in SubtenantPolicyGroup().list(filter=api_filter):
                print(subtenant_policy_group.name)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
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
        :rtype: mbed_cloud.pagination.PaginatedResponse(SubtenantPolicyGroup)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import SubtenantPolicyGroup
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=SubtenantPolicyGroup._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = SubtenantPolicyGroup._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=SubtenantPolicyGroup,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_api_keys(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get API keys in a group.
        
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
        query_params["order"] = fields.StringField(order, enum=enums.SubtenantPolicyGroupOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/policy-groups/{group_id}/api-keys",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "group_id": self._id.to_api(),},
            query_params=query_params,
            unpack=False,
        )

    def _paginate_list(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get policy groups.
        
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
        query_params["order"] = fields.StringField(order, enum=enums.SubtenantPolicyGroupOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/policy-groups",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(),},
            query_params=query_params,
            unpack=False,
        )

    def _paginate_users(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get users in a policy group.
        
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
        query_params["order"] = fields.StringField(order, enum=enums.SubtenantPolicyGroupOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/policy-groups/{group_id}/users",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "group_id": self._id.to_api(),},
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get policy group.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/policy-groups/{group_id}>`_.
        
        :rtype: SubtenantPolicyGroup
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/policy-groups/{group_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "group_id": self._id.to_api(),},
            unpack=self,
        )

    def update(self):
        """Update the group name.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/policy-groups/{group_id}>`_.
        
        :rtype: SubtenantPolicyGroup
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._name.value_set:
            body_params["name"] = self._name.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/accounts/{account_id}/policy-groups/{group_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "group_id": self._id.to_api(),},
            body_params=body_params,
            unpack=self,
        )

    def users(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get users in a policy group.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/policy-groups/{group_id}/users>`_.

        **API Filters**

        The following filters are supported by the API when listing SubtenantPolicyGroup entities:

        +--------+------+------+------+------+------+------+------+
        | Field  | eq   | neq  | gte  | lte  | in   | nin  | like |
        +========+======+======+======+======+======+======+======+
        | status | Y    |      |      |      | Y    | Y    |      |
        +--------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import SubtenantPolicyGroup
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("status", "eq", <filter value>)
            for user in SubtenantPolicyGroup().users(filter=api_filter):
                print(user.status)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
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
        :rtype: mbed_cloud.pagination.PaginatedResponse(SubtenantUser)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import SubtenantUser
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=SubtenantUser._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = SubtenantUser._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=SubtenantUser,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_users,
        )
