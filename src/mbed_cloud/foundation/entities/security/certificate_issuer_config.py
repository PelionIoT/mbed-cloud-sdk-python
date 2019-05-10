"""
.. warning::
    CertificateIssuerConfig should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: CertificateIssuerConfig
==========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`CertificateIssuerConfig.create`
- :meth:`CertificateIssuerConfig.delete`
- :meth:`CertificateIssuerConfig.get_default`
- :meth:`CertificateIssuerConfig.list`
- :meth:`CertificateIssuerConfig.read`
- :meth:`CertificateIssuerConfig.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    certificate_issuer_configs = pelion_dm_sdk.foundation.certificate_issuer_config()

How to import CertificateIssuerConfig directly:

.. code-block:: python
    
    from mbed_cloud.foundation import CertificateIssuerConfig

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class CertificateIssuerConfig(Entity):
    """Represents the `CertificateIssuerConfig` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["certificate_issuer_id", "created_at", "id", "reference", "updated_at"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self, _client=None, certificate_issuer_id=None, created_at=None, id=None, reference=None, updated_at=None
    ):
        """Creates a local `CertificateIssuerConfig` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param certificate_issuer_id: (Required) The ID of the certificate issuer.
            Null if Device Management
            internal HSM is used.
        :type certificate_issuer_id: str
        :param created_at: Created UTC time RFC3339.
        :type created_at: datetime
        :param id: (Required) The ID of the certificate issuer configuration.
        :type id: str
        :param reference: (Required) The certificate name to which the certificate issuer configuration
            applies.
        :type reference: str
        :param updated_at: Updated UTC time RFC3339.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._certificate_issuer_id = fields.StringField(value=certificate_issuer_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._id = fields.StringField(value=id)
        self._reference = fields.StringField(value=reference)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def certificate_issuer_id(self):
        """The ID of the certificate issuer.
        Null if Device Management internal HSM is
        used.

        This field must be set when creating a new CertificateIssuerConfig Entity.
        
        api example: '01648415a2a30242ac18000500000000'
        
        :rtype: str
        """

        return self._certificate_issuer_id.value

    @certificate_issuer_id.setter
    def certificate_issuer_id(self, value):
        """Set value of `certificate_issuer_id`

        :param value: value to set
        :type value: str
        """

        self._certificate_issuer_id.set(value)

    @property
    def created_at(self):
        """Created UTC time RFC3339.
        
        api example: '2017-01-01T00:00:00Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def id(self):
        """The ID of the certificate issuer configuration.

        This field must be set when updating or deleting an existing CertificateIssuerConfig Entity.
        
        api example: '01648415a2a30242ac18000500000000'
        
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
    def reference(self):
        """The certificate name to which the certificate issuer configuration applies.

        This field must be set when creating a new CertificateIssuerConfig Entity.
        
        api example: 'customer.dlms'
        
        :rtype: str
        """

        return self._reference.value

    @reference.setter
    def reference(self, value):
        """Set value of `reference`

        :param value: value to set
        :type value: str
        """

        self._reference.set(value)

    @property
    def updated_at(self):
        """Updated UTC time RFC3339.
        
        api example: '2017-02-01T00:00:00Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def create(self):
        """Create certificate issuer configuration.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-issuer-configurations>`_.
        
        :rtype: CertificateIssuerConfig
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._certificate_issuer_id.value_set:
            body_params["certificate_issuer_id"] = self._certificate_issuer_id.to_api()
        if self._reference.value_set:
            body_params["reference"] = self._reference.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/certificate-issuer-configurations",
            content_type="application/json",
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete certificate issuer configuration.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}>`_.
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="delete",
            path="/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}",
            content_type="application/json",
            path_params={"certificate-issuer-configuration-id": self._id.to_api()},
            unpack=self,
        )

    def get_default(self):
        """Get certificate issuer configuration.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-issuer-configurations/lwm2m>`_.
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="get",
            path="/v3/certificate-issuer-configurations/lwm2m",
            content_type="application/json",
            unpack=self,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get certificate issuer configurations.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-issuer-configurations>`_.

        **API Filters**

        The following filters are supported by the API when listing CertificateIssuerConfig entities:

        +-----------+------+------+------+------+------+------+------+
        | Field     | eq   | neq  | gte  | lte  | in   | nin  | like |
        +===========+======+======+======+======+======+======+======+
        | reference | Y    |      |      |      |      |      |      |
        +-----------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import CertificateIssuerConfig
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("reference", "eq", <filter value>)
            for certificate_issuer_config in CertificateIssuerConfig().list(filter=api_filter):
                print(certificate_issuer_config.reference)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(CertificateIssuerConfig)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import CertificateIssuerConfig
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=CertificateIssuerConfig._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = CertificateIssuerConfig._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=CertificateIssuerConfig,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get certificate issuer configurations.
        
        :param after: The ID of The item after which to retrieve the next page.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/certificate-issuer-configurations",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get certificate issuer configuration.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}>`_.
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="get",
            path="/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}",
            content_type="application/json",
            path_params={"certificate-issuer-configuration-id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Update certificate issuer configuration.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}>`_.
        
        :rtype: CertificateIssuerConfig
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._certificate_issuer_id.value_set:
            body_params["certificate_issuer_id"] = self._certificate_issuer_id.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}",
            content_type="application/json",
            body_params=body_params,
            path_params={"certificate-issuer-configuration-id": self._id.to_api()},
            unpack=self,
        )
