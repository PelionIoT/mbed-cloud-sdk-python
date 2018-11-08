"""Tests for entities in the security module."""

from tests.common import BaseCase, CrudMixinTests

from mbed_cloud.sdk.entities import CertificateEnrollment
from mbed_cloud.sdk.entities import CertificateIssuerConfig
from mbed_cloud.sdk.entities import CertificateIssuer
from mbed_cloud.sdk.entities import DeveloperCertificate
from mbed_cloud.sdk.entities import ServerCredentials
from mbed_cloud.sdk.entities import TrustedCertificate

from mbed_cloud.sdk.common.exceptions import ApiErrorResponse


@BaseCase._skip_in_ci
class TestCertificateEnrollment(BaseCase, CrudMixinTests):
    """Test certificate enrollment in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = CertificateEnrollment
        super(TestCertificateEnrollment, cls).setUpClass()
        

@BaseCase._skip_in_ci
class TestCertificateIssuer(BaseCase, CrudMixinTests):
    """Test certificate issuer in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = CertificateIssuer
        super(TestCertificateIssuer, cls).setUpClass()


@BaseCase._skip_in_ci
class TestCertificateIssuerConfig(BaseCase, CrudMixinTests):
    """Test certificate issuer configuration in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = CertificateIssuerConfig
        super(TestCertificateIssuerConfig, cls).setUpClass()


# @BaseCase._skip_in_ci
# class TestDeveloperCertificate(BaseCase, CrudMixinTests):
#     """Test developer certificate in lieu of proper tests."""
#
#     @classmethod
#     def setUpClass(cls):
#         cls.class_under_test = DeveloperCertificate
#         super(TestDeveloperCertificate, cls).setUpClass()


# @BaseCase._skip_in_ci
# class TestServerCredentials(BaseCase, CrudMixinTests):
#     """Test server credentials in lieu of proper tests."""
#
#     @classmethod
#     def setUpClass(cls):
#         cls.class_under_test = ServerCredentials
#         super(TestServerCredentials, cls).setUpClass()


@BaseCase._skip_in_ci
class TestTrustedCertificate(BaseCase, CrudMixinTests):
    """Test certificates in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = TrustedCertificate
        super(TestTrustedCertificate, cls).setUpClass()

    def test_developer_certificate_info(self):
        for trusted_certs in TrustedCertificate().list():
            # Check name is set and of a sensible type
            self.assertIsInstance(trusted_certs.name, str, "Expected a certification name to be a string")
            self.assertTrue(len(trusted_certs.name) > 0, "Expected a certificate to have a non zero length name")

            if trusted_certs.is_developer_certificate:
                # If this is a developer certificate retrieve it
                self.assertEqual(trusted_certs.developer_certificate_info().__class__.__name__, "DeveloperCertificate")
            else:
                # If this is not a developer certificate check that it cannot be retrieved
                with self.assertRaises(ApiErrorResponse) as api_error:
                    trusted_certs.developer_certificate_info()
                    self.assertEqual(api_error.exception.status_code, 404)
