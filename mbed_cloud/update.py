"""API reference for update components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

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
    def list_update_campaigns(self, **kwargs):
        """List all update campaigns.

        :param limit: number of campaigns to retrieve (int)
        :param order: sort direction of campaigns when ordered by creation time (desc|asc)
        :param after: get campaigns after given campaign ID (str)
        :return: paginated response object with list of campaign objects
        """
        api = self.deployment_service.DefaultApi()
        kwargs = self._verify_sort_options(kwargs)
        return api.update_campaign_list(**kwargs)

    @catch_exceptions(DeploymentServiceApiException)
    def create_update_campaign(self, name, **kwargs):
        """Create new update campaign.

        :param description: Optional description of the campaign (str)
        :param filter: Devices to apply the update on. Provide filter ID (str)
        :param root_manifest_id: Manifest with metadata/description of the update (str)
        :param name: Name of the update campaign (str)
        :return: newly created campaign object
        """
        api = self.deployment_service.DefaultApi()
        return api.update_campaign_create(name, **kwargs)

    @catch_exceptions(FirmwareCatalogApiException)
    def list_firmware_images(self, **kwargs):
        """List all firmware images.

        :param limit: number of firmware images to retrieve (int)
        :param order: ordering of images when ordered by time. 'desc' or 'asc' (str)
        :param after: get firmware images after given `image_id` (str)
        :return: list of firmware image objects
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.firmware_catalog.DefaultApi()
        return PaginatedResponse(api.firmware_image_list, **kwargs)

    @catch_exceptions(FirmwareCatalogApiException)
    def list_manifests(self, **kwargs):
        """List all manifests.

        :param limit: number of manifests to retrieve (int)
        :param order: sort direction of manifests when ordered by time. 'desc' or 'asc' (str)
        :param after: get manifests after given `image_id` (str)
        :return: list of manifest objects
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.firmware_catalog.DefaultApi()
        return PaginatedResponse(api.firmware_manifest_list, **kwargs)

    @catch_exceptions(FirmwareCatalogApiException)
    def upload_manifest(self, name, datafile, description=""):
        """Upload/create a new manifest reference.

        :return: the newly created manifest object
        """
        api = self.firmware_catalog.DefaultApi()
        return api.firmware_manifest_create(name=name, datafile=datafile, description=description)
