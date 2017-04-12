# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Functionality for access-related actions in mbed Cloud."""
from __future__ import absolute_import

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import config
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.iam as iam
from mbed_cloud._backends.iam.models import AccountInfo
from mbed_cloud._backends.iam.models import AccountUpdateReq
from mbed_cloud._backends.iam.models import ApiKeyInfoResp
from mbed_cloud._backends.iam.models import GroupSummary
from mbed_cloud._backends.iam.models import UserInfoResp
import mbed_cloud._backends.iam.rest as ApiException


class AccessAPI(BaseAPI):
    """API reference for the Access API.

    Exposing functionality for creating and managing accounts,
    users, groups and API keys in the organisation.
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(AccessAPI, self).__init__(params)

        # Set the api_key for the requests
        iam.configuration.api_key['Authorization'] = config.get("api_key")
        iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

        # Override host, if defined
        if config.get("host"):
            iam.configuration.host = config.get("host")

    @catch_exceptions(ApiException)
    def list_api_keys(self, **kwargs):
        """List the API keys registered in the organisation.

        :param limit: Number of API keys to get (int)
        :param after: Entity ID after which to start fetching (str)
        :param order: Order of the records to return (asc|desc) (str)
        :returns: a list of :py:class:`ApiKey` objects
        :rtype: PaginatedResponse
        """
        api = iam.DeveloperApi()

        # Return the data array
        return PaginatedResponse(api.get_all_api_keys, lwrap_type=ApiKey, **kwargs)

    @catch_exceptions(ApiException)
    def get_api_key(self, api_key):
        """Get API key details for key registered in organisation.

        :param api_key: The ID of the API key to be updated
        :returns: API key object
        :rtype: ApiKey
        """
        api = iam.DeveloperApi()
        return ApiKey(api.get_api_key(api_key))

    @catch_exceptions(ApiException)
    def delete_api_key(self, api_key):
        """Delete an API key registered in the organisation.

        :param api_key: The ID of the API key
        :returns: void
        """
        api = iam.DeveloperApi()
        api.delete_api_key(api_key)
        return

    @catch_exceptions(ApiException)
    def add_api_key(self, name, groups=[], owner=None):
        """Create new API key registered to organisation.

        :param str name: The name of the API key
        :param list groups: Optional list of group IDs (`str`)
        :param str owner: Optional user ID owning the API key
        :returns: Newly created API key object
        :rtype: ApiKey
        """
        api = iam.DeveloperApi()
        body = iam.ApiKeyInfoReq(name=name, groups=groups, owner=owner)
        return ApiKey(api.create_api_key(body))

    @catch_exceptions(ApiException)
    def update_api_key(self, api_key, name, owner=None):
        """Update API key.

        :param str api_key: The ID of the API key to be updated.
        :param str name: The name of the API key.
        :param str owner: Optional user ID owning the API key.
        :returns: Newly created API key object
        :rtype: ApiKey
        """
        api = iam.DeveloperApi()
        body = iam.ApiKeyUpdateReq(name=name, owner=owner)
        return ApiKey(api.update_api_key(api_key, body))

    @catch_exceptions(ApiException)
    def list_users(self, **kwargs):
        """List all users in organisation.

        :param int limit: The number of devices to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get devices after/starting at given user ID
        :returns: a list of :py:class:`User` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)

        api = iam.AccountAdminApi()
        return PaginatedResponse(api.get_all_users, lwrap_type=User, **kwargs)

    @catch_exceptions(ApiException)
    def get_user(self, user_id):
        """Get user details of specified user.

        :param str user_id: the ID of the user to get
        :returns: the user object with details about the user.
        :rtype: User
        """
        api = iam.AccountAdminApi()
        return User(api.get_user(user_id))

    @catch_exceptions(ApiException)
    def update_user(self, user_id, **kwargs):
        """Update user properties of specified user.

        Accepts same parameters as `add_user`.

        :param str user_id: the ID of the user to update
        :returns: the updated user object
        :rtype: User
        """
        api = iam.AccountAdminApi()
        body = iam.UserInfoReq(**kwargs)
        return User(api.update_user(user_id, body))

    @catch_exceptions(ApiException)
    def delete_user(self, user_id):
        """Delete user specified user.

        :param str user_id: the ID of the user to delete
        :returns: void
        """
        api = iam.AccountAdminApi()
        api.delete_user(user_id)
        return

    @catch_exceptions(ApiException)
    def add_user(self, username, email, **kwargs):
        """Create a new user with provided details.

        :param str username: Required. The unique username of the user
        :param str email: Required. The unique email of the user
        :param str full_name: Optional. The full name of the user
        :param list groups: Optional. List of group IDs (`str`) which this user belongs to
        :param str password: Optional. The password string of the user.
            Need to adhere to password policy
        :param str phone_number: Optional. Phone number of the user
        :param bool is_gtc_accepted: Optional. Is 'General Terms & Conditions' accepted
        :param bool is_marketing_accepted: Optional. Is receiving marketing information accepted?
        :returns: the new user object
        :rtype: User
        """
        api = iam.AccountAdminApi()
        kwargs.update({'username': username, 'email': email})
        body = iam.UserInfoReq(**kwargs)
        return User(api.create_user(body))

    @catch_exceptions(ApiException)
    def get_account(self):
        """Get details of the current account.

        :returns: an account object.
        :rtype: Account
        """
        api = iam.DeveloperApi()
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
        api = iam.AccountAdminApi()
        body = AccountUpdateReq(**kwargs)
        return Account(api.update_my_account(body))

    @catch_exceptions(ApiException)
    def list_groups(self, **kwargs):
        """List all groups in organisation.

        :param int limit: The number of groups to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get groups after/starting at given group ID
        :returns: a list of :py:class:`Group` objects.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)

        api = iam.DeveloperApi()
        return PaginatedResponse(api.get_all_groups, lwrap_type=Group, **kwargs)

    @catch_exceptions(ApiException)
    def get_group(self, group_id):
        """Get details of the group.

        :param str group_id: The group ID.
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get groups after/starting at given group ID
        :returns: :py:class:`Group` object.
        :rtype: Group
        """
        api = iam.DeveloperApi()
        return Group(api.get_group_summary(group_id))

    @catch_exceptions(ApiException)
    def list_group_users(self, group_id, **kwargs):
        """List users of a group.

        :param str group_id: The group ID.
        :param int limit: The number of users to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc).
        :param str after: Get api keys after/starting at given user ID.
        :returns: a list of :py:class:`User` objects.
        :rtype: PaginatedResponse
        """
        kwargs["group_id"] = group_id
        kwargs = self._verify_sort_options(kwargs)

        api = iam.AccountAdminApi()
        return PaginatedResponse(api.get_users_of_group, lwrap_type=User, **kwargs)

    @catch_exceptions(ApiException)
    def list_group_api_keys(self, group_id, **kwargs):
        """List API keys of a group.

        :param str group_id: The group ID.
        :param int limit: The number of api keys to retrieve.
        :param str order: The ordering direction, ascending (asc) or descending (desc).
        :param str after: Get api keys after/starting at given api key ID.
        :returns: a list of :py:class:`ApiKey` objects.
        :rtype: PaginatedResponse
        """
        kwargs["group_id"] = group_id
        kwargs = self._verify_sort_options(kwargs)
        api = iam.DeveloperApi()
        return PaginatedResponse(api.get_api_keys_of_group, lwrap_type=ApiKey, **kwargs)


class Account(AccountInfo):
    """Describes account object.

    Example usage:

    .. code-block:: python

        api = AccessAPI()

        # Get account owning the API key in use
        current_account = api.get_account()
        print(current_account.company)
    """

    def __init__(self, account_info_obj):
        """Override __init__ and allow passing in backend object."""
        super(Account, self).__init__(**account_info_obj.to_dict())


class User(UserInfoResp):
    """Describes user object.

    Example usage:

    .. code-block:: python

        api = AccessAPI()

        # Listing existing users
        for user, idx in api.list_users().iteritems()
            print(user.full_name)

        # Creating a new user
        new_user = api.add_user("username",
                                "user@example.org",
                                full_name = "David Bowie",
                                password = "hunter2")
    """

    def __init__(self, user_obj):
        """Override __init__ and allow passing in backend object."""
        super(User, self).__init__(**user_obj.to_dict())


class Group(GroupSummary):
    """Describes group object.

    Example usage:

    .. code-block:: python

        api = AccessAPI()

        # Listing existing groups
        for g, idx in api.list_groups().iteritems():
            print(g.name)
    """

    def __init__(self, group_obj):
        """Override __init__ and allow passing in backend object."""
        super(Group, self).__init__(**group_obj.to_dict())


class ApiKey(ApiKeyInfoResp):
    """Describes API key object.

    Example usage:

    .. code-block:: python

        api = AccessAPI()

        # Listing existing keys
        for k, idx in api.list_api_keys().iteritems():
            print(k.name, k.key)

        # Creating a new key
        new_k = api.add_api_key("New key name")
        print(new_k.key)
    """

    def __init__(self, api_key_obj):
        """Override __init__ and allow passing in backend object."""
        super(ApiKey, self).__init__(**api_key_obj.to_dict())
