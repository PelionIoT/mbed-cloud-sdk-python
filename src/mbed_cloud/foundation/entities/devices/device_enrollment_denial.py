"""
.. warning::
    DeviceEnrollmentDenial should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DeviceEnrollmentDenial
=========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DeviceEnrollmentDenial.list`
- :meth:`DeviceEnrollmentDenial.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    device_enrollment_denials = pelion_dm_sdk.foundation.device_enrollment_denial()

How to import DeviceEnrollmentDenial directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DeviceEnrollmentDenial

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class DeviceEnrollmentDenial(Entity):
    """Represents the `DeviceEnrollmentDenial` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["account_id", "created_at", "endpoint_name", "id", "trusted_certificate_id"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self, _client=None, account_id=None, created_at=None, endpoint_name=None, id=None, trusted_certificate_id=None
    ):
        """Creates a local `DeviceEnrollmentDenial` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: account id
        :type account_id: str
        :param created_at: date on which the failed bootstrap was attempted on
        :type created_at: datetime
        :param endpoint_name: endpoint name
        :type endpoint_name: str
        :param id: id of the recorded failed bootstrap attempt
        :type id: str
        :param trusted_certificate_id: Trusted certificate id
        :type trusted_certificate_id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._endpoint_name = fields.StringField(value=endpoint_name)
        self._id = fields.StringField(value=id)
        self._trusted_certificate_id = fields.StringField(value=trusted_certificate_id)

    @property
    def account_id(self):
        """account id
        
        api example: '00005a4e027f0a580a01081c00000000'
        
        :rtype: str
        """

        return self._account_id.value

    @property
    def created_at(self):
        """date on which the failed bootstrap was attempted on
        
        api example: '2000-01-23T04:56:07.000+00:00'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def endpoint_name(self):
        """endpoint name
        
        api example: 'Endpoint_1234'
        
        :rtype: str
        """

        return self._endpoint_name.value

    @property
    def id(self):
        """id of the recorded failed bootstrap attempt
        
        api example: '00005a4e027f0a580a04567c00000000'
        
        :rtype: str
        """

        return self._id.value

    @property
    def trusted_certificate_id(self):
        """Trusted certificate id
        
        api example: '00005a4e027f0a580a01081c00000000'
        
        :rtype: str
        """

        return self._trusted_certificate_id.value

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Return list of devices which were denied to bootstrap due to being subjected to blacklisting.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollment-denials>`_.

        **API Filters**

        The following filters are supported by the API when listing DeviceEnrollmentDenial entities:

        +------------------------+------+------+------+------+------+------+------+
        | Field                  | eq   | neq  | gte  | lte  | in   | nin  | like |
        +========================+======+======+======+======+======+======+======+
        | endpoint_name          | Y    |      |      |      |      |      |      |
        +------------------------+------+------+------+------+------+------+------+
        | trusted_certificate_id | Y    |      |      |      |      |      |      |
        +------------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import DeviceEnrollmentDenial
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("endpoint_name", "eq", <filter value>)
            for device_enrollment_denial in DeviceEnrollmentDenial().list(filter=api_filter):
                print(device_enrollment_denial.endpoint_name)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Optional parameter for pagination.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: Optional parameter for pagination.
        :type page_size: int
        
        :param include: Comma separated additional data to return.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(DeviceEnrollmentDenial)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import DeviceEnrollmentDenial
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=DeviceEnrollmentDenial._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = DeviceEnrollmentDenial._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=DeviceEnrollmentDenial,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """Return list of devices which were denied to bootstrap due to being subjected to blacklisting.
        
        :param after: Optional parameter for pagination. Denied device ID.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Optional parameter for pagination.
        :type order: str
        
        :param limit: Optional parameter for pagination.
        :type limit: int
        
        :param include: Not supported by the API.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.DeviceEnrollmentDenialOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/device-enrollment-denials",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self, device_enrollment_denial_id):
        """Query for a single device by ID

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/device-enrollment-denials/{device_enrollment_denial_id}>`_.
        
        :param device_enrollment_denial_id: id of the recorded failed bootstrap attempt
        :type device_enrollment_denial_id: str
        
        :rtype: DeviceEnrollmentDenial
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-enrollment-denials/{device_enrollment_denial_id}",
            content_type="application/json",
            path_params={"device_enrollment_denial_id": fields.StringField(device_enrollment_denial_id).to_api()},
            unpack=self,
        )
