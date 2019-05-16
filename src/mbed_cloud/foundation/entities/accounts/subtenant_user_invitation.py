"""
.. warning::
    SubtenantUserInvitation should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SubtenantUserInvitation
==========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`SubtenantUserInvitation.create`
- :meth:`SubtenantUserInvitation.delete`
- :meth:`SubtenantUserInvitation.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    subtenant_user_invitations = pelion_dm_sdk.foundation.subtenant_user_invitation()

How to import SubtenantUserInvitation directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SubtenantUserInvitation

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SubtenantUserInvitation(Entity):
    """Represents the `SubtenantUserInvitation` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "account_id",
        "created_at",
        "email",
        "expiration",
        "id",
        "login_profiles",
        "updated_at",
        "user_id",
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
        email=None,
        expiration=None,
        id=None,
        login_profiles=None,
        updated_at=None,
        user_id=None,
    ):
        """Creates a local `SubtenantUserInvitation` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: (Required) The ID of the account the user is invited to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param email: (Required) Email address of the invited user.
        :type email: str
        :param expiration: Invitation expiration as UTC time RFC3339.
        :type expiration: datetime
        :param id: (Required) The ID of the invitation.
        :type id: str
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_id: The ID of the invited user.
        :type user_id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        from mbed_cloud.foundation.entities.accounts.login_profile import LoginProfile

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._email = fields.StringField(value=email)
        self._expiration = fields.DateTimeField(value=expiration)
        self._id = fields.StringField(value=id)
        self._login_profiles = fields.ListField(value=login_profiles, entity=LoginProfile)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._user_id = fields.StringField(value=user_id)

    @property
    def account_id(self):
        """The ID of the account the user is invited to.

        This field must be set when creating a new SubtenantUserInvitation Entity.
        
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
    def email(self):
        """Email address of the invited user.

        This field must be set when creating a new SubtenantUserInvitation Entity.
        
        api example: 'friend@arm.com'
        
        :rtype: str
        """

        return self._email.value

    @email.setter
    def email(self, value):
        """Set value of `email`

        :param value: value to set
        :type value: str
        """

        self._email.set(value)

    @property
    def expiration(self):
        """Invitation expiration as UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._expiration.value

    @property
    def id(self):
        """The ID of the invitation.

        This field must be set when updating or deleting an existing SubtenantUserInvitation Entity.
        
        api example: '01619571e2e89242ac12000600000000'
        
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
    def login_profiles(self):
        """A list of login profiles for the user. Specified as the identity providers the
        user is associated with.
        
        :rtype: list[LoginProfile]
        """

        return self._login_profiles.value

    @login_profiles.setter
    def login_profiles(self, value):
        """Set value of `login_profiles`

        :param value: value to set
        :type value: list[LoginProfile]
        """

        self._login_profiles.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @property
    def user_id(self):
        """The ID of the invited user.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._user_id.value

    def create(self, valid_for_days=30):
        """Create a user invitation.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/user-invitations>`_.
        
        :param valid_for_days: Specifies how many days the invitation will be valid for.
        :type valid_for_days: int
        
        :rtype: SubtenantUserInvitation
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._email.value_set:
            body_params["email"] = self._email.to_api()
        if self._login_profiles.value_set:
            body_params["login_profiles"] = self._login_profiles.to_api()
        # Method parameters are unconditionally sent even if set to None
        body_params["valid_for_days"] = fields.IntegerField(valid_for_days).to_api()

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account_id}/user-invitations",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api()},
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete a user invitation.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/user-invitations/{invitation_id}>`_.
        
        :rtype: SubtenantUserInvitation
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account_id}/user-invitations/{invitation_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "invitation_id": self._id.to_api()},
            unpack=self,
        )

    def read(self):
        """Details of a user invitation.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/user-invitations/{invitation_id}>`_.
        
        :rtype: SubtenantUserInvitation
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/user-invitations/{invitation_id}",
            content_type="application/json",
            path_params={"account_id": self._account_id.to_api(), "invitation_id": self._id.to_api()},
            unpack=self,
        )
