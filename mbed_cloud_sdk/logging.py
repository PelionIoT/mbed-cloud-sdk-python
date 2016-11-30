"""API reference for logging components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI
from mbed_cloud_sdk import config
from mbed_cloud_sdk.decorators import catch_exceptions

# TODO(Herman): Import backend API
import mbed_cloud_sdk._backends.device_catalog as device_catalog
from mbed_cloud_sdk._backends.device_catalog.rest import ApiException

LOG = logging.getLogger(__name__)


class LoggingAPI(BaseAPI):
    """Describing the public logging API.

    Exposing functionality from the following underlying services:

        - Device logging
        - Access logging
        - Update campaign logging
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(LoggingAPI, self).__init__(params)
        device_catalog.configuration.api_key['Authorization'] = config.get("api_key")
        device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'
        if config.get("host"):
            device_catalog.configuration.host = config.get("host")

    @catch_exceptions(ApiException)
    def list_device_logs(self, **kwargs):
        """List all device logs.

        :param date_time: (Optional)
        :param device_id: (Optional)
        :param device_log_id: (Optional)
        :param event_type: (Optional)
        :param state_change: (Optional)
        :return: list of device log objects
        """
        api = device_catalog.DefaultApi()
        return api.device_log_list(**kwargs)

    @catch_exceptions(ApiException)
    def get_device_log(self, device_log_id):
        """Get device log with provided ID."""
        api = device_catalog.DefaultApi()
        return api.device_log_retrieve(device_log_id)

    @catch_exceptions(ApiException)
    def delete_device_log(self, device_log_id, **kwargs):
        """Delete device logs matching log ID and filters.

        :param device_log_id: the device log ID to delete.
        :param date_time: (Optional)
        :param device_id: (Optional)
        :param device_log_id2: (Optional)
        :param event_type: (Optional)
        :param state_change: (Optional)
        :return: void
        """
        api = device_catalog.DefaultApi()
        return api.device_log_destroy(device_log_id, **kwargs)

    @catch_exceptions(ApiException)
    def create_device_log(self, date_time, **kwargs):
        """Delete device logs matching log ID and filters.

        :param date_time: the date time (ISO-8601) string.
        :param device_log_id: (Optional) (str)
        :param event_type: (Optional) (str)
        :param state_change: (Optional) (bool)
        :param device_id: (Optional)
        :param device_log_id2: (Optional)
        :param event_type2: (Optional)
        :param state_change2: (Optional)
        :return: void
        """
        api = device_catalog.DefaultApi()
        return api.device_log_create(date_time, **kwargs)
