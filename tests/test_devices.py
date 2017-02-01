# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Tests describing the device API."""
from mbed_cloud.devices import DeviceAPI
import mock
import unittest


class TestDevices(unittest.TestCase):
    """Unit tests for devices."""

    def __init__(self, *args, **kwargs):
        """Initialize the devices API."""
        super(TestDevices, self).__init__(*args, **kwargs)
        self.api = DeviceAPI({'api_key': '1234'})

    @mock.patch('mbed_cloud._backends.mds.EndpointsApi.v2_endpoints_get')
    def test_list_endpoints(self, c):
        """Ensure we call the expected backends function."""
        self.api.list_connected_devices()
        c.assert_called_once_with()

    @mock.patch('mbed_cloud._backends.mds.SubscriptionsApi.v2_subscriptions_put')
    def test_pre_subscribe(self, c):
        """Ensure we call the expected backends function."""
        self.api.add_pre_subscription('endpoint_foo', '/some/path')
        c.assert_called_once_with(mock.ANY)

if __name__ == '__main__':
    unittest.main()
