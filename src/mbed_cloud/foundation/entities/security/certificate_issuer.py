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


class CertificateIssuer(Entity):
    """Represents the `CertificateIssuer` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "created_at",
        "description",
        "id",
        "issuer_attributes",
        "issuer_type",
        "name",
    ]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        created_at=None,
        description=None,
        id=None,
        issuer_attributes=None,
        issuer_type=None,
        name=None,
    ):
        """Creates a local `CertificateIssuer` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: General description for the certificate issuer.
        :type description: str
        :param id: (Required) The ID of the certificate issuer.
        :type id: str
        :param issuer_attributes: General attributes for connecting the certificate issuer.
            When the
            issuer_type is GLOBAL_SIGN, the value shall be empty.
            When the
            issuer_type is CFSSL_AUTH, see definition of CfsslAttributes.
        :type issuer_attributes: dict
        :param issuer_type: (Required) The type of the certificate issuer.
            - GLOBAL_SIGN:
              Certificates
            are issued by GlobalSign service. The users must provide their own
            GlobalSign account credentials.
            - CFSSL_AUTH:
              Certificates are
            issued by CFSSL authenticated signing service.
              The users must
            provide their own CFSSL host_url and credentials.
        :type issuer_type: str
        :param name: (Required) Certificate issuer name, unique per account.
        :type name: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._created_at = fields.DateTimeField(value=created_at)
        self._description = fields.StringField(value=description)
        self._id = fields.StringField(value=id)
        self._issuer_attributes = fields.DictField(value=issuer_attributes)
        self._issuer_type = fields.StringField(
            value=issuer_type, enum=enums.CertificateIssuerTypeEnum
        )
        self._name = fields.StringField(value=name)

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
    def description(self):
        """General description for the certificate issuer.
        
        api example: 'GlobalSign sample issuer'
        
        :rtype: str
        """

        return self._description.value

    @description.setter
    def description(self, value):
        """Set value of `description`

        :param value: value to set
        :type value: str
        """

        self._description.set(value)

    @property
    def id(self):
        """The ID of the certificate issuer.

        This field must be set when updating or deleting an existing CertificateIssuer Entity.
        
        api example: '01234567890ABCDEF01234567890ABCDEF'
        
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
    def issuer_attributes(self):
        """General attributes for connecting the certificate issuer.
        When the issuer_type
        is GLOBAL_SIGN, the value shall be empty.
        When the issuer_type is CFSSL_AUTH,
        see definition of CfsslAttributes.
        
        :rtype: dict
        """

        return self._issuer_attributes.value

    @issuer_attributes.setter
    def issuer_attributes(self, value):
        """Set value of `issuer_attributes`

        :param value: value to set
        :type value: dict
        """

        self._issuer_attributes.set(value)

    @property
    def issuer_type(self):
        """The type of the certificate issuer.
        - GLOBAL_SIGN:
          Certificates are issued
        by GlobalSign service. The users must provide their own GlobalSign account
        credentials.
        - CFSSL_AUTH:
          Certificates are issued by CFSSL authenticated
        signing service.
          The users must provide their own CFSSL host_url and
        credentials.

        This field must be set when creating a new CertificateIssuer Entity.
        
        api example: 'GLOBAL_SIGN'
        
        :rtype: str
        """

        return self._issuer_type.value

    @issuer_type.setter
    def issuer_type(self, value):
        """Set value of `issuer_type`

        :param value: value to set
        :type value: str
        """

        self._issuer_type.set(value)

    @property
    def name(self):
        """Certificate issuer name, unique per account.

        This field must be set when creating a new CertificateIssuer Entity.
        
        api example: 'GS Issuer'
        
        :rtype: str
        """

        return self._name.value

    @name.setter
    def name(self, value):
        """Set value of `name`

        :param value: value to set
        :type value: str
        """

        self._name.set(value)

    def create(self, issuer_credentials=None):
        """Create certificate issuer.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuers
        
        :param issuer_credentials: The credentials required for connecting to the certificate issuer.
            When the issuer_type is GLOBAL_SIGN, see definition of
            GlobalSignCredentials.
            When the issuer_type is CFSSL_AUTH, see
            definition of CfsslAuthCredentials.
        :type issuer_credentials: dict
        
        :rtype: CertificateIssuer
        """

        return self._client.call_api(
            method="post",
            path="/v3/certificate-issuers",
            body_params={
                "description": self._description.to_api(),
                "issuer_attributes": self._issuer_attributes.to_api(),
                "issuer_credentials": fields.DictField(issuer_credentials).to_api(),
                "issuer_type": self._issuer_type.to_api(),
                "name": self._name.to_api(),
            },
            unpack=self,
        )

    def delete(self):
        """Delete certificate issuer.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuers/{certificate-issuer-id}
        
        :rtype: CertificateIssuer
        """

        return self._client.call_api(
            method="delete",
            path="/v3/certificate-issuers/{certificate-issuer-id}",
            path_params={"certificate-issuer-id": self._id.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get certificate issuers list.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuers
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.ApiFilter
        
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
        :rtype: mbed_cloud.pagination.PaginatedResponse(CertificateIssuer)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import CertificateIssuer
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(
                filter_definition=filter, field_renames=CertificateIssuer._renames_to_api
            )
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = CertificateIssuer._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=CertificateIssuer,
            include=include,
            max_results=max_results,
            page_size=page_size,
            order=order,
            filter=filter,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get certificate issuers list.
        
        :param after: The ID of The item after which to retrieve the next page.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.ApiFilter
        
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
            path="/v3/certificate-issuers",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get certificate issuer by ID.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuers/{certificate-issuer-id}
        
        :rtype: CertificateIssuer
        """

        return self._client.call_api(
            method="get",
            path="/v3/certificate-issuers/{certificate-issuer-id}",
            path_params={"certificate-issuer-id": self._id.to_api()},
            unpack=self,
        )

    def update(self, issuer_credentials=None):
        """Update certificate issuer.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuers/{certificate-issuer-id}
        
        :param issuer_credentials: The credentials required for connecting to the certificate issuer.
            When the issuer_type is GLOBAL_SIGN, see definition of
            GlobalSignCredentials.
            When the issuer_type is CFSSL_AUTH, see
            definition of CfsslAuthCredentials.
        :type issuer_credentials: dict
        
        :rtype: CertificateIssuer
        """

        return self._client.call_api(
            method="put",
            path="/v3/certificate-issuers/{certificate-issuer-id}",
            body_params={
                "description": self._description.to_api(),
                "issuer_attributes": self._issuer_attributes.to_api(),
                "issuer_credentials": fields.DictField(issuer_credentials).to_api(),
                "name": self._name.to_api(),
            },
            path_params={"certificate-issuer-id": self._id.to_api()},
            unpack=self,
        )

    def verify(self):
        """Verify certificate issuer.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuers/{certificate-issuer-id}/verify
        
        :rtype: VerificationResponse
        """

        from mbed_cloud.foundation import VerificationResponse

        return self._client.call_api(
            method="post",
            path="/v3/certificate-issuers/{certificate-issuer-id}/verify",
            path_params={"certificate-issuer-id": self._id.to_api()},
            unpack=VerificationResponse,
        )
