"""
.. warning::
    CertificateEnrollment should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: CertificateEnrollment
========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`CertificateEnrollment.list`
- :meth:`CertificateEnrollment.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    certificate_enrollments = pelion_dm_sdk.foundation.certificate_enrollment()

How to import CertificateEnrollment directly:

.. code-block:: python
    
    from mbed_cloud.foundation import CertificateEnrollment

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class CertificateEnrollment(Entity):
    """Represents the `CertificateEnrollment` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "certificate_name",
        "created_at",
        "device_id",
        "enroll_result",
        "enroll_result_detail",
        "enroll_status",
        "id",
        "updated_at",
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
        certificate_name=None,
        created_at=None,
        device_id=None,
        enroll_result=None,
        enroll_result_detail=None,
        enroll_status=None,
        id=None,
        updated_at=None,
    ):
        """Creates a local `CertificateEnrollment` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param certificate_name: The certificate name.
        :type certificate_name: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param device_id: The device ID.
        :type device_id: str
        :param enroll_result: The result of certificate enrollment request.
        :type enroll_result: str
        :param enroll_result_detail: Additional information in case of failure.
        :type enroll_result_detail: str
        :param enroll_status: The status of certificate enrollment request.
        :type enroll_status: str
        :param id: (Required) The certificate enrollment ID.
        :type id: str
        :param updated_at: Update UTC time RFC3339.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._certificate_name = fields.StringField(value=certificate_name)
        self._created_at = fields.DateTimeField(value=created_at)
        self._device_id = fields.StringField(value=device_id)
        self._enroll_result = fields.StringField(value=enroll_result, enum=enums.CertificateEnrollmentEnrollResultEnum)
        self._enroll_result_detail = fields.StringField(value=enroll_result_detail)
        self._enroll_status = fields.StringField(value=enroll_status, enum=enums.CertificateEnrollmentEnrollStatusEnum)
        self._id = fields.StringField(value=id)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def certificate_name(self):
        """The certificate name.
        
        api example: 'customer.dlms'
        
        :rtype: str
        """

        return self._certificate_name.value

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2017-01-01T00:00:00Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def device_id(self):
        """The device ID.
        
        api example: '01625daa23230a580a0100bd00000000'
        
        :rtype: str
        """

        return self._device_id.value

    @property
    def enroll_result(self):
        """The result of certificate enrollment request.
        
        api example: 'success'
        
        :rtype: str
        """

        return self._enroll_result.value

    @property
    def enroll_result_detail(self):
        """Additional information in case of failure.
        
        api example: 'The device is currently processing too many certificate renewals.'
        
        :rtype: str
        """

        return self._enroll_result_detail.value

    @property
    def enroll_status(self):
        """The status of certificate enrollment request.
        
        :rtype: str
        """

        return self._enroll_status.value

    @property
    def id(self):
        """The certificate enrollment ID.

        This field must be set when updating or deleting an existing CertificateEnrollment Entity.
        
        api example: '01612df56f3b0a580a010fc700000000'
        
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
    def updated_at(self):
        """Update UTC time RFC3339.
        
        api example: '2017-01-01T00:00:00Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get certificate enrollments list.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-enrollments>`_.

        **API Filters**

        The following filters are supported by the API when listing CertificateEnrollment entities:

        +------------------+------+------+------+------+------+------+------+
        | Field            | eq   | neq  | gte  | lte  | in   | nin  | like |
        +==================+======+======+======+======+======+======+======+
        | certificate_name | Y    |      |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | created_at       |      |      | Y    | Y    |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | device_id        | Y    |      |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | enroll_result    | Y    | Y    |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | enroll_status    | Y    | Y    |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | updated_at       |      |      | Y    | Y    |      |      |      |
        +------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import CertificateEnrollment
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("certificate_name", "eq", <filter value>)
            for certificate_enrollment in CertificateEnrollment().list(filter=api_filter):
                print(certificate_enrollment.certificate_name)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of results.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000).
        :type page_size: int
        
        :param include: a comma-separated list of data fields to return.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(CertificateEnrollment)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import CertificateEnrollment
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=CertificateEnrollment._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = CertificateEnrollment._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=CertificateEnrollment,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get certificate enrollments list.
        
        :param after: The ID of the item after which to retrieve the next page.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of results.
        :type order: str
        
        :param limit: The number of results to return (2-1000).
        :type limit: int
        
        :param include: a comma-separated list of data fields to return.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.CertificateEnrollmentOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include, enum=enums.CertificateEnrollmentIncludeEnum).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/certificate-enrollments",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get a certificate enrollment by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-enrollments/{certificate-enrollment-id}>`_.
        
        :rtype: CertificateEnrollment
        """

        return self._client.call_api(
            method="get",
            path="/v3/certificate-enrollments/{certificate-enrollment-id}",
            content_type="application/json",
            path_params={"certificate-enrollment-id": self._id.to_api()},
            unpack=self,
        )
