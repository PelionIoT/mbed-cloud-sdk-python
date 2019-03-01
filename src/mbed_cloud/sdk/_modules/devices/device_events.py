"""
Entity module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class DeviceEvents(Entity):
    """Represents the `DeviceEvents` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
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

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

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

    @changes.setter
    def changes(self, value):
        """Set value of `changes`

        :param value: value to set
        :type value: dict
        """

        self._changes.set(value)

    @property
    def created_at(self):
        """
        
        api example: '2017-05-22T12:37:55.576563Z'
        
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
    def data(self):
        """Additional data relevant to the event.
        
        api example: {'campaign_id': '00000000000000000000000000000000'}
        
        :rtype: dict
        """

        return self._data.value

    @data.setter
    def data(self, value):
        """Set value of `data`

        :param value: value to set
        :type value: dict
        """

        self._data.set(value)

    @property
    def date_time(self):
        """
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._date_time.value

    @date_time.setter
    def date_time(self, value):
        """Set value of `date_time`

        :param value: value to set
        :type value: datetime
        """

        self._date_time.set(value)

    @property
    def description(self):
        """
        
        api example: 'Device record created'
        
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
    def device_id(self):
        """
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._device_id.value

    @device_id.setter
    def device_id(self, value):
        """Set value of `device_id`

        :param value: value to set
        :type value: str
        """

        self._device_id.set(value)

    @property
    def event_type(self):
        """Event code
        
        api example: 'UPD2_100'
        
        :rtype: str
        """

        return self._event_type.value

    @event_type.setter
    def event_type(self, value):
        """Set value of `event_type`

        :param value: value to set
        :type value: str
        """

        self._event_type.set(value)

    @property
    def event_type_category(self):
        """Category code which groups the event type by a summary category.
        
        api example: 'FAIL_MANIFEST_REJECTED'
        
        :rtype: str
        """

        return self._event_type_category.value

    @event_type_category.setter
    def event_type_category(self, value):
        """Set value of `event_type_category`

        :param value: value to set
        :type value: str
        """

        self._event_type_category.set(value)

    @property
    def event_type_description(self):
        """Generic description of the event
        
        api example: 'FAIL'
        
        :rtype: str
        """

        return self._event_type_description.value

    @event_type_description.setter
    def event_type_description(self, value):
        """Set value of `event_type_description`

        :param value: value to set
        :type value: str
        """

        self._event_type_description.set(value)

    @property
    def id(self):
        """
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        This field must be set when updating or deleting an existing DeviceEvents Entity.

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

    @state_change.setter
    def state_change(self, value):
        """Set value of `state_change`

        :param value: value to set
        :type value: bool
        """

        self._state_change.set(value)

    def list(self, include=None, max_results=None, page_size=None, order=None):
        """List all device events.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/device-events/
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`
        :type include: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
            
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(DeviceEvents)
        """

        from mbed_cloud.sdk.common._custom_methods import paginate
        from mbed_cloud.sdk.entities import DeviceEvents

        return paginate(
            self=self,
            foreign_key=DeviceEvents,
            include=include,
            max_results=max_results,
            page_size=page_size,
            order=order,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, include=None, limit=None, order=None):
        """List all device events.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/device-events/
        
        :param after: The ID of The item after which to retrieve the next page.
        :type after: str
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`
        :type include: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-events/",
            query_params={
                "after": fields.StringField(after).to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": fields.IntegerField(limit).to_api(),
                "order": fields.StringField(order).to_api(),
            },
            unpack=False,
        )

    def read(self):
        """Retrieve a device event.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/device-events/{device_event_id}/
        
        :rtype: DeviceEvents
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-events/{device_event_id}/",
            path_params={"device_event_id": self._id.to_api()},
            unpack=self,
        )
