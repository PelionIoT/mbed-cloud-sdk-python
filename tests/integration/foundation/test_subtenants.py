# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

import unittest
import random
from tests.common import BaseCase

from mbed_cloud.sdk import SDK
from mbed_cloud.sdk.common import util
from mbed_cloud.sdk.modules.accounts import SubtenantAccount


def random_string():
    return str(random.randint(1e6, 1e7 - 1))


@unittest.skip('accounts cant be removed after creation')
class TestSubTenants(BaseCase):
    """Demonstrate a subtenant workflow"""
    def test_flow(self):
        # an example: creating and managing a subtenant account
        new_subtenant = SubtenantAccount(
            display_name='sdk test bob',
            aliases=['sdk_test_bob_'+random_string()],
            end_market='connected warrens',
            admin_full_name='bob the wombat',
            admin_email='bob@example.com',
        )
        # when creating a new subtenant, this is the only opportunity to obtain
        # the `admin_key` for that subtenant account
        new_subtenant.create()  # populates new_subtenant.admin_key

        print(util.pretty_literal(new_subtenant.to_literal()))

        # now log in as this subtenant using the `admin_key`
        sdk = SDK(api_key=new_subtenant.admin_key)

        # and add another user
        user_name = 'jo_the_wombat_'+random_string()
        user = sdk.entities.user()
        user.full_name = 'jo the wombat'
        user.username = user_name
        user.phone_number = '1800966228'
        user.email = 'jo_%s@example.com' % random_string()
        user.create()

        # back as the aggregator again ...
        users = list(new_subtenant.users())
        self.assertEqual(2, len(users))

        for user in users:
            print(util.pretty_literal(user.to_literal()))
        # end of example

        if not any(user.username == user_name for user in users):
            self.fail('no user here')
