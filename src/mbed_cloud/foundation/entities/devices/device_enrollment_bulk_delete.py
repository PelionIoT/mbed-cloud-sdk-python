"""
.. warning::
    DeviceEnrollmentBulkDelete should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DeviceEnrollmentBulkDelete
=============================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DeviceEnrollmentBulkDelete.delete`
- :meth:`DeviceEnrollmentBulkDelete.download_errors_report_file`
- :meth:`DeviceEnrollmentBulkDelete.download_full_report_file`
- :meth:`DeviceEnrollmentBulkDelete.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    device_enrollment_bulk_deletes = pelion_dm_sdk.foundation.device_enrollment_bulk_delete()

How to import DeviceEnrollmentBulkDelete directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DeviceEnrollmentBulkDelete

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super
import six

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class DeviceEnrollmentBulkDelete(Entity):
    """Represents the `DeviceEnrollmentBulkDelete` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "account_id",
        "completed_at",
        "created_at",
        "errors_count",
        "errors_report_file",
        "full_report_file",
        "id",
        "processed_count",
        "status",
        "total_count",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        completed_at=None,
        created_at=None,
        errors_count=None,
        errors_report_file=None,
        full_report_file=None,
        id=None,
        processed_count=None,
        status=None,
        total_count=None,
    ):
        """Creates a local `DeviceEnrollmentBulkDelete` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: ID
        :type account_id: str
        :param completed_at: The time the bulk creation task was completed.
            Null when creating
            bulk upload or delete.
        :type completed_at: datetime
        :param created_at: The time of receiving the bulk creation task.
        :type created_at: datetime
        :param errors_count: The number of enrollment identities with failed processing.
        :type errors_count: int
        :param errors_report_file: Link to error report file.
            Null when creating bulk upload or
            delete.
        :type errors_report_file: str
        :param full_report_file: Link to full report file.
            Null when creating bulk upload or
            delete.
        :type full_report_file: str
        :param id: (Required) Bulk ID
        :type id: str
        :param processed_count: The number of enrollment identities processed until now.
        :type processed_count: int
        :param status: The state of the process is 'new' at the time of creation. If
            creation is still in progress, the state shows as 'processing'.
            When the request is fully processed, the state changes to
            'completed'.
        :type status: str
        :param total_count: Total number of enrollment identities found in the input CSV.
        :type total_count: int
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._completed_at = fields.DateTimeField(value=completed_at)
        self._created_at = fields.DateTimeField(value=created_at)
        self._errors_count = fields.IntegerField(value=errors_count)
        self._errors_report_file = fields.StringField(value=errors_report_file)
        self._full_report_file = fields.StringField(value=full_report_file)
        self._id = fields.StringField(value=id)
        self._processed_count = fields.IntegerField(value=processed_count)
        self._status = fields.StringField(value=status, enum=enums.DeviceEnrollmentBulkDeleteStatusEnum)
        self._total_count = fields.IntegerField(value=total_count)

    @property
    def account_id(self):
        """ID
        
        api example: '00005a4e027f0a580a01081c00000000'
        
        :rtype: str
        """

        return self._account_id.value

    @property
    def completed_at(self):
        """The time the bulk creation task was completed.
        Null when creating bulk upload
        or delete.
        
        :rtype: datetime
        """

        return self._completed_at.value

    @property
    def created_at(self):
        """The time of receiving the bulk creation task.
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def errors_count(self):
        """The number of enrollment identities with failed processing.
        
        :rtype: int
        """

        return self._errors_count.value

    @property
    def errors_report_file(self):
        """Link to error report file.
        Null when creating bulk upload or delete.
        
        api example: 'https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-
            uploads/2d238a89038b4ddb84699dd36a901063/errors_report.csv'
        
        :rtype: str
        """

        return self._errors_report_file.value

    @property
    def full_report_file(self):
        """Link to full report file.
        Null when creating bulk upload or delete.
        
        api example: 'https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-
            uploads/2d238a89038b4ddb84699dd36a901063/full_report.csv'
        
        :rtype: str
        """

        return self._full_report_file.value

    @property
    def id(self):
        """Bulk ID

        This field must be set when updating or deleting an existing DeviceEnrollmentBulkDelete Entity.
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        self._id.set(value)

    @property
    def processed_count(self):
        """The number of enrollment identities processed until now.
        
        :rtype: int
        """

        return self._processed_count.value

    @property
    def status(self):
        """The state of the process is 'new' at the time of creation. If creation is
        still in progress, the state shows as 'processing'. When the request is fully
        processed, the state changes to 'completed'.
        
        api example: 'new'
        
        :rtype: str
        """

        return self._status.value

    @property
    def total_count(self):
        """Total number of enrollment identities found in the input CSV.
        
        api example: 10
        
        :rtype: int
        """

        return self._total_count.value

    def delete(self, enrollment_identities):
        """Bulk delete.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollments-bulk-deletes>`_.
        
        :param enrollment_identities: The `CSV` file containing the enrollment IDs. The maximum file size is
            10MB. Files can be provided as a file object or a path to an existing
            file on disk.
        :type enrollment_identities: file
        
        :rtype: DeviceEnrollmentBulkDelete
        """

        auto_close_enrollment_identities = False

        # If enrollment_identities is a string rather than a file, treat as a path and attempt to open the file.
        if enrollment_identities and isinstance(enrollment_identities, six.string_types):
            enrollment_identities = open(enrollment_identities, "rb")
            auto_close_enrollment_identities = True

        try:

            return self._client.call_api(
                method="post",
                path="/v3/device-enrollments-bulk-deletes",
                stream_params={
                    "enrollment_identities": ("enrollment_identities.csv", enrollment_identities, "text/csv")
                },
                unpack=self,
            )
        finally:
            # Calling the API may result in an exception being raised so close the files in a finally statement.
            # Note: Files are only closed if they were opened by the method.
            if auto_close_enrollment_identities:
                enrollment_identities.close()

    def download_errors_report_file(self):
        """Download the error report file for the bulk enrollment deletion.
        
        :rtype: file
        """

        from mbed_cloud.foundation._custom_methods import download_errors_report_file

        return download_errors_report_file(self=self, foreign_key=self.__class__)

    def download_full_report_file(self):
        """Download the full report file for the bulk enrollment deletion.
        
        :rtype: file
        """

        from mbed_cloud.foundation._custom_methods import download_full_report_file

        return download_full_report_file(self=self, foreign_key=self.__class__)

    def read(self):
        """Get bulk delete entity.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollments-bulk-deletes/{id}>`_.
        
        :rtype: DeviceEnrollmentBulkDelete
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-enrollments-bulk-deletes/{id}",
            content_type="application/json",
            path_params={"id": self._id.to_api()},
            unpack=self,
        )
