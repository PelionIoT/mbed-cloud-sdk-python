"""Test the format of HTTP Requests sent to the APIs."""

import urllib3
from mock import patch

import mbed_cloud

from tests.common import BaseCase


class RequestCallException(Exception):
    """Derived an exception so an explicitly defined exception can be caught."""
    pass


class TestUserAgent(BaseCase):
    """Test a User-Agent HTTP header is set for the SDK.

    Pick one method of each API to check header is as expected.
    """

    def setUp(self):
        """Setup mocks for testing with urlib3."""
        patcher = patch.object(urllib3.PoolManager, 'request')
        self.addCleanup(patcher.stop)
        self.mocked_pool_manager = patcher.start()

        # Create a side effect of raising a known exception when 'request' is
        # called. This avoids mocking all the properties of the object returned
        # by the call to 'request' which are accessed by the calling code.
        self.mocked_pool_manager.side_effect = RequestCallException()

    def check_user_agent(self, list_method):
        """Issue a GET request and check contents of User-Agent HTTP header.
        :param PaginatedResponse list_method: An API list method
        """
        # Attempt to get the first item from the paginated response which will
        # call 'urllib3.PoolManager.request'.
        try:
            list_method.first()
        except RequestCallException:
            pass

        # Retrieve header from call arguments and check User-Agent header is set.
        user_agent = self.mocked_pool_manager.call_args[1]['headers'].get('User-Agent')
        self.assertIsNotNone(user_agent, "User-Agent header missing")

        # Check User-Agent header, it should look something like:
        # "mbed-cloud-sdk-python/1.2.6.850 (Darwin-17.4.0-x86_64-i386-64bit) Python/3.6.3"
        self.assertRegexpMatches(
            user_agent,
            r"^mbed-cloud-sdk-python/\d+.\d+.\d+.\w+ \(\S*\) Python/\d+.\d+.\d+$",
            "User-Agent does not have the expected format")

    def test_account_management_api(self):
        self.check_user_agent(mbed_cloud.AccountManagementAPI().list_api_keys())

    def test_certificates_api(self):
        self.check_user_agent(mbed_cloud.CertificatesAPI().list_certificates())

    def test_connect_api(self):
        self.check_user_agent(mbed_cloud.ConnectAPI().list_connected_devices())

    def test_device_directory_api(self):
        self.check_user_agent(mbed_cloud.DeviceDirectoryAPI().list_devices())

    def test_enrollment_api(self):
        self.check_user_agent(mbed_cloud.EnrollmentAPI().list_enrollment_claims())

    def test_update_api(self):
        self.check_user_agent(mbed_cloud.UpdateAPI().list_campaigns())
