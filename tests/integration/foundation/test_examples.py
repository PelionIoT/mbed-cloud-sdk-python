# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

import os

from tests.common import BaseCase

from mbed_cloud.sdk import ApiErrorResponse
from mbed_cloud.pagination import PaginatedResponse


@BaseCase._skip_in_ci
class TestExamples(BaseCase):

    def test_hello_world(self):
        # an example: hello world
        from mbed_cloud.foundation import Device

        # List the first 10 devices on your Pelion Device Management account.
        for device in Device().list(max_results=10):
            print("Hello device %s" % device.name)
        # end of example

    def test_hello_world_with_sdk_instance(self):
        # an example: hello world with sdk instance
        from mbed_cloud import SDK

        # Create an instance of the Pelion Device Management SDK
        pelion_dm_sdk = SDK()
        # List the first 10 devices on your Pelion DM account
        for device in pelion_dm_sdk.foundation.device().list(max_results=10):
            print("Hello device %s" % device.name)
        # end of example

    def test_hello_world_with_multiple_api_keys(self):
        ACCOUNT_ONE_API_KEY = os.getenv("MBED_CLOUD_SDK_API_KEY")
        ACCOUNT_TWO_API_KEY = os.getenv("MBED_CLOUD_SDK_API_KEY")
        # an example: hello world with multiple api keys
        from mbed_cloud import SDK

        # Create instances of the Pelion Device Management SDK for two accounts
        account_one = SDK(api_key=ACCOUNT_ONE_API_KEY)
        account_two = SDK(api_key=ACCOUNT_TWO_API_KEY)

        # List the first 10 devices on the first account
        for device in account_one.foundation.device().list(max_results=10):
            print("Account One device %s" % device.name)

        # List the first 10 devices on the second account
        for device in account_two.foundation.device().list(max_results=10):
            print("Account Two device %s" % device.name)
        # end of example

    def test_quick(self):
        # an example: checking account status
        from mbed_cloud.foundation import Account
        from mbed_cloud.foundation.enums import AccountStatusEnum

        my_account = Account()
        my_account.me()
        print(my_account.display_name)
        is_active = my_account.status == AccountStatusEnum.ACTIVE
        # end of example
        self.assertTrue(is_active)

    def test_listing(self):
        # an example: listing api keys
        from mbed_cloud.foundation import ApiKey
        all_keys = ApiKey().list()
        all_key_names = [key.name for key in all_keys]
        # end of example
        self.assertGreaterEqual(len(all_key_names), 1)

    def test_really_custom_config(self):
        # an example: using custom hosts
        from mbed_cloud import SDK
        from mbed_cloud.sdk import Config
        config = Config(api_key='ak_1', host='https://example')
        all_users = SDK(config).foundation.user().list()
        # end of example
        self.assertIsInstance(all_users, PaginatedResponse)

    def test_custom_api_call(self):
        # an example: custom api call
        from mbed_cloud import SDK
        from mbed_cloud.foundation import User
        response = SDK().client.call_api('get', '/v3/users', query_params={'limit': 2})
        # response object from the`requests` library
        for user_data in response.json()['data']:
            user = User().from_api(**user_data)
        # end of example
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
