"""Custom methods for device entities."""

from urllib.parse import urlparse
from io import StringIO


def download_report_file(self, absolute_url):
    """Download a report file.

    :param self: Instance of the entity for which this is being called.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param absolute_url: URL of the report file in Pelion Device Management.
    :type absolute_url: str

    :rtype: StringIO - contents of the downloaded file.
    """
    relative_path = urlparse(absolute_url).path
    if relative_path:
        response = self._client.call_api(method="get", path=relative_path)
        return StringIO(response.text)
    else:
        return StringIO("")


def download_full_report_file(self, foreign_key):
    """Download a full report file.

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param foreign_key: Class name.

    :rtype: StringIO - contents of the downloaded file.
    """
    return download_report_file(self, self.full_report_file)


def download_errors_report_file(self, foreign_key):
    """Download an error report file.

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.DeviceEnrollmentBulkCreate or mbed_cloud.sdk.entities.DeviceEnrollmentBulkDelete
    :param foreign_key: Class name.

    :rtype: StringIO - contents of the downloaded file.
    """
    return download_report_file(self, self.errors_report_file)
