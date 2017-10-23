from tests.common import BaseCase
from mbed_cloud.certificates import CertificatesAPI
from mbed_cloud.certificates import CertificateType
from mbed_cloud.exceptions import CloudValueError


class TestCertificates(BaseCase):

    @classmethod
    def setUpClass(cls):
        cls.api = CertificatesAPI()

    def _run(self, expected, **kwargs):
        outcome = self.api.list_certificates(**kwargs)
        self.assertGreaterEqual(list(outcome), expected)

    def test_invalid_type(self):
        with self.assertRaises(CloudValueError):
            self._run(None, type__eq='banana')

    def test_bootstrap(self):
        self._run([], type__eq=CertificateType.bootstrap)

    def test_developer(self):
        self._run([], type__eq=CertificateType.developer)

    def test_lwm2m(self):
        self._run([], type__eq=CertificateType.lwm2m)
