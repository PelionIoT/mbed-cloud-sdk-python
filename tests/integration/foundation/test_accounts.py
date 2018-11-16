"""Tests for entities in the account module."""

import random

from tests.common import BaseCase, CrudMixinTests

from mbed_cloud.sdk.entities import Account
from mbed_cloud.sdk.entities import ApiKey
from mbed_cloud.sdk.entities import User
from mbed_cloud.sdk.entities import UserInvitation
from mbed_cloud.sdk.entities import SubtenantTrustedCertificate
from mbed_cloud.sdk.entities import SubtenantUser
from mbed_cloud.sdk.entities import SubtenantUserInvitation

from mbed_cloud.sdk.common.exceptions import ApiErrorResponse


def random_string():
    return str(random.randint(1e6, 1e7 - 1))


@BaseCase._skip_in_ci
class TestAccount(BaseCase, CrudMixinTests):
    """Test certificate enrollment in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = Account
        super(TestAccount, cls).setUpClass()

    def test_policies(self):
        for account in Account().list(include="policies"):
            policies = account.policies
            self.assertIsInstance(policies, list)
            for policy in policies:
                self.assertIsInstance(policy.action, str)
                self.assertIsInstance(policy.allow, bool)
                self.assertIsInstance(policy.feature, str)
                self.assertIsInstance(policy.inherited, bool)

    def test_password_policy(self):
        for account in Account().list():
            if account.password_policy:
                self.assertIsInstance(account.password_policy, dict)

    def check_subtenant_listing(self, listmethod, expected_entity):
        count = 0
        for entity in listmethod(page_size=3, max_results=5):
            self.assertEqual(expected_entity, entity.__class__, "Unexpected class returned from the list method")
            count += 1

        self.assertTrue(count <= 5, "At most 5 entities should be returned due to the max_results parameter")

    def test_trusted_certificates(self):
        my_account = Account().me()
        self.check_subtenant_listing(my_account.trusted_certificates, SubtenantTrustedCertificate)

    def test_user_invitations(self):
        my_account = Account().me()
        self.check_subtenant_listing(my_account.user_invitations, SubtenantUserInvitation)

    def test_users(self):
        my_account = Account().me()
        self.check_subtenant_listing(my_account.users, SubtenantUser)

    def test_subtenant_user(self):
        """Example of creating a user in a subtenant account"""

        # Keep the example at the same indent level so the documentation looks sensible
        try:
            # an example: creating and managing a subtenant account
            from mbed_cloud.sdk.entities import Account, SubtenantUser

            # Populate the new account details
            new_subtenant = Account(
                display_name='sdk test bob',
                aliases=['sdk_test_bob_' + random_string()],
                end_market='connected warrens',
                # Admin user details
                admin_full_name='bob the wombat',
                admin_email='bob@example.com',
            )
            # Create the new account
            new_subtenant.create()
            # cloak
        except ApiErrorResponse as api_error:
            self.assertEqual(api_error.status_code, 403, "The limit of account creation may have been reached")

            account = None
            for account in Account().list():
                if account.display_name == "sdk_test_bob":
                    break
            self.assertIsNotNone(account, "Account could not be found")

            # Fake the creation
            new_subtenant = account
        finally:
            # uncloak
            account_id = new_subtenant.id
            print("This is my new Account ID: %s" % account_id)

            # cloak
            # Record the number of users to check that creating and deleting works
            num_users = len(new_subtenant.users())
            # uncloak

            # Populate the new user details
            new_user = SubtenantUser(
                # Link this user to the account
                account_id=account_id,
                # User details
                username='JaneDoeSDK',
                full_name='Jane Doe',
                email='jane.doe@example.com',
                phone_number='1800966228',
            )
            # Create the new user
            new_user.create()

            # end of example
            self.assertEqual(len(new_subtenant.users()), num_users+1, "There should be one more user")
            new_user.delete()
            self.assertEqual(len(new_subtenant.users()), num_users,
                             "The number of users should be back to it's original value")

@BaseCase._skip_in_ci
class TestApiKey(BaseCase, CrudMixinTests):
    """Test certificate issuer in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = ApiKey
        super(TestApiKey, cls).setUpClass()

    def test_me(self):
        my_apikey = ApiKey().me()
        self.assertTrue(my_apikey.key.startswith("ak_"))

@BaseCase._skip_in_ci
class TestUser(BaseCase, CrudMixinTests):
    """Test certificate issuer configuration in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = User
        super(TestUser, cls).setUpClass()

    def test_login_history(self):
        from datetime import datetime
        for user in User().list():
            if isinstance(user.login_history, list):
                for login in user.login_history:
                    self.assertIsInstance(login.date, datetime)
                    self.assertIsInstance(login.ip_address, str)
                    self.assertIsInstance(login.success, bool)
                    self.assertIsInstance(login.user_agent, str)

@BaseCase._skip_in_ci
class TestUserInvitation(BaseCase, CrudMixinTests):
    """Test certificates in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = UserInvitation
        super(TestUserInvitation, cls).setUpClass()

