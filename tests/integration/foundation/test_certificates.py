# Python 2 compatibility
from __future__ import unicode_literals

from tests.common import BaseCase

from mbed_cloud.sdk.entities import TrustedCertificate
from mbed_cloud.sdk.common.exceptions import ApiErrorResponse


class CrudMixinTest(object):
    """Test certificates in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        print("\n** %s **" % cls.class_under_test.__name__)

    def test_listing(self):
        count = 0
        for entity in self.class_under_test().list(page_size=3, max_results=5):
            self.assertEqual(self.class_under_test, entity.__class__, "Unexpected class returned from the list method")
            count += 1

        self.assertTrue(count <= 5, "At most 5 entities should be returned due to the max_results parameter")


@BaseCase._skip_in_ci
class TestTrustedCertificates(BaseCase, CrudMixinTest):
    """Test certificates in lieu of proper tests."""

    @classmethod
    def setUpClass(cls):
        cls.class_under_test = TrustedCertificate
        super(TestTrustedCertificates, cls).setUpClass()

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
