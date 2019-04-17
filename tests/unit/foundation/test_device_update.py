"""Tests for entities in the device update module."""

import six
import httpretty

from tests.common import BaseCase, CrudMixinTests

from mbed_cloud import SDK

from mbed_cloud.sdk.exceptions import ApiErrorResponse


@httpretty.activate
class TestFirmwareImage(BaseCase):
    """Test creation of firware imamge request."""

    @classmethod
    def setUpClass(cls):
        cls.sdk = SDK()

    def setUp(self):
        httpretty.register_uri(
            httpretty.POST,
            self.sdk.config.host + "/v3/firmware-images/",
            body='{"origin": "127.0.0.1"}'
        )

    def test_image_upload(self):
        """Example of renewing a certificate on a device."""

        file_name = "/Users/graham01/development/private-sdks/testrunner/test_fixtures/firmware_image.bin"

        # with open(file_name, mode='rb') as file:
        #     image = self.sdk.foundation.firmware_image(description="GH Test").upload(firmware_image_file=file)

        image = self.sdk.foundation.firmware_image(description="Test Description", name="Test Name")
        image.upload(firmware_image_file=file_name)

        last_request = httpretty.last_request()

        # The content type needs to set as multipart and define the boundary
        self.assertIn("multipart/form-data; boundary=", last_request.headers["Content-Type"])

        # The message needs to have three sections
        self.assertIn(six.b('Content-Disposition: form-data; name="description"\r\nContent-Type: text/plain\r\n\r\nTest Description'), last_request.parsed_body)
        self.assertIn(six.b('Content-Disposition: form-data; name="name"\r\nContent-Type: text/plain\r\n\r\nTest Name'), last_request.parsed_body)
        self.assertIn(six.b('Content-Disposition: form-data; name="datafile"; filename="firmware_image_file.bin"\r\nContent-Type: application/octet-stream'), last_request.parsed_body)
