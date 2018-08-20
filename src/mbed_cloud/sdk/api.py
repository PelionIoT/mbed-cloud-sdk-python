from mbed_cloud import pagination
from mbed_cloud.sdk import common


class InstanceFactory:
    """Creates instances of Entities with a client mixed in"""

    def __init__(self, client):
        self.client = client

    def account_group(self, **kwargs):
        """
        :rtype: AccountGroup
        """
        return AccountGroup(client=self.client, **kwargs)

    def api_key(self, **kwargs):
        """
        :rtype: ApiKey
        """
        return ApiKey(client=self.client, **kwargs)

    def psk(self, **kwargs):
        """
        :rtype: PSK
        """
        return PSK(client=self.client, **kwargs)

    def user(self, **kwargs):
        """
        :rtype: User
        """
        return User(client=self.client, **kwargs)


class AccountGroup(common.Entity):
    """Represents the `AccountGroup` entity in Mbed Cloud"""

    _fieldnames = [
        "account_id",
        "apikey_count",
        "code",
        "created_at",
        "id",
        "message",
        "name",
        "request_id",
        "updated_at",
        "user_count",
    ]

    def __init__(
        self,
        client=None,
        account_id=None,
        apikey_count=None,
        code=None,
        created_at=None,
        id=None,
        message=None,
        name=None,
        request_id=None,
        updated_at=None,
        user_count=None,
    ):
        """Creates a local `AccountGroup` instance

        :param account_id: The UUID of the account this group belongs to.
        :type account_id: string
        :param apikey_count: The number of API keys in this group.
        :type apikey_count: integer
        :param code: Response code.
        :type code: integer
        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param id: Entity ID.
        :type id: string
        :param message: A human readable message with detailed info.
        :type message: string
        :param name: The name of the group.
        :type name: string
        :param request_id: Request ID.
        :type request_id: string
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        :param user_count: The number of users in this group.
        :type user_count: integer
        """

        super().__init__(client=client)

        # Attributes
        self._account_id = account_id
        self._apikey_count = apikey_count
        self._code = code
        self._created_at = created_at
        self._id = id
        self._message = message
        self._name = name
        self._request_id = request_id
        self._updated_at = updated_at
        self._user_count = user_count

    @property
    def account_id(self):
        """The UUID of the account this group belongs to.
        
        api example: '01619571e2e90242ac12000600000000'
        
        """
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    @property
    def apikey_count(self):
        """The number of API keys in this group.
        
        """
        return self._apikey_count

    @apikey_count.setter
    def apikey_count(self, value):
        self._apikey_count = value

    @property
    def code(self):
        """Response code.
        
        api example: 200
        
        """
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    @property
    def id(self):
        """Entity ID.
        
        api example: '01619571dad80242ac12000600000000'
        
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def message(self):
        """A human readable message with detailed info.
        
        api example: 'success'
        
        """
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def name(self):
        """The name of the group.
        
        api example: 'Administrators'
        
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def request_id(self):
        """Request ID.
        
        api example: '0161991d63150242ac12000600000000'
        
        """
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        self._updated_at = value

    @property
    def user_count(self):
        """The number of users in this group.
        
        api example: 1
        
        """
        return self._user_count

    @user_count.setter
    def user_count(self, value):
        self._user_count = value

    def read(self, groupid):
        """Get group information.
        
        :param groupid: The ID of the group to be retrieved.
        :type groupid: string
        
        """

        return self._call_api(
            method="get",
            path="/v3/policy-groups/{groupID}",
            path_params={"groupID": groupid},
        )

    def update(self, groupid):
        """Update the group name.
        
        :param groupid: The ID of the group to be updated.
        :type groupid: string
        
        """

        return self._call_api(
            method="put",
            path="/v3/policy-groups/{groupID}",
            path_params={"groupID": groupid},
        )


class ApiKey(common.Entity):
    """Represents the `ApiKey` entity in Mbed Cloud"""

    _fieldnames = [
        "created_at",
        "creation_time",
        "groups",
        "id",
        "key",
        "last_login_time",
        "name",
        "owner",
        "status",
        "updated_at",
    ]

    def __init__(
        self,
        client=None,
        created_at=None,
        creation_time=None,
        groups=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `ApiKey` instance

        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param creation_time: The timestamp of the API key creation in the storage, in milliseconds.
        :type creation_time: integer
        :param groups: A list of group IDs this API key belongs to.
        :type groups: array
        :param id: The UUID of the API key.
        :type id: string
        :param key: The API key.
        :type key: string
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: integer
        :param name: The display name for the API key.
        :type name: string
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: string
        :param status: The status of the API key.
        :type status: string
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        """

        super().__init__(client=client)

        # Attributes
        self._created_at = created_at
        self._creation_time = creation_time
        self._groups = groups
        self._id = id
        self._key = key
        self._last_login_time = last_login_time
        self._name = name
        self._owner = owner
        self._status = status
        self._updated_at = updated_at

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    @property
    def creation_time(self):
        """The timestamp of the API key creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        self._creation_time = value

    @property
    def groups(self):
        """A list of group IDs this API key belongs to.
        
        """
        return self._groups

    @groups.setter
    def groups(self, value):
        self._groups = value

    @property
    def id(self):
        """The UUID of the API key.
        
        api example: '01619571f7020242ac12000600000000'
        
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def key(self):
        """The API key.
        
        api example: 'ak_1MDE2MTk1NzFmNmU4MDI0MmFjMTIwMDA2MDAwMDAwMDA01619571f7020242ac12000600000000'
        
        """
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def last_login_time(self):
        """The timestamp of the latest API key usage, in milliseconds.
        
        api example: 1518630727688
        
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, value):
        self._last_login_time = value

    @property
    def name(self):
        """The display name for the API key.
        
        api example: 'API key gorgon'
        
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def owner(self):
        """The owner of this API key, who is the creator by default.
        
        api example: '01619571e2e89242ac12000600000000'
        
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def status(self):
        """The status of the API key.
        
        api example: 'ACTIVE'
        
        """
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        self._updated_at = value

    def create(self):
        """Create a new API key.
        """

        return self._call_api(
            method="post",
            path="/v3/api-keys",
            body_params={
                "groups": self.groups,
                "name": self.name,
                "owner": self.owner,
                "status": self.status,
            },
        )

    def delete(self):
        """Delete API key.
        """

        return self._call_api(method="delete", path="/v3/api-keys/{apiKey}")

    def group_ids(self, after, include, limit, order):
        """Get groups of the API key.
        
        :param after: The entity ID to fetch after the given one.
        :type after: string
        :param include: Comma separated additional data to return. Currently supported: total_count
        :type include: string
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: integer
        :param order: The order of the records based on creation time, ASC or DESC; by default ASC
        :type order: string
        
        """

        return self._call_api(
            method="get",
            path="/v3/api-keys/me/groups",
            query_params={
                "after": after,
                "include": include,
                "limit": limit,
                "order": order,
            },
        )

    def list(self, after, include, limit, order):
        """Get all API keys
        
        :param after: The entity ID to fetch after the given one.
        :type after: string
        :param include: Comma separated additional data to return. Currently supported: total_count
        :type include: string
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: integer
        :param order: The order of the records based on creation time, ASC or DESC; by default ASC
        :type order: string
        
        """

        return pagination.PaginatedResponse(
            func=self._list,
            lwrap_type=self.__class__,
            after=after,
            include=include,
            limit=limit,
            order=order,
        )

    def _list(self, after, include, limit, order):
        """Internal 'next-page' behaviour for pagination"""

        return self._call_api(
            method="get",
            path="/v3/api-keys",
            query_params={
                "after": after,
                "include": include,
                "limit": limit,
                "order": order,
            },
            unpack=False,
        )

    def read(self):
        """Get API key details.
        """

        return self._call_api(
            method="get", path="/v3/api-keys/{apiKey}", path_params={"apiKey": self.id}
        )

    def update(self):
        """Update API key details.
        """

        return self._call_api(
            method="put",
            path="/v3/api-keys/{apiKey}",
            path_params={"apiKey": self.id},
            body_params={
                "groups": self.groups,
                "name": self.name,
                "owner": self.owner,
                "status": self.status,
            },
        )


class PSK(common.Entity):
    """Represents the `PSK` entity in Mbed Cloud"""

    _fieldnames = ["created_at", "endpoint_name"]

    def __init__(self, client=None, created_at=None, endpoint_name=None):
        """Creates a local `PSK` instance

        :param created_at: The date-time (RFC3339) when this pre-shared key was uploaded to Mbed Cloud.
        :type created_at: string
        :param endpoint_name: The unique endpoint identifier that this pre-shared key applies to. 16-64 [printable](https://en.wikipedia.org/wiki/ASCII#Printable_characters) (non-control) ASCII characters.
        :type endpoint_name: string
        """

        super().__init__(client=client)

        # Attributes
        self._created_at = created_at
        self._endpoint_name = endpoint_name

    @property
    def created_at(self):
        """The date-time (RFC3339) when this pre-shared key was uploaded to Mbed Cloud.
        
        api example: '2017-07-21T17:32:28.012Z'
        
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    @property
    def endpoint_name(self):
        """The unique endpoint identifier that this pre-shared key applies to. 16-64 [printable](https://en.wikipedia.org/wiki/ASCII#Printable_characters) (non-control) ASCII characters.
        
        api example: 'my-endpoint-0001'
        
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, value):
        self._endpoint_name = value

    def create(self, secret_hex):
        """Upload a pre-shared key to Mbed Cloud.
        
        :param secret_hex: The secret of the pre-shared key in hexadecimal. It is not case sensitive; 4a is same as 4A, and it is allowed with or without 0x in the beginning. The minimum length of the secret is 128 bits and maximum 256 bits.
        :type secret_hex: string
        
        """

        return self._call_api(
            method="post",
            path="/v2/device-shared-keys",
            body_params={"secret_hex": secret_hex},
        )

    def delete(self):
        """Remove a pre-shared key.
        """

        return self._call_api(
            method="delete", path="/v2/device-shared-keys/{endpoint_name}"
        )

    def list(self, after, limit):
        """List pre-shared keys.
        
        :param after: An offset token for fetching a specific page. Provided by the server.
        :type after: string
        :param limit: The number of entries per page
        :type limit: integer
        
        """

        return pagination.PaginatedResponse(
            func=self._list, lwrap_type=self.__class__, after=after, limit=limit
        )

    def _list(self, after, limit):
        """Internal 'next-page' behaviour for pagination"""

        return self._call_api(
            method="get",
            path="/v2/device-shared-keys",
            query_params={"after": after, "limit": limit},
            unpack=False,
        )

    def read(self):
        """Get a pre-shared key.
        """

        return self._call_api(
            method="get",
            path="/v2/device-shared-keys/{endpoint_name}",
            path_params={"endpoint_name": self.endpoint_name},
        )


class User(common.Entity):
    """Represents the `User` entity in Mbed Cloud"""

    _fieldnames = [
        "account_id",
        "address",
        "created_at",
        "creation_time",
        "email",
        "email_verified",
        "full_name",
        "groups",
        "id",
        "is_gtc_accepted",
        "is_marketing_accepted",
        "last_login_time",
        "login_history",
        "password",
        "password_changed_time",
        "phone_number",
        "status",
        "two_factor_auth_enabled",
        "updated_at",
        "username",
    ]

    def __init__(
        self,
        client=None,
        account_id=None,
        address=None,
        created_at=None,
        creation_time=None,
        email=None,
        email_verified=None,
        full_name=None,
        groups=None,
        id=None,
        is_gtc_accepted=None,
        is_marketing_accepted=None,
        last_login_time=None,
        login_history=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        two_factor_auth_enabled=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `User` instance

        :param account_id: The UUID of the account.
        :type account_id: string
        :param address: Address.
        :type address: string
        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: integer
        :param email: The email address.
        :type email: string
        :param email_verified: A flag indicating whether the user's email address has been verified or not.
        :type email_verified: boolean
        :param full_name: The full name of the user.
        :type full_name: string
        :param groups: A list of IDs of the groups this user belongs to.
        :type groups: array
        :param id: The UUID of the user.
        :type id: string
        :param is_gtc_accepted: A flag indicating that the General Terms and Conditions has been accepted.
        :type is_gtc_accepted: boolean
        :param is_marketing_accepted: A flag indicating that receiving marketing information has been accepted.
        :type is_marketing_accepted: boolean
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: integer
        :param login_history: Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format.
        :type login_history: array
        :param password: The password when creating a new user. It will be generated when not present in the request.
        :type password: string
        :param password_changed_time: A timestamp of the latest change of the user password, in milliseconds.
        :type password_changed_time: integer
        :param phone_number: Phone number.
        :type phone_number: string
        :param status: The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system.
        :type status: string
        :param two_factor_auth_enabled: A flag indicating whether 2-factor authentication (TOTP) has been enabled.
        :type two_factor_auth_enabled: boolean
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        :param username: A username containing alphanumerical letters and -,._@+= characters.
        :type username: string
        """

        super().__init__(client=client)

        # Attributes
        self._account_id = account_id
        self._address = address
        self._created_at = created_at
        self._creation_time = creation_time
        self._email = email
        self._email_verified = email_verified
        self._full_name = full_name
        self._groups = groups
        self._id = id
        self._is_gtc_accepted = is_gtc_accepted
        self._is_marketing_accepted = is_marketing_accepted
        self._last_login_time = last_login_time
        self._login_history = login_history
        self._password = password
        self._password_changed_time = password_changed_time
        self._phone_number = phone_number
        self._status = status
        self._two_factor_auth_enabled = two_factor_auth_enabled
        self._updated_at = updated_at
        self._username = username

    @property
    def account_id(self):
        """The UUID of the account.
        
        api example: '01619571e2e90242ac12000600000000'
        
        """
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    @property
    def address(self):
        """Address.
        
        api example: '110 Fulbourn Rd, Cambridge, United Kingdom'
        
        """
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    @property
    def creation_time(self):
        """A timestamp of the user creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        self._creation_time = value

    @property
    def email(self):
        """The email address.
        
        api example: 'user@arm.com'
        
        """
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def email_verified(self):
        """A flag indicating whether the user's email address has been verified or not.
        
        api example: True
        
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, value):
        self._email_verified = value

    @property
    def full_name(self):
        """The full name of the user.
        
        api example: 'User Doe'
        
        """
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def groups(self):
        """A list of IDs of the groups this user belongs to.
        
        """
        return self._groups

    @groups.setter
    def groups(self, value):
        self._groups = value

    @property
    def id(self):
        """The UUID of the user.
        
        api example: '01619571e2e89242ac12000600000000'
        
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def is_gtc_accepted(self):
        """A flag indicating that the General Terms and Conditions has been accepted.
        
        api example: True
        
        """
        return self._is_gtc_accepted

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, value):
        self._is_gtc_accepted = value

    @property
    def is_marketing_accepted(self):
        """A flag indicating that receiving marketing information has been accepted.
        
        api example: True
        
        """
        return self._is_marketing_accepted

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, value):
        self._is_marketing_accepted = value

    @property
    def last_login_time(self):
        """A timestamp of the latest login of the user, in milliseconds.
        
        api example: 1518630727688
        
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, value):
        self._last_login_time = value

    @property
    def login_history(self):
        """Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format.
        
        """
        return self._login_history

    @login_history.setter
    def login_history(self, value):
        self._login_history = value

    @property
    def password(self):
        """The password when creating a new user. It will be generated when not present in the request.
        
        api example: 'PZf9eEUH43DAPE9ULINFeuj'
        
        """
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def password_changed_time(self):
        """A timestamp of the latest change of the user password, in milliseconds.
        
        api example: 1518630727688
        
        """
        return self._password_changed_time

    @password_changed_time.setter
    def password_changed_time(self, value):
        self._password_changed_time = value

    @property
    def phone_number(self):
        """Phone number.
        
        api example: '+44 (1223) 400 400'
        
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def status(self):
        """The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system.
        
        api example: 'ACTIVE'
        
        """
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def two_factor_auth_enabled(self):
        """A flag indicating whether 2-factor authentication (TOTP) has been enabled.
        
        api example: True
        
        """
        return self._two_factor_auth_enabled

    @two_factor_auth_enabled.setter
    def two_factor_auth_enabled(self, value):
        self._two_factor_auth_enabled = value

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        self._updated_at = value

    @property
    def username(self):
        """A username containing alphanumerical letters and -,._@+= characters.
        
        api example: 'admin'
        
        """
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    def delete(self):
        """Delete a user.
        """

        return self._call_api(
            method="delete",
            path="/v3/users/{user-id}",
            path_params={"user-id": self.id},
            inbound_renames={"is_totp_enabled": "two_factor_auth_enabled"},
        )

    def group_ids(self, accountid, after, include, limit, order):
        """Get groups of the user.
        
        :param accountid: Account ID.
        :type accountid: string
        :param after: The entity ID to fetch after the given one.
        :type after: string
        :param include: Comma separated additional data to return. Currently supported: total_count
        :type include: string
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: integer
        :param order: The order of the records based on creation time, ASC or DESC; by default ASC
        :type order: string
        
        """

        return self._call_api(
            method="get",
            path="/v3/accounts/{accountID}/users/{user-id}/groups",
            path_params={"accountID": accountid},
            query_params={
                "after": after,
                "include": include,
                "limit": limit,
                "order": order,
            },
            inbound_renames={"is_totp_enabled": "two_factor_auth_enabled"},
        )

    def list(self, after, include, limit, order):
        """Get the details of all users.
        
        :param after: The entity ID to fetch after the given one.
        :type after: string
        :param include: Comma separated additional data to return. Currently supported: total_count
        :type include: string
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: integer
        :param order: The order of the records based on creation time, ASC or DESC; by default ASC
        :type order: string
        
        """

        return pagination.PaginatedResponse(
            func=self._list,
            lwrap_type=self.__class__,
            after=after,
            include=include,
            limit=limit,
            order=order,
        )

    def _list(self, after, include, limit, order):
        """Internal 'next-page' behaviour for pagination"""

        return self._call_api(
            method="get",
            path="/v3/users",
            query_params={
                "after": after,
                "include": include,
                "limit": limit,
                "order": order,
            },
            inbound_renames={"is_totp_enabled": "two_factor_auth_enabled"},
            unpack=False,
        )

    def read(self):
        """Details of a user.
        """

        return self._call_api(
            method="get",
            path="/v3/users/{user-id}",
            path_params={"user-id": self.id},
            inbound_renames={"is_totp_enabled": "two_factor_auth_enabled"},
        )

    def update(self):
        """Update user details.
        """

        return self._call_api(
            method="put",
            path="/v3/users/{user-id}",
            path_params={"user-id": self.id},
            body_params={
                "address": self.address,
                "full_name": self.full_name,
                "groups": self.groups,
                "is_gtc_accepted": self.is_gtc_accepted,
                "is_marketing_accepted": self.is_marketing_accepted,
                "phone_number": self.phone_number,
                "username": self.username,
            },
            inbound_renames={"is_totp_enabled": "two_factor_auth_enabled"},
        )
