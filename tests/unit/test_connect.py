from tests.common import BaseCase
from mbed_cloud.connect import ConnectAPI


class TestBase64Encode(BaseCase):
    def test_string(self):
        self.assertEqual(ConnectAPI._base64_encode("Hello World"), "SGVsbG8gV29ybGQ=")

    def test_empty_string(self):
        self.assertEqual(ConnectAPI._base64_encode(""), "")

    def test_positive_int(self):
        self.assertEqual(ConnectAPI._base64_encode(1), "MQ==")

    def test_negative_int(self):
        self.assertEqual(ConnectAPI._base64_encode(-1), "LTE=")

    def test_positive_float(self):
        self.assertEqual(ConnectAPI._base64_encode(1.0), "MS4w")

    def test_negative_float(self):
        self.assertEqual(ConnectAPI._base64_encode(-1.0), "LTEuMA==")

    def test_none(self):
        self.assertEqual(ConnectAPI._base64_encode(None), "")