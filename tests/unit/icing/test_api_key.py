# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str

import random

from tests.common import BaseCase

from mbed_cloud.sdk import enums


class TestApiKey(BaseCase):

    def test_list(self):
        from mbed_cloud.sdk.api import ApiKey
        api_key = ApiKey()
        all_keys = api_key.list()
        print(len(all_keys))
        print(all_keys)
        for key in all_keys:
            print(key)
