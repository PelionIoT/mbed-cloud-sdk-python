"""
.. warning::
    UpdateCampaign should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: UpdateCampaign
=================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`UpdateCampaign.archive`
- :meth:`UpdateCampaign.create`
- :meth:`UpdateCampaign.delete`
- :meth:`UpdateCampaign.device_metadata`
- :meth:`UpdateCampaign.list`
- :meth:`UpdateCampaign.read`
- :meth:`UpdateCampaign.start`
- :meth:`UpdateCampaign.stop`
- :meth:`UpdateCampaign.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    update_campaigns = pelion_dm_sdk.foundation.update_campaign()

How to import UpdateCampaign directly:

.. code-block:: python
    
    from mbed_cloud.foundation import UpdateCampaign

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class UpdateCampaign(Entity):
    """Represents the `UpdateCampaign` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "autostop_reason",
        "created_at",
        "description",
        "device_filter",
        "device_filter_helper",
        "finished",
        "id",
        "name",
        "phase",
        "root_manifest_id",
        "root_manifest_url",
        "started_at",
        "updated_at",
        "when",
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
        autostop_reason=None,
        created_at=None,
        description=None,
        device_filter=None,
        device_filter_helper=None,
        finished=None,
        id=None,
        name=None,
        phase=None,
        root_manifest_id=None,
        root_manifest_url=None,
        started_at=None,
        updated_at=None,
        when=None,
    ):
        """Creates a local `UpdateCampaign` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param autostop_reason: Text description of why a campaign failed to start or why a
            campaign stopped.
        :type autostop_reason: str
        :param created_at: The time the update campaign was created
        :type created_at: datetime
        :param description: An optional description of the campaign
        :type description: str
        :param device_filter: (Required) The filter for the devices the campaign is targeting at
        :type device_filter: str
        :param device_filter_helper: Helper for creating the device filter string.
        :type device_filter_helper: mbed_cloud.client.api_filter.ApiFilter
        :param finished: The campaign finish timestamp
        :type finished: datetime
        :param id: (Required) The campaign ID
        :type id: str
        :param name: The campaign name
        :type name: str
        :param phase: The current phase of the campaign.
        :type phase: str
        :param root_manifest_id: 
        :type root_manifest_id: str
        :param root_manifest_url: 
        :type root_manifest_url: str
        :param started_at: 
        :type started_at: datetime
        :param updated_at: The time the object was updated
        :type updated_at: datetime
        :param when: The scheduled start time for the campaign. The campaign will start
            within 1 minute when then start time has elapsed.
        :type when: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._autostop_reason = fields.StringField(value=autostop_reason)
        self._created_at = fields.DateTimeField(value=created_at)
        self._description = fields.StringField(value=description)
        self._device_filter = fields.StringField(value=device_filter)
        self._device_filter_helper = fields.DictField(value=device_filter_helper)
        self._finished = fields.DateTimeField(value=finished)
        self._id = fields.StringField(value=id)
        self._name = fields.StringField(value=name)
        self._phase = fields.StringField(value=phase)
        self._root_manifest_id = fields.StringField(value=root_manifest_id)
        self._root_manifest_url = fields.StringField(value=root_manifest_url)
        self._started_at = fields.DateTimeField(value=started_at)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._when = fields.DateTimeField(value=when)

    @property
    def autostop_reason(self):
        """Text description of why a campaign failed to start or why a campaign stopped.
        
        api example: 'Insufficient billing credit.'
        
        :rtype: str
        """

        return self._autostop_reason.value

    @property
    def created_at(self):
        """The time the update campaign was created
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def description(self):
        """An optional description of the campaign
        
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
    def device_filter(self):
        """The filter for the devices the campaign is targeting at

        This field must be set when creating a new UpdateCampaign Entity.
        
        api example: 'id__eq=00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._device_filter.value

    @device_filter.setter
    def device_filter(self, value):
        """Set value of `device_filter`

        :param value: value to set
        :type value: str
        """

        self._device_filter.set(value)

    @property
    def device_filter_helper(self):
        """Helper for creating the device filter string.

        This helper can be used instead of setting device filter directly. This allows
        the campaign filter to be created in a way which is similar to the device
        listing filter.

        - See mbed_cloud.foundation.entities.devices.device.Device.list for details.
        
        :rtype: mbed_cloud.client.api_filter.ApiFilter
        """

        from mbed_cloud.foundation._custom_methods import device_filter_helper_getter

        return device_filter_helper_getter(self=self)

    @device_filter_helper.setter
    def device_filter_helper(self, value):
        """Set value of `device_filter_helper`

        :param value: value to set
        :type value: mbed_cloud.client.api_filter.ApiFilter
        """

        from mbed_cloud.foundation._custom_methods import device_filter_helper_setter

        device_filter_helper_setter(self=self, value=value)

    @property
    def finished(self):
        """The campaign finish timestamp
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._finished.value

    @property
    def id(self):
        """The campaign ID

        This field must be set when updating or deleting an existing UpdateCampaign Entity.
        
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
    def name(self):
        """The campaign name
        
        api example: 'campaign'
        
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
    def phase(self):
        """The current phase of the campaign.
        
        :rtype: str
        """

        return self._phase.value

    @property
    def root_manifest_id(self):
        """
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._root_manifest_id.value

    @root_manifest_id.setter
    def root_manifest_id(self, value):
        """Set value of `root_manifest_id`

        :param value: value to set
        :type value: str
        """

        self._root_manifest_id.set(value)

    @property
    def root_manifest_url(self):
        """
        
        api example: 'http://example.com/00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._root_manifest_url.value

    @property
    def started_at(self):
        """
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._started_at.value

    @property
    def updated_at(self):
        """The time the object was updated
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @property
    def when(self):
        """The scheduled start time for the campaign. The campaign will start within 1
        minute when then start time has elapsed.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._when.value

    @when.setter
    def when(self, value):
        """Set value of `when`

        :param value: value to set
        :type value: datetime
        """

        self._when.set(value)

    def archive(self):
        """Archive a campaign.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/archive>`_.
        
        :rtype: UpdateCampaign
        """

        return self._client.call_api(
            method="post",
            path="/v3/update-campaigns/{campaign_id}/archive",
            content_type="application/json",
            path_params={"campaign_id": self._id.to_api()},
            unpack=self,
        )

    def create(self):
        """Create a campaign

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/>`_.
        
        :rtype: UpdateCampaign
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._device_filter.value_set:
            body_params["device_filter"] = self._device_filter.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        if self._root_manifest_id.value_set:
            body_params["root_manifest_id"] = self._root_manifest_id.to_api()
        if self._when.value_set:
            body_params["when"] = self._when.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/update-campaigns/",
            content_type="application/json",
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete a campaign

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/>`_.
        
        :rtype: UpdateCampaign
        """

        return self._client.call_api(
            method="delete",
            path="/v3/update-campaigns/{campaign_id}/",
            content_type="application/json",
            path_params={"campaign_id": self._id.to_api()},
            unpack=self,
        )

    def device_metadata(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """List all campaign device metadata

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/campaign-device-metadata/>`_.
        
        :param filter: Filtering when listing entities is not supported by the API for this
            entity.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: ASC or DESC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param include: A comma-separated list of data fields to return. Currently supported:
            total_count
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(CampaignDeviceMetadata)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import CampaignDeviceMetadata
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=CampaignDeviceMetadata._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = CampaignDeviceMetadata._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=CampaignDeviceMetadata,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_device_metadata,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """List all campaigns

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/>`_.

        **API Filters**

        The following filters are supported by the API when listing UpdateCampaign entities:

        +------------------+------+------+------+------+------+------+------+
        | Field            | eq   | neq  | gte  | lte  | in   | nin  | like |
        +==================+======+======+======+======+======+======+======+
        | created_at       |      |      | Y    | Y    | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | description      | Y    | Y    |      |      | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | device_filter    | Y    | Y    |      |      | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | finished         |      |      | Y    | Y    | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | id               | Y    | Y    |      |      | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | name             | Y    | Y    |      |      | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | root_manifest_id | Y    | Y    |      |      | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | started_at       |      |      | Y    | Y    | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | state            | Y    | Y    |      |      | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | updated_at       |      |      | Y    | Y    | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+
        | when             |      |      | Y    | Y    | Y    | Y    |      |
        +------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import UpdateCampaign
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("created_at", "in", <filter value>)
            for update_campaign in UpdateCampaign().list(filter=api_filter):
                print(update_campaign.created_at)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records. Acceptable values: ASC, DESC. Default: ASC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param include: A comma-separated list of data fields to return. Currently supported:
            total_count
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(UpdateCampaign)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import UpdateCampaign
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=UpdateCampaign._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = UpdateCampaign._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=UpdateCampaign,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_device_metadata(self, after=None, filter=None, order=None, limit=None, include=None):
        """List all campaign device metadata
        
        :param after: The ID of the the item after which to retrieve the next page
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: ASC or DESC
        :type order: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param include: A comma-separated list of data fields to return. Currently supported:
            total_count
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.UpdateCampaignOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/{campaign_id}/campaign-device-metadata/",
            content_type="application/json",
            query_params=query_params,
            path_params={"campaign_id": self._id.to_api()},
            unpack=False,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """List all campaigns
        
        :param after: The ID of the the item after which to retrieve the next page
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records. Acceptable values: ASC, DESC. Default: ASC
        :type order: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param include: A comma-separated list of data fields to return. Currently supported:
            total_count
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.UpdateCampaignOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get a campaign.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/>`_.
        
        :rtype: UpdateCampaign
        """

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/{campaign_id}/",
            content_type="application/json",
            path_params={"campaign_id": self._id.to_api()},
            unpack=self,
        )

    def start(self):
        """Start a campaign.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/start>`_.
        
        :rtype: UpdateCampaign
        """

        return self._client.call_api(
            method="post",
            path="/v3/update-campaigns/{campaign_id}/start",
            content_type="application/json",
            path_params={"campaign_id": self._id.to_api()},
            unpack=self,
        )

    def stop(self):
        """Stop a campaign.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/stop>`_.
        
        :rtype: UpdateCampaign
        """

        return self._client.call_api(
            method="post",
            path="/v3/update-campaigns/{campaign_id}/stop",
            content_type="application/json",
            path_params={"campaign_id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Modify a campaign

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/>`_.
        
        :rtype: UpdateCampaign
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._device_filter.value_set:
            body_params["device_filter"] = self._device_filter.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        if self._root_manifest_id.value_set:
            body_params["root_manifest_id"] = self._root_manifest_id.to_api()
        if self._when.value_set:
            body_params["when"] = self._when.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/update-campaigns/{campaign_id}/",
            content_type="application/json",
            body_params=body_params,
            path_params={"campaign_id": self._id.to_api()},
            unpack=self,
        )
