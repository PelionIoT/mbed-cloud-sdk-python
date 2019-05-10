"""
.. warning::
    CampaignStatisticsEvents should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: CampaignStatisticsEvents
===========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`CampaignStatisticsEvents.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    campaign_statistics_eventss = pelion_dm_sdk.foundation.campaign_statistics_events()

How to import CampaignStatisticsEvents directly:

.. code-block:: python
    
    from mbed_cloud.foundation import CampaignStatisticsEvents

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class CampaignStatisticsEvents(Entity):
    """Represents the `CampaignStatisticsEvents` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "campaign_id",
        "count",
        "created_at",
        "description",
        "event_type",
        "id",
        "summary_status",
        "summary_status_id",
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
        campaign_id=None,
        count=None,
        created_at=None,
        description=None,
        event_type=None,
        id=None,
        summary_status=None,
        summary_status_id=None,
    ):
        """Creates a local `CampaignStatisticsEvents` instance

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
        :param description: 
        :type description: str
        :param event_type: 
        :type event_type: str
        :param id: (Required) 
        :type id: str
        :param summary_status: 
        :type summary_status: str
        :param summary_status_id: (Required) 
        :type summary_status_id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._campaign_id = fields.StringField(value=campaign_id)
        self._count = fields.IntegerField(value=count)
        self._created_at = fields.DateTimeField(value=created_at)
        self._description = fields.StringField(value=description)
        self._event_type = fields.StringField(value=event_type)
        self._id = fields.StringField(value=id)
        self._summary_status = fields.StringField(value=summary_status)
        self._summary_status_id = fields.StringField(value=summary_status_id)

    @property
    def campaign_id(self):
        """ID of the associated campaign.

        This field must be set when creating a new CampaignStatisticsEvents Entity.
        
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
    def description(self):
        """
        
        api example: 'Update error, nonspecific network error'
        
        :rtype: str
        """

        return self._description.value

    @property
    def event_type(self):
        """
        
        api example: 'UPD4_FAIL_101'
        
        :rtype: str
        """

        return self._event_type.value

    @property
    def id(self):
        """

        This field must be set when updating or deleting an existing CampaignStatisticsEvents Entity.
        
        api example: 'upd_fail_101'
        
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
        """
        
        api example: 'FAIL'
        
        :rtype: str
        """

        return self._summary_status.value

    @property
    def summary_status_id(self):
        """

        This field must be set when creating a new CampaignStatisticsEvents Entity.
        
        api example: 'fail'
        
        :rtype: str
        """

        return self._summary_status_id.value

    @summary_status_id.setter
    def summary_status_id(self, value):
        """Set value of `summary_status_id`

        :param value: value to set
        :type value: str
        """

        self._summary_status_id.set(value)

    def read(self):
        """Get an event type for a campaign

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/statistics/{summary_status_id}/event_types/{event_type_id}>`_.
        
        :rtype: CampaignStatisticsEvents
        """

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/{campaign_id}/statistics/{summary_status_id}/event_types/{event_type_id}",
            content_type="application/json",
            path_params={
                "campaign_id": self._campaign_id.to_api(),
                "event_type_id": self._id.to_api(),
                "summary_status_id": self._summary_status_id.to_api(),
            },
            unpack=self,
        )
