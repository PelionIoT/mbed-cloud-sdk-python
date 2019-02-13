"""Tests for entities in the security module."""

import time

from tests.common import BaseCase, CrudMixinTests

from mbed_cloud.sdk.entities import CertificateIssuerConfig
from mbed_cloud.sdk.entities import Device
from mbed_cloud.sdk.entities import DeviceEnrollmentBulkCreate
from mbed_cloud.sdk.entities import DeviceEnrollmentBulkDelete
from mbed_cloud.sdk.entities import DeviceEnrollment
from mbed_cloud.sdk.entities import DeviceEvents

from mbed_cloud.sdk.enums import DeviceStateEnum
from mbed_cloud.sdk.enums import DeviceEnrollmentBulkCreateStatusEnum
from mbed_cloud.sdk.enums import DeviceEnrollmentBulkDeleteStatusEnum

from mbed_cloud.sdk.common.exceptions import ApiErrorResponse


@BaseCase._skip_in_ci
class TestDevice(BaseCase, CrudMixinTests):
    """Test devices in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = Device
        super(TestDevice, cls).setUpClass()

    def test_hello_world(self):
        from mbed_cloud.sdk.entities import Device

        # List the first 10 devices on your Pelion DM account
        for device in Device().list(max_results=10):
            print("Hello device %s" % device.name)

    def test_cert_renew(self):
        """Example of renewing a certificate on a device."""
        # an example: certificate renew

        # Find all certificate issuers that may be in use
        certificate_references = []
        for certificate_issuer_config in CertificateIssuerConfig().list():
            certificate_references.append(certificate_issuer_config.certificate_reference)

        # List all devices
        for device in Device().list():
            # A certificate can only be renewed on a registered device
            if device.state == DeviceStateEnum.REGISTERED:
                # It is not possible to determine which certificate issuer has been used on a
                # device so try them in turn.
                for certificate_reference in certificate_references:
                    try:
                        # If the wrong certificate issuer is selected then the renew will fail
                        device.renew_certificate(certificate_reference)
                    except ApiErrorResponse:
                        print("Certificate '%s' could not be renewed on device '%s'" % (
                            certificate_reference, device.name))
                    else:
                        print("Certificate '%s' was renewed on device '%s'" % (
                            certificate_reference, device.name))
        # end of example

@BaseCase._skip_in_ci
class TestDeviceEnrollment(BaseCase, CrudMixinTests):
    """Test device enrollment in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = DeviceEnrollment
        super(TestDeviceEnrollment, cls).setUpClass()

    def test_device_enrollment_single(self):
        """Example of enrolling a device in Pelion Device Management."""
        try:
            # an example: device enrollment single

            # Enroll a single device using the enrollment ID for the device
            device_enrollment = DeviceEnrollment(
                enrollment_identity = "A-4E:63:2D:AE:14:BC:D1:09:77:21:95:44:ED:34:06:57:1E:03:B1:EF:0E:F2:59:44:71:93:23:22:15:43:23:12")

            device_enrollment.create()
            # end of example
        except ApiErrorResponse as api_error:
            self.assertEqual(api_error.status_code, 409, "This should be a duplicate identity")

    def test_device_enrollment_bulk_create(self):
        """Example of enrolling a device in Pelion Device Management."""
        # an example: device enrollment bulk
        with open("tests/fixtures/bulk_device_enrollment.csv", "rb") as csv_file_handle:
            bulk_device_enrollment = DeviceEnrollmentBulkCreate().create(csv_file_handle)

        while bulk_device_enrollment.status != DeviceEnrollmentBulkCreateStatusEnum.COMPLETED:
            time.sleep(1)
            bulk_device_enrollment.get()

        print(bulk_device_enrollment.download_full_report_file().read())
        print(bulk_device_enrollment.download_errors_report_file().read())
        # end of example

    def test_device_enrollment_bulk_delete(self):
        """Example of enrolling a device in Pelion Device Management."""
        with open("tests/fixtures/bulk_device_enrollment.csv", "rb") as csv_file_handle:
            bulk_device_enrollment = DeviceEnrollmentBulkDelete().delete(csv_file_handle)

        while bulk_device_enrollment.status != DeviceEnrollmentBulkDeleteStatusEnum.COMPLETED:
            time.sleep(1)
            bulk_device_enrollment.get()

        print(bulk_device_enrollment.download_full_report_file().read())
        print(bulk_device_enrollment.download_errors_report_file().read())

@BaseCase._skip_in_ci
class TestDeviceEvents(BaseCase, CrudMixinTests):
    """Test device events in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = DeviceEvents
        super(TestDeviceEvents, cls).setUpClass()
