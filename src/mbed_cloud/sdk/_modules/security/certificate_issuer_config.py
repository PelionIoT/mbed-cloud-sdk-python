"""
Entity module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


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

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {"reference": "certificate_reference"}

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
        
        api example: '01648415a2a30242ac18000500000000'
        
        :rtype: str
        """

        return self._certificate_issuer_id.value

    @certificate_issuer_id.setter
    def certificate_issuer_id(self, value):
        """Set value of `certificate_issuer_id`

        This field must be set when creating a new CertificateIssuerConfig Entity.

        :param value: value to set
        :type value: str
        """

        self._certificate_issuer_id.set(value)

    @property
    def certificate_reference(self):
        """The certificate name to which the certificate issuer configuration applies.
        
        api example: 'customer.dlms'
        
        :rtype: str
        """

        return self._certificate_reference.value

    @certificate_reference.setter
    def certificate_reference(self, value):
        """Set value of `certificate_reference`

        This field must be set when creating a new CertificateIssuerConfig Entity.

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
        
        api example: '01648415a2a30242ac18000500000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        This field must be set when updating or deleting an existing CertificateIssuerConfig Entity.

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
            method="get",
            path="/v3/certificate-issuer-configurations/lwm2m",
            unpack=self,
        )

    def list(self, include=None, max_results=None, page_size=None, order=None):
        """Get certificate issuer configurations.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuer-configurations
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`
        :type include: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
            
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(CertificateIssuerConfig)
        """

        from mbed_cloud.sdk.common._custom_methods import paginate
        from mbed_cloud.sdk.entities import CertificateIssuerConfig

        return paginate(
            self=self,
            foreign_key=CertificateIssuerConfig,
            include=include,
            max_results=max_results,
            page_size=page_size,
            order=order,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, include=None, limit=None, order=None):
        """Get certificate issuer configurations.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/certificate-issuer-configurations
        
        :param after: The ID of The item after which to retrieve the next page.
        :type after: str
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`
        :type include: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        return self._client.call_api(
            method="get",
            path="/v3/certificate-issuer-configurations",
            query_params={
                "after": fields.StringField(after).to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": fields.IntegerField(limit).to_api(),
                "order": fields.StringField(order).to_api(),
            },
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
