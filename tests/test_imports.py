from tests.common import BaseCase


class Test(BaseCase):
    """Verify high level APIs are importable in the expected manner"""

    def test_account(self):
        from mbed_cloud import AccountManagementAPI
        from mbed_cloud.account_management import User
        from mbed_cloud.account_management import Group
        from mbed_cloud.account_management import ApiKey
        from mbed_cloud.account_management import AccountManagementAPI

    def test_certs(self):
        from mbed_cloud import CertificatesAPI
        from mbed_cloud.certificates import Certificate
        from mbed_cloud.certificates import CertificateType

    def test_connect(self):
        from mbed_cloud import ConnectAPI
        from mbed_cloud.connect import AsyncConsumer
        from mbed_cloud.connect import Resource
        from mbed_cloud.connect import Webhook

    def test_device(self):
        from mbed_cloud import DeviceDirectoryAPI
        from mbed_cloud.device_directory import Device
        from mbed_cloud.device_directory import DeviceEvent
        from mbed_cloud.device_directory import Query

    def test_update(self):
        from mbed_cloud import UpdateAPI
        from mbed_cloud.update import Campaign
        from mbed_cloud.update import FirmwareImage
        from mbed_cloud.update import FirmwareManifest
