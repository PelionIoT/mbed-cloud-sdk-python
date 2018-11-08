"""Tests for entities in the security module."""

from tests.common import BaseCase, CrudMixinTests

from mbed_cloud.sdk.entities import CertificateIssuerConfig
from mbed_cloud.sdk.entities import Device
from mbed_cloud.sdk.entities import DeviceEnrollmentBulkCreate
from mbed_cloud.sdk.entities import DeviceEnrollmentBulkDelete
from mbed_cloud.sdk.entities import DeviceEnrollment
from mbed_cloud.sdk.entities import DeviceEvents

from mbed_cloud.sdk.enums import DeviceStateEnum

from mbed_cloud.sdk.common.exceptions import ApiErrorResponse


@BaseCase._skip_in_ci
class TestDevice(BaseCase, CrudMixinTests):
    """Test devices in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = Device
        super(TestDevice, cls).setUpClass()

    def test_cert_renew(self):
        # an example: certificate renew

        # Find all certificate issuers that may be in use
        certificate_references = []
        for certificate_issuer_config in CertificateIssuerConfig().list():
            certificate_references.append(certificate_issuer_config.reference)

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


@BaseCase._skip_in_ci
class TestDeviceEnrollment(BaseCase, CrudMixinTests):
    """Test device enrollment in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = DeviceEnrollment
        super(TestDeviceEnrollment, cls).setUpClass()

    def test_device_enrollment_single(self):
        # an example: device enrollment single
        pass

    def test_device_enrollment_bulk(self):
        # an example: device enrollment bulk
        pass


@BaseCase._skip_in_ci
class TestDeviceEvents(BaseCase, CrudMixinTests):
    """Test device events in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = DeviceEvents
        super(TestDeviceEvents, cls).setUpClass()