# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

from tests.common import BaseCase

from mbed_cloud.sdk import ApiErrorResponse
from mbed_cloud.pagination import PaginatedResponse


@BaseCase._skip_in_ci
class TestExamples(BaseCase):

    def test_quick(self):
        # an example: checking account status
        from mbed_cloud.sdk.entities import Account
        from mbed_cloud.sdk.enums import AccountStatusEnum

        my_account = Account()
        my_account.me()
        print(my_account.display_name)
        is_active = my_account.status == AccountStatusEnum.ACTIVE
        # end of example
        self.assertTrue(is_active)

    def test_listing(self):
        # an example: listing api keys
        from mbed_cloud.sdk.entities import ApiKey
        all_keys = ApiKey().list()
        all_key_names = [key.name for key in all_keys]
        # end of example
        self.assertGreaterEqual(len(all_key_names), 1)

    def test_custom_config(self):
        with self.assertRaises(ApiErrorResponse):
            # an example: using multiple api keys
            from mbed_cloud.sdk import SDK
            all_users = []
            for account_key in ('ak_1', 'ak_2'):
                all_users.extend(SDK(api_key=account_key).entities.user().list())
            # end of example

    def test_really_custom_config(self):
        # an example: using custom hosts
        from mbed_cloud.sdk import SDK
        from mbed_cloud.sdk import Config
        config = Config(api_key='ak_1', host='https://example')
        all_users = SDK(config).entities.user().list()
        # end of example
        self.assertIsInstance(all_users, PaginatedResponse)

    def test_custom_api_call(self):
        # an example: custom api call
        from mbed_cloud.sdk import SDK
        from mbed_cloud.sdk.entities import User
        response = SDK().client.call_api('get', '/v3/users', query_params={'limit': 2})
        # response object from the`requests` library
        for user_data in response.json()['data']:
            user = User().from_api(**user_data)
        # end of example
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
