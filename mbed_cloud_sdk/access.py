"""Functionality for access-related actions in mbed Cloud."""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI
from mbed_cloud_sdk import config
from mbed_cloud_sdk.decorators import catch_exceptions

# Import backend API
import mbed_cloud_sdk._backends.iam as iam
import mbed_cloud_sdk._backends.iam.rest as ApiException

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
    def list_api_keys(self, start=0, sort_by=None, sort_direction="asc"):
        """List the API keys registered in the organisation.

        :param start: Not yet implemented.
        :param sort_by: Not yet implemented.
        :param sort_direction: Not yet implemented.
        """
        api = iam.DeveloperApi()

        if start != 0 or sort_by is not None or sort_direction != "asc":
            raise NotImplementedError("Sorting and pagination is not yet implemented")

        # Return the data array
        return api.get_all_api_keys().data

    @catch_exceptions(ApiException)
    def get_api_key(self, api_key):
        """Get API key details for key registered in organisation.

        :param api_key: The key name (str)
        """
        api = iam.DeveloperApi()
        return api.get_api_key(api_key)

    @catch_exceptions(ApiException)
    def delete_api_key(self, api_key):
        """Delete an API key registered in the organisation.

        :param api_key: The key name (str)
        """
        api = iam.DeveloperApi()
        return api.delete_api_key(api_key)

    @catch_exceptions(ApiException)
    def create_api_key(self, name, groups=[], owner=None):
        """Create new API key registered to organisation.

        :param name: The name of the API key (str)
        :param groups: Optional list of group IDs (str)
        :param owner: Optional user ID owning the API key (str)
        """
        api = iam.DeveloperApi()
        body = iam.ApiKeyInfoReq(name=name, groups=groups, owner=owner)
        return api.create_api_key(body)

    @catch_exceptions(ApiException)
    def list_groups(self):
        """TODO: Write docstring."""
        api = iam.DeveloperApi()

        # Return the data array
        return api.get_all_groups().data

    @catch_exceptions(ApiException)
    def list_users(self):
        """TODO: Write docstring."""
        api = iam.AccountAdminApi()

        # Return the data array
        return api.get_all_users().data

    @catch_exceptions(ApiException)
    def get_user(self, user_id):
        """TODO: Write docstring."""
        api = iam.AccountAdminApi()
        return api.get_user(user_id)

    @catch_exceptions(ApiException)
    def update_user(self, user_id, **kwargs):
        """TODO: Write docstring."""
        api = iam.AccountAdminApi()
        body = iam.UserInfoReq(**kwargs)
        return api.update_user(user_id, body)

    @catch_exceptions(ApiException)
    def delete_user(self, user_id):
        """TODO: Write docstring."""
        api = iam.AccountAdminApi()
        api.delete_user(user_id)
        return

    @catch_exceptions(ApiException)
    def create_user(self, **kwargs):
        """TODO: Write docstring."""
        api = iam.AccountAdminApi()
        body = iam.UserInfoReq(**kwargs)
        return api.create_user(body)
