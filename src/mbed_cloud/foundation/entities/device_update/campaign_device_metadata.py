"""
.. warning::
    CampaignDeviceMetadata should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: CampaignDeviceMetadata
=========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`CampaignDeviceMetadata.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    campaign_device_metadatas = pelion_dm_sdk.foundation.campaign_device_metadata()

How to import CampaignDeviceMetadata directly:

.. code-block:: python
    
    from mbed_cloud.foundation import CampaignDeviceMetadata

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class CampaignDeviceMetadata(Entity):
    """Represents the `CampaignDeviceMetadata` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "campaign_id",
        "created_at",
        "deployment_state",
        "description",
        "device_id",
        "id",
        "mechanism",
        "mechanism_url",
        "name",
        "updated_at",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {"campaign": "campaign_id"}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {"campaign_id": "campaign"}

    def __init__(
        self,
        _client=None,
        campaign_id=None,
        created_at=None,
        deployment_state=None,
        description=None,
        device_id=None,
        id=None,
        mechanism=None,
        mechanism_url=None,
        name=None,
        updated_at=None,
    ):
        """Creates a local `CampaignDeviceMetadata` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param campaign_id: (Required) The device's campaign ID
        :type campaign_id: str
        :param created_at: The time the campaign was created
        :type created_at: datetime
        :param deployment_state: The state of the update campaign on the device
        :type deployment_state: str
        :param description: Description
        :type description: str
        :param device_id: The device ID
        :type device_id: str
        :param id: (Required) The metadata record ID
        :type id: str
        :param mechanism: How the firmware is delivered (connector or direct)
        :type mechanism: str
        :param mechanism_url: The Device Management Connect URL
        :type mechanism_url: str
        :param name: The record name
        :type name: str
        :param updated_at: The record was modified in the database format: date-time
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._campaign_id = fields.StringField(value=campaign_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._deployment_state = fields.StringField(
            value=deployment_state, enum=enums.CampaignDeviceMetadataDeploymentStateEnum
        )
        self._description = fields.StringField(value=description)
        self._device_id = fields.StringField(value=device_id)
        self._id = fields.StringField(value=id)
        self._mechanism = fields.StringField(value=mechanism)
        self._mechanism_url = fields.StringField(value=mechanism_url)
        self._name = fields.StringField(value=name)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def campaign_id(self):
        """The device's campaign ID

        This field must be set when creating a new CampaignDeviceMetadata Entity.
        
        api example: '015bf72fccda00000000000100100280'
        
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
    def created_at(self):
        """The time the campaign was created
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def deployment_state(self):
        """The state of the update campaign on the device
        
        :rtype: str
        """

        return self._deployment_state.value

    @property
    def description(self):
        """Description
        
        :rtype: str
        """

        return self._description.value

    @property
    def device_id(self):
        """The device ID
        
        api example: '015c2fec9bba0000000000010010036f'
        
        :rtype: str
        """

        return self._device_id.value

    @property
    def id(self):
        """The metadata record ID

        This field must be set when updating or deleting an existing CampaignDeviceMetadata Entity.
        
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
    def mechanism(self):
        """How the firmware is delivered (connector or direct)
        
        api example: 'connector'
        
        :rtype: str
        """

        return self._mechanism.value

    @property
    def mechanism_url(self):
        """The Device Management Connect URL
        
        :rtype: str
        """

        return self._mechanism_url.value

    @property
    def name(self):
        """The record name
        
        api example: 'default_object_name'
        
        :rtype: str
        """

        return self._name.value

    @property
    def updated_at(self):
        """The record was modified in the database format: date-time
        
        api example: '2017-05-22T12:37:58.776736Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def read(self):
        """Get a campaign device metadata

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/update-campaigns/{campaign_id}/campaign-device-metadata/{campaign_device_metadata_id}/>`_.
        
        :rtype: CampaignDeviceMetadata
        """

        return self._client.call_api(
            method="get",
            path="/v3/update-campaigns/{campaign_id}/campaign-device-metadata/{campaign_device_metadata_id}/",
            content_type="application/json",
            path_params={"campaign_id": self._campaign_id.to_api(), "campaign_device_metadata_id": self._id.to_api()},
            unpack=self,
        )
