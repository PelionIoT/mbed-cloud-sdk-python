"""
.. warning::
    ServerCredentials should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: ServerCredentials
====================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`ServerCredentials.get_bootstrap`
- :meth:`ServerCredentials.get_lwm2m`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    server_credentialss = pelion_dm_sdk.foundation.server_credentials()

How to import ServerCredentials directly:

.. code-block:: python
    
    from mbed_cloud.foundation import ServerCredentials

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class ServerCredentials(Entity):
    """Represents the `ServerCredentials` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["created_at", "id", "server_certificate", "server_uri"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, created_at=None, id=None, server_certificate=None, server_uri=None):
        """Creates a local `ServerCredentials` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: Unique entity ID.
        :type id: str
        :param server_certificate: PEM-format X.509 server certificate used to validate the server
            certificate received during the TLS/DTLS handshake.
        :type server_certificate: str
        :param server_uri: Server URI that the client connects to.
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

    @property
    def id(self):
        """Unique entity ID.
        
        :rtype: str
        """

        return self._id.value

    @property
    def server_certificate(self):
        """PEM-format X.509 server certificate used to validate the server certificate
        received during the TLS/DTLS handshake.
        
        :rtype: str
        """

        return self._server_certificate.value

    @property
    def server_uri(self):
        """Server URI that the client connects to.
        
        :rtype: str
        """

        return self._server_uri.value

    def get_bootstrap(self):
        """Fetch bootstrap server credentials.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/server-credentials/bootstrap>`_.
        
        :rtype: ServerCredentials
        """

        return self._client.call_api(
            method="get", path="/v3/server-credentials/bootstrap", content_type="application/json", unpack=self
        )

    def get_lwm2m(self):
        """Fetch LwM2M server credentials.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/server-credentials/lwm2m>`_.
        
        :rtype: ServerCredentials
        """

        return self._client.call_api(
            method="get", path="/v3/server-credentials/lwm2m", content_type="application/json", unpack=self
        )
