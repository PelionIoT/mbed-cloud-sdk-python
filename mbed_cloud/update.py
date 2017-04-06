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
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

import mbed_cloud._backends.deployment_service as deployment_service
from mbed_cloud._backends.deployment_service.models\
    import UpdateCampaign as UpdateCampaignObj
from mbed_cloud._backends.deployment_service.rest\
    import ApiException as DeploymentServiceApiException
import mbed_cloud._backends.firmware_catalog as firmware_catalog
from mbed_cloud._backends.firmware_catalog.models import FirmwareImage
from mbed_cloud._backends.firmware_catalog.models import FirmwareManifest
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
    def list_update_campaigns(self, **kwargs):
        """List all update campaigns.

        :param int limit: number of campaigns to retrieve
        :param str order: sort direction of campaigns when ordered by creation time (desc|asc)
        :param str after: get campaigns after given campaign ID
        :return: List of :py:class:`UpdateCampaign` objects
        :rtype: PaginatedResponse
        """
        api = self.deployment_service.DefaultApi()
        kwargs = self._verify_sort_options(kwargs)
        return PaginatedResponse(api.update_campaign_list, lwrap_type=UpdateCampaign, **kwargs)

    @catch_exceptions(DeploymentServiceApiException)
    def get_update_campaign(self, campaign_id):
        """Get existing update campaign.

        :param str campaign_id: Campaign to retrieve
        :return: Update campaign object matching provided ID.
        :rtype: UpdateCampaign
        """
        api = self.deployment_service.DefaultApi()
        return api.update_campaign_retrieve(campaign_id)

    @catch_exceptions(DeploymentServiceApiException)
    def get_update_campaign_status(self, campaign_id):
        """Get status of existing update campaign.

        :param str campaign_id: Campaign to retrieve status
        :return: Update campaign status object matching provided ID.
        :rtype: UpdateCampaign
        """
        api = self.deployment_service.DefaultApi()
        return api.update_campaign_status(campaign_id)

    @catch_exceptions(DeploymentServiceApiException)
    def add_update_campaign(self, name, device_filter, **kwargs):
        """Add new update campaign.

        Add an update campaign with given name and device filtering. Example:

        .. code-block:: python

            device_api, update_api = DeviceAPI(), UpdateAPI()

            # Get a filter to use for update campaign
            device_filter_obj = device_api.get_filter(filter_id="MYID")

            # Create the campaign
            new_campaign = update_api.add_update_campaign(
                name="foo",
                device_filter=device_filter_obj.query
            )

        :param str name: Name of the update campaign
        :param str device_filter: Devices to apply the update on. Provide filter ID
        :param str root_manifest_id: Manifest with metadata/description of the update
        :param str description: Optional description of the campaign
        :param str when: The timestamp at which update campaign scheduled to start
        :return: newly created campaign object
        :rtype: UpdateCampaign
        """
        api = self.deployment_service.DefaultApi()
        body = self.deployment_service.UpdateCampaignPostRequest(
            name=name,
            device_filter=device_filter,
            **kwargs)
        return api.update_campaign_create(body)

    @catch_exceptions(DeploymentServiceApiException)
    def start_update_campaign(self, campaign_object):
        """Start an update campaign in draft state.

        :param UpdateCampaign campaign_object: Campaign object to schedule for immediate start.
        :return: newly edited campaign object
        :rtype: UpdateCampaign
        """
        api = self.deployment_service.DefaultApi()
        campaign_object.state = "scheduled"
        return api.update_campaign_update(campaign_id=campaign_object.id, body=campaign_object)

    @catch_exceptions(DeploymentServiceApiException)
    def delete_update_campaign(self, campaign_id):
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
        return Firmware(api.firmware_image_retrieve(image_id))

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
        return PaginatedResponse(api.firmware_image_list, lwrap_type=Firmware, **kwargs)

    @catch_exceptions(FirmwareCatalogApiException)
    def add_firmware(self, name, datafile, description=""):
        """Add a new firmware reference.

        :param str name: firmware file short name
        :param str datafile: the *path* to the manifest file
        :param str description: optional firmware file description
        :return: the newly created firmware file object
        :rtype: Firmware
        """
        api = self.firmware_catalog.DefaultApi()
        return Firmware(
            api.firmware_image_create(name=name, datafile=datafile, description=description)
        )

    @catch_exceptions(FirmwareCatalogApiException)
    def delete_firmware(self, firmware_image_id):
        """Delete a firmware image.

        :param str firmware_image_id: image ID for the firmware to remove/delete
        :return: void
        """
        api = self.firmware_catalog.DefaultApi()
        api.firmware_image_destroy(image_id=firmware_image_id)
        return

    @catch_exceptions(FirmwareCatalogApiException)
    def get_manifest(self, manifest_id):
        """Get manifest with provided manifest_id.

        :param str manifest_id: ID of manifest to retrieve
        :return Manifest
        """
        api = self.firmware_catalog.DefaultApi()
        return Manifest(api.firmware_manifest_retrieve(manifest_id=manifest_id))

    @catch_exceptions(FirmwareCatalogApiException)
    def list_manifests(self, **kwargs):
        """List all manifests.

        :param int limit: number of manifests to retrieve
        :param str order: sort direction of manifests when ordered by time. 'desc' or 'asc'
        :param str after: get manifests after given `image_id`
        :return: list of :py:class:`Manifest` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.firmware_catalog.DefaultApi()
        return PaginatedResponse(api.firmware_manifest_list, lwrap_type=Manifest, **kwargs)

    @catch_exceptions(FirmwareCatalogApiException)
    def add_manifest(self, name, datafile, description=""):
        """Add a new manifest reference.

        :param str name: manifest file short name
        :param str datafile: the *path* to the manifest file
        :param str description: optional manifest file description
        :return: the newly created manifest file object
        :rtype: Manifest
        """
        api = self.firmware_catalog.DefaultApi()
        return Manifest(
            api.firmware_manifest_create(name=name, datafile=datafile, description=description)
        )

    @catch_exceptions(FirmwareCatalogApiException)
    def delete_manifest(self, manifest_id):
        """Delete an existing manifest.

        :param str manifest_id: Manifest file ID to delete
        :return: void.
        """
        api = self.firmware_catalog.DefaultApi()
        return api.firmware_manifest_destroy(manifest_id)


class Firmware(FirmwareImage):
    """Describes firmware object."""

    def __init__(self, firmware_image_obj):
        """Override __init__ and allow passing in backend object."""
        super(Firmware, self).__init__(**firmware_image_obj.to_dict())


class Manifest(FirmwareManifest):
    """Describes firmware manifest object."""

    def __init__(self, manifest_image_obj):
        """Override __init__ and allow passing in backend object."""
        super(Manifest, self).__init__(**manifest_image_obj.to_dict())


class UpdateCampaign(UpdateCampaignObj):
    """Describes update campaign object."""

    def __init__(self, device_certificate_obj):
        """Override __init__ and allow passing in backend object."""
        super(UpdateCampaign, self).__init__(**device_certificate_obj.to_dict())
