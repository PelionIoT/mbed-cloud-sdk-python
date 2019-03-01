"""Tests for entities in the security module."""

from tests.common import BaseCase, CrudMixinTests

from mbed_cloud.sdk.entities import CertificateEnrollment
from mbed_cloud.sdk.entities import CertificateIssuerConfig
from mbed_cloud.sdk.entities import CertificateIssuer
from mbed_cloud.sdk.entities import DeveloperCertificate
from mbed_cloud.sdk.entities import ServerCredentials
from mbed_cloud.sdk.entities import SubtenantTrustedCertificate
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


@BaseCase._skip_in_ci
class TestServerCredentials(BaseCase):
    """Test server credentials in lieu of proper tests."""

    def check_server_credentials(self, server_credentials):
        self.assertIn("BEGIN CERTIFICATE", server_credentials.server_certificate)
        self.assertIn("END CERTIFICATE", server_credentials.server_certificate)

    def test_get_bootstrap(self):
        self.check_server_credentials(ServerCredentials().get_bootstrap())

    def test_get_lwm2m(self):
        self.check_server_credentials(ServerCredentials().get_lwm2m())


@BaseCase._skip_in_ci
class TestTrustedandDeveloperCertificate(BaseCase, CrudMixinTests):
    """Test certificates in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = TrustedCertificate
        super(TestTrustedandDeveloperCertificate, cls).setUpClass()

    def test_certificate_info(self):
        for trusted_cert in TrustedCertificate().list():
            # Check name is set and of a sensible type
            self.assertIsInstance(trusted_cert.name, str, "Expected a certification name to be a string")
            self.assertTrue(len(trusted_cert.name) > 0, "Expected a certificate to have a non zero length name")

            if trusted_cert.is_developer_certificate:
                # If this is a developer certificate retrieve it
                developer_certificate = trusted_cert.get_developer_certificate_info()
                self.assertEqual(developer_certificate.__class__.__name__, "DeveloperCertificate")

                new_developer_certificate = DeveloperCertificate(id=developer_certificate.id)
                # Test the link back to the trusted certificate
                back_linked_cert = new_developer_certificate.get_trusted_certificate_info()
                self.assertEqual(back_linked_cert.__class__.__name__, "TrustedCertificate")
                self.assertEqual(trusted_cert.id, back_linked_cert.id, "These should be the same trusted certificate")
            else:
                # If this is not a developer certificate check that it cannot be retrieved
                with self.assertRaises(ApiErrorResponse) as api_error:
                    trusted_cert.get_developer_certificate_info()
                    self.assertEqual(api_error.exception.status_code, 404)
