"""
Entity module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class CertificateEnrollment(Entity):
    """Represents the `CertificateEnrollment` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "certificate_name",
        "created_at",
        "device_id",
        "enroll_result",
        "enroll_status",
        "id",
        "updated_at",
    ]

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
        :param enroll_result: 
        :type enroll_result: str
        :param enroll_status: 
        :type enroll_status: str
        :param id: (Required) The ID of the certificate enrollment.
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
        self._enroll_result = fields.StringField(
            value=enroll_result, enum=enums.CertificateEnrollmentEnrollResultEnum
        )
        self._enroll_status = fields.StringField(
            value=enroll_status, enum=enums.CertificateEnrollmentEnrollStatusEnum
        )
        self._id = fields.StringField(value=id)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def certificate_name(self):
        """The certificate name.
        
        api example: 'customer.dlms'
        
        :rtype: str
        """

        return self._certificate_name.value

    @certificate_name.setter
    def certificate_name(self, value):
        """Set value of `certificate_name`

        :param value: value to set
        :type value: str
        """

        self._certificate_name.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2017-01-01T00:00:00Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """Set value of `created_at`

        :param value: value to set
        :type value: datetime
        """

        self._created_at.set(value)

    @property
    def device_id(self):
        """The device ID.
        
        api example: '01625daa23230a580a0100bd00000000'
        
        :rtype: str
        """

        return self._device_id.value

    @device_id.setter
    def device_id(self, value):
        """Set value of `device_id`

        :param value: value to set
        :type value: str
        """

        self._device_id.set(value)

    @property
    def enroll_result(self):
        """
        
        :rtype: str
        """

        return self._enroll_result.value

    @enroll_result.setter
    def enroll_result(self, value):
        """Set value of `enroll_result`

        :param value: value to set
        :type value: str
        """

        self._enroll_result.set(value)

    @property
    def enroll_status(self):
        """
        
        :rtype: str
        """

        return self._enroll_status.value

    @enroll_status.setter
    def enroll_status(self, value):
        """Set value of `enroll_status`

        :param value: value to set
        :type value: str
        """

        self._enroll_status.set(value)

    @property
    def id(self):
        """The ID of the certificate enrollment.

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

    @updated_at.setter
    def updated_at(self, value):
        """Set value of `updated_at`

        :param value: value to set
        :type value: datetime
        """

        self._updated_at.set(value)

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get certificate enrollments list.

        **API Filters**

        The following filters are supported by the API when listing CertificateEnrollment entities:

        +------------------+------+------+------+------+------+------+------+
        | Field            | eq   | neq  | gte  | lte  | in   | nin  | like |
        +==================+======+======+======+======+======+======+======+
        | certificate_name | *    |      |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | created_at       |      |      | *    | *    |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | device_id        | *    |      |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | enroll_result    | *    | *    |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | enroll_status    | *    | *    |      |      |      |      |      |
        +------------------+------+------+------+------+------+------+------+
        | updated_at       |      |      | *    | *    |      |      |      |
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
        
        :param page_size: The number of results to be returned. Between 2 and 1000, inclusive.
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
            filter = ApiFilter(
                filter_definition=filter,
                field_renames=CertificateEnrollment._renames_to_api,
            )
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
        
        :param limit: The number of results to be returned. Between 2 and 1000, inclusive.
        :type limit: int
        
        :param include: a comma-separated list of data fields to return.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(
            order, enum=enums.CertificateEnrollmentOrderEnum
        ).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(
            include, enum=enums.CertificateEnrollmentIncludeEnum
        ).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/certificate-enrollments",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get a certificate enrollment by ID.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-enrollments/{certificate-enrollment-id}
        
        :rtype: CertificateEnrollment
        """

        return self._client.call_api(
            method="get",
            path="/v3/certificate-enrollments/{certificate-enrollment-id}",
            path_params={"certificate-enrollment-id": self._id.to_api()},
            unpack=self,
        )
