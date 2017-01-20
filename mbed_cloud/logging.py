"""API reference for logging components in mbed Cloud"""
from __future__ import absolute_import

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

import mbed_cloud._backends.device_catalog as device_catalog
from mbed_cloud._backends.device_catalog.models import DeviceLogSerializerData
from mbed_cloud._backends.device_catalog.rest import ApiException


class LoggingAPI(BaseAPI):
    """Logging API reference.

    Exposing functionality allowing developers to easily track and manage logs
    from devices, access, and updates.
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(LoggingAPI, self).__init__(params)
        self.dc = self._init_api(device_catalog)

    @catch_exceptions(ApiException)
    def list_device_logs(self, **kwargs):
        """List all device logs.

        :param int limit: (Optional) The number of logs to retrieve. (int)
        :param str order: (Optional) The ordering direction, ascending (asc) or
            descending (desc) (str)
        :param str after: (Optional) Get logs after/starting at given `device_log_id` (str)
        :param dict filters: (Optional) Dictionary of filters to apply.
        :return: list of :py:class:`DeviceLog` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        api = self.dc.DefaultApi()
        return PaginatedResponse(api.device_log_list, lwrap_type=DeviceLog, **kwargs)

    @catch_exceptions(ApiException)
    def get_device_log(self, device_log_id):
        """Get device log with provided ID.

        :rtype: DeviceLog
        """
        api = self.dc.DefaultApi()
        return DeviceLog(api.device_log_retrieve(device_log_id))


class DeviceLog(DeviceLogSerializerData):
    """Describes device log object."""

    def __init__(self, device_log_obj):
        """Override __init__ and allow passing in backend object."""
        super(DeviceLog, self).__init__(**device_log_obj.to_dict())
