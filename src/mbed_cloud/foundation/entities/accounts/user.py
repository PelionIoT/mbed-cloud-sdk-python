"""
.. warning::
    User should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: User
=======================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`User.create`
- :meth:`User.delete`
- :meth:`User.list`
- :meth:`User.read`
- :meth:`User.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    users = pelion_dm_sdk.foundation.user()

How to import User directly:

.. code-block:: python
    
    from mbed_cloud.foundation import User

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class User(Entity):
    """Represents the `User` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
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
        "is_gtc_accepted",
        "is_marketing_accepted",
        "is_totp_enabled",
        "last_login_time",
        "login_history",
        "login_profiles",
        "password",
        "password_changed_time",
        "phone_number",
        "status",
        "totp_scratch_codes",
        "updated_at",
        "username",
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
        active_sessions=None,
        address=None,
        created_at=None,
        creation_time=None,
        custom_fields=None,
        email=None,
        email_verified=None,
        full_name=None,
        id=None,
        is_gtc_accepted=None,
        is_marketing_accepted=None,
        is_totp_enabled=None,
        last_login_time=None,
        login_history=None,
        login_profiles=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        totp_scratch_codes=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `User` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: The ID of the account.
        :type account_id: str
        :param active_sessions: List of active user sessions.
        :type active_sessions: list
        :param address: Address.
        :type address: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: int
        :param custom_fields: User's account-specific custom properties. The value is a string.
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
        :param is_gtc_accepted: A flag indicating that the user has accepted General Terms and
            Conditions.
        :type is_gtc_accepted: bool
        :param is_marketing_accepted: A flag indicating that the user has consented to receive marketing
            information.
        :type is_marketing_accepted: bool
        :param is_totp_enabled: A flag indicating whether two-factor authentication (TOTP) has
            been enabled.
        :type is_totp_enabled: bool
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: int
        :param login_history: Timestamps, succeedings, IP addresses and user agent information
            of the last five logins of the user, with timestamps in RFC3339
            format.
        :type login_history: list
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
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
        :param totp_scratch_codes: A list of scratch codes for the two-factor authentication. Visible
            only when 2FA is requested to be enabled or the codes regenerated.
        :type totp_scratch_codes: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param username: A username.
        :type username: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        from mbed_cloud.foundation.entities.accounts.active_session import ActiveSession
        from mbed_cloud.foundation.entities.accounts.login_history import LoginHistory
        from mbed_cloud.foundation.entities.accounts.login_profile import LoginProfile

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._active_sessions = fields.ListField(value=active_sessions, entity=ActiveSession)
        self._address = fields.StringField(value=address)
        self._created_at = fields.DateTimeField(value=created_at)
        self._creation_time = fields.IntegerField(value=creation_time)
        self._custom_fields = fields.DictField(value=custom_fields)
        self._email = fields.StringField(value=email)
        self._email_verified = fields.BooleanField(value=email_verified)
        self._full_name = fields.StringField(value=full_name)
        self._id = fields.StringField(value=id)
        self._is_gtc_accepted = fields.BooleanField(value=is_gtc_accepted)
        self._is_marketing_accepted = fields.BooleanField(value=is_marketing_accepted)
        self._is_totp_enabled = fields.BooleanField(value=is_totp_enabled)
        self._last_login_time = fields.IntegerField(value=last_login_time)
        self._login_history = fields.ListField(value=login_history, entity=LoginHistory)
        self._login_profiles = fields.ListField(value=login_profiles, entity=LoginProfile)
        self._password = fields.StringField(value=password)
        self._password_changed_time = fields.IntegerField(value=password_changed_time)
        self._phone_number = fields.StringField(value=phone_number)
        self._status = fields.StringField(value=status, enum=enums.UserStatusEnum)
        self._totp_scratch_codes = fields.ListField(value=totp_scratch_codes)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._username = fields.StringField(value=username)

    @property
    def account_id(self):
        """The ID of the account.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._account_id.value

    @property
    def active_sessions(self):
        """List of active user sessions.
        
        :rtype: list[ActiveSession]
        """

        return self._active_sessions.value

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

    @property
    def creation_time(self):
        """A timestamp of the user creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """

        return self._creation_time.value

    @property
    def custom_fields(self):
        """User's account-specific custom properties. The value is a string.
        
        :rtype: dict
        """

        return self._custom_fields.value

    @property
    def email(self):
        """The email address.

        This field must be set when creating a new User Entity.
        
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

        This field must be set when updating or deleting an existing User Entity.
        
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
    def is_gtc_accepted(self):
        """A flag indicating that the user has accepted General Terms and Conditions.
        
        api example: True
        
        :rtype: bool
        """

        return self._is_gtc_accepted.value

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, value):
        """Set value of `is_gtc_accepted`

        :param value: value to set
        :type value: bool
        """

        self._is_gtc_accepted.set(value)

    @property
    def is_marketing_accepted(self):
        """A flag indicating that the user has consented to receive marketing
        information.
        
        api example: True
        
        :rtype: bool
        """

        return self._is_marketing_accepted.value

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, value):
        """Set value of `is_marketing_accepted`

        :param value: value to set
        :type value: bool
        """

        self._is_marketing_accepted.set(value)

    @property
    def is_totp_enabled(self):
        """A flag indicating whether two-factor authentication (TOTP) has been enabled.
        
        api example: True
        
        :rtype: bool
        """

        return self._is_totp_enabled.value

    @is_totp_enabled.setter
    def is_totp_enabled(self, value):
        """Set value of `is_totp_enabled`

        :param value: value to set
        :type value: bool
        """

        self._is_totp_enabled.set(value)

    @property
    def last_login_time(self):
        """A timestamp of the latest login of the user, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """

        return self._last_login_time.value

    @property
    def login_history(self):
        """Timestamps, succeedings, IP addresses and user agent information of the last
        five logins of the user, with timestamps in RFC3339 format.
        
        :rtype: list[LoginHistory]
        """

        return self._login_history.value

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
    def totp_scratch_codes(self):
        """A list of scratch codes for the two-factor authentication. Visible only when
        2FA is requested to be enabled or the codes regenerated.
        
        :rtype: list
        """

        return self._totp_scratch_codes.value

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @property
    def username(self):
        """A username.
        
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

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/users>`_.
        
        :param action: Action, either `create` or `invite`.
        :type action: str
        
        :rtype: User
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._address.value_set:
            body_params["address"] = self._address.to_api()
        if self._email.value_set:
            body_params["email"] = self._email.to_api()
        if self._full_name.value_set:
            body_params["full_name"] = self._full_name.to_api()
        if self._is_gtc_accepted.value_set:
            body_params["is_gtc_accepted"] = self._is_gtc_accepted.to_api()
        if self._is_marketing_accepted.value_set:
            body_params["is_marketing_accepted"] = self._is_marketing_accepted.to_api()
        if self._login_profiles.value_set:
            body_params["login_profiles"] = self._login_profiles.to_api()
        if self._password.value_set:
            body_params["password"] = self._password.to_api()
        if self._phone_number.value_set:
            body_params["phone_number"] = self._phone_number.to_api()
        if self._username.value_set:
            body_params["username"] = self._username.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/users",
            content_type="application/json",
            query_params={"action": fields.StringField(action).to_api()},
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Delete a user.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/users/{user_id}>`_.
        
        :rtype: User
        """

        return self._client.call_api(
            method="delete",
            path="/v3/users/{user_id}",
            content_type="application/json",
            path_params={"user_id": self._id.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get the details of all users.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/users>`_.

        **API Filters**

        The following filters are supported by the API when listing User entities:

        +----------------+------+------+------+------+------+------+------+
        | Field          | eq   | neq  | gte  | lte  | in   | nin  | like |
        +================+======+======+======+======+======+======+======+
        | email          | Y    |      |      |      |      |      |      |
        +----------------+------+------+------+------+------+------+------+
        | login_profiles | Y    |      |      |      |      |      |      |
        +----------------+------+------+------+------+------+------+------+
        | status         | Y    |      |      |      | Y    | Y    |      |
        +----------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import User
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("email", "eq", <filter value>)
            for user in User().list(filter=api_filter):
                print(user.email)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000). Default 50.
        :type page_size: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(User)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import User
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=User._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = User._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=User,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get the details of all users.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param limit: The number of results to return (2-1000). Default 50.
        :type limit: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.UserOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get", path="/v3/users", content_type="application/json", query_params=query_params, unpack=False
        )

    def read(self):
        """Details of a user.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/users/{user_id}>`_.
        
        :rtype: User
        """

        return self._client.call_api(
            method="get",
            path="/v3/users/{user_id}",
            content_type="application/json",
            path_params={"user_id": self._id.to_api()},
            unpack=self,
        )

    def update(self):
        """Update user details.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/users/{user_id}>`_.
        
        :rtype: User
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._address.value_set:
            body_params["address"] = self._address.to_api()
        if self._full_name.value_set:
            body_params["full_name"] = self._full_name.to_api()
        if self._is_gtc_accepted.value_set:
            body_params["is_gtc_accepted"] = self._is_gtc_accepted.to_api()
        if self._is_marketing_accepted.value_set:
            body_params["is_marketing_accepted"] = self._is_marketing_accepted.to_api()
        if self._is_totp_enabled.value_set:
            body_params["is_totp_enabled"] = self._is_totp_enabled.to_api()
        if self._login_profiles.value_set:
            body_params["login_profiles"] = self._login_profiles.to_api()
        if self._phone_number.value_set:
            body_params["phone_number"] = self._phone_number.to_api()
        if self._username.value_set:
            body_params["username"] = self._username.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/users/{user_id}",
            content_type="application/json",
            body_params=body_params,
            path_params={"user_id": self._id.to_api()},
            unpack=self,
        )
