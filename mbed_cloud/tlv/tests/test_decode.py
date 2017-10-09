from mbed_cloud.tlv.tests import test_common
from mbed_cloud.tlv.decode import binary_tlv_to_python
from mbed_cloud.tlv.decode import combine_bytes


class TestDecode(test_common.BaseCase):
    def test_nullstring(self):
        self.assertEqual(
            binary_tlv_to_python(''.encode()),
            {}
        )

    def test_combine_bytes_two(self):
        b1 = 0b00000001  # 1
        b2 = 0b00000101  # 5
        b3 = b1 + b2     # 261
        self.assertEqual(
            combine_bytes((b1, b2)),
            261
        )

    def test_combine_bytes_three(self):
        b1 = 0b00000001    # 1
        b2 = 0b00000101    # 5
        b3 = 0b00011111    # 31
        b4 = b1 + b2 + b3  # 66847 [NOT 37]
        self.assertEqual(
            combine_bytes((b1, b2, b3)),
            66847
        )
