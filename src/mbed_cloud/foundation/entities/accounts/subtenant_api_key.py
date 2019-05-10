"""
.. warning::
    SubtenantApiKey should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SubtenantApiKey
==================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`SubtenantApiKey.create`
- :meth:`SubtenantApiKey.delete`
- :meth:`SubtenantApiKey.read`
- :meth:`SubtenantApiKey.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    subtenant_api_keys = pelion_dm_sdk.foundation.subtenant_api_key()

How to import SubtenantApiKey directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SubtenantApiKey

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SubtenantApiKey(Entity):
    """Represents the `SubtenantApiKey` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "account_id",
        "created_at",
        "creation_time",
        "id",
        "key",
        "last_login_time",
        "name",
        "owner",
        "status",
        "updated_at",
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
        account_id=None,
        created_at=None,
        creation_time=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `SubtenantApiKey` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: (Required) The ID of the account.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: The timestamp of the API key creation in the storage, in
            milliseconds.
        :type creation_time: int
        :param id: (Required) The ID of the API key.
        :type id: str
        :param key: The API key.
        :type key: str
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: int
        :param name: (Required) The display name for the API key.
        :type name: str
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: str
        :param status: The status of the API key.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._creation_time = fields.IntegerField(value=creation_time)
        self._id = fields.StringField(value=id)
        self._key = fields.StringField(value=key)
        self._last_login_time = fields.IntegerField(value=last_login_time)
        self._name = fields.StringField(value=name)
        self._owner = fields.StringField(value=owner)
        self._status = fields.StringField(value=status, enum=enums.SubtenantApiKeyStatusEnum)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def account_id(self):
        """The ID of the account.

        This field must be set when creating a new SubtenantApiKey Entity.
        
        api example: '01619571e2e90242ac12000600000000'
        
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
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def creation_time(self):
        """The timestamp of the API key creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """

        return self._creation_time.value

    @property
    def id(self):
        """The ID of the API key.

        This field must be set when updating or deleting an existing SubtenantApiKey Entity.
        
        api example: '01619571f7020242ac12000600000000'
        
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
    def key(self):
        """The API key.
        
        api example: 'ak_1MDE2MTk1NzFmNmU4MDI0MmFjMTIwMDA2MDAwMDAwMDA01619571f7020242ac120006000000
            00'
        
        :rtype: str
        """

        return self._key.value

    @property
    def last_login_time(self):
        """The timestamp of the latest API key usage, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """

        return self._last_login_time.value

    @property
    def name(self):
        """The display name for the API key.

        This field must be set when creating a new SubtenantApiKey Entity.
        
        api example: 'API key gorgon'
        
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
    def owner(self):
        """The owner of this API key, who is the creator by default.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """

        return self._owner.value

    @owner.setter
    def owner(self, value):
        """Set value of `owner`

        :param value: value to set
        :type value: str
        """

        self._owner.set(value)

    @property
    def status(self):
        """The status of the API key.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """

        return self._status.value

    @status.setter
    def status(self, value):
        """Set value of `status`

        :param value: value to set
        :type value: str
        """

        self._status.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def create(self):
        """Create a new API key.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/api-keys>`_.
        
        :rtype: SubtenantApiKey
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        if self._owner.value_set:
            body_params["owner"] = self._owner.to_api()
        if self._status.value_set:
            body_params["status"] = self._status.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account_id}/api-keys",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api()},
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete the API key.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/api-keys/{apikey_id}>`_.
        
        :rtype: SubtenantApiKey
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account_id}/api-keys/{apikey_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "apikey_id": self._id.to_api()},
            unpack=self,
        )

    def read(self):
        """Get API key details.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/api-keys/{apikey_id}>`_.
        
        :rtype: SubtenantApiKey
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/api-keys/{apikey_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "apikey_id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Update API key details.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/api-keys/{apikey_id}>`_.
        
        :rtype: SubtenantApiKey
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        if self._owner.value_set:
            body_params["owner"] = self._owner.to_api()
        if self._status.value_set:
            body_params["status"] = self._status.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/accounts/{account_id}/api-keys/{apikey_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "apikey_id": self._id.to_api()},
            body_params=body_params,
            unpack=self,
        )
