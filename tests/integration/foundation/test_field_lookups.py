# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

import datetime
import random

from tests.common import BaseCase

from mbed_cloud.sdk.modules.accounts import User
from mbed_cloud.sdk.modules.accounts import PolicyGroup


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
        group = PolicyGroup().list().first()

        new_user = self.new_user()
        new_user.group_ids = [group.id]
        new_user.create()
        self.created = new_user.id

        self.assertEqual('1800966228', new_user.phone_number)

        # we have at least one group id
        self.assertGreaterEqual(len(new_user.group_ids), 1)

        all_users = new_user.list()

        found = [user for user in all_users if user == new_user].pop()

        self.assertEqual(found, new_user)
        for user in all_users:
            if user.login_history:
                history_item = user.login_history.pop()
                self.assertIsInstance(history_item.date, datetime.datetime)

        my_groups = new_user.groups()
        for group in my_groups:
            self.assertGreaterEqual(group.user_count, 1)
