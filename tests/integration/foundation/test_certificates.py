# Python 2 compatibility
from __future__ import unicode_literals

from tests.common import BaseCase

from mbed_cloud.sdk.entities import TrustedCertificate


@BaseCase._skip_in_ci
class CrudMixinTest(BaseCase):
    """Test certificates in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        class_name = cls.class_under_test.__name__
        print("\n** %s **" % cls.class_under_test.__name__)

    def test_listing(self):
        for entity in self.class_under_test().list():
            print(entity.name)

    def test_crud(self):


@BaseCase._skip_in_ci
class TestTrustedtCertificates(CrudMixinTest):
    """Test certificates in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = TrustedCertificate
        super(TestTrustedtCertificates, cls).setUpClass()


    def test_developer_certificate_info(self):
        for trusted_certs in TrustedCertificate().list():
            print("="*40)
            print(trusted_certs.name)

            if trusted_certs.is_developer_certificate:
                self.assertEqual(trusted_certs.developer_certificate_info().__name__, DeveloperCertificate)
            else:
                print("Not a developer certificate")
        print("=" * 40)