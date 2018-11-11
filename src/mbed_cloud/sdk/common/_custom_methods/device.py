"""Custom methods for device entities."""

from urllib.parse import urlparse
from io import StringIO


def get_full_report_file_setter(self, field, value):
    """Set the full report file - No Implemented

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param field: Name of the field which is this is a setter method.
    :type field: str
    :param value: Set to True if a developer certificate
    :type value: bool

    :raise NotImplementedError - It is not possible to upload a report file
    """

    raise NotImplementedError


def get_errors_report_file_setter(self, field, value):
    """Set the errors report file - No Implemented

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param field: Name of the field which is this is a setter method.
    :type field: str
    :param value: Set to True if a developer certificate
    :type value: bool

    :raise NotImplementedError - It is not possible to upload a report file
    """

    raise NotImplementedError


def download_report_file(self, file_url):
    """Download a report file.

    :param self: Instance of the entity for which this is being called.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param file_url: URL of the report file in Pelion Device Management.
    :type file_url: str

    :rtype: StringIO - contents of the downloaded file.
    """
    print(file_url, urlparse(file_url).path)
    response = self._client.call_api(method="get", path=urlparse(file_url).path)
    return StringIO(response.text)


def get_full_report_file_getter(self, field):
    """Download a full report file.

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param field: Name of the field which is this is a setter method.
    :type field: str

    :rtype: StringIO - contents of the downloaded file.
    """
    return download_report_file(self, self.full_report_file)


def get_errors_report_file_getter(self, field):
    """Download an error report file.

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param field: Name of the field which is this is a setter method.
    :type field: str

    :rtype: StringIO - contents of the downloaded file.
    """
    return download_report_file(self, self.errors_report_file)
