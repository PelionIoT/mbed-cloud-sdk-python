"""
Foundation Entity: ServerCredentials
====================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:
- :meth:`ServerCredentials.get_bootstrap`
- :meth:`ServerCredentials.get_lwm2m`

.. warning::
    ServerCredentials should not be imported directly from this module as the
    organisation may change in the future, please use the top level foundation module to import entities.

How to import ServerCredentials:

.. code-block:: python
    
    from mbed_cloud.foundation import ServerCredentials
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class ServerCredentials(Entity):
    """Represents the `ServerCredentials` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = ["created_at", "id", "server_certificate", "server_uri"]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        created_at=None,
        id=None,
        server_certificate=None,
        server_uri=None,
    ):
        """Creates a local `ServerCredentials` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: mUUID that uniquely identifies the entity.
        :type id: str
        :param server_certificate: PEM format X.509 server certificate that will be used to validate
            the server certificate that will be received during the TLS/DTLS
            handshake.
        :type server_certificate: str
        :param server_uri: Server URI to which the client needs to connect to.
        :type server_uri: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._created_at = fields.DateTimeField(value=created_at)
        self._id = fields.StringField(value=id)
        self._server_certificate = fields.StringField(value=server_certificate)
        self._server_uri = fields.StringField(value=server_uri)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
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
        """mUUID that uniquely identifies the entity.
        
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
    def server_certificate(self):
        """PEM format X.509 server certificate that will be used to validate the server
        certificate that will be received during the TLS/DTLS handshake.
        
        :rtype: str
        """

        return self._server_certificate.value

    @server_certificate.setter
    def server_certificate(self, value):
        """Set value of `server_certificate`

        :param value: value to set
        :type value: str
        """

        self._server_certificate.set(value)

    @property
    def server_uri(self):
        """Server URI to which the client needs to connect to.
        
        :rtype: str
        """

        return self._server_uri.value

    @server_uri.setter
    def server_uri(self, value):
        """Set value of `server_uri`

        :param value: value to set
        :type value: str
        """

        self._server_uri.set(value)

    def get_bootstrap(self):
        """Fetch bootstrap server credentials.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/server-credentials/bootstrap
        
        :rtype: ServerCredentials
        """

        return self._client.call_api(
            method="get", path="/v3/server-credentials/bootstrap", unpack=self
        )

    def get_lwm2m(self):
        """Fetch LwM2M server credentials.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/server-credentials/lwm2m
        
        :rtype: ServerCredentials
        """

        return self._client.call_api(
            method="get", path="/v3/server-credentials/lwm2m", unpack=self
        )
