"""
.. warning::
    SubtenantUser should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SubtenantUser
================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`SubtenantUser.create`
- :meth:`SubtenantUser.delete`
- :meth:`SubtenantUser.read`
- :meth:`SubtenantUser.update`
- :meth:`SubtenantUser.validate_email`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    subtenant_users = pelion_dm_sdk.foundation.subtenant_user()

How to import SubtenantUser directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SubtenantUser

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SubtenantUser(Entity):
    """Represents the `SubtenantUser` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "active_sessions",
        "address",
        "created_at",
        "creation_time",
        "custom_fields",
        "email",
        "email_verified",
        "full_name",
        "id",
        "last_login_time",
        "login_history",
        "login_profiles",
        "marketing_accepted",
        "password",
        "password_changed_time",
        "phone_number",
        "status",
        "terms_accepted",
        "totp_scratch_codes",
        "two_factor_authentication",
        "updated_at",
        "username",
    ]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {
        "is_marketing_accepted": "marketing_accepted",
        "is_gtc_accepted": "terms_accepted",
        "is_totp_enabled": "two_factor_authentication",
    }

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {
        "marketing_accepted": "is_marketing_accepted",
        "terms_accepted": "is_gtc_accepted",
        "two_factor_authentication": "is_totp_enabled",
    }

    def __init__(
        self,
        _client=None,
        account_id=None,
        active_sessions=None,
        address=None,
        created_at=None,
        creation_time=None,
        custom_fields=None,
        email=None,
        email_verified=None,
        full_name=None,
        id=None,
        last_login_time=None,
        login_history=None,
        login_profiles=None,
        marketing_accepted=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        terms_accepted=None,
        totp_scratch_codes=None,
        two_factor_authentication=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `SubtenantUser` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: (Required) The ID of the account.
        :type account_id: str
        :param active_sessions: List of active user sessions.
        :type active_sessions: list
        :param address: Address.
        :type address: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: int
        :param custom_fields: User's account specific custom properties. The value is a string.
        :type custom_fields: dict
        :param email: (Required) The email address.
        :type email: str
        :param email_verified: A flag indicating whether the user's email address has been
            verified or not.
        :type email_verified: bool
        :param full_name: The full name of the user.
        :type full_name: str
        :param id: (Required) The ID of the user.
        :type id: str
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: int
        :param login_history: Timestamps, succeedings, IP addresses and user agent information
            of the last five logins of the user, with timestamps in RFC3339
            format.
        :type login_history: list
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
        :param marketing_accepted: A flag indicating that receiving marketing information has been
            accepted.
        :type marketing_accepted: bool
        :param password: The password when creating a new user. It will be generated when
            not present in the request.
        :type password: str
        :param password_changed_time: A timestamp of the latest change of the user password, in
            milliseconds.
        :type password_changed_time: int
        :param phone_number: Phone number.
        :type phone_number: str
        :param status: The status of the user. ENROLLING state indicates that the user is
            in the middle of the enrollment process. INVITED means that the
            user has not accepted the invitation request. RESET means that the
            password must be changed immediately. INACTIVE users are locked
            out and not permitted to use the system.
        :type status: str
        :param terms_accepted: A flag indicating that the General Terms and Conditions has been
            accepted.
        :type terms_accepted: bool
        :param totp_scratch_codes: A list of scratch codes for the 2-factor authentication. Visible
            only when 2FA is requested to be enabled or the codes regenerated.
        :type totp_scratch_codes: list
        :param two_factor_authentication: A flag indicating whether 2-factor authentication (TOTP) has been
            enabled.
        :type two_factor_authentication: bool
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param username: A username containing alphanumerical letters and -,._@+=
            characters.
        :type username: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        from mbed_cloud.foundation.entities.accounts.active_session import ActiveSession
        from mbed_cloud.foundation.entities.accounts.login_history import LoginHistory
        from mbed_cloud.foundation.entities.accounts.login_profile import LoginProfile

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._active_sessions = fields.ListField(
            value=active_sessions, entity=ActiveSession
        )
        self._address = fields.StringField(value=address)
        self._created_at = fields.DateTimeField(value=created_at)
        self._creation_time = fields.IntegerField(value=creation_time)
        self._custom_fields = fields.DictField(value=custom_fields)
        self._email = fields.StringField(value=email)
        self._email_verified = fields.BooleanField(value=email_verified)
        self._full_name = fields.StringField(value=full_name)
        self._id = fields.StringField(value=id)
        self._last_login_time = fields.IntegerField(value=last_login_time)
        self._login_history = fields.ListField(value=login_history, entity=LoginHistory)
        self._login_profiles = fields.ListField(value=login_profiles, entity=LoginProfile)
        self._marketing_accepted = fields.BooleanField(value=marketing_accepted)
        self._password = fields.StringField(value=password)
        self._password_changed_time = fields.IntegerField(value=password_changed_time)
        self._phone_number = fields.StringField(value=phone_number)
        self._status = fields.StringField(value=status, enum=enums.SubtenantUserStatusEnum)
        self._terms_accepted = fields.BooleanField(value=terms_accepted)
        self._totp_scratch_codes = fields.ListField(value=totp_scratch_codes)
        self._two_factor_authentication = fields.BooleanField(
            value=two_factor_authentication
        )
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._username = fields.StringField(value=username)

    @property
    def account_id(self):
        """The ID of the account.

        This field must be set when creating a new SubtenantUser Entity.
        
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
    def active_sessions(self):
        """List of active user sessions.
        
        :rtype: list[ActiveSession]
        """

        return self._active_sessions.value

    @active_sessions.setter
    def active_sessions(self, value):
        """Set value of `active_sessions`

        :param value: value to set
        :type value: list[ActiveSession]
        """

        self._active_sessions.set(value)

    @property
    def address(self):
        """Address.
        
        api example: '110 Fulbourn Rd, Cambridge, United Kingdom'
        
        :rtype: str
        """

        return self._address.value

    @address.setter
    def address(self, value):
        """Set value of `address`

        :param value: value to set
        :type value: str
        """

        self._address.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
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
    def creation_time(self):
        """A timestamp of the user creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """

        return self._creation_time.value

    @creation_time.setter
    def creation_time(self, value):
        """Set value of `creation_time`

        :param value: value to set
        :type value: int
        """

        self._creation_time.set(value)

    @property
    def custom_fields(self):
        """User's account specific custom properties. The value is a string.
        
        :rtype: dict
        """

        return self._custom_fields.value

    @custom_fields.setter
    def custom_fields(self, value):
        """Set value of `custom_fields`

        :param value: value to set
        :type value: dict
        """

        self._custom_fields.set(value)

    @property
    def email(self):
        """The email address.

        This field must be set when creating a new SubtenantUser Entity.
        
        api example: 'user@arm.com'
        
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
    def email_verified(self):
        """A flag indicating whether the user's email address has been verified or not.
        
        api example: True
        
        :rtype: bool
        """

        return self._email_verified.value

    @email_verified.setter
    def email_verified(self, value):
        """Set value of `email_verified`

        :param value: value to set
        :type value: bool
        """

        self._email_verified.set(value)

    @property
    def full_name(self):
        """The full name of the user.
        
        api example: 'User Doe'
        
        :rtype: str
        """

        return self._full_name.value

    @full_name.setter
    def full_name(self, value):
        """Set value of `full_name`

        :param value: value to set
        :type value: str
        """

        self._full_name.set(value)

    @property
    def id(self):
        """The ID of the user.

        This field must be set when updating or deleting an existing SubtenantUser Entity.
        
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
    def last_login_time(self):
        """A timestamp of the latest login of the user, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """

        return self._last_login_time.value

    @last_login_time.setter
    def last_login_time(self, value):
        """Set value of `last_login_time`

        :param value: value to set
        :type value: int
        """

        self._last_login_time.set(value)

    @property
    def login_history(self):
        """Timestamps, succeedings, IP addresses and user agent information of the last
        five logins of the user, with timestamps in RFC3339 format.
        
        :rtype: list[LoginHistory]
        """

        return self._login_history.value

    @login_history.setter
    def login_history(self, value):
        """Set value of `login_history`

        :param value: value to set
        :type value: list[LoginHistory]
        """

        self._login_history.set(value)

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
    def marketing_accepted(self):
        """A flag indicating that receiving marketing information has been accepted.
        
        api example: True
        
        :rtype: bool
        """

        return self._marketing_accepted.value

    @marketing_accepted.setter
    def marketing_accepted(self, value):
        """Set value of `marketing_accepted`

        :param value: value to set
        :type value: bool
        """

        self._marketing_accepted.set(value)

    @property
    def password(self):
        """The password when creating a new user. It will be generated when not present
        in the request.
        
        api example: 'PZf9eEUH43DAPE9ULINFeuj'
        
        :rtype: str
        """

        return self._password.value

    @password.setter
    def password(self, value):
        """Set value of `password`

        :param value: value to set
        :type value: str
        """

        self._password.set(value)

    @property
    def password_changed_time(self):
        """A timestamp of the latest change of the user password, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """

        return self._password_changed_time.value

    @password_changed_time.setter
    def password_changed_time(self, value):
        """Set value of `password_changed_time`

        :param value: value to set
        :type value: int
        """

        self._password_changed_time.set(value)

    @property
    def phone_number(self):
        """Phone number.
        
        api example: '+44 (1223) 400 400'
        
        :rtype: str
        """

        return self._phone_number.value

    @phone_number.setter
    def phone_number(self, value):
        """Set value of `phone_number`

        :param value: value to set
        :type value: str
        """

        self._phone_number.set(value)

    @property
    def status(self):
        """The status of the user. ENROLLING state indicates that the user is in the
        middle of the enrollment process. INVITED means that the user has not accepted
        the invitation request. RESET means that the password must be changed
        immediately. INACTIVE users are locked out and not permitted to use the
        system.
        
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
    def terms_accepted(self):
        """A flag indicating that the General Terms and Conditions has been accepted.
        
        api example: True
        
        :rtype: bool
        """

        return self._terms_accepted.value

    @terms_accepted.setter
    def terms_accepted(self, value):
        """Set value of `terms_accepted`

        :param value: value to set
        :type value: bool
        """

        self._terms_accepted.set(value)

    @property
    def totp_scratch_codes(self):
        """A list of scratch codes for the 2-factor authentication. Visible only when 2FA
        is requested to be enabled or the codes regenerated.
        
        :rtype: list
        """

        return self._totp_scratch_codes.value

    @totp_scratch_codes.setter
    def totp_scratch_codes(self, value):
        """Set value of `totp_scratch_codes`

        :param value: value to set
        :type value: list
        """

        self._totp_scratch_codes.set(value)

    @property
    def two_factor_authentication(self):
        """A flag indicating whether 2-factor authentication (TOTP) has been enabled.
        
        api example: True
        
        :rtype: bool
        """

        return self._two_factor_authentication.value

    @two_factor_authentication.setter
    def two_factor_authentication(self, value):
        """Set value of `two_factor_authentication`

        :param value: value to set
        :type value: bool
        """

        self._two_factor_authentication.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
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

    @property
    def username(self):
        """A username containing alphanumerical letters and -,._@+= characters.
        
        api example: 'admin'
        
        :rtype: str
        """

        return self._username.value

    @username.setter
    def username(self, value):
        """Set value of `username`

        :param value: value to set
        :type value: str
        """

        self._username.set(value)

    def create(self, action="create"):
        """Create a new user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account_id}/users
        
        :param action: Create or invite user.
        :type action: str
        
        :rtype: SubtenantUser
        """

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account_id}/users",
            path_params={"account_id": self._account_id.to_api()},
            query_params={"action": fields.StringField(action).to_api()},
            body_params={
                "address": self._address.to_api(),
                "email": self._email.to_api(),
                "full_name": self._full_name.to_api(),
                "login_profiles": self._login_profiles.to_api(),
                "is_marketing_accepted": self._marketing_accepted.to_api(),
                "password": self._password.to_api(),
                "phone_number": self._phone_number.to_api(),
                "is_gtc_accepted": self._terms_accepted.to_api(),
                "username": self._username.to_api(),
            },
            unpack=self,
        )

    def delete(self):
        """Delete a user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account_id}/users/{user_id}
        
        :rtype: SubtenantUser
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account_id}/users/{user_id}",
            path_params={
                "account_id": self._account_id.to_api(),
                "user_id": self._id.to_api(),
            },
            unpack=self,
        )

    def read(self):
        """Details of the user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account_id}/users/{user_id}
        
        :rtype: SubtenantUser
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/users/{user_id}",
            path_params={
                "account_id": self._account_id.to_api(),
                "user_id": self._id.to_api(),
            },
            unpack=self,
        )

    def update(self):
        """Update user details.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account_id}/users/{user_id}
        
        :rtype: SubtenantUser
        """

        return self._client.call_api(
            method="put",
            path="/v3/accounts/{account_id}/users/{user_id}",
            path_params={
                "account_id": self._account_id.to_api(),
                "user_id": self._id.to_api(),
            },
            body_params={
                "address": self._address.to_api(),
                "full_name": self._full_name.to_api(),
                "login_profiles": self._login_profiles.to_api(),
                "is_marketing_accepted": self._marketing_accepted.to_api(),
                "phone_number": self._phone_number.to_api(),
                "is_gtc_accepted": self._terms_accepted.to_api(),
                "is_totp_enabled": self._two_factor_authentication.to_api(),
                "username": self._username.to_api(),
            },
            unpack=self,
        )

    def validate_email(self):
        """Validate the user email.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account_id}/users/{user_id}/validate-email
        
        :rtype: SubtenantUser
        """

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account_id}/users/{user_id}/validate-email",
            path_params={
                "account_id": self._account_id.to_api(),
                "user_id": self._id.to_api(),
            },
            unpack=self,
        )
