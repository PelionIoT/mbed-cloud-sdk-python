"""API reference for logging components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import config
from mbed_cloud.decorators import catch_exceptions

import mbed_cloud._backends.device_catalog as device_catalog
from mbed_cloud._backends.device_catalog.rest import ApiException

LOG = logging.getLogger(__name__)


class LoggingAPI(BaseAPI):
    """Logging API reference.

    Exposing functionality allowing developers to easily track and manage logs
    from devices, access, and updates.
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

        :param limit: (Optional) The number of logs to retrieve. (int)
        :param order: (Optional) The ordering direction, ascending (asc) or
            descending (desc) (str)
        :param after: (Optional) Get logs after/starting at given `device_log_id` (str)
        :param filters: (Optional) Dictionary of filters to apply.
        :return: list of device log objects
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        api = device_catalog.DefaultApi()
        return api.device_log_list(**kwargs).data

    @catch_exceptions(ApiException)
    def get_device_log(self, device_log_id):
        """Get device log with provided ID."""
        api = device_catalog.DefaultApi()
        return api.device_log_retrieve(device_log_id)
