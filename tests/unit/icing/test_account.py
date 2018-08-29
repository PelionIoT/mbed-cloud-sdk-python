# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

from tests.common import BaseCase

from mbed_cloud.sdk.modules import accounts
from mbed_cloud.sdk import common


class TestAccount(BaseCase):

    def test_attr_read_set(self):
        user = accounts.User(id='015f4d70658002420a010a1000000000')
        user.get()
        user.creation_time
        account_id = user.account_id
        # g = user.groups()
        # print(list(g))
        # account = entities.Account(id=account_id)
        # account.get()
        # print(common.pretty_literal(account.to_literal()))

        sub_account = accounts.SubtenantAccount(id=account_id)
        sub_account.get()
        sub_account.api_keys(group_id=user.group_ids[0])
        # print(common.pretty_literal(sub_account.to_literal()))
        account_users = sub_account.users(group_id=user.group_ids[0])

        print(common.pretty_literal(account_users.first().to_literal()))

        sub_account.create()