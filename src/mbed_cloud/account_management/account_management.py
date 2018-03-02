# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Functionality for Account Management related actions in Mbed Cloud."""
from __future__ import absolute_import
from __future__ import unicode_literals

# Import common functions and exceptions from frontend API
from mbed_cloud.core import BaseAPI
from mbed_cloud.core import BaseObject
from mbed_cloud.pagination import PaginatedResponse

from mbed_cloud.decorators import catch_exceptions

# Import backend API
from mbed_cloud._backends import iam
from mbed_cloud._backends.iam.models import AccountUpdateReq
from mbed_cloud._backends.iam.rest import ApiException


class AccountManagementAPI(BaseAPI):
    """API reference for the AccountManagement API.

    Exposing functionality for creating and managing accounts,
    users, groups and API keys in the organisation.
    """

    api_structure = {iam: [iam.DeveloperApi, iam.AccountAdminApi]}

    @catch_exceptions(ApiException)
    def list_api_keys(self, **kwargs):
        """List the API keys registered in the organisation.

        List api keys Example:

        .. code-block:: python

            account_management_api = AccountManagementAPI()

            # List api keys
            api_keys_paginated_response = account_management_api.list_api_keys()
            # get single api key
            api_keys_paginated_response.data[0]

        :param int limit: Number of API keys to get
        :param str after: Entity ID after which to start fetching
        :param str order: Order of the records to return (asc|desc)
        :param dict filters: Dictionary of filters to apply: str owner (eq)
        :returns: a list of :class:`ApiKey` objects
        :rtype: PaginatedResponse
        :raises: ApiException
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, ApiKey)

        api = self._get_api(iam.DeveloperApi)

        # Return the data array
        return PaginatedResponse(api.get_all_api_keys, lwrap_type=ApiKey, **kwargs)

    @catch_exceptions(ApiException)
    def get_api_key(self, api_key_id):
        """Get API key details for key registered in organisation.

        :param str api_key_id: The ID of the API key to be updated (Required)
        :returns: API key object
        :rtype: ApiKey
        """
        api = self._get_api(iam.DeveloperApi)
        return ApiKey(api.get_api_key(api_key_id))

    @catch_exceptions(ApiException)
    def delete_api_key(self, api_key_id):
        """Delete an API key registered in the organisation.

        :param str api_key_id: The ID of the API key (Required)
        :returns: void
        """
        api = self._get_api(iam.DeveloperApi)
        api.delete_api_key(api_key_id)
        return

    @catch_exceptions(ApiException)
    def add_api_key(self, name, **kwargs):
        """Create new API key registered to organisation.

        :param str name: The name of the API key (Required)
        :param list groups: List of group IDs (`str`)
        :param str owner: User ID owning the API key
        :param str status: The status of the API key. Values: ACTIVE, INACTIVE
        :returns: Newly created API key object
        :rtype: ApiKey
        """
        api = self._get_api(iam.DeveloperApi)
        kwargs.update({'name': name})
        api_key = ApiKey._create_request_map(kwargs)
        body = iam.ApiKeyInfoReq(**api_key)
        return ApiKey(api.create_api_key(body))

    @catch_exceptions(ApiException)
    def update_api_key(self, api_key_id, **kwargs):
        """Update API key.

        :param str api_key_id: The ID of the API key to be updated (Required)
        :param str name: The name of the API key
        :param str owner: User ID owning the API key
        :param str status: The status of the API key. Values: ACTIVE, INACTIVE
        :returns: Newly created API key object
        :rtype: ApiKey
        """
        api = self._get_api(iam.DeveloperApi)
        apikey = ApiKey._create_request_map(kwargs)
        body = iam.ApiKeyUpdateReq(**apikey)
        return ApiKey(api.update_api_key(api_key_id, body))

    @catch_exceptions(ApiException)
    def list_users(self, **kwargs):
        """List all users in organisation.

        :param int limit: The number of users to retrieve
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get users after/starting at given user ID
        :param dict filters: Dictionary of filters to apply: str status (eq)
        :returns: a list of :py:class:`User` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, User)
        api = self._get_api(iam.AccountAdminApi)
        return PaginatedResponse(api.get_all_users, lwrap_type=User, **kwargs)

    @catch_exceptions(ApiException)
    def get_user(self, user_id):
        """Get user details of specified user.

        :param str user_id: the ID of the user to get (Required)
        :returns: the user object with details about the user.
        :rtype: User
        """
        api = self._get_api(iam.AccountAdminApi)
        return User(api.get_user(user_id))

    @catch_exceptions(ApiException)
    def update_user(self, user_id, **kwargs):
        """Update user properties of specified user.

        :param str user_id: The ID of the user to update (Required)
        :param str username: The unique username of the user
        :param str email: The unique email of the user
        :param str full_name: The full name of the user
        :param str password: The password string of the user.
        :param str phone_number: Phone number of the user
        :param bool terms_accepted: Is 'General Terms & Conditions' accepted
        :param bool marketing_accepted: Is receiving marketing information accepted?
        :returns: the updated user object
        :rtype: User
        """
        api = self._get_api(iam.AccountAdminApi)
        user = User._create_request_map(kwargs)
        body = iam.UserUpdateReq(**user)
        return User(api.update_user(user_id, body))

    @catch_exceptions(ApiException)
    def delete_user(self, user_id):
        """Delete user specified user.

        :param str user_id: the ID of the user to delete (Required)
        :returns: void
        """
        api = self._get_api(iam.AccountAdminApi)
        api.delete_user(user_id)
        return

    @catch_exceptions(ApiException)
    def add_user(self, username, email, **kwargs):
        """Create a new user with provided details.

        Add user example:

        .. code-block:: python

            account_management_api = AccountManagementAPI()
            # Add user
            user = {
                "username": "test_user",
                "email": "test@gmail.com",
                "phone_number": "0123456789"
            }
            new_user = account_management_api.add_user(**user)

        :param str username: The unique username of the user (Required)
        :param str email: The unique email of the user (Required)
        :param str full_name: The full name of the user
        :param list groups: List of group IDs (`str`) which this user belongs to
        :param str password: The password string of the user
        :param str phone_number: Phone number of the user
        :param bool terms_accepted: 'General Terms & Conditions' have been accepted
        :param bool marketing_accepted: Marketing Information opt-in
        :returns: the new user object
        :rtype: User
        """
        api = self._get_api(iam.AccountAdminApi)
        kwargs.update({'username': username, 'email': email})
        user = User._create_request_map(kwargs)
        body = iam.UserUpdateReq(**user)
        return User(api.create_user(body))

    @catch_exceptions(ApiException)
    def get_account(self):
        """Get details of the current account.

        :returns: an account object.
        :rtype: Account
        """
        api = self._get_api(iam.DeveloperApi)
        return Account(api.get_my_account_info(include="limits, policies"))

    @catch_exceptions(ApiException)
    def update_account(self, **kwargs):
        """Update details of account associated with current API key.

        :param str address_line1: Postal address line 1.
        :param str address_line2: Postal address line 2.
        :param str city: The city part of the postal address.
        :param str display_name: The display name for the account.
        :param str country: The country part of the postal address.
        :param str company: The name of the company.
        :param str state: The state part of the postal address.
        :param str contact: The name of the contact person for this account.
        :param str postal_code: The postal code part of the postal address.
        :param str parent_id: The ID of the parent account.
        :param str phone_number: The phone number of the company.
        :param str email: Email address for this account.
        :param list[str] aliases: List of aliases
        :returns: an account object.
        :rtype: Account
        """
        api = self._get_api(iam.AccountAdminApi)
        account = Account._create_request_map(kwargs)
        body = AccountUpdateReq(**account)
        return Account(api.update_my_account(body))

    @catch_exceptions(ApiException)
    def list_groups(self, **kwargs):
        """List all groups in organisation.

        :param int limit: The number of groups to retrieve
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get groups after/starting at given group ID
        :returns: a list of :py:class:`Group` objects.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self._get_api(iam.DeveloperApi)
        return PaginatedResponse(api.get_all_groups, lwrap_type=Group, **kwargs)

    @catch_exceptions(ApiException)
    def get_group(self, group_id):
        """Get details of the group.

        :param str group_id: The group ID (Required)
        :returns: :py:class:`Group` object.
        :rtype: Group
        """
        api = self._get_api(iam.DeveloperApi)
        return Group(api.get_group_summary(group_id))

    @catch_exceptions(ApiException)
    def list_group_users(self, group_id, **kwargs):
        """List users of a group.

        :param str group_id: The group ID (Required)
        :param int limit: The number of users to retrieve
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get API keys after/starting at given user ID
        :returns: a list of :py:class:`User` objects.
        :rtype: PaginatedResponse
        """
        kwargs["group_id"] = group_id
        kwargs = self._verify_sort_options(kwargs)
        api = self._get_api(iam.AccountAdminApi)
        return PaginatedResponse(api.get_users_of_group, lwrap_type=User, **kwargs)

    @catch_exceptions(ApiException)
    def list_group_api_keys(self, group_id, **kwargs):
        """List API keys of a group.

        :param str group_id: The group ID (Required)
        :param int limit: The number of api keys to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc).
        :param str after: Get API keys after/starting at given api key ID.
        :returns: a list of :py:class:`ApiKey` objects.
        :rtype: PaginatedResponse
        """
        kwargs["group_id"] = group_id
        kwargs = self._verify_sort_options(kwargs)
        api = self._get_api(iam.DeveloperApi)
        return PaginatedResponse(api.get_api_keys_of_group, lwrap_type=ApiKey, **kwargs)


class Account(BaseObject):
    """Describes account object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Get account owning the API key in use
        current_account = api.get_account()
        print(current_account.company)
    """

    @staticmethod
    def _get_attributes_map():
        return {
            "display_name": "display_name",
            "aliases": "aliases",
            "company": "company",
            "contact": "contact",
            "email": "email",
            "phone_number": "phone_number",
            "address_line1": "address_line1",
            "address_line2": "address_line2",
            "city": "city",
            "state": "state",
            "postcode": "postal_code",
            "country": "country",
            "id": "id",
            "status": "status",
            "tier": "tier",
            "limits": "limits",
            "policies": "policies",
            "provisioning_allowed": "is_provisioning_allowed",
            "created_at": "created_at",
            "upgraded_at": "upgraded_at",
            "updated_at": "updated_at",
            "reason": "reason",
            "template_id": "template_id",
            "custom_properties": "account_properties",
            "sales_contact_email": "sales_contact",
            "contract_number": "contract_number",
            "customer_number": "customer_number",
            "reference_note": "reference_note",
            "notification_emails": "notification_emails",
            "multifactor_authentication_status": "mfa_status",
            "expiry_warning": "expiration_warning_threshold",
        }

    @property
    def display_name(self):
        """The display name for the account.

        :rtype: str
        """
        return self._display_name

    @property
    def aliases(self):
        """An array of aliases.

        :rtype: str[]
        """
        return self._aliases

    @property
    def company(self):
        """The name of the company.

        :rtype: str
        """
        return self._company

    @property
    def contact(self):
        """The name of the contact person for this account.

        :rtype: str
        """
        return self._contact

    @property
    def email(self):
        """The company email address for this account.

        :rtype: str
        """
        return self._email

    @property
    def phone_number(self):
        """The phone number of the company.

        :rtype: str
        """
        return self._phone_number

    @property
    def address_line1(self):
        """Postal address line 1.

        :rtype: str
        """
        return self._address_line1

    @property
    def address_line2(self):
        """Postal address line 2.

        :rtype: str
        """
        return self._address_line2

    @property
    def city(self):
        """The city part of the postal address.

        :rtype: str
        """
        return self._city

    @property
    def state(self):
        """The state part of the postal address.

        :rtype: str
        """
        return self._state

    @property
    def postcode(self):
        """The postal code part of the postal address.

        :rtype: str
        """
        return self._postcode

    @property
    def country(self):
        """The country part of the postal address.

        :rtype: str
        """
        return self._country

    @property
    def id(self):
        """Account ID (readonly).

        :rtype: str
        """
        return self._id

    @property
    def status(self):
        """The status of the account.

        values: ENROLLING, ACTIVE, RESTRICTED, SUSPENDED

        :rtype: str
        """
        return self._status

    @property
    def tier(self):
        """The tier level of the account; '0': free tier, '1': commercial account.

        Other values are reserved for the future.

        :rtype: str
        """
        return self._tier

    @property
    def limits(self):
        """List of limits as key-value pairs if requested.

        :rtype: list of Limits
        """
        return self._limits

    @property
    def policies(self):
        """List of policies if requested.

        :rtype: list of Policies
        """
        return self._policies

    @property
    def provisioning_allowed(self):
        """Flag (true/false) indicating whether Factory Tool is allowed to download or not.

        :rtype: bool
        """
        return self._provisioning_allowed

    @property
    def created_at(self):
        """Creation UTC time RFC3339.

        :rtype: datetime
        """
        return self._created_at

    @property
    def upgraded_at(self):
        """Time when upgraded to commercial account in UTC format RFC3339.

        :rtype: datetime
        """
        return self._upgraded_at

    @property
    def reason(self):
        """A note about the reason for updating the status of the account.

        :rtype: str
        """
        return self._reason

    @property
    def template_id(self):
        """Account template ID.

        :rtype: str
        """
        return self._template_id

    @property
    def contract_number(self):
        """Gets the contract_number of this AccountInfo.

        Contract number of the customer.

        :return: The contract_number of this AccountInfo.
        :rtype: str
        """
        return self._contract_number

    @property
    def custom_properties(self):
        """Gets the custom_properties of this AccountInfo.

        Account specific custom properties.

        :return: The account_properties of this AccountInfo.
        :rtype: dict(str, dict(str, str))
        """
        return self._custom_properties

    @property
    def customer_number(self):
        """Gets the customer_number of this AccountInfo.

        Customer number of the customer.

        :return: The customer_number of this AccountInfo.
        :rtype: str
        """
        return self._customer_number

    @property
    def reference_note(self):
        """Gets the reference_note of this AccountInfo.

        A reference note for updating the status of the account

        :return: The reference_note of this AccountInfo.
        :rtype: str
        """
        return self._reference_note

    @property
    def notification_emails(self):
        """Gets the notification_emails of this AccountInfo.

        A list of notification email addresses.

        :return: The notification_emails of this AccountInfo.
        :rtype: list[str]
        """
        return self._notification_emails

    @property
    def sales_contact_email(self):
        """Gets the sales_contact_email of this AccountInfo.

        Email address of the sales contact.

        :return: The sales_contact_email of this AccountInfo.
        :rtype: str
        """
        return self._sales_contact_email

    @property
    def multifactor_authentication_status(self):
        """Gets the multifactor_authentication_status of this AccountInfo.

        The enforcement status of the multi-factor authentication, either 'enforced' or 'optional'.

        :return: The mfa_status of this AccountInfo.
        :rtype: str
        """
        return self._multifactor_authentication_status

    @property
    def expiry_warning(self):
        """Gets the expiry_warning of this AccountInfo.

        Indicates how many days (1-180) before account expiration
        a notification email should be sent.

        :return: The expiration_warning_threshold of this AccountInfo.
        :rtype: str
        """
        return self._expiry_warning

    @property
    def updated_at(self):
        """Gets the updated_at of this AccountInfo.

        Last update UTC time RFC3339.

        :return: The updated_at of this AccountInfo.
        :rtype: datetime
        """
        return self._updated_at


class User(BaseObject):
    """Describes user object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Listing existing users
        for idx, user in enumerate(api.list_users())
            print(user.full_name)

        # Creating a new user
        new_user = api.add_user("username",
                                "user@example.org",
                                full_name = "David Bowie",
                                password = "hunter2")
    """

    def __init__(self, dictionary):
        """Initialize object."""
        super(User, self).__init__(dictionary)
        self._login_history = [LoginHistory(login) for login in getattr(self, 'login_history')]

    @staticmethod
    def _get_attributes_map():
        return {
            "full_name": "full_name",
            "username": "username",
            "password": "password",
            "email": "email",
            "phone_number": "phone_number",
            "address": "address",
            "terms_accepted": "is_gtc_accepted",
            "marketing_accepted": "is_marketing_accepted",
            "groups": "groups",
            "id": "id",
            "status": "status",
            "account_id": "account_id",
            "email_verified": "email_verified",
            "created_at": "created_at",
            "creation_time": "creation_time",
            "password_changed_time": "password_changed_time",
            "last_login_time": "last_login_time",
            "two_factor_authentication": "is_totp_enabled",
            "login_history": "login_history",
            "custom_properties": "user_properties",
        }

    @property
    def full_name(self):
        """The full name of the user.

        :rtype: str
        """
        return self._full_name

    @property
    def username(self):
        """A username containing alphanumerical letters and -,._@+= characters.

        :rtype: str
        """
        return self._username

    @property
    def password(self):
        """The password when creating a new user. It will be generated when not present in the request.

        :rtype: str
        """
        return self._password

    @property
    def email(self):
        """The email address.

        :rtype: str
        """
        return self._email

    @property
    def phone_number(self):
        """Phone number.

        :rtype: str
        """
        return self._phone_number

    @property
    def address(self):
        """Address.

        :rtype: str
        """
        return self._address

    @property
    def terms_accepted(self):
        """A flag indicating that the General Terms and Conditions has been accepted.

        :rtype: bool
        """
        return self._terms_accepted

    @property
    def marketing_accepted(self):
        """A flag indicating that receiving marketing information has been accepted.

        :rtype: bool
        """
        return self._marketing_accepted

    @property
    def groups(self):
        """A list of group IDs this user belongs to (readonly).

        :rtype: str[]
        """
        return self._groups

    @property
    def id(self):
        """The UUID of the user (readonly).

        :rtype: str
        """
        return self._id

    @property
    def status(self):
        """The status of the user (readonly).

        INVITED means that the user has not accepted the invitation request.
        RESET means that the password must be changed immediately.
        values: ENROLLING, INVITED, ACTIVE, RESET, INACTIVE

        :rtype: str
        """
        return self._status

    @property
    def account_id(self):
        """The UUID of the account (readonly).

        :rtype: str
        """
        return self._account_id

    @property
    def email_verified(self):
        """A flag indicating whether the user's email address has been verified or not.

        :rtype: bool
        """
        return self._email_verified

    @property
    def created_at(self):
        """Creation UTC time RFC3339 (readonly).

        :rtype: datetime
        """
        return self._created_at

    @property
    def creation_time(self):
        """A timestamp of the user creation in the storage, in milliseconds (readonly).

        :rtype: int
        """
        return self._creation_time

    @property
    def password_changed_time(self):
        """A timestamp of the latest change of the user password, in milliseconds (readonly).

        :rtype: int
        """
        return self._password_changed_time

    @property
    def last_login_time(self):
        """A timestamp of the latest login of the user, in milliseconds (readonly).

        :rtype: int
        """
        return self._last_login_time

    @property
    def two_factor_authentication(self):
        """Whether two factor authentication has been enabled for this user (readonly).

        :rtype: bool
        """
        return self._two_factor_authentication

    @property
    def login_history(self):
        """History of logins for this user (readonly).

        :returns: List of LoginHistory.
        :rtype: LoginHistory
        """
        return self._login_history

    @property
    def custom_properties(self):
        """User properties

        :returns: dictionary of properties
        :rtype: dict(str, dict(str, str))
        """
        return self._custom_properties


class Group(BaseObject):
    """Describes group object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Listing existing groups
        for idx, g in enumerate(api.list_groups())
            print(g.name)
    """

    @staticmethod
    def _get_attributes_map():
        return {
            "id": "id",
            "account_id": "account_id",
            "name": "name",
            "user_count": "user_count",
            "api_key_count": "apikey_count",
            "created_at": "created_at",
            "creation_time": "creation_time",
            "last_update_time": "last_update_time",
        }

    @property
    def id(self):
        """The UUID of the group. (readonly)

        :rtype: str
        """
        return self._id

    @property
    def account_id(self):
        """The UUID of the account this group belongs to. (readonly)

        :rtype: str
        """
        return self._account_id

    @property
    def name(self):
        """The name of the group. (readonly)

        :rtype: str
        """
        return self._name

    @property
    def user_count(self):
        """The number of users in this group. (readonly)

        :rtype: int
        """
        return self._user_count

    @property
    def api_key_count(self):
        """The number of API keys in this group. (readonly)

        :rtype: int
        """
        return self._api_key_count

    @property
    def created_at(self):
        """Creation UTC time RFC3339. (readonly)

        :rtype: datetime
        """
        return self._created_at

    @property
    def creation_time(self):
        """A timestamp of the group creation in the storage, in milliseconds. (readonly)

        :rtype: int
        """
        return self._creation_time

    @property
    def last_update_time(self):
        """The last update time

        :rtype: datetime
        """
        return self._last_update_time


class ApiKey(BaseObject):
    """Describes API key object.

    Example usage:

    .. code-block:: python

        api = AccountManagementAPI()

        # Listing existing keys
        for idx, k in enumerate(api.list_api_keys()):
            print(k.name, k.key)

        # Creating a new key
        new_k = api.add_api_key("New key name")
        print(new_k.key)
    """

    @staticmethod
    def _get_attributes_map():
        return {
            "name": "name",
            "owner_id": "owner",
            "groups": "groups",
            "id": "id",
            "key": "key",
            "status": "status",
            "created_at": "created_at",
            "creation_time": "creation_time",
            "last_login_time": "last_login_time"
        }

    @property
    def name(self):
        """The display name for the API key.

        :rtype: str
        """
        return self._name

    @property
    def owner_id(self):
        """The owner of this API key, who is the creator by default.

        :rtype: str
        """
        return self._owner_id

    @property
    def groups(self):
        """A list of group IDs this API key belongs to.

        :rtype: str[]
        """
        return self._groups

    @property
    def id(self):
        """The UUID of the API key. (readonly)

        :rtype: str
        """
        return self._id

    @property
    def key(self):
        """The API key. (readonly)

        :rtype: str
        """
        return self._key

    @property
    def status(self):
        """The status of the API key. (readonly)

        values: ACTIVE, INACTIVE

        :rtype: str
        """
        return self._status

    @property
    def created_at(self):
        """Creation UTC time RFC3339. (readonly)

        :rtype: datetime
        """
        return self._created_at

    @property
    def creation_time(self):
        """The timestamp of the API key creation in the storage, in milliseconds. (readonly)

        :rtype: int
        """
        return self._creation_time

    @property
    def last_login_time(self):
        """The timestamp of the latest API key usage, in milliseconds. (readonly)

        :rtype: int
        """
        return self._last_login_time


class LoginHistory(BaseObject):
    """Login History."""

    @staticmethod
    def _get_attributes_map():
        return {
            "date": "date",
            "user_agent": "user_agent",
            "ip_address": "ip_address",
            "success": "success"
        }

    @property
    def date(self):
        """Date of login.

        :rtype: datetime
        """
        return self._date

    @property
    def user_agent(self):
        """User agent used for login.

        :rtype: str
        """
        return self._user_agent

    @property
    def ip_address(self):
        """IP Address login from.

        :rtype: str
        """
        return self._ip_address

    @property
    def success(self):
        """Whether login was successful.

        :rtype: bool
        """
        return self._success
