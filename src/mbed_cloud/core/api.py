import os

import requests
import dotenv

from mbed_cloud import utils

dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True))
DEFAULT_HOST = 'https://api.us-east-1.mbedcloud.com'

def pluck_if_not_none(source, *pluck):
    return {k: source[k] for k in pluck if source[k] is not None}

def strip_none_values(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}


class User:
    """Represents the remote `User` entity in Mbed Cloud"""
    def __init__(self, id=None, created_at=None, updated_at=None, status=None, username=None, password=None, full_name=None, email=None, address=None, phone_number=None, groups=None, is_gtc_accepted=None, is_marketing_accepted=None, email_verified=None, creation_time=None, last_login_time=None, password_changed_time=None, account_id=None, login_history=None, two_factor_auth_enabled=None, ):
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
            'id',
            'created_at',
            'updated_at',
            'status',
            'username',
            'password',
            'full_name',
            'email',
            'address',
            'phone_number',
            'groups',
            'is_gtc_accepted',
            'is_marketing_accepted',
            'email_verified',
            'creation_time',
            'last_login_time',
            'password_changed_time',
            'account_id',
            'login_history',
            'two_factor_auth_enabled',
        ]
        self._auth_api_key = os.getenv('MBED_CLOUD_SDK_API_KEY')
        self._auth_host = os.getenv('MBED_CLOUD_SDK_HOST')
        self._default_headers = {
            'Authorization': 'Bearer %s' % self._auth_api_key,
            'UserAgent': utils.get_user_agent(),
        }

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})

    def read(
        self,
    ):
        """Details of a user.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='get',
            url='{host}/v3/users/{user-id}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
            'is_totp_enabled': 'two_factor_auth_enabled',
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def update(
        self,
    ):
        """Update user details.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='put',
            url='{host}/v3/users/{user-id}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
            'is_totp_enabled': 'two_factor_auth_enabled',
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def delete(
        self,
    ):
        """Delete a user.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='delete',
            url='{host}/v3/users/{user-id}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
            'is_totp_enabled': 'two_factor_auth_enabled',
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def list(
        self,
        limit,
        after,
        order,
        include,
        email__eq,
        status__eq,
        status__in,
        status__nin,
    ):
        """Get the details of all users.
        """
        path_params = {
        }
        query = strip_none_values({
            'limit': limit,
            'after': after,
            'order': order,
            'include': include,
            'email__eq': email__eq,
            'status__eq': status__eq,
            'status__in': status__in,
            'status__nin': status__nin,
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='get',
            url='{host}/v3/users'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
            'is_totp_enabled': 'two_factor_auth_enabled',
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response


class ApiKey:
    """Represents the remote `ApiKey` entity in Mbed Cloud"""
    def __init__(self, id=None, created_at=None, updated_at=None, key=None, name=None, groups=None, owner=None, status=None, creation_time=None, last_login_time=None, ):
        """Creates a local `ApiKey` instance

        :param id: The UUID of the API key.
        :type id: string
        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        :param key: The API key.
        :type key: string
        :param name: The display name for the API key.
        :type name: string
        :param groups: A list of group IDs this API key belongs to.
        :type groups: array
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: string
        :param status: The status of the API key.
        :type status: string
        :param creation_time: The timestamp of the API key creation in the storage, in milliseconds.
        :type creation_time: integer
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: integer
        """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.key = key
        self.name = name
        self.groups = groups
        self.owner = owner
        self.status = status
        self.creation_time = creation_time
        self.last_login_time = last_login_time
        self._fieldnames = [
            'id',
            'created_at',
            'updated_at',
            'key',
            'name',
            'groups',
            'owner',
            'status',
            'creation_time',
            'last_login_time',
        ]
        self._auth_api_key = os.getenv('MBED_CLOUD_SDK_API_KEY')
        self._auth_host = os.getenv('MBED_CLOUD_SDK_HOST')
        self._default_headers = {
            'Authorization': 'Bearer %s' % self._auth_api_key,
            'UserAgent': utils.get_user_agent(),
        }

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})

    def create(
        self,
    ):
        """Create a new API key.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='post',
            url='{host}/v3/api-keys'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def read(
        self,
    ):
        """Get API key details.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='get',
            url='{host}/v3/api-keys/{apiKey}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def update(
        self,
    ):
        """Update API key details.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='put',
            url='{host}/v3/api-keys/{apiKey}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def delete(
        self,
    ):
        """Delete API key.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='delete',
            url='{host}/v3/api-keys/{apiKey}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def list(
        self,
        limit,
        after,
        order,
        include,
        key__eq,
        owner__eq,
    ):
        """Get all API keys
        """
        path_params = {
        }
        query = strip_none_values({
            'limit': limit,
            'after': after,
            'order': order,
            'include': include,
            'key__eq': key__eq,
            'owner__eq': owner__eq,
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='get',
            url='{host}/v3/api-keys'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response


class PSK:
    """Represents the remote `PSK` entity in Mbed Cloud"""
    def __init__(self, endpoint_name=None, created_at=None, ):
        """Creates a local `PSK` instance

        :param endpoint_name: The unique endpoint identifier that this pre-shared key applies to. 16-64 [printable](https://en.wikipedia.org/wiki/ASCII#Printable_characters) (non-control) ASCII characters.
        :type endpoint_name: string
        :param created_at: The date-time (RFC3339) when this pre-shared key was uploaded to Mbed Cloud.
        :type created_at: string
        """
        self.endpoint_name = endpoint_name
        self.created_at = created_at
        self._fieldnames = [
            'endpoint_name',
            'created_at',
        ]
        self._auth_api_key = os.getenv('MBED_CLOUD_SDK_API_KEY')
        self._auth_host = os.getenv('MBED_CLOUD_SDK_HOST')
        self._default_headers = {
            'Authorization': 'Bearer %s' % self._auth_api_key,
            'UserAgent': utils.get_user_agent(),
        }

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})

    def create(
        self,
    ):
        """Upload a pre-shared key to Mbed Cloud.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='post',
            url='{host}/v2/device-shared-keys'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def read(
        self,
    ):
        """Get a pre-shared key.
        """
        path_params = {
            'endpoint_name': self.endpoint_name,
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='get',
            url='{host}/v2/device-shared-keys/{endpoint_name}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def delete(
        self,
    ):
        """Remove a pre-shared key.
        """
        path_params = {
        }
        query = strip_none_values({
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='delete',
            url='{host}/v2/device-shared-keys/{endpoint_name}'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response

    def list(
        self,
        limit,
        after,
    ):
        """List pre-shared keys.
        """
        path_params = {
        }
        query = strip_none_values({
            'limit': limit,
            'after': after,
        })
        data = strip_none_values({
        })
        headers = {}
        headers.update(self._default_headers)
        headers.update(strip_none_values({
        }))
        response = requests.request(
            method='get',
            url='{host}/v2/device-shared-keys'.format(host=self._auth_host or DEFAULT_HOST, **path_params),
            json=data,
            params=query,
            headers=headers
        )
        inbound_renames = {
        }
        if response.status_code // 100 == 2:
            for k, v in response.json().items():
                setattr(self, inbound_renames.get(k, k), v)
        else:
            print(response.content)
        response.raise_for_status()
        return response
