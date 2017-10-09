from mbed_cloud.tlv.tests import test_common
from mbed_cloud.tlv import decode
from mbed_cloud.tlv.decode import maybe_decode_payload


class B64(object):
    # hides the inheritance from unittest

    class TestCase(test_common.BaseCase):
        b64 = None  # an ascii string containing b64 encoded data
        result = None  # the python-native data we expect to decode

        def test_run(self):
            self.assertEqual(maybe_decode_payload(self.b64), self.result)


class TestADevice(B64.TestCase):
    """
    a random device from the integration lab
    """
    b64 = "iAsLSAAIAAAAAAAAAADBEFXIABAAAAAAAAAAAAAAAAAAAAAAyAEQAAAAAAAAAAAAAAAAAAAAAMECMMgRD2Rldl9kZXZpY2VfdHlwZcgSFGRldl9oYXJkd2FyZV92ZXJzaW9uyBUIAAAAAAAAAADIDQgAAAAAWdOfCg=="
    result = []


class TestValueIsZero(B64.TestCase):
    """
    a value of 0
    """
    b64 = "iAsLSAAIAAAAAAAAAAA="
    result = 0
