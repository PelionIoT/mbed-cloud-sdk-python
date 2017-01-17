"""Functionality for access-related actions in mbed Cloud."""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import config
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.iam as iam
from mbed_cloud._backends.iam.models import AccountInfo
import mbed_cloud._backends.iam.rest as ApiException

LOG = logging.getLogger(__name__)


class AccessAPI(BaseAPI):
    """Describing the public access API.

    Exposing functionality from the following underlying services:
        - IAM
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
        :returns: a list of API key objects
        """
        api = iam.DeveloperApi()

        # Return the data array
        return PaginatedResponse(api.get_all_api_keys, **kwargs)

    @catch_exceptions(ApiException)
    def get_account_details(self):
        """Get details of the current account.

        :returns: an account object.
        :rtype: Account
        """
        api = iam.DeveloperApi()
        return api.get_my_account_info()

    @catch_exceptions(ApiException)
    def get_api_key(self, api_key):
        """Get API key details for key registered in organisation.

        :param api_key: The key name (str)
        :returns: a API key object.
        """
        api = iam.DeveloperApi()
        return api.get_api_key(api_key)

    @catch_exceptions(ApiException)
    def delete_api_key(self, api_key):
        """Delete an API key registered in the organisation.

        :param api_key: The key name (str)
        :returns: void
        """
        api = iam.DeveloperApi()
        return api.delete_api_key(api_key)

    @catch_exceptions(ApiException)
    def create_api_key(self, name, groups=[], owner=None):
        """Create new API key registered to organisation.

        :param name: The name of the API key (str)
        :param groups: Optional list of group IDs (list[str])
        :param owner: Optional user ID owning the API key (str)
        :returns: a list of API key objects.
        """
        api = iam.DeveloperApi()
        body = iam.ApiKeyInfoReq(name=name, groups=groups, owner=owner)
        return api.create_api_key(body)

    @catch_exceptions(ApiException)
    def list_groups(self, start=0, sort_by=None, sort_direction="asc"):
        """List all groups in organisation.

        :param start: Not yet implemented.
        :param sort_by: Not yet implemented.
        :param sort_direction: Not yet implemented.
        :returns: a list of group objects.
        """
        if start != 0 or sort_by is not None or sort_direction != "asc":
            raise NotImplementedError("Sorting and pagination is not yet implemented")

        api = iam.DeveloperApi()
        # Return the data array
        return api.get_all_groups().data

    @catch_exceptions(ApiException)
    def list_users(self, start=0, sort_by=None, sort_direction="asc"):
        """List all users in organisation.

        :param start: Not yet implemented.
        :param sort_by: Not yet implemented.
        :param sort_direction: Not yet implemented.
        :returns: a list of user objects.
        """
        if start != 0 or sort_by is not None or sort_direction != "asc":
            raise NotImplementedError("Sorting and pagination is not yet implemented")

        api = iam.AccountAdminApi()
        # Return the data array
        return api.get_all_users().data

    @catch_exceptions(ApiException)
    def get_user(self, user_id):
        """Get user details of specified user.

        :param user_id: the ID of the user to get (str)
        :returns: the user object with details about the user.
        """
        api = iam.AccountAdminApi()
        return api.get_user(user_id)

    @catch_exceptions(ApiException)
    def update_user(self, user_id, **kwargs):
        """Update user properties of specified user.

        Accepts same parameters as `create_user`.

        :param user_id: the ID of the user to update (str)
        :returns: the updated user object, as it was called with `get_user`.
        """
        api = iam.AccountAdminApi()
        body = iam.UserInfoReq(**kwargs)
        return api.update_user(user_id, body)

    @catch_exceptions(ApiException)
    def delete_user(self, user_id):
        """Delete user specified user.

        :param user_id: the ID of the user to delete (str)
        :returns: void
        """
        api = iam.AccountAdminApi()
        api.delete_user(user_id)
        return

    @catch_exceptions(ApiException)
    def create_user(self, username, email, **kwargs):
        """Create a new user with provided details.

        :param username: Required. The unique username of the user (str)
        :param email: Required. The unique email of the user (str)
        :param full_name: Optional. The full name of the user (str)
        :param groups: Optional. List of group IDs which this user belongs to (list[str])
        :param password: Optional. The password string of the user.
            Need to adhere to password policy (str)
        :param phone_number: Optional. Phone number of the user (str)
        :param is_gtc_accepted: Optional. Is 'General Terms & Conditions' accepted (bool)
        :param is_marketing_accepted: Optional. Is receiving marketing information accepted? (bool)
        :returns: the new user as it was called using `get_user`.
        """
        api = iam.AccountAdminApi()
        kwargs.update({'username': username, 'email': email})
        body = iam.UserInfoReq(**kwargs)
        return api.create_user(body)

class Account(AccountInfo):
    """Describes account object."""

    def __init__(self, account_info_obj):
        """Override __init__ and allow passing in backend object."""
        super(Account, self).__init__(**account_info_obj.to_dict())
