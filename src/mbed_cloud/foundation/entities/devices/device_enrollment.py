"""
.. warning::
    DeviceEnrollment should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DeviceEnrollment
===================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DeviceEnrollment.create`
- :meth:`DeviceEnrollment.delete`
- :meth:`DeviceEnrollment.list`
- :meth:`DeviceEnrollment.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    device_enrollments = pelion_dm_sdk.foundation.device_enrollment()

How to import DeviceEnrollment directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DeviceEnrollment

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class DeviceEnrollment(Entity):
    """Represents the `DeviceEnrollment` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "account_id",
        "claimed_at",
        "created_at",
        "enrolled_device_id",
        "enrollment_identity",
        "expires_at",
        "id",
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
        claimed_at=None,
        created_at=None,
        enrolled_device_id=None,
        enrollment_identity=None,
        expires_at=None,
        id=None,
    ):
        """Creates a local `DeviceEnrollment` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: ID
        :type account_id: str
        :param claimed_at: The time the device was claimed.
        :type claimed_at: datetime
        :param created_at: The time of the enrollment identity creation.
        :type created_at: datetime
        :param enrolled_device_id: The ID of the device in the Device Directory once it is
            registered.
        :type enrolled_device_id: str
        :param enrollment_identity: (Required) Enrollment identity.
        :type enrollment_identity: str
        :param expires_at: The enrollment claim expiration time. If the device does not
            connect to Device Management before expiration, the claim is
            removed without separate notice.
        :type expires_at: datetime
        :param id: (Required) Enrollment identity.
        :type id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._claimed_at = fields.DateTimeField(value=claimed_at)
        self._created_at = fields.DateTimeField(value=created_at)
        self._enrolled_device_id = fields.StringField(value=enrolled_device_id)
        self._enrollment_identity = fields.StringField(value=enrollment_identity)
        self._expires_at = fields.DateTimeField(value=expires_at)
        self._id = fields.StringField(value=id)

    @property
    def account_id(self):
        """ID
        
        api example: '00005a4e027f0a580a01081c00000000'
        
        :rtype: str
        """

        return self._account_id.value

    @property
    def claimed_at(self):
        """The time the device was claimed.
        
        :rtype: datetime
        """

        return self._claimed_at.value

    @property
    def created_at(self):
        """The time of the enrollment identity creation.
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def enrolled_device_id(self):
        """The ID of the device in the Device Directory once it is registered.
        
        api example: '00005a4e027f0a580a01081c00000000'
        
        :rtype: str
        """

        return self._enrolled_device_id.value

    @property
    def enrollment_identity(self):
        """Enrollment identity.

        This field must be set when creating a new DeviceEnrollment Entity.
        
        api example: 'A-35:e7:72:8a:07:50:3b:3d:75:96:57:52:72:41:0d:78:cc:c6:e5:53:48:c6:65:58:5b:
            fa:af:4d:2d:73:95:c5'
        
        :rtype: str
        """

        return self._enrollment_identity.value

    @enrollment_identity.setter
    def enrollment_identity(self, value):
        """Set value of `enrollment_identity`

        :param value: value to set
        :type value: str
        """

        self._enrollment_identity.set(value)

    @property
    def expires_at(self):
        """The enrollment claim expiration time. If the device does not connect to Device
        Management before expiration, the claim is removed without separate notice.
        
        :rtype: datetime
        """

        return self._expires_at.value

    @property
    def id(self):
        """Enrollment identity.

        This field must be set when updating or deleting an existing DeviceEnrollment Entity.
        
        api example: '00005a4e027f0a580a01081c00000000'
        
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

    def create(self):
        """Create a single enrollment.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollments>`_.
        
        :rtype: DeviceEnrollment
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._enrollment_identity.value_set:
            body_params["enrollment_identity"] = self._enrollment_identity.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/device-enrollments",
            content_type="application/json",
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete an enrollment by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollments/{id}>`_.
        
        :rtype: DeviceEnrollment
        """

        return self._client.call_api(
            method="delete",
            path="/v3/device-enrollments/{id}",
            content_type="application/json",
            path_params={"id": self._id.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order="ASC", max_results=None, page_size=None, include=None):
        """Get a list of enrollments per account.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollments>`_.
        
        :param filter: Filtering when listing entities is not supported by the API for this
            entity.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: ASC or DESC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: Number of results to return (2-1000).
        :type page_size: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(DeviceEnrollment)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import DeviceEnrollment
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=DeviceEnrollment._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = DeviceEnrollment._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=DeviceEnrollment,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order="ASC", limit=None, include=None):
        """Get a list of enrollments per account.
        
        :param after: Entity ID to fetch after.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: ASC or DESC
        :type order: str
        
        :param limit: Number of results to return (2-1000).
        :type limit: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.DeviceEnrollmentOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/device-enrollments",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get details of an single enrollment by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollments/{id}>`_.
        
        :rtype: DeviceEnrollment
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-enrollments/{id}",
            content_type="application/json",
            path_params={"id": self._id.to_api()},
            unpack=self,
        )
