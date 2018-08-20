import os

from mbed_cloud import utils
from mbed_cloud.sdk import common


class User:
    """Represents the remote `User` entity in Mbed Cloud"""

    def __init__(
        self,
        id=None,
        created_at=None,
        updated_at=None,
        status=None,
        username=None,
        password=None,
        full_name=None,
        email=None,
        address=None,
        phone_number=None,
        groups=None,
        is_gtc_accepted=None,
        is_marketing_accepted=None,
        email_verified=None,
        creation_time=None,
        last_login_time=None,
        password_changed_time=None,
        account_id=None,
        login_history=None,
        two_factor_auth_enabled=None,
    ):
        """Creates a local `User` instance

        :param id: The UUID of the user.
        :type id: string
        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        :param status: The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system.
        :type status: string
        :param username: A username containing alphanumerical letters and -,._@+= characters.
        :type username: string
        :param password: The password when creating a new user. It will be generated when not present in the request.
        :type password: string
        :param full_name: The full name of the user.
        :type full_name: string
        :param email: The email address.
        :type email: string
        :param address: Address.
        :type address: string
        :param phone_number: Phone number.
        :type phone_number: string
        :param groups: A list of IDs of the groups this user belongs to.
        :type groups: array
        :param is_gtc_accepted: A flag indicating that the General Terms and Conditions has been accepted.
        :type is_gtc_accepted: boolean
        :param is_marketing_accepted: A flag indicating that receiving marketing information has been accepted.
        :type is_marketing_accepted: boolean
        :param email_verified: A flag indicating whether the user's email address has been verified or not.
        :type email_verified: boolean
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: integer
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: integer
        :param password_changed_time: A timestamp of the latest change of the user password, in milliseconds.
        :type password_changed_time: integer
        :param account_id: The UUID of the account.
        :type account_id: string
        :param login_history: Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format.
        :type login_history: array
        :param two_factor_auth_enabled: A flag indicating whether 2-factor authentication (TOTP) has been enabled.
        :type two_factor_auth_enabled: boolean
        """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.groups = groups
        self.is_gtc_accepted = is_gtc_accepted
        self.is_marketing_accepted = is_marketing_accepted
        self.email_verified = email_verified
        self.creation_time = creation_time
        self.last_login_time = last_login_time
        self.password_changed_time = password_changed_time
        self.account_id = account_id
        self.login_history = login_history
        self.two_factor_auth_enabled = two_factor_auth_enabled
        self._fieldnames = [
            "id",
            "created_at",
            "updated_at",
            "status",
            "username",
            "password",
            "full_name",
            "email",
            "address",
            "phone_number",
            "groups",
            "is_gtc_accepted",
            "is_marketing_accepted",
            "email_verified",
            "creation_time",
            "last_login_time",
            "password_changed_time",
            "account_id",
            "login_history",
            "two_factor_auth_enabled",
        ]
        self._auth_api_key = os.getenv("MBED_CLOUD_SDK_API_KEY")
        self._auth_host = os.getenv("MBED_CLOUD_SDK_HOST")
        self._default_headers = {
            "Authorization": "Bearer %s" % self._auth_api_key,
            "UserAgent": utils.get_user_agent(),
        }

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})

    def read(self,):
        """Details of a user.
        """
        path_params = {}
        query = strip_none_values({})
        data = strip_none_values({})
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({}))
        response = requests.request(
            method="get",
            url="{host}/v3/users/{user-id}".format(
                host=self._auth_host or DEFAULT_HOST, **path_params
            ),
            json=data,
            params=query,
            headers=headers,
        )
        inbound_renames = {"is_totp_enabled": "two_factor_auth_enabled"}
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def update(self,):
        """Update user details.
        """
        path_params = {}
        query = strip_none_values({})
        data = strip_none_values(
            {
                "username": self.username,
                "full_name": self.full_name,
                "address": self.address,
                "phone_number": self.phone_number,
                "groups": self.groups,
                "is_gtc_accepted": self.is_gtc_accepted,
                "is_marketing_accepted": self.is_marketing_accepted,
                "is_totp_enabled": self.two_factor_auth_enabled,
            }
        )
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({}))
        response = requests.request(
            method="put",
            url="{host}/v3/users/{user-id}".format(
                host=self._auth_host or DEFAULT_HOST, **path_params
            ),
            json=data,
            params=query,
            headers=headers,
        )
        inbound_renames = {"is_totp_enabled": "two_factor_auth_enabled"}
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def delete(self,):
        """Delete a user.
        """
        path_params = {}
        query = strip_none_values({})
        data = strip_none_values({})
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({}))
        response = requests.request(
            method="delete",
            url="{host}/v3/users/{user-id}".format(
                host=self._auth_host or DEFAULT_HOST, **path_params
            ),
            json=data,
            params=query,
            headers=headers,
        )
        inbound_renames = {"is_totp_enabled": "two_factor_auth_enabled"}
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def list(self, limit, after, order, include):
        """Get the details of all users.
        """
        path_params = {}
        query = strip_none_values(
            {"limit": limit, "after": after, "order": order, "include": include}
        )
        data = strip_none_values({})
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({}))
        response = requests.request(
            method="get",
            url="{host}/v3/users".format(
                host=self._auth_host or DEFAULT_HOST, **path_params
            ),
            json=data,
            params=query,
            headers=headers,
        )
        inbound_renames = {"is_totp_enabled": "two_factor_auth_enabled"}
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def group_ids(self, limit, after, order, include, accountid):
        """Get groups of the user.
        """
        path_params = {"accountID": accountid}
        query = strip_none_values(
            {"limit": limit, "after": after, "order": order, "include": include}
        )
        data = strip_none_values({})
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({}))
        response = requests.request(
            method="get",
            url="{host}/v3/accounts/{accountID}/users/{user-id}/groups".format(
                host=self._auth_host or DEFAULT_HOST, **path_params
            ),
            json=data,
            params=query,
            headers=headers,
        )
        inbound_renames = {"is_totp_enabled": "two_factor_auth_enabled"}
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response
