from mbed_cloud import BaseAPI
from mbed_cloud import connect
from mbed_cloud._backends.mds.apis.endpoints_api import EndpointsApi
from tests.common import BaseCase
import urllib3


class Test(BaseCase):
    """A simple test for validating coverage"""

    def test_run(self):
        from mbed_cloud import account_management
        from mbed_cloud import certificates
        from mbed_cloud import connect
        from mbed_cloud import device_directory
        from mbed_cloud import update
        from mbed_cloud import _version
