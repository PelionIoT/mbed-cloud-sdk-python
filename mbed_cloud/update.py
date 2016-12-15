"""API reference for update components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import config
from mbed_cloud.decorators import catch_exceptions

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
        firmware_catalog.configuration.api_key['Authorization'] = config.get('api_key')
        firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'
        if config.get('host'):
            firmware_catalog.configuration.host = config.get('host')

    @catch_exceptions(FirmwareCatalogApiException)
    def list_firmware_images(self, **kwargs):
        """List all firmware images.

        :param limit: number of firmware images to retrieve (int)
        :param order: ordering of images when ordered by time. 'desc' or 'asc' (str)
        :param after: get firmware images after given `image_id` (str)
        :return: list of firmware image objects
        """
        kwargs = self._verify_sort_options(kwargs)
        api = firmware_catalog.DefaultApi()
        return api.firmware_image_list(
            **kwargs
        ).data
