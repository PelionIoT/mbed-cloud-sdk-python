# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

import random

from tests.common import BaseCase

from mbed_cloud.sdk import enums
from mbed_cloud.sdk import entities
from mbed_cloud.sdk import common


class TestAccount(BaseCase):

    def test_attr_read_set(self):
        user = entities.User(id='015f4d70658002420a010a1000000000')
        user.get()
        account_id = user.account_id
        g = user.groups()
        print(list(g))
        # account = entities.Account(id=account_id)
        # account.get()
        # print(common.pretty_literal(account.to_literal()))

        sub_account = entities.SubtenantAccount(id=account_id)
        sub_account.get(accountid=user.account_id)
        # print(common.pretty_literal(sub_account.to_literal()))
        account_users = sub_account.users(accountid=user.account_id, groupid=user.group_ids[0])

        print(account_users.first().to_literal())