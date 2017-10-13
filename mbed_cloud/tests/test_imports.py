from mbed_cloud.tests.common import BaseCase


class TestImports(BaseCase):
    """A simple test for validating coverage etc"""
    def test_run(self):
        from mbed_cloud import *  # noqa
