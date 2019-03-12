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


class CertificateIssuerConfig(Entity):
    """Represents the `CertificateIssuerConfig` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "certificate_issuer_id",
        "certificate_reference",
        "created_at",
        "id",
        "updated_at",
    ]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {"reference": "certificate_reference"}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {"certificate_reference": "reference"}

    def __init__(
        self,
        _client=None,
        certificate_issuer_id=None,
        certificate_reference=None,
        created_at=None,
        id=None,
        updated_at=None,
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
        :param certificate_reference: (Required) The certificate name to which the certificate issuer configuration
            applies.
        :type certificate_reference: str
        :param created_at: Created UTC time RFC3339.
        :type created_at: datetime
        :param id: (Required) The ID of the certificate issuer configuration.
        :type id: str
        :param updated_at: Updated UTC time RFC3339.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._certificate_issuer_id = fields.StringField(value=certificate_issuer_id)
        self._certificate_reference = fields.StringField(value=certificate_reference)
        self._created_at = fields.DateTimeField(value=created_at)
        self._id = fields.StringField(value=id)
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
    def certificate_reference(self):
        """The certificate name to which the certificate issuer configuration applies.

        This field must be set when creating a new CertificateIssuerConfig Entity.
        
        api example: 'customer.dlms'
        
        :rtype: str
        """

        return self._certificate_reference.value

    @certificate_reference.setter
    def certificate_reference(self, value):
        """Set value of `certificate_reference`

        :param value: value to set
        :type value: str
        """

        self._certificate_reference.set(value)

    @property
    def created_at(self):
        """Created UTC time RFC3339.
        
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
    def updated_at(self):
        """Updated UTC time RFC3339.
        
        api example: '2017-02-01T00:00:00Z'
        
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

    def create(self):
        """Create certificate issuer configuration.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuer-configurations
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="post",
            path="/v3/certificate-issuer-configurations",
            body_params={
                "certificate_issuer_id": self._certificate_issuer_id.to_api(),
                "reference": self._certificate_reference.to_api(),
            },
            unpack=self,
        )

    def delete(self):
        """Delete certificate issuer configuration.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="delete",
            path="/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}",
            path_params={"certificate-issuer-configuration-id": self._id.to_api()},
            unpack=self,
        )

    def get_default(self):
        """Get certificate issuer configuration.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuer-configurations/lwm2m
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="get", path="/v3/certificate-issuer-configurations/lwm2m", unpack=self
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get certificate issuer configurations.

        **API Filters**

        The following filters are supported by the API when listing CertificateIssuerConfig entities:

        +-----------------------+------+------+------+------+------+------+------+
        | Field                 | eq   | neq  | gte  | lte  | in   | nin  | like |
        +=======================+======+======+======+======+======+======+======+
        | certificate_reference | ✔    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import CertificateIssuerConfig
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("certificate_reference", "eq", <filter value>)
            for certificate_issuer_config in CertificateIssuerConfig().list(filter=api_filter):
                print(certificate_issuer_config.certificate_reference)
        
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
            filter = ApiFilter(
                filter_definition=filter,
                field_renames=CertificateIssuerConfig._renames_to_api,
            )
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
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get certificate issuer configuration.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="get",
            path="/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}",
            path_params={"certificate-issuer-configuration-id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Update certificate issuer configuration.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}
        
        :rtype: CertificateIssuerConfig
        """

        return self._client.call_api(
            method="put",
            path="/v3/certificate-issuer-configurations/{certificate-issuer-configuration-id}",
            body_params={"certificate_issuer_id": self._certificate_issuer_id.to_api()},
            path_params={"certificate-issuer-configuration-id": self._id.to_api()},
            unpack=self,
        )
