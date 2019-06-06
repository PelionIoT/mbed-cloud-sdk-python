"""
.. warning::
    DeviceGroup should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DeviceGroup
==============================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DeviceGroup.add_device`
- :meth:`DeviceGroup.create`
- :meth:`DeviceGroup.delete`
- :meth:`DeviceGroup.devices`
- :meth:`DeviceGroup.list`
- :meth:`DeviceGroup.read`
- :meth:`DeviceGroup.remove_device`
- :meth:`DeviceGroup.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    device_groups = pelion_dm_sdk.foundation.device_group()

How to import DeviceGroup directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DeviceGroup

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class DeviceGroup(Entity):
    """Represents the `DeviceGroup` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["created_at", "custom_attributes", "description", "devices_count", "id", "name", "updated_at"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        created_at=None,
        custom_attributes=None,
        description=None,
        devices_count=None,
        id=None,
        name=None,
        updated_at=None,
    ):
        """Creates a local `DeviceGroup` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param created_at: The time the campaign was created.
        :type created_at: datetime
        :param custom_attributes: Up to ten custom key-value attributes. Note that keys cannot begin
            with a number. Both keys and values are limited to 128 characters.
            Updating this field replaces existing contents.
        :type custom_attributes: dict
        :param description: The description of the group.
        :type description: str
        :param devices_count: The number of devices in this group.
        :type devices_count: int
        :param id: (Required) The group ID.
        :type id: str
        :param name: Name of the group.
        :type name: str
        :param updated_at: The time the object was updated.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._created_at = fields.DateTimeField(value=created_at)
        self._custom_attributes = fields.DictField(value=custom_attributes)
        self._description = fields.StringField(value=description)
        self._devices_count = fields.IntegerField(value=devices_count)
        self._id = fields.StringField(value=id)
        self._name = fields.StringField(value=name)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def created_at(self):
        """The time the campaign was created.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def custom_attributes(self):
        """Up to ten custom key-value attributes. Note that keys cannot begin with a
        number. Both keys and values are limited to 128 characters. Updating this
        field replaces existing contents.
        
        api example: {'key': 'value'}
        
        :rtype: dict
        """

        return self._custom_attributes.value

    @custom_attributes.setter
    def custom_attributes(self, value):
        """Set value of `custom_attributes`

        :param value: value to set
        :type value: dict
        """

        self._custom_attributes.set(value)

    @property
    def description(self):
        """The description of the group.
        
        api example: 'Devices on the factory floor.'
        
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
    def devices_count(self):
        """The number of devices in this group.
        
        api example: 10
        
        :rtype: int
        """

        return self._devices_count.value

    @property
    def id(self):
        """The group ID.

        This field must be set when updating or deleting an existing DeviceGroup Entity.
        
        api example: '015c3029f6f7000000000001001000c3'
        
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
        """Name of the group.
        
        api example: 'My devices'
        
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
        """The time the object was updated.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def add_device(self, device_id=None):
        """Add a device to a group

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/{device-group-id}/devices/add/>`_.
        
        :param device_id: No description available
        :type device_id: str
        
        :rtype: 
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        # Method parameters are unconditionally sent even if set to None
        body_params["device_id"] = fields.StringField(device_id).to_api()

        return self._client.call_api(
            method="post",
            path="/v3/device-groups/{device-group-id}/devices/add/",
            content_type="application/json",
            body_params=body_params,
            path_params={"device-group-id": self._id.to_api()},
            unpack=self,
        )

    def create(self):
        """Create a group

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/>`_.
        
        :rtype: DeviceGroup
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._custom_attributes.value_set:
            body_params["custom_attributes"] = self._custom_attributes.to_api()
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/device-groups/",
            content_type="application/json",
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete a group

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/{device-group-id}/>`_.
        
        :rtype: DeviceGroup
        """

        return self._client.call_api(
            method="delete",
            path="/v3/device-groups/{device-group-id}/",
            content_type="application/json",
            path_params={"device-group-id": self._id.to_api()},
            unpack=self,
        )

    def devices(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get a page of devices

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/{device-group-id}/devices/>`_.

        **API Filters**

        The following filters are supported by the API when listing DeviceGroup entities:

        +---------------------------+------+------+------+------+------+------+------+
        | Field                     | eq   | neq  | gte  | lte  | in   | nin  | like |
        +===========================+======+======+======+======+======+======+======+
        | account_id                | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | auto_update               | Y    | Y    |      |      |      |      |      |
        +---------------------------+------+------+------+------+------+------+------+
        | bootstrap_expiration_date |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | bootstrapped_timestamp    |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | ca_id                     | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | connector_expiration_date |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | created_at                |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | deployed_state            | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | deployment                | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | description               | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | device_class              | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | device_execution_mode     | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | device_key                | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | endpoint_name             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | endpoint_type             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | enrolment_list_timestamp  |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | firmware_checksum         | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | host_gateway              | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | id                        | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | manifest                  | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | manifest_timestamp        |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | mechanism                 | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | mechanism_url             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | name                      | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | serial_number             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | state                     | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | updated_at                |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | vendor_id                 | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import DeviceGroup
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("account_id", "eq", <filter value>)
            for device in DeviceGroup().devices(filter=api_filter):
                print(device.account_id)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(Device)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import Device
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=Device._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = Device._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=Device,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_devices,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """List all groups.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/>`_.

        **API Filters**

        The following filters are supported by the API when listing DeviceGroup entities:

        +---------------+------+------+------+------+------+------+------+
        | Field         | eq   | neq  | gte  | lte  | in   | nin  | like |
        +===============+======+======+======+======+======+======+======+
        | created_at    |      |      | Y    | Y    | Y    | Y    |      |
        +---------------+------+------+------+------+------+------+------+
        | devices_count | Y    | Y    | Y    | Y    | Y    | Y    |      |
        +---------------+------+------+------+------+------+------+------+
        | id            | Y    | Y    |      |      | Y    | Y    |      |
        +---------------+------+------+------+------+------+------+------+
        | name          | Y    | Y    |      |      | Y    | Y    |      |
        +---------------+------+------+------+------+------+------+------+
        | updated_at    |      |      | Y    | Y    | Y    | Y    |      |
        +---------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import DeviceGroup
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("created_at", "in", <filter value>)
            for device_group in DeviceGroup().list(filter=api_filter):
                print(device_group.created_at)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(DeviceGroup)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import DeviceGroup
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=DeviceGroup._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = DeviceGroup._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=DeviceGroup,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_devices(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get a page of devices
        
        :param after: The ID of The item after which to retrieve the next page.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/device-groups/{device-group-id}/devices/",
            content_type="application/json",
            query_params=query_params,
            path_params={"device-group-id": self._id.to_api()},
            unpack=False,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """List all groups.
        
        :param after: The ID of The item after which to retrieve the next page.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/device-groups/",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get a group.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/{device-group-id}/>`_.
        
        :rtype: DeviceGroup
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-groups/{device-group-id}/",
            content_type="application/json",
            path_params={"device-group-id": self._id.to_api()},
            unpack=self,
        )

    def remove_device(self, device_id=None):
        """Remove a device from a group

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/{device-group-id}/devices/remove/>`_.
        
        :param device_id: No description available
        :type device_id: str
        
        :rtype: 
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        # Method parameters are unconditionally sent even if set to None
        body_params["device_id"] = fields.StringField(device_id).to_api()

        return self._client.call_api(
            method="post",
            path="/v3/device-groups/{device-group-id}/devices/remove/",
            content_type="application/json",
            body_params=body_params,
            path_params={"device-group-id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Modify the attributes of a group.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-groups/{device-group-id}/>`_.
        
        :rtype: DeviceGroup
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._custom_attributes.value_set:
            body_params["custom_attributes"] = self._custom_attributes.to_api()
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/device-groups/{device-group-id}/",
            content_type="application/json",
            body_params=body_params,
            path_params={"device-group-id": self._id.to_api()},
            unpack=self,
        )
