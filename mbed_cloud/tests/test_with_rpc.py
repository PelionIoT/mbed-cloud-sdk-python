from mbed_cloud.tests.common import BaseCase
import docker


class TestWithRPC(BaseCase):
    image = 'trunner'

    @staticmethod
    def setUpClass(cls):
        cls.client = docker.from_env()

    def test_run(self):
        self.client.containers.run(image="trunner", network_mode='host')

