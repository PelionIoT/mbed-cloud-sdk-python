from tests.common import BaseCase
from mbed_cloud.tlv.decode import binary_tlv_to_python
from mbed_cloud.tlv.decode import combine_bytes
from mbed_cloud.tlv.decode import get_value_length
from mbed_cloud.tlv.decode import get_id_length


class TestDecode(BaseCase):
    def test_nullstring(self):
        self.assertEqual(
            binary_tlv_to_python(''.encode()),
            {}
        )

    def test_get_id_length_1(self):
        self.assertEqual(get_id_length(0b11011111), 1)

    def test_get_id_length_2(self):
        self.assertEqual(get_id_length(0b11111111), 2)

    def test_get_value_length_1(self):
        self.assertEqual(get_value_length(0b11101111), 1)

    def test_get_value_length_2(self):
        self.assertEqual(get_value_length(0b11110111), 2)

    def test_get_value_length_3(self):
        self.assertEqual(get_value_length(0b11111111), 3)

    def test_get_value_length_custom(self):
        # for example:
        # both bits for the relevant mask are zero, which means it defers
        # to the remaining bits (instead of the hardcoded values)
        # the remainder are the least significant bits - here, 110
        self.assertEqual(get_value_length(0b11100110), 6)

    def test_combine_bytes_two(self):
        b1 = 0b00000001  # 1
        b2 = 0b00000101  # 5
        b3 = b1 + b2     # 261 instead of 6
        self.assertEqual(b3, 6)
        self.assertEqual(
            combine_bytes((b1, b2)),
            261
        )

    def test_combine_bytes_three(self):
        b1 = 0b00000001    # 1
        b2 = 0b00000101    # 5
        b3 = 0b00011111    # 31
        b4 = b1 + b2 + b3  # 66847 instead of 37
        self.assertEqual(b4, 37)
        self.assertEqual(
            combine_bytes((b1, b2, b3)),
            66847
        )
