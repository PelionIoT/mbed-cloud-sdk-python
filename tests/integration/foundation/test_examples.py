# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

import os

from tests.common import BaseCase

from mbed_cloud.sdk import ApiErrorResponse
from mbed_cloud.pagination import PaginatedResponse
from mbed_cloud.foundation import User


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

    def test_crud_of_an_entity(self):
        """Example of create, read, update and delete of a user"""
        from mbed_cloud import SDK

        pelion_dm_sdk = SDK()

        num_users = len(pelion_dm_sdk.foundation.user().list())

        # Keep the example at the same indent level so the documentation looks sensible
        try:
            # an example: create an entity
            new_user = pelion_dm_sdk.foundation.user(
                email="python.sdk.user@arm.com",
            )
            new_user.create()
            # end of example

            self.assertEqual(len(User().list()), num_users+1, "The number of users should have increase")
            user_id = new_user.id

            # an example: read an entity
            user_one = pelion_dm_sdk.foundation.user(id=user_id).read()
            print("User email address: %s" % user_one.email)
            # end of example

            # an example: update an entity
            user_two = pelion_dm_sdk.foundation.user(id=user_id).read()
            user_two.full_name = "Python SDK User"
            user_two.update()
            # end of example

            self.assertEqual(user_two.read().full_name, "Python SDK User", "User name should have been changed")

            # an example: delete an entity
            pelion_dm_sdk.foundation.user(id=user_id).delete()
            # end of example

        except Exception:
            new_user.delete()
        self.assertEqual(len(User().list()), num_users, "The number of users should be back to it's original value")

    def test_list_entities(self):
        from mbed_cloud import SDK

        pelion_dm_sdk = SDK()

        # an example: list entities
        paginator = pelion_dm_sdk.foundation.user().list(
            order="ASC",
            page_size=5,
            max_results=10,
            include="total_count")

        for user in paginator:
            print("%s (%s): %s" % (user.full_name, user.id, user.email))

        print("Total Count: %d" % paginator.count())
        # end of example

    def test_read_first_entity_in_list(self):
        from mbed_cloud import SDK

        pelion_dm_sdk = SDK()

        # an example: read first entity in list
        first_user_in_list = pelion_dm_sdk.foundation.user().list().first()
        print("User email address: %s" % first_user_in_list.email)
        # end of example

    def test_list_entities_with_filters(self):
        from mbed_cloud import SDK
        pelion_dm_sdk = SDK()

        # an example: list entities with filters
        from mbed_cloud import ApiFilter
        from mbed_cloud.foundation.enums import UserStatusEnum

        api_filter = ApiFilter()
        api_filter.add_filter("email", "eq", "python.sdk.user@arm.com")
        api_filter.add_filter("status", "in", [UserStatusEnum.ACTIVE, UserStatusEnum.ENROLLING])

        for user in pelion_dm_sdk.foundation.user().list(filter=api_filter):
            print("%s (%s): %s" % (user.full_name, user.id, user.email))
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

    def test_certificate_black_listing(self):
        from mbed_cloud.foundation import TrustedCertificate

        # Find a production certificate
        my_certificate = TrustedCertificate().list(filter={"device_execution_mode": {"neq": 1}}).first()
        my_cert_id = my_certificate.id
        # Record the original status to revert to it's original state at the end
        original_status = TrustedCertificate(id=my_cert_id).read().status

        # an example: certificate black listing
        from mbed_cloud import SDK
        from mbed_cloud import ApiFilter
        from mbed_cloud.foundation.enums import TrustedCertificateStatusEnum

        pelion_dm_sdk = SDK()

        # Set the certificate to inactive
        my_cert = pelion_dm_sdk.foundation.trusted_certificate(id=my_cert_id).read()
        my_cert.status = TrustedCertificateStatusEnum.INACTIVE
        my_cert.update()

        # List all devices which have tried to bootstrap
        api_filter = ApiFilter()
        api_filter.add_filter("trusted_certificate_id", "eq", my_cert)

        for device_denial in pelion_dm_sdk.foundation.device_enrollment_denial().list(filter=api_filter):
            print("Device endpoint name: %s" % device_denial.endpoint_name)
        # end of example

        new_status = my_cert.read().status
        self.assertEqual(TrustedCertificateStatusEnum.INACTIVE, new_status, "Status should have been set to disabled")

        # Revert the certificate to its original status
        my_cert.status = original_status
        my_cert.update()

        end_status = my_cert.read().status
        self.assertEqual(original_status, end_status, "Status should have been reverted back to its original value")
