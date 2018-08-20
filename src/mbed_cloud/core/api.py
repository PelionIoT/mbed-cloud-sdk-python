from mbed_cloud import pagination
from mbed_cloud.core import common


class PSK(common.Entity):
    """Represents the remote `PSK` entity in Mbed Cloud"""

    _fieldnames = ["created_at", "endpoint_name"]
    __slots__ = _fieldnames

    def __init__(self, created_at=None, endpoint_name=None):
        """Creates a local `PSK` instance
        :param created_at: The date-time (RFC3339) when this pre-shared key was uploaded to Mbed Cloud.
        :type created_at: string
        :param endpoint_name: The unique endpoint identifier that this pre-shared key applies to. 16-64 [printable](https://en.wikipedia.org/wiki/ASCII#Printable_characters) (non-control) ASCII characters.
        :type endpoint_name: string
        """

        super(PSK).__init__()

        # Attributes
        self.created_at = created_at
        self.endpoint_name = endpoint_name

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


class AccountGroup(common.Entity):
    """Represents the remote `AccountGroup` entity in Mbed Cloud"""

    _fieldnames = [
        "account_id",
        "apikey_count",
        "code",
        "created_at",
        "id",
        "message",
        "name",
        "request_id",
        "type",
        "updated_at",
        "user_count",
    ]
    __slots__ = _fieldnames

    def __init__(
        self,
        account_id=None,
        apikey_count=None,
        code=None,
        created_at=None,
        id=None,
        message=None,
        name=None,
        request_id=None,
        type=None,
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
        :param type: Response type: success.
        :type type: string
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        :param user_count: The number of users in this group.
        :type user_count: integer
        """

        super(AccountGroup).__init__()

        # Attributes
        self.account_id = account_id
        self.apikey_count = apikey_count
        self.code = code
        self.created_at = created_at
        self.id = id
        self.message = message
        self.name = name
        self.request_id = request_id
        self.type = type
        self.updated_at = updated_at
        self.user_count = user_count

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
    """Represents the remote `ApiKey` entity in Mbed Cloud"""

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
    __slots__ = _fieldnames

    def __init__(
        self,
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

        super(ApiKey).__init__()

        # Attributes
        self.created_at = created_at
        self.creation_time = creation_time
        self.groups = groups
        self.id = id
        self.key = key
        self.last_login_time = last_login_time
        self.name = name
        self.owner = owner
        self.status = status
        self.updated_at = updated_at

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

        return self._call_api(method="get", path="/v3/api-keys/{apiKey}")

    def update(self):
        """Update API key details.
        """

        return self._call_api(
            method="put",
            path="/v3/api-keys/{apiKey}",
            body_params={
                "groups": self.groups,
                "name": self.name,
                "owner": self.owner,
                "status": self.status,
            },
        )


class User(common.Entity):
    """Represents the remote `User` entity in Mbed Cloud"""

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
    __slots__ = _fieldnames

    def __init__(
        self,
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

        super(User).__init__()

        # Attributes
        self.account_id = account_id
        self.address = address
        self.created_at = created_at
        self.creation_time = creation_time
        self.email = email
        self.email_verified = email_verified
        self.full_name = full_name
        self.groups = groups
        self.id = id
        self.is_gtc_accepted = is_gtc_accepted
        self.is_marketing_accepted = is_marketing_accepted
        self.last_login_time = last_login_time
        self.login_history = login_history
        self.password = password
        self.password_changed_time = password_changed_time
        self.phone_number = phone_number
        self.status = status
        self.two_factor_auth_enabled = two_factor_auth_enabled
        self.updated_at = updated_at
        self.username = username

    def delete(self):
        """Delete a user.
        """

        return self._call_api(
            method="delete",
            path="/v3/users/{user-id}",
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
            inbound_renames={"is_totp_enabled": "two_factor_auth_enabled"},
        )

    def update(self):
        """Update user details.
        """

        return self._call_api(
            method="put",
            path="/v3/users/{user-id}",
            body_params={
                "address": self.address,
                "full_name": self.full_name,
                "groups": self.groups,
                "is_gtc_accepted": self.is_gtc_accepted,
                "is_marketing_accepted": self.is_marketing_accepted,
                "phone_number": self.phone_number,
                "is_totp_enabled": self.two_factor_auth_enabled,
                "username": self.username,
            },
            inbound_renames={"is_totp_enabled": "two_factor_auth_enabled"},
        )
