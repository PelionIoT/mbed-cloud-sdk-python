import logging

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI, config
from mbed_cloud_sdk.decorators import catch_exceptions

# Import backend API
import mbed_cloud_sdk.access.iam as iam
import mbed_cloud_sdk.access.iam.rest as ApiException

logger = logging.getLogger(__name__)

class AccountsAPI(BaseAPI):
    def __init__(self):
        # Set the api_key for the requests
        iam.configuration.api_key['Authorization'] = config.get("api_key")
        iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

    @catch_exceptions(ApiException)
    def list_api_keys(self):
        api = iam.DeveloperApi()

        # Return the data array
        return api.get_all_api_keys().data

    @catch_exceptions(ApiException)
    def get_api_key(self, api_key):
        api = iam.DeveloperApi()
        return api.get_api_key(api_key)

    @catch_exceptions(ApiException)
    def delete_api_key(self, api_key):
        api = iam.DeveloperApi()
        return api.delete_api_key(api_key)

    @catch_exceptions(ApiException)
    def list_groups(self):
        api = iam.DeveloperApi()

        # Return the data array
        return api.get_all_groups().data

    @catch_exceptions(ApiException)
    def list_users(self):
        api = iam.AccountAdminApi()

        # Return the data array
        return api.get_all_users().data

    @catch_exceptions(ApiException)
    def get_user(self, user_id):
        api = iam.AccountAdminApi()
        return api.get_user(user_id)

    @catch_exceptions(ApiException)
    def update_user(self, user_id, **kwargs):
        api = iam.AccountAdminApi()
        body = iam.UserInfoReq(**kwargs)
        return api.update_user(user_id, body)

    @catch_exceptions(ApiException)
    def delete_user(self, user_id):
        api = iam.AccountAdminApi()
        api.delete_user(user_id)
        return

    @catch_exceptions(ApiException)
    def create_user(self, **kwargs):
        api = iam.AccountAdminApi()
        body = iam.UserInfoReq(**kwargs)
        return api.create_user(body)
