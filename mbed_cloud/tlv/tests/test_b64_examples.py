from mbed_cloud.tlv.tests import test_common
from mbed_cloud.tlv.decode import maybe_decode_payload


class B64(object):
    # hides the inheritance from unittest

    class TestCase(test_common.BaseCase):
        b64 = None  # an ascii string containing b64 encoded data
        result = None  # the python-native data we expect to decode
        decoded = None  # we'll store the result here in the test

        def test_run(self):
            self.decoded = maybe_decode_payload(self.b64)
            self.assertion()

        def assertion(self):
            self.assertEqual(self.decoded, self.result)


class TestDevice(B64.TestCase):
    """
    a random device from the integration lab
    """
    b64 = "iAsLSAAIAAAAAAAAAADBEFXIABAAAAAAAAAAAAAAAAAAAAAAyAEQAAAAAAAAAAAAAAAAAAAAAMECMMgRD2Rldl9kZXZpY2VfdHlwZcgSFGRldl9oYXJkd2FyZV92ZXJzaW9uyBUIAAAAAAAAAADIDQgAAAAAWdH0Bw=="
    result = {
        '/0': 0,
        '/1': 0,
        '/11/0': 0,
        '/13': 1506931719,
        '/16': 'U',
        '/17': 'dev_device_type',
        '/18': 'dev_hardware_version',
        '/2': '0',
        '/21': 0
    }


class TestValueBlank(B64.TestCase):
    b64 = "VQ=="
    result = {'/0': ''}


class TestValueZero(B64.TestCase):
    b64 = "iAsLSAAIAAAAAAAAAAA="
    result = {'/11/0': 0}
