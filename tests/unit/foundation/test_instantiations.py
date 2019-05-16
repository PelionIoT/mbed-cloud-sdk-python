# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

from tests.common import BaseCase

from mbed_cloud.foundation import User
from mbed_cloud import SDK


class TestUserFactory(BaseCase):

    def get_user(self, **kwargs):
        sdk = SDK()
        return sdk.foundation.user(**kwargs)

    def test_attr(self):
        user = self.get_user()
        self.assertIsNone(user.phone_number)

    def test_attr_set(self):
        user = self.get_user(id='1')
        self.assertEqual(user.id, '1')


class TestImplicitSDK(TestUserFactory):
    # magically uses global SDK instance
    def get_user(self, **kwargs):
        return User(**kwargs)


class TestExplicitSDK(TestUserFactory):
    # can instantiate models with a client
    def get_user(self, **kwargs):
        sdk = SDK()
        return User(_client=sdk.client, **kwargs)


class TestUserLazyExplicit(TestUserFactory):
    # can set a client before calling apis
    def get_user(self, **kwargs):
        sdk = SDK()
        u = User(**kwargs)
        u._client = sdk.client
        return u


class TestEquality(BaseCase):

    def test_fast(self):
        from mbed_cloud.foundation import User
        a = User()
        b = a
        c = 'cat'
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_ids(self):
        from mbed_cloud.foundation import User
        a = User(id='1')
        b = User(id='1')
        c = User(id='cat')
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_values(self):
        from mbed_cloud.foundation import User
        a = User(full_name='1')
        b = User(full_name='1')
        c = User(full_name='cat')
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
