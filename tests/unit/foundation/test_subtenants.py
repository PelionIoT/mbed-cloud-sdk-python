# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

from tests.common import BaseCase

from mbed_cloud.sdk.modules.accounts import MyAccount
from mbed_cloud.sdk.modules.accounts import SubtenantAccount


class TestSubTenants(BaseCase):

    def test_flow(self):
        my_account = MyAccount().get()

        new_subtenant = SubtenantAccount(
            parent_id=my_account.id,
            display_name='sdk_test_bob',
            end_market='connected warrens',
            admin_full_name='bob the wombat',
            admin_email='bob@example.com',
        )
        new_subtenant.create()

        # check that our account now has some subtenants
        subtenants = list(SubtenantAccount().list(parent__eq=my_account.id))
        self.assertGreaterEqual(len(subtenants), 1)

        # check that we can retrieve the auto-created api key for this new account
        keys = list(subtenants[0].api_keys())
        self.assertEqual(1, len(keys))

        nested = SubtenantAccount(
            parent_id=new_subtenant.id,
            display_name='sdk_test_sam',
            end_market='connected warrens',
            admin_full_name='sam the wombat',
            admin_email='sam@example.com',
        )
        nested.create()

        # again check that we can retrieve the auto-created api key for this new account
        keys = nested.api_keys()
        self.assertEqual(1, len(keys))
