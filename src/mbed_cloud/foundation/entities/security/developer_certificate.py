"""
.. warning::
    DeveloperCertificate should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DeveloperCertificate
=======================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DeveloperCertificate.create`
- :meth:`DeveloperCertificate.delete`
- :meth:`DeveloperCertificate.get_trusted_certificate_info`
- :meth:`DeveloperCertificate.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    developer_certificates = pelion_dm_sdk.foundation.developer_certificate()

How to import DeveloperCertificate directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DeveloperCertificate

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class DeveloperCertificate(Entity):
    """Represents the `DeveloperCertificate` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "certificate",
        "created_at",
        "description",
        "id",
        "name",
        "security_file_content",
    ]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {
        "developer_certificate": "certificate",
        "developer_private_key": "private_key",
    }

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {
        "certificate": "developer_certificate",
        "private_key": "developer_private_key",
    }

    def __init__(
        self,
        _client=None,
        account_id=None,
        certificate=None,
        created_at=None,
        description=None,
        id=None,
        name=None,
        security_file_content=None,
    ):
        """Creates a local `DeveloperCertificate` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: account to which the developer certificate belongs
        :type account_id: str
        :param certificate: PEM format X.509 developer certificate.
        :type certificate: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Description for the developer certificate.
        :type description: str
        :param id: (Required) mUUID that uniquely identifies the developer certificate.
        :type id: str
        :param name: (Required) Name of the developer certificate.
        :type name: str
        :param security_file_content: Content of the security.c file that will be flashed into the
            device to provide the security credentials
        :type security_file_content: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._certificate = fields.StringField(value=certificate)
        self._created_at = fields.DateTimeField(value=created_at)
        self._description = fields.StringField(value=description)
        self._id = fields.StringField(value=id)
        self._name = fields.StringField(value=name)
        self._security_file_content = fields.StringField(value=security_file_content)

    @property
    def account_id(self):
        """account to which the developer certificate belongs
        
        :rtype: str
        """

        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """Set value of `account_id`

        :param value: value to set
        :type value: str
        """

        self._account_id.set(value)

    @property
    def certificate(self):
        """PEM format X.509 developer certificate.
        
        :rtype: str
        """

        return self._certificate.value

    @certificate.setter
    def certificate(self, value):
        """Set value of `certificate`

        :param value: value to set
        :type value: str
        """

        self._certificate.set(value)

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
    def description(self):
        """Description for the developer certificate.
        
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
        """mUUID that uniquely identifies the developer certificate.

        This field must be set when updating or deleting an existing DeveloperCertificate Entity.
        
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
    def name(self):
        """Name of the developer certificate.

        This field must be set when creating a new DeveloperCertificate Entity.
        
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

    @property
    def security_file_content(self):
        """Content of the security.c file that will be flashed into the device to provide
        the security credentials
        
        :rtype: str
        """

        return self._security_file_content.value

    @security_file_content.setter
    def security_file_content(self, value):
        """Set value of `security_file_content`

        :param value: value to set
        :type value: str
        """

        self._security_file_content.set(value)

    def create(self):
        """Create a new developer certificate to connect to the bootstrap server.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/developer-certificates>`_.
        
        :rtype: DeveloperCertificate
        """

        return self._client.call_api(
            method="post",
            path="/v3/developer-certificates",
            body_params={
                "description": self._description.to_api(),
                "name": self._name.to_api(),
            },
            unpack=self,
        )

    def delete(self):
        """Delete a trusted certificate by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/trusted-certificates/{cert_id}>`_.
        
        :rtype: DeveloperCertificate
        """

        return self._client.call_api(
            method="delete",
            path="/v3/trusted-certificates/{cert_id}",
            path_params={"cert_id": self._id.to_api()},
            unpack=self,
        )

    def get_trusted_certificate_info(self):
        """Get trusted certificate by ID.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/trusted-certificates/{cert_id}>`_.
        
        :rtype: TrustedCertificate
        """

        from mbed_cloud.foundation import TrustedCertificate

        return self._client.call_api(
            method="get",
            path="/v3/trusted-certificates/{cert_id}",
            path_params={"cert_id": self._id.to_api()},
            unpack=TrustedCertificate,
        )

    def read(self):
        """Fetch an existing developer certificate to connect to the bootstrap server.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/developer-certificates/{developerCertificateId}>`_.
        
        :rtype: DeveloperCertificate
        """

        return self._client.call_api(
            method="get",
            path="/v3/developer-certificates/{developerCertificateId}",
            path_params={"developerCertificateId": self._id.to_api()},
            unpack=self,
        )
