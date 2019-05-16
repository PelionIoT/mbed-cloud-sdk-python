# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

import datetime

from tests.common import BaseCase

from mbed_cloud.foundation import User
from mbed_cloud.sdk.exceptions import ApiErrorResponse

@BaseCase._skip_in_ci
class TestLookups(BaseCase):
    """This test should implement something like the following sequence:

    plain attr -> print / read / set / read / print phone number
    list of ids - > print first id of group_ids
    paginated self -> print first full_name of first user
    list of nested -> print first date of first loginhistory
    paginated other -> print name of first group

    """

    created = None

    def new_user(self):
        return User(
            username='wombat',
            full_name='Scratchy The Wombat',
            email='wombat1@thewombat.den',
            phone_number='1800966228',
        )

    def tearDown(self):
        if self.created:
            User(id=self.created).delete()

    def test_modify_simple_attributes(self):
        new_user = self.new_user()
        self.assertEqual('1800966228', new_user.phone_number)
        new_user.phone_number = '0800966228'
        self.assertEqual('0800966228', new_user.phone_number)

    def test_sequence(self):

        new_user = self.new_user()

        try:
            new_user.create()
        except ApiErrorResponse as api_error:
            # If there is an error then it should be a 409
            # as at some point the user was not deleted
            self.assertEqual(api_error.status_code, 409)
        else:
            self.created = new_user.id

            self.assertEqual('1800966228', new_user.phone_number, "User should have been created with the phone number")
            new_user.phone_number = '999'
            self.assertEqual('999', new_user.phone_number, "The phone number property should contain the local update")

            new_user.read()
            self.assertEqual('1800966228', new_user.phone_number,
                             "After getting the user the local update should be reverted")

            new_user.phone_number = '0800966228'
            new_user.update()
            new_user.read()
            self.assertEqual('0800966228', new_user.phone_number,
                             "The local update should now be in the replicated in the cloud")
