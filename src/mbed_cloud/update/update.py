# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""API reference for update components in Mbed Cloud"""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud.core import BaseAPI
from mbed_cloud.core import BaseObject
from mbed_cloud.pagination import PaginatedResponse
from mbed_cloud.utils import force_utc

from mbed_cloud.decorators import catch_exceptions

from mbed_cloud.device_directory import Device

from six import iteritems

from mbed_cloud import filters

import mbed_cloud._backends.update_service as update_service
from mbed_cloud._backends.update_service.models import UpdateCampaignPostRequest
from mbed_cloud._backends.update_service.rest import ApiException as UpdateServiceApiException

LOG = logging.getLogger(__name__)


class UpdateAPI(BaseAPI):
    """Describing the public update API.

    Exposing functionality from the following underlying services:

        - Update service
        - Update campaigns
        - Manifest management
    """

    api_structure = {update_service: [update_service.DefaultApi]}

    @catch_exceptions(UpdateServiceApiException)
    def list_campaigns(self, **kwargs):
        """List all update campaigns.

        :param int limit: number of campaigns to retrieve
        :param str order: sort direction of campaigns when ordered by creation time (desc|asc)
        :param str after: get campaigns after given campaign ID
        :param dict filters: Dictionary of filters to apply
        :return: List of :py:class:`Campaign` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, Campaign, True)
        api = self._get_api(update_service.DefaultApi)
        return PaginatedResponse(api.update_campaign_list, lwrap_type=Campaign, **kwargs)

    @catch_exceptions(UpdateServiceApiException)
    def get_campaign(self, campaign_id):
        """Get existing update campaign.

        :param str campaign_id: Campaign ID to retrieve (Required)
        :return: Update campaign object matching provided ID
        :rtype: Campaign
        """
        api = self._get_api(update_service.DefaultApi)
        return Campaign(api.update_campaign_retrieve(campaign_id))

    @catch_exceptions(UpdateServiceApiException)
    def add_campaign(self, name, device_filter, **kwargs):
        """Add new update campaign.

        Add an update campaign with a name and device filtering. Example:

        .. code-block:: python

            device_api, update_api = DeviceDirectoryAPI(), UpdateAPI()

            # Get a filter to use for update campaign
            query_obj = device_api.get_query(query_id="MYID")

            # Create the campaign
            new_campaign = update_api.add_campaign(
                name="foo",
                device_filter=query_obj.filter
            )

        :param str name: Name of the update campaign (Required)
        :param str device_filter: The device filter to use (Required)
        :param str manifest_id: ID of the manifest with description of the update
        :param str description: Description of the campaign
        :param int scheduled_at: The timestamp at which update campaign is scheduled to start
        :param str state: The state of the campaign. Values:
            "draft", "scheduled", "devicefetch", "devicecopy", "publishing",
            "deploying", "deployed", "manifestremoved", "expired"
        :return: newly created campaign object
        :rtype: Campaign
        """
        device_filter = filters.legacy_filter_formatter(
            dict(filter=device_filter),
            Device._get_attributes_map()
        )
        campaign = Campaign._create_request_map(kwargs)
        if 'when' in campaign:
            # FIXME: randomly validating an input here is a sure route to nasty surprises elsewhere
            campaign['when'] = force_utc(campaign['when'])
        body = UpdateCampaignPostRequest(
            name=name,
            device_filter=device_filter['filter'],
            **campaign)
        api = self._get_api(update_service.DefaultApi)
        return Campaign(api.update_campaign_create(body))

    @catch_exceptions(UpdateServiceApiException)
    def start_campaign(self, campaign_object):
        """Start a draft update campaign.

        :param Campaign campaign_object: Campaign object to schedule for immediate start (Required)
        :return: newly edited campaign object
        :rtype: Campaign
        """
        campaign_object._state = "scheduled"
        return self.update_campaign(campaign_object)

    @catch_exceptions(UpdateServiceApiException)
    def update_campaign(self, campaign_object=None, campaign_id=None, **kwargs):
        """Update an update campaign.

        :param :class:`Campaign` campaign_object: Campaign object to update (Required)
        :return: updated campaign object
        :rtype: Campaign
        """
        api = self._get_api(update_service.DefaultApi)
        if campaign_object:
            campaign_id = campaign_object.id
            campaign_object = campaign_object._create_patch_request()
        else:
            campaign_object = Campaign._create_request_map(kwargs)
        if 'device_filter' in campaign_object:
            campaign_object["device_filter"] = filters.legacy_filter_formatter(
                dict(filter=campaign_object["device_filter"]),
                Device._get_attributes_map()
            )['filter']
        if 'when' in campaign_object:
            # FIXME: randomly validating an input here is a sure route to nasty surprises elsewhere
            campaign_object['when'] = force_utc(campaign_object['when'])
        return Campaign(api.update_campaign_update(campaign_id=campaign_id,
                                                   campaign=campaign_object))

    @catch_exceptions(UpdateServiceApiException)
    def delete_campaign(self, campaign_id):
        """Delete an update campaign.

        :param str campaign_id: Campaign ID to delete (Required)
        :return: void
        """
        api = self._get_api(update_service.DefaultApi)
        api.update_campaign_destroy(campaign_id)
        return

    @catch_exceptions(UpdateServiceApiException)
    def list_campaign_device_states(self, campaign_id, **kwargs):
        """List campaign devices status.

        :param str campaign_id: Id of the update campaign (Required)
        :param int limit: number of devices state to retrieve
        :param str order: sort direction of device state when ordered by creation time (desc|asc)
        :param str after: get devices state after given id
        :return: List of :py:class:`CampaignDeviceState` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, CampaignDeviceState, True)
        kwargs["campaign_id"] = campaign_id
        api = self._get_api(update_service.DefaultApi)
        return PaginatedResponse(api.update_campaign_metadata_list,
                                 lwrap_type=CampaignDeviceState, **kwargs)

    @catch_exceptions(UpdateServiceApiException)
    def get_firmware_image(self, image_id):
        """Get a firmware image with provided image_id.

        :param str image_id: The firmware ID for the image to retrieve (Required)
        :return: FirmwareImage
        """
        api = self._get_api(update_service.DefaultApi)
        return FirmwareImage(api.firmware_image_retrieve(image_id))

    @catch_exceptions(UpdateServiceApiException)
    def list_firmware_images(self, **kwargs):
        """List all firmware images.

        :param int limit: number of firmware images to retrieve
        :param str order: ordering of images when ordered by time. 'desc' or 'asc'
        :param str after: get firmware images after given `image_id`
        :param dict filters: Dictionary of filters to apply
        :return: list of :py:class:`FirmwareImage` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, FirmwareImage, True)
        api = self._get_api(update_service.DefaultApi)
        return PaginatedResponse(api.firmware_image_list, lwrap_type=FirmwareImage, **kwargs)

    @catch_exceptions(UpdateServiceApiException)
    def add_firmware_image(self, name, datafile, **kwargs):
        """Add a new firmware reference.

        :param str name: Firmware file short name (Required)
        :param str datafile: The file object or *path* to the firmware image file (Required)
        :param str description: Firmware file description
        :return: the newly created firmware file object
        :rtype: FirmwareImage
        """
        kwargs.update({'name': name})
        firmware_image = FirmwareImage._create_request_map(kwargs)
        firmware_image.update({'datafile': datafile})
        api = self._get_api(update_service.DefaultApi)
        return FirmwareImage(
            api.firmware_image_create(**firmware_image)
        )

    @catch_exceptions(UpdateServiceApiException)
    def delete_firmware_image(self, image_id):
        """Delete a firmware image.

        :param str image_id: image ID for the firmware to remove/delete (Required)
        :return: void
        """
        api = self._get_api(update_service.DefaultApi)
        api.firmware_image_destroy(image_id=image_id)
        return

    @catch_exceptions(UpdateServiceApiException)
    def get_firmware_manifest(self, manifest_id):
        """Get manifest with provided manifest_id.

        :param str manifest_id: ID of manifest to retrieve (Required)
        :return: FirmwareManifest
        """
        api = self._get_api(update_service.DefaultApi)
        return FirmwareManifest(api.firmware_manifest_retrieve(manifest_id=manifest_id))

    @catch_exceptions(UpdateServiceApiException)
    def list_firmware_manifests(self, **kwargs):
        """List all manifests.

        :param int limit: number of manifests to retrieve
        :param str order: sort direction of manifests when ordered by time. 'desc' or 'asc'
        :param str after: get manifests after given `image_id`
        :param dict filters: Dictionary of filters to apply
        :return: list of :py:class:`FirmwareManifest` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, FirmwareManifest, True)
        api = self._get_api(update_service.DefaultApi)
        return PaginatedResponse(api.firmware_manifest_list, lwrap_type=FirmwareManifest, **kwargs)

    @catch_exceptions(UpdateServiceApiException)
    def add_firmware_manifest(self, name, datafile, key_table_file=None, **kwargs):
        """Add a new manifest reference.

        :param str name: Manifest file short name (Required)
        :param str datafile: The file object or path to the manifest file (Required)
        :param str key_table_file: The file object or path to the key_table file (Optional)
        :param str description: Manifest file description
        :return: the newly created manifest file object
        :rtype: FirmwareManifest
        """
        kwargs.update({
            'name': name,
            'url': datafile,  # really it's the datafile
        })
        if key_table_file is not None:
            kwargs.update({'key_table_url': key_table_file})  # really it's the key_table
        firmware_manifest = FirmwareManifest._create_request_map(kwargs)
        api = self._get_api(update_service.DefaultApi)
        return FirmwareManifest(
            api.firmware_manifest_create(**firmware_manifest)
        )

    @catch_exceptions(UpdateServiceApiException)
    def delete_firmware_manifest(self, manifest_id):
        """Delete an existing manifest.

        :param str manifest_id: Manifest file ID to delete (Required)
        :return: void
        """
        api = self._get_api(update_service.DefaultApi)
        return api.firmware_manifest_destroy(manifest_id)


class FirmwareImage(BaseObject):
    """Describes firmware object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "created_at": "created_at",
            "datafile_checksum": "datafile_checksum",
            "datafile_size": "datafile_size",
            "description": "description",
            "id": "id",
            "name": "name",
            "updated_at": "updated_at",
            "url": "datafile",
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
    def datafile_size(self):
        """Size of the datafile (in bytes) (readonly).

        :rtype: int
        """
        return self._datafile_size

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
            "key_table_url": "key_table",
            "description": "description",
            "device_class": "device_class",
            "datafile_size": "datafile_size",
            "id": "id",
            "name": "name",
            "timestamp": "timestamp",
            "updated_at": "updated_at",
            "version": "version"
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
    def key_table_url(self):
        """The URL of the key_table (readonly).

        :rtype: str
        """
        return self._key_table_url

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
    def datafile_size(self):
        """Size of the datafile (in bytes) (readonly).

        :rtype: int
        """
        return self._datafile_size

    @property
    def id(self):
        """The ID of the firmware manifest (readonly).

        :rtype: str
        """
        return self._id

    @property
    def name(self):
        """The name of the firmware manifest (readonly).

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

    @property
    def version(self):
        """The time the object was updated (readonly).

        :rtype: str
        """
        return self._version


class Campaign(BaseObject):
    """Describes update campaign object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "created_at": "created_at",
            "description": "description",
            "device_filter": "device_filter",
            "finished_at": "finished",
            "id": "id",
            "manifest_id": "root_manifest_id",
            "manifest_url": "root_manifest_url",
            "name": "name",
            "phase": "phase",
            "scheduled_at": "when",
            "started_at": "started_at",
            "state": "state",
            "updated_at": "updated_at",
        }

    def _create_patch_request(self):
        patch_map = {
            "description": "description",
            "device_filter": "device_filter",
            "manifest_id": "root_manifest_id",
            "name": "name",
            "scheduled_at": "when",
            "state": "state",
        }
        map_patch = {}
        for key, value in iteritems(patch_map):
            val = getattr(self, key, None)
            if val is not None:
                map_patch[value] = val
        return map_patch

    @property
    def phase(self):
        """The phase of this Campaign.

        :return: The phase of this Campaign.
        :rtype: str
        """
        return self._phase

    @property
    def device_filter(self):
        """The device filter to use.

        :rtype: dict
        """
        if isinstance(self._device_filter, str):
            return self._decode_query(self._device_filter)
        return self._device_filter

    @device_filter.setter
    def device_filter(self, device_filter):
        """The device filter of this campaign.

        The filter for the devices the campaign will target

        :param device_filter: The device filter of this campaign.
        :type: dict
        """
        self._device_filter = device_filter

    @property
    def created_at(self):
        """The time the object was created (readonly).

        :rtype: datetime
        """
        return self._created_at

    @property
    def updated_at(self):
        """The time the object was last updated (readonly).

        :rtype: datetime
        """
        return self._updated_at

    @property
    def description(self):
        """The description of the campaign.

        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """The description of this Campaign.

        An description of the campaign

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
        """The URL of the manifest used (readonly).

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
        """The timestamp at which update campaign is scheduled to start (readonly).

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
        """The timestamp at which update campaign is scheduled to start.

        :param scheduled_at: The timestamp of this Cmapaign.
        :type: str
        """
        self._scheduled_at = scheduled_at


class CampaignDeviceState(BaseObject):
    """Describes update campaign device state."""

    @staticmethod
    def _get_attributes_map():
        return {
            "id": "id",
            "device_id": "device_id",
            "campaign_id": "campaign",
            "state": "deployment_state",
            "name": "name",
            "description": "description",
            "created_at": "created_at",
            "updated_at": "updated_at",
            "mechanism": "mechanism",
            "mechanism_url": "mechanism_url"
        }

    @property
    def id(self):
        """The id of the metadata record (readonly).

        :rtype: str
        """
        return self._id

    @property
    def device_id(self):
        """The id of the device (readonly).

        :rtype: str
        """
        return self._device_id

    @property
    def campaign_id(self):
        """The id of the campaign the device is in (readonly).

        :rtype: str
        """
        return self._campaign_id

    @property
    def state(self):
        """The state of the update campaign on the device (readonly).

        values: pending, updated_connector_channel, failed_connector_channel_update,
        deployed, manifestremoved, deregistered

        :rtype: str
        """
        return self._state

    @property
    def name(self):
        """The name of the device (readonly).

        :rtype: str
        """
        return self._name

    @property
    def description(self):
        """Description of the device (readonly).

        :rtype: str
        """
        return self._description

    @property
    def created_at(self):
        """This time the record was created in the database (readonly).

        :rtype: datetime
        """
        return self._created_at

    @property
    def updated_at(self):
        """This time this record was modified in the database (readonly).

        :rtype: datetime
        """
        return self._updated_at

    @property
    def mechanism(self):
        """The mechanism used to deliver the firmware (connector or direct) (readonly).

        :rtype: str
        """
        return self._mechanism

    @property
    def mechanism_url(self):
        """The url of cloud connect used (readonly).

        :rtype: str
        """
        return self._mechanism_url
