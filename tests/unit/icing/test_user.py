import random

from tests.common import BaseCase


class TestUserFactory(BaseCase):
    """
    Samples
    """

    def get_user(self, **kwargs):
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        return sdk.factory.user(**kwargs)


    def test_attr(self):
        user = self.get_user()
        self.assertIsNone(user.phone_number)

    def test_attr_set(self):
        user = self.get_user(id='015f4d70658002420a010a1000000000')
        self.assertEqual(user.id, '015f4d70658002420a010a1000000000')

    def test_attr_read(self):
        user = self.get_user(id='015f4d70658002420a010a1000000000')
        user.read()
        self.assertEqual(user.id, '015f4d70658002420a010a1000000000')
        self.assertIsNotNone(user.phone_number)

    def test_attr_read(self):
        user = self.get_user(id='015f4d70658002420a010a1000000000')
        user.read()


class TestUserImplicit(TestUserFactory):

    def get_user(self, **kwargs):
        from mbed_cloud.sdk.api import User
        return User(**kwargs)


class TestUserExplicit(TestUserFactory):

    def get_user(self, **kwargs):
        from mbed_cloud.sdk.api import User
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        return User(client=sdk, **kwargs)  # instantiated object is introspectable


class TestUserLazyExplicit(TestUserFactory):
    def get_user(self, **kwargs):
        from mbed_cloud.sdk.api import User
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        u = User(**kwargs)  # instantiated object is introspectable
        u.client = sdk
        return u


class TestUserMethods(BaseCase):

    def test_attr_read_set(self):
        from mbed_cloud.sdk.api import User
        user = User(id='015f4d70658002420a010a1000000000')
        print(user.phone_number)
        user.read()

        print(user._phone_number.value)

        print(user.phone_number)
        print(user.created_at)
        print(user.updated_at)
        print(user.updated_at.year)

        new_number = str(random.randint(1e6, 1e7 - 1))
        user.phone_number = new_number
        self.assertEqual(user.phone_number, new_number)
        user.update()
        print(user.phone_number)

        user = User(id='015f4d70658002420a010a1000000000')
        self.assertEqual(user.phone_number, None)
        print(user.phone_number)
        user.read()
        self.assertEqual(user.phone_number, new_number)
        print(user.phone_number)

        print(user.groups)
        print(user.login_history)

    def test_paginate_get(self):
        from mbed_cloud.sdk.api import User
        user = User(id='015f4d70658002420a010a1000000000')
        user.read()
        print(user.group_ids(accountid=user.account_id))
