"""
.. warning::
    DeviceEvents should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DeviceEvents
===============================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DeviceEvents.list`
- :meth:`DeviceEvents.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    device_eventss = pelion_dm_sdk.foundation.device_events()

How to import DeviceEvents directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DeviceEvents

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class DeviceEvents(Entity):
    """Represents the `DeviceEvents` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "changes",
        "created_at",
        "data",
        "date_time",
        "description",
        "device_id",
        "event_type",
        "event_type_category",
        "event_type_description",
        "id",
        "state_change",
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
        changes=None,
        created_at=None,
        data=None,
        date_time=None,
        description=None,
        device_id=None,
        event_type=None,
        event_type_category=None,
        event_type_description=None,
        id=None,
        state_change=None,
    ):
        """Creates a local `DeviceEvents` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param changes: 
        :type changes: dict
        :param created_at: 
        :type created_at: datetime
        :param data: Additional data relevant to the event.
        :type data: dict
        :param date_time: 
        :type date_time: datetime
        :param description: 
        :type description: str
        :param device_id: 
        :type device_id: str
        :param event_type: Event code
        :type event_type: str
        :param event_type_category: Category code which groups the event type by a summary category.
        :type event_type_category: str
        :param event_type_description: Generic description of the event
        :type event_type_description: str
        :param id: (Required) 
        :type id: str
        :param state_change: 
        :type state_change: bool
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._changes = fields.DictField(value=changes)
        self._created_at = fields.DateTimeField(value=created_at)
        self._data = fields.DictField(value=data)
        self._date_time = fields.DateTimeField(value=date_time)
        self._description = fields.StringField(value=description)
        self._device_id = fields.StringField(value=device_id)
        self._event_type = fields.StringField(value=event_type)
        self._event_type_category = fields.StringField(value=event_type_category)
        self._event_type_description = fields.StringField(value=event_type_description)
        self._id = fields.StringField(value=id)
        self._state_change = fields.BooleanField(value=state_change)

    @property
    def changes(self):
        """
        
        :rtype: dict
        """

        return self._changes.value

    @property
    def created_at(self):
        """
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def data(self):
        """Additional data relevant to the event.
        
        api example: {'campaign_id': '00000000000000000000000000000000'}
        
        :rtype: dict
        """

        return self._data.value

    @property
    def date_time(self):
        """
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._date_time.value

    @property
    def description(self):
        """
        
        api example: 'Device record created'
        
        :rtype: str
        """

        return self._description.value

    @property
    def device_id(self):
        """
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._device_id.value

    @property
    def event_type(self):
        """Event code
        
        api example: 'UPD2_100'
        
        :rtype: str
        """

        return self._event_type.value

    @property
    def event_type_category(self):
        """Category code which groups the event type by a summary category.
        
        api example: 'FAIL_MANIFEST_REJECTED'
        
        :rtype: str
        """

        return self._event_type_category.value

    @property
    def event_type_description(self):
        """Generic description of the event
        
        api example: 'FAIL'
        
        :rtype: str
        """

        return self._event_type_description.value

    @property
    def id(self):
        """

        This field must be set when updating or deleting an existing DeviceEvents Entity.
        
        api example: '00000000000000000000000000000000'
        
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
    def state_change(self):
        """
        
        :rtype: bool
        """

        return self._state_change.value

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """List all device events.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-events/>`_.

        **API Filters**

        The following filters are supported by the API when listing DeviceEvents entities:

        +--------------+------+------+------+------+------+------+------+
        | Field        | eq   | neq  | gte  | lte  | in   | nin  | like |
        +==============+======+======+======+======+======+======+======+
        | date_time    |      |      | Y    | Y    | Y    | Y    |      |
        +--------------+------+------+------+------+------+------+------+
        | description  | Y    | Y    |      |      | Y    | Y    |      |
        +--------------+------+------+------+------+------+------+------+
        | device_id    | Y    | Y    |      |      | Y    | Y    |      |
        +--------------+------+------+------+------+------+------+------+
        | event_type   | Y    | Y    |      |      | Y    | Y    |      |
        +--------------+------+------+------+------+------+------+------+
        | id           | Y    | Y    |      |      | Y    | Y    |      |
        +--------------+------+------+------+------+------+------+------+
        | state_change | Y    | Y    |      |      |      |      |      |
        +--------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import DeviceEvents
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("date_time", "in", <filter value>)
            for device_event in DeviceEvents().list(filter=api_filter):
                print(device_event.date_time)
        
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
            `total_count`
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(DeviceEvents)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import DeviceEvents
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=DeviceEvents._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = DeviceEvents._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=DeviceEvents,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """List all device events.
        
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
            `total_count`
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
            path="/v3/device-events/",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Retrieve a device event.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-events/{device_event_id}/>`_.
        
        :rtype: DeviceEvents
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-events/{device_event_id}/",
            content_type="application/json",
            path_params={"device_event_id": self._id.to_api()},
            unpack=self,
        )
