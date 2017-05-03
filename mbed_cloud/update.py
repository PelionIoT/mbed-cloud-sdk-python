# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""API reference for update components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import BaseObject
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse
from six import iteritems

import mbed_cloud._backends.deployment_service as deployment_service
from mbed_cloud._backends.deployment_service.rest\
    import ApiException as DeploymentServiceApiException
import mbed_cloud._backends.firmware_catalog as firmware_catalog
from mbed_cloud._backends.firmware_catalog.rest\
    import ApiException as FirmwareCatalogApiException

LOG = logging.getLogger(__name__)


class UpdateAPI(BaseAPI):
    """Describing the public update API.

    Exposing functionality from the following underlying services:

        - Update service
        - Update campaigns
        - Manifest management
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(UpdateAPI, self).__init__(params)

        self.firmware_catalog = self._init_api(firmware_catalog)
        self.deployment_service = self._init_api(deployment_service)

    @catch_exceptions(DeploymentServiceApiException)
    def list_campaigns(self, **kwargs):
        """List all update campaigns.

        :param int limit: number of campaigns to retrieve
        :param str order: sort direction of campaigns when ordered by creation time (desc|asc)
        :param str after: get campaigns after given campaign ID
        :return: List of :py:class:`Campaign` objects
        :rtype: PaginatedResponse
        """
        api = self.deployment_service.DefaultApi()
        kwargs = self._verify_sort_options(kwargs)
        return PaginatedResponse(api.update_campaign_list, lwrap_type=Campaign, **kwargs)

    @catch_exceptions(DeploymentServiceApiException)
    def get_campaign(self, campaign_id):
        """Get existing update campaign.

        :param str campaign_id: Campaign to retrieve
        :return: Update campaign object matching provided ID.
        :rtype: Campaign
        """
        api = self.deployment_service.DefaultApi()
        return Campaign(api.update_campaign_retrieve(campaign_id))

    @catch_exceptions(DeploymentServiceApiException)
    def add_campaign(self, name, device_filter, **kwargs):
        """Add new update campaign.

        Add an update campaign with given name and device filtering. Example:

        .. code-block:: python

            device_api, update_api = DeviceDirectoryAPI(), UpdateAPI()

            # Get a filter to use for update campaign
            device_filter_obj = device_api.get_filter(filter_id="MYID")

            # Create the campaign
            new_campaign = update_api.add_campaign(
                name="foo",
                device_filter=device_filter_obj.query
            )

        :param str name: Name of the update campaign
        :param str device_filter: Devices to apply the update on. Provide filter ID
        :param str root_manifest_id: Manifest with metadata/description of the update
        :param str description: Optional description of the campaign
        :param str when: The timestamp at which update campaign scheduled to start
        :return: newly created campaign object
        :rtype: Campaign
        """
        api = self.deployment_service.DefaultApi()
        body = self.deployment_service.UpdateCampaignPostRequest(
            name=name,
            device_filter=device_filter,
            **kwargs)
        return Campaign(api.update_campaign_create(body))

    @catch_exceptions(DeploymentServiceApiException)
    def start_campaign(self, campaign_object):
        """Start an update campaign in draft state.

        :param Campaign campaign_object: Campaign object to schedule for immediate start.
        :return: newly edited campaign object
        :rtype: Campaign
        """
        campaign_object._state = "scheduled"
        return self.update_campaign(campaign_object)

    @catch_exceptions(DeploymentServiceApiException)
    def update_campaign(self, campaign_object):
        """Update an update campaign.

        :param Campaign campaign_object: Campaign object to update.
        :return: updated campaign object
        :rtype: Campaign
        """
        api = self.deployment_service.DefaultApi()
        campaign_id = campaign_object.id
        campaign_object = campaign_object._create_patch_request()
        return Campaign(api.update_campaign_partial_update(campaign_id=campaign_id,
                                                           campaign=campaign_object))

    @catch_exceptions(DeploymentServiceApiException)
    def delete_campaign(self, campaign_id):
        """Delete an update campaign.

        :param campaign_id: Campaign ID to delete (str)
        :return: void
        """
        api = self.deployment_service.DefaultApi()
        api.update_campaign_destroy(campaign_id)
        return

    @catch_exceptions(FirmwareCatalogApiException)
    def get_firmware_image(self, image_id):
        """Get a firmware image with provided image_id.

        :param str image_id: The firmware ID for the image to retrieve
        :return: Firmware
        """
        api = self.firmware_catalog.DefaultApi()
        return FirmwareImage(api.firmware_image_retrieve(image_id))

    @catch_exceptions(FirmwareCatalogApiException)
    def list_firmware_images(self, **kwargs):
        """List all firmware images.

        :param int limit: number of firmware images to retrieve
        :param str order: ordering of images when ordered by time. 'desc' or 'asc'
        :param str after: get firmware images after given `image_id`
        :return: list of :py:class:`Firmware` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.firmware_catalog.DefaultApi()
        return PaginatedResponse(api.firmware_image_list, lwrap_type=FirmwareImage, **kwargs)

    @catch_exceptions(FirmwareCatalogApiException)
    def add_firmware_image(self, name, url, description=""):
        """Add a new firmware reference.

        :param str name: firmware file short name
        :param str url: the *path* to the firmware file
        :param str description: optional firmware file description
        :return: the newly created firmware file object
        :rtype: FirmwareImage
        """
        api = self.firmware_catalog.DefaultApi()
        return FirmwareImage(
            api.firmware_image_create(name=name, datafile=url, description=description)
        )

    @catch_exceptions(FirmwareCatalogApiException)
    def delete_firmware_image(self, firmware_image_id):
        """Delete a firmware image.

        :param str firmware_image_id: image ID for the firmware to remove/delete
        :return: void
        """
        api = self.firmware_catalog.DefaultApi()
        api.firmware_image_destroy(image_id=firmware_image_id)
        return

    @catch_exceptions(FirmwareCatalogApiException)
    def get_firmware_manifest(self, manifest_id):
        """Get manifest with provided manifest_id.

        :param str manifest_id: ID of manifest to retrieve
        :return Manifest
        """
        api = self.firmware_catalog.DefaultApi()
        return FirmwareManifest(api.firmware_manifest_retrieve(manifest_id=manifest_id))

    @catch_exceptions(FirmwareCatalogApiException)
    def list_firmware_manifests(self, **kwargs):
        """List all manifests.

        :param int limit: number of manifests to retrieve
        :param str order: sort direction of manifests when ordered by time. 'desc' or 'asc'
        :param str after: get manifests after given `image_id`
        :return: list of :py:class:`Manifest` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.firmware_catalog.DefaultApi()
        return PaginatedResponse(api.firmware_manifest_list, lwrap_type=FirmwareManifest, **kwargs)

    @catch_exceptions(FirmwareCatalogApiException)
    def add_firmware_manifest(self, name, url, description=""):
        """Add a new manifest reference.

        :param str name: manifest file short name
        :param str url: the *path* to the manifest file
        :param str description: optional manifest file description
        :return: the newly created manifest file object
        :rtype: FirmwareManifest
        """
        api = self.firmware_catalog.DefaultApi()
        return FirmwareManifest(
            api.firmware_manifest_create(name=name, datafile=url, description=description)
        )

    @catch_exceptions(FirmwareCatalogApiException)
    def delete_firmware_manifest(self, manifest_id):
        """Delete an existing manifest.

        :param str manifest_id: Manifest file ID to delete
        :return: void.
        """
        api = self.firmware_catalog.DefaultApi()
        return api.firmware_manifest_destroy(manifest_id)


class FirmwareImage(BaseObject):
    """Describes firmware object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "created_at": "created_at",
            "url": "datafile",
            "datafile_checksum": "datafile_checksum",
            "description": "description",
            "id": "id",
            "name": "name",
            "updated_at": "updated_at"
        }

    @property
    def created_at(self):
        """The time the object was created (readonly).

        :rtype: datetime
        """
        return self._created_at

    @property
    def url(self):
        """The URL of the firmware image (readonly).

        :rtype: str
        """
        return self._url

    @property
    def datafile_checksum(self):
        """The checksum generated for the datafile (readonly).

        :rtype: str
        """
        return self._datafile_checksum

    @property
    def description(self):
        """Get the description of firmware image (readonly).

        :rtype: str
        """
        return self._description

    @property
    def id(self):
        """Get the ID of the firmware image (readonly).

        :rtype: str
        """
        return self._id

    @property
    def name(self):
        """Get the name of firmware image (readonly).

        :rtype: str
        """
        return self._name

    @property
    def updated_at(self):
        """Get the time the object was updated (readonly).

        :rtype: datetime
        """
        return self._updated_at


class FirmwareManifest(BaseObject):
    """Describes firmware object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "created_at": "created_at",
            "url": "datafile",
            "description": "description",
            "device_class": "device_class",
            "id": "id",
            "manifest_contents": "manifest_contents",
            "name": "name",
            "timestamp": "timestamp",
            "updated_at": "updated_at"
        }

    @property
    def created_at(self):
        """Get the time the object was created (readonly).

        :rtype: datetime
        """
        return self._created_at

    @property
    def url(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._url

    @property
    def description(self):
        """Get the description of firmware manifest (readonly).

        :rtype: str
        """
        return self._description

    @property
    def device_class(self):
        """The class of device (readonly).

        :rtype: str
        """
        return self._device_class

    @property
    def id(self):
        """The ID of the firmware manifest (readonly).

        :rtype: str
        """
        return self._id

    @property
    def manifest_contents(self):
        """The contents of the manifest (readonly).

        :rtype: object
        """
        return self._manifest_contents

    @property
    def name(self):
        """The time the object was created (readonly).

        :rtype: str
        """
        return self._name

    @property
    def timestamp(self):
        """The timestamp of the firmware manifest (readonly).

        :rtype: datetime
        """
        return self._timestamp

    @property
    def updated_at(self):
        """The time the object was updated (readonly).

        :rtype: datetime
        """
        return self._updated_at


class Campaign(BaseObject):
    """Describes update campaign object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "device_filter": "device_filter",
            "created_at": "created_at",
            "description": "description",
            "finished_at": "finished",
            "id": "id",
            "manifest_id": "root_manifest_id",
            "manifest_url": "root_manifest_url",
            "name": "name",
            "started_at": "started_at",
            "state": "state",
            "scheduled_at": "when"
        }

    def _create_patch_request(self):
        patch_map = {
            "device_filter": "device_filter",
            "description": "description",
            "manifest_id": "root_manifest_id",
            "name": "name",
            "state": "state",
            "scheduled_at": "when"
        }
        map_patch = {}
        for key, value in iteritems(patch_map):
            val = getattr(self, key, None)
            if val is not None:
                map_patch[value] = val
        return map_patch

    @property
    def device_filter(self):
        """The device filter to use.

        :rtype: str
        """
        return self._device_filter

    @device_filter.setter
    def device_filter(self, device_filter):
        """The device filter of this campaign.

        The filter for the devices the campaign will target

        :param device_filter: The device filter of this campaign.
        :type: str
        """
        self._device_filter = device_filter

    @property
    def created_at(self):
        """The time the object was created (readonly).

        :rtype: datetime
        """
        return self._created_at

    @property
    def description(self):
        """The description of the campaign.

        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """The description of this Campaign.

        An optional description of the campaign

        :param description: The description of this Campaign.
        :type: str
        """
        self._description = description

    @property
    def finished_at(self):
        """The timestamp when the update campaign finished (readonly).

        :rtype: datetime
        """
        return self._finished_at

    @property
    def id(self):
        """The ID of the campaign (readonly).

        :rtype: str
        """
        return self._id

    @property
    def manifest_id(self):
        """The ID of the manifest to use for update.

        :rtype: str
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        """The manifest id of this Update Campaign.

        :param manifest_id: The ID of manifest.
        :type: str
        """
        self._manifest_id = manifest_id

    @property
    def manifest_url(self):
        """The URl of the manifest used (readonly).

        :rtype: str
        """
        return self._manifest_url

    @property
    def name(self):
        """The name for this campaign.

        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """The name of this campaign.

        A name for this campaign

        :param name: The name of this campaign.
        :type: str
        """
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")

        self._name = name

    @property
    def started_at(self):
        """The timestamp at which update campaign scheduled to start (readonly).

        :rtype: datetime
        """
        return self._started_at

    @property
    def state(self):
        """The state of the campaign (readonly).

        values: draft, scheduled, devicefetch, devicecopy, devicecopycomplete, publishing,
        deploying, deployed, manifestremoved, expired

        :rtype: str
        """
        return self._state

    @property
    def scheduled_at(self):
        """The time the object was created.

        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """The timestamp at which update campaign scheduled to start.

        :param scheduled_at: The timestamp of this Cmapaign.
        :type: str
        """
        self._scheduled_at = scheduled_at
