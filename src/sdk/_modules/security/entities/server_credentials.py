"""
Entity module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class ServerCredentials(Entity):
    """Represents the `ServerCredentials` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "bootstrap",
        "created_at",
        "id",
        "lwm2m",
        "server_certificate",
        "server_uri",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(
        self,
        _client=None,
        bootstrap=None,
        created_at=None,
        id=None,
        lwm2m=None,
        server_certificate=None,
        server_uri=None,
    ):
        """Creates a local `ServerCredentials` instance

        :param bootstrap: 
        :type bootstrap: dict
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: mUUID that uniquely identifies the entity.
        :type id: str
        :param lwm2m: 
        :type lwm2m: dict
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
        self._bootstrap = fields.DictField(value=bootstrap)
        self._created_at = fields.DateTimeField(value=created_at)
        self._id = fields.StringField(value=id)
        self._lwm2m = fields.DictField(value=lwm2m)
        self._server_certificate = fields.StringField(value=server_certificate)
        self._server_uri = fields.StringField(value=server_uri)

    @property
    def bootstrap(self):
        """
        
        :rtype: dict
        """
        return self._bootstrap.value

    @bootstrap.setter
    def bootstrap(self, value):
        """Set value of `bootstrap`

        :param value: value to set
        :type value: dict
        """
        self._bootstrap.set(value)

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
    def lwm2m(self):
        """
        
        :rtype: dict
        """
        return self._lwm2m.value

    @lwm2m.setter
    def lwm2m(self, value):
        """Set value of `lwm2m`

        :param value: value to set
        :type value: dict
        """
        self._lwm2m.set(value)

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
