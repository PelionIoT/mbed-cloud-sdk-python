"""
.. warning::
    SAML2Request should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SAML2Request
===============================

The SAML2Request entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    saml2requests = pelion_dm_sdk.foundation.saml2request()

How to import SAML2Request directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SAML2Request

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SAML2Request(Entity):
    """Represents the `SAML2Request` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "entity_descriptor",
        "idp_entity_id",
        "idp_x509_certs",
        "slo_endpoint",
        "sp_entity_id",
        "sso_endpoint",
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
        entity_descriptor=None,
        idp_entity_id=None,
        idp_x509_certs=None,
        slo_endpoint=None,
        sp_entity_id=None,
        sso_endpoint=None,
    ):
        """Creates a local `SAML2Request` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param entity_descriptor: Contains an entity descriptor document for the identity provider.
            Can be used as an alternative method to provide the identity
            provider's attributes.
        :type entity_descriptor: bytes
        :param idp_entity_id: Entity ID of the identity provider.
        :type idp_entity_id: str
        :param idp_x509_certs: List of public X509 certificates of the identity provider.
            Certificates must be in PEM format.
        :type idp_x509_certs: list
        :param slo_endpoint: URL of the identity provider's SLO endpoint.
        :type slo_endpoint: str
        :param sp_entity_id: Entity ID of the service provider. We recommend that you leave it
            empty and let the system generate it.
        :type sp_entity_id: str
        :param sso_endpoint: URL of the identity provider's SSO endpoint.
        :type sso_endpoint: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._entity_descriptor = fields.BinaryField(value=entity_descriptor)
        self._idp_entity_id = fields.StringField(value=idp_entity_id)
        self._idp_x509_certs = fields.ListField(value=idp_x509_certs)
        self._slo_endpoint = fields.StringField(value=slo_endpoint)
        self._sp_entity_id = fields.StringField(value=sp_entity_id)
        self._sso_endpoint = fields.StringField(value=sso_endpoint)

    @property
    def entity_descriptor(self):
        """Contains an entity descriptor document for the identity provider. Can be used
        as an alternative method to provide the identity provider's attributes.
        
        :rtype: bytes
        """

        return self._entity_descriptor.value

    @property
    def idp_entity_id(self):
        """Entity ID of the identity provider.
        
        :rtype: str
        """

        return self._idp_entity_id.value

    @property
    def idp_x509_certs(self):
        """List of public X509 certificates of the identity provider. Certificates must
        be in PEM format.
        
        :rtype: list
        """

        return self._idp_x509_certs.value

    @property
    def slo_endpoint(self):
        """URL of the identity provider's SLO endpoint.
        
        :rtype: str
        """

        return self._slo_endpoint.value

    @property
    def sp_entity_id(self):
        """Entity ID of the service provider. We recommend that you leave it empty and
        let the system generate it.
        
        :rtype: str
        """

        return self._sp_entity_id.value

    @property
    def sso_endpoint(self):
        """URL of the identity provider's SSO endpoint.
        
        :rtype: str
        """

        return self._sso_endpoint.value
