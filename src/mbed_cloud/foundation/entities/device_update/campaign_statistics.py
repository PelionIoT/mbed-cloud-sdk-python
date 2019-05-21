"""
.. warning::
    CampaignStatistics should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: CampaignStatistics
=====================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`CampaignStatistics.events`
- :meth:`CampaignStatistics.list`
- :meth:`CampaignStatistics.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    campaign_statisticss = pelion_dm_sdk.foundation.campaign_statistics()

How to import CampaignStatistics directly:

.. code-block:: python
    
    from mbed_cloud.foundation import CampaignStatistics

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class CampaignStatistics(Entity):
    """Represents the `CampaignStatistics` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["campaign_id", "count", "created_at", "id", "summary_status"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, campaign_id=None, count=None, created_at=None, id=None, summary_status=None):
        """Creates a local `CampaignStatistics` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param campaign_id: (Required) ID of the associated campaign.
        :type campaign_id: str
        :param count: 
        :type count: int
        :param created_at: 
        :type created_at: datetime
        :param id: (Required) ID of the event type description
        :type id: str
        :param summary_status: The event type description.
        :type summary_status: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._campaign_id = fields.StringField(value=campaign_id)
        self._count = fields.IntegerField(value=count)
        self._created_at = fields.DateTimeField(value=created_at)
        self._id = fields.StringField(value=id, enum=enums.CampaignStatisticsIdEnum)
        self._summary_status = fields.StringField(value=summary_status, enum=enums.CampaignStatisticsSummaryStatusEnum)

    @property
    def campaign_id(self):
        """ID of the associated campaign.

        This field must be set when creating a new CampaignStatistics Entity.
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._campaign_id.value

    @campaign_id.setter
    def campaign_id(self, value):
        """Set value of `campaign_id`

        :param value: value to set
        :type value: str
        """

        self._campaign_id.set(value)

    @property
    def count(self):
        """
        
        api example: 10
        
        :rtype: int
        """

        return self._count.value

    @property
    def created_at(self):
        """
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def id(self):
        """ID of the event type description

        This field must be set when updating or deleting an existing CampaignStatistics Entity.
        
        api example: 'fail'
        
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
    def summary_status(self):
        """The event type description.
        
        api example: 'FAIL'
        
        :rtype: str
        """

        return self._summary_status.value

    def events(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get a list of events grouped by summary

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/statistics/{summary_status_id}/event_types/>`_.
        
        :param filter: Filtering when listing entities is not supported by the API for this
            entity.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, ASC or DESC. Default
            value is ASC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return for each page.
        :type page_size: int
        
        :param include: Comma separated additional data to return.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(CampaignStatisticsEvents)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import CampaignStatisticsEvents
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=CampaignStatisticsEvents._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = CampaignStatisticsEvents._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=CampaignStatisticsEvents,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_events,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get a list of statistics for a campaign

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/statistics/>`_.
        
        :param filter: Filtering when listing entities is not supported by the API for this
            entity.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, ASC or DESC. Default
            value is ASC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return for each page.
        :type page_size: int
        
        :param include: Comma separated additional data to return.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(CampaignStatistics)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import CampaignStatistics
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=CampaignStatistics._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = CampaignStatistics._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=CampaignStatistics,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_events(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get a list of events grouped by summary
        
        :param after: Not supported by the API.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Not supported by the API.
        :type order: str
        
        :param limit: Not supported by the API.
        :type limit: int
        
        :param include: Not supported by the API.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/{campaign_id}/statistics/{summary_status_id}/event_types/",
            content_type="application/json",
            path_params={"campaign_id": self._campaign_id.to_api(), "summary_status_id": self._id.to_api()},
            unpack=False,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get a list of statistics for a campaign
        
        :param after: Not supported by the API.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Not supported by the API.
        :type order: str
        
        :param limit: Not supported by the API.
        :type limit: int
        
        :param include: Not supported by the API.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/{campaign_id}/statistics/",
            content_type="application/json",
            path_params={"campaign_id": self._campaign_id.to_api()},
            unpack=False,
        )

    def read(self):
        """Get a summary status

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/statistics/{summary_status_id}>`_.
        
        :rtype: CampaignStatistics
        """

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/{campaign_id}/statistics/{summary_status_id}",
            content_type="application/json",
            path_params={"campaign_id": self._campaign_id.to_api(), "summary_status_id": self._id.to_api()},
            unpack=self,
        )
