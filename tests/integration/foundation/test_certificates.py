# Python 2 compatibility
from __future__ import unicode_literals

from tests.common import BaseCase

from mbed_cloud.sdk.entities import TrustedCertificate


@BaseCase._skip_in_ci
class TestTrustedtCertificates(BaseCase):
    """Test certificates in lieu of proper tests."""

    def test_listing(self):
        for trusted_certs in TrustedCertificate().list():
            print("="*40)
            print(trusted_certs.name)

            if trusted_certs.is_developer_certificate:
                print(trusted_certs.developer_certificate_info())
            else:
                print("Not a developer certificate")
        print("=" * 40)