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
from __future__ import unicode_literals
from builtins import object
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import BaseObject
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse
from six import iteritems

import mbed_cloud._backends.update_service as update_service
from mbed_cloud._backends.update_service.rest\
    import ApiException as UpdateServiceApiException

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

        self.update_service = self._init_api(update_service)

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
        api = self.update_service.DefaultApi()
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, True)
        return PaginatedResponse(api.update_campaign_list, lwrap_type=Campaign, **kwargs)

    @catch_exceptions(UpdateServiceApiException)
    def get_campaign(self, campaign_id):
        """Get existing update campaign.

        :param str campaign_id: Campaign id to retrieve (Required)
        :return: Update campaign object matching provided ID.
        :rtype: Campaign
        """
        api = self.update_service.DefaultApi()
        return Campaign(api.update_campaign_retrieve(campaign_id))

    @catch_exceptions(UpdateServiceApiException)
    def add_campaign(self, name, device_filter, **kwargs):
        """Add new update campaign.

        Add an update campaign with given name and device filtering. Example:

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
        :param str device_filter: Devices to apply the update on. Provide filter ID (Required)
        :param str manifest_id: Manifest with metadata/description of the update
        :param str description: Description of the campaign
        :param date when: The timestamp at which update campaign scheduled to start
        :param str state: The state of the campaign. Values:
            "draft", "scheduled", "devicefetch", "devicecopy", "publishing",
            "deploying", "deployed", "manifestremoved", "expired"
        :return: newly created campaign object
        :rtype: Campaign
        """
        api = self.update_service.DefaultApi()
        device_filter = self._encode_query(device_filter)
        campaign = Campaign.create_request_map(kwargs)
        body = self.update_service.UpdateCampaignPostRequest(
            name=name,
            device_filter=device_filter,
            **campaign)
        return Campaign(api.update_campaign_create(body))

    @catch_exceptions(UpdateServiceApiException)
    def start_campaign(self, campaign_object):
        """Start an update campaign in draft state.

        :param Campaign campaign_object: Campaign object to schedule for immediate start (Required)
        :return: newly edited campaign object
        :rtype: Campaign
        """
        campaign_object._state = "scheduled"
        return self.update_campaign(campaign_object)

    @catch_exceptions(UpdateServiceApiException)
    def update_campaign(self, campaign_object):
        """Update an update campaign.

        :param str campaign_object: Campaign object to update (Required)
        :return: updated campaign object
        :rtype: Campaign
        """
        api = self.update_service.DefaultApi()
        campaign_id = campaign_object.id
        print(campaign_object)
        campaign_object = campaign_object._create_patch_request()
        print(campaign_object)
        if 'device_filter' in campaign_object:
            campaign_object["device_filter"] = self._encode_query(campaign_object["device_filter"])
        return Campaign(api.update_campaign_partial_update(campaign_id=campaign_id,
                                                           campaign=campaign_object))

    @catch_exceptions(UpdateServiceApiException)
    def delete_campaign(self, campaign_id):
        """Delete an update campaign.

        :param str campaign_id: Campaign ID to delete (Required)
        :return: void
        """
        api = self.update_service.DefaultApi()
        api.update_campaign_destroy(campaign_id)
        return

    @catch_exceptions(UpdateServiceApiException)
    def get_firmware_image(self, image_id):
        """Get a firmware image with provided image_id.

        :param str image_id: The firmware ID for the image to retrieve (Required)
        :return: FirmwareImage
        """
        api = self.update_service.DefaultApi()
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
        kwargs = self._verify_filters(kwargs, True)
        api = self.update_service.DefaultApi()
        return PaginatedResponse(api.firmware_image_list, lwrap_type=FirmwareImage, **kwargs)

    @catch_exceptions(UpdateServiceApiException)
    def add_firmware_image(self, name, datafile, **kwargs):
        """Add a new firmware reference.

        :param str name: Firmware file short name (Required)
        :param str datafile: Required. The *path* to the firmware file
        :param str description: Firmware file description
        :return: the newly created firmware file object
        :rtype: FirmwareImage
        """
        api = self.update_service.DefaultApi()
        kwargs.update({'name': name})
        firmware_image = FirmwareImage.create_request_map(kwargs)
        firmware_image.update({'datafile': datafile})
        return FirmwareImage(
            api.firmware_image_create(**firmware_image)
        )

    @catch_exceptions(UpdateServiceApiException)
    def delete_firmware_image(self, image_id):
        """Delete a firmware image.

        :param str image_id: image ID for the firmware to remove/delete (Required)
        :return: void
        """
        api = self.update_service.DefaultApi()
        api.firmware_image_destroy(image_id=image_id)
        return

    @catch_exceptions(UpdateServiceApiException)
    def get_firmware_manifest(self, manifest_id):
        """Get manifest with provided manifest_id.

        :param str manifest_id: ID of manifest to retrieve (Required)
        :return: FirmwareManifest
        """
        api = self.update_service.DefaultApi()
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
        kwargs = self._verify_filters(kwargs, True)
        api = self.update_service.DefaultApi()
        return PaginatedResponse(api.firmware_manifest_list, lwrap_type=FirmwareManifest, **kwargs)

    @catch_exceptions(UpdateServiceApiException)
    def add_firmware_manifest(self, name, datafile, **kwargs):
        """Add a new manifest reference.

        :param str name: Manifest file short name (Required)
        :param str datafile: The *path* to the manifest file (Required)
        :param str description: Manifest file description
        :return: the newly created manifest file object
        :rtype: FirmwareManifest
        """
        api = self.update_service.DefaultApi()
        kwargs.update({'name': name})
        firmware_manifest = FirmwareManifest.create_request_map(kwargs)
        firmware_manifest.update({'datafile': datafile})
        return FirmwareManifest(
            api.firmware_manifest_create(**firmware_manifest)
        )

    @catch_exceptions(UpdateServiceApiException)
    def delete_firmware_manifest(self, manifest_id):
        """Delete an existing manifest.

        :param str manifest_id: Manifest file ID to delete (Required)
        :return: void
        """
        api = self.update_service.DefaultApi()
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


class FirmwareManifestContents(object):
    """Describes firmware contents"""

    def __init__(self, dictionary):
        """Initialize object."""
        self._class_id = dictionary.get("class_id", None)
        self._vendor_id = dictionary.get("vendor_id", None)
        self._version = dictionary.get("manifest_version", None)
        self._description = dictionary.get("description", None)
        self._nonce = dictionary.get("nonce", None)
        self._created_at = dictionary.get("timestamp", None)
        self._apply_immediately = dictionary.get("apply_immediately", None)
        self._device_id = dictionary.get("device_id", None)
        self._encryption_mode = None
        self._payload_format = None
        self._payload_storage_identifier = None
        self._payload_hash = None
        self._payload_uri = None
        self._payload_size = None
        encryption_mode = dictionary.get("encryption_mode", None)
        if encryption_mode and "enum" in encryption_mode:
            self._set_encryption_mode(encryption_mode)
        payload = dictionary.get("payload", None)
        if payload:
            self._set_payload(payload)

    def _set_encryption_mode(self, encryption_mode):
        mode = encryption_mode["enum"]
        if mode == 1:
            self._encryption_mode = "none-ecc-secp256r1-sha256"
        if mode == 2:
            self._encryption_mode = "aes-128-ctr-ecc-secp256r1-sha256"
        if mode == 3:
            self._encryption_mode = "none-none-sha256"

    def _set_payload(self, payload):
        self._payload_storage_identifier = payload.get("storage_identifier", None)
        reference = payload.get("reference", None)
        payload_format = payload.get("format")
        if payload_format:
            format_enum = payload_format.get("enum", False)
            if format_enum:
                if format_enum == 1:
                    self._payload_format = "raw-binary"
                if format_enum == 2:
                    self._payload_format = "cbor"
                if format_enum == 3:
                    self._payload_format = "hex-location-length-data"
                if format_enum == 4:
                    self._payload_format = "elf"
        if reference:
            self._payload_hash = reference.get("hash", None)
            self._payload_uri = reference.get("uri", None)
            self._payload_size = reference.get("size", None)

    @property
    def class_id(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._class_id

    @property
    def vendor_id(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._vendor_id

    @property
    def version(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._version

    @property
    def description(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._description

    @property
    def nonce(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._nonce

    @property
    def created_at(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: int
        """
        return self._created_at

    @property
    def encryption_mode(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._encryption_mode

    @property
    def apply_immediately(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: bool
        """
        return self._apply_immediately

    @property
    def device_id(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._device_id

    @property
    def payload_format(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._payload_format

    @property
    def payload_storage_identifier(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._payload_storage_identifier

    @property
    def payload_hash(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._payload_hash

    @property
    def payload_uri(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._payload_uri

    @property
    def payload_size(self):
        """Get the URL of the firmware manifest (readonly).

        :rtype: str
        """
        return self._payload_size

    def to_dict(self):
        """Return the model properties as a dict"""
        return {
            "class_id": self.class_id,
            "vendor_id": self.vendor_id,
            "version": self.version,
            "description": self.description,
            "nonce": self.nonce,
            "created_at": self.created_at,
            "encryption_mode": self.encryption_mode,
            "apply_immediately": self.apply_immediately,
            "device_id": self.device_id,
            "payload_format": self.payload_format,
            "payload_storage_identifier": self.payload_storage_identifier,
            "payload_hash": self.payload_hash,
            "payload_uri": self.payload_uri,
            "payload_size": self.payload_size
        }

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())


class FirmwareManifest(BaseObject):
    """Describes firmware object."""

    def __init__(self, dictionary):
        """Initialize object."""
        super(FirmwareManifest, self).__init__(dictionary)
        self._contents = FirmwareManifestContents(self.contents).to_dict()

    @staticmethod
    def _get_attributes_map():
        return {
            "created_at": "created_at",
            "url": "datafile",
            "description": "description",
            "device_class": "device_class",
            "id": "id",
            "contents": "manifest_contents",
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
    def contents(self):
        """The contents of the manifest (readonly).

        :rtype: FirmwareManifestContents
        """
        return self._contents

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
