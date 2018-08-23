import random

from tests.common import BaseCase

from mbed_cloud.sdk import enums


class TestPSK(BaseCase):

    def test_list(self):
        from mbed_cloud.sdk.api import PSK
        psk = PSK()
        all = psk.list()


    def test_related(self):
        from mbed_cloud.sdk.api import User
        user = User(id='015f4d70658002420a010a1000000000')
        user.read()
        for g in user.group_ids:
            print('group_ids', g)

    def test_nested(self):
        from mbed_cloud.sdk.api import User
        user = User(id='015f4d70658002420a010a1000000000')
        user.read()
        print(user)
        for history in user.login_history:
            print(history)

    def test_paginate_get(self):
        from mbed_cloud.sdk.api import User
        user = User(id='015f4d70658002420a010a1000000000')
        user.read()
        groups = user.groups()
        print(type(groups))
        print(len(groups))
        print(user.group_ids)
        for group in groups:
            print(group)
        print(groups)
