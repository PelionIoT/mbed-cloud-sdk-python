from mbed_cloud.tests.common import BaseCase


class TestImports(BaseCase):
    """A simple test for validating coverage etc"""
    def test_run(self):
        from mbed_cloud import account_management
        from mbed_cloud import certificates
        from mbed_cloud import connect
        from mbed_cloud import device_directory
        from mbed_cloud import update

    def test_config(self):
        from mbed_cloud import config
        self.assertIn('lab.', config.get('host'))
