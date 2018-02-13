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

    def test_z_object_attr_maps(self):
        from mbed_cloud.core import BaseObject
        all_objs_classes = BaseObject.__subclasses__()
        self.assertEqual(len(all_objs_classes), 16)
        fail = {}
        for obj in all_objs_classes:
            attr_map = obj._get_attributes_map()
            in_attr_map_not_object = [k for k in attr_map if not hasattr(obj, k)]
            in_object_not_attr_map = [k for k in vars(obj) if (not k.startswith('_') and k not in attr_map)]
            if in_attr_map_not_object or in_object_not_attr_map:
                fail[str(obj)] = dict(missing=in_attr_map_not_object, excess=in_object_not_attr_map)
        if fail:
            raise self.failureException('mapped fields are wrong.\n%s' % (fail,))
