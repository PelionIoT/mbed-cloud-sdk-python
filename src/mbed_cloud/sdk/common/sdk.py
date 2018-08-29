from mbed_cloud import utils
from mbed_cloud.sdk import Config
from mbed_cloud.sdk.common.http import Client

global_sdk = None


class SDK(object):
    def __init__(self, config=None, **config_overrides):
        self._config = Config()
        self._config.update({"user_agent": utils.get_user_agent()})
        self._config.update(config or {})
        self._config.update(config_overrides)

        self._client = Client(self._config)

        from mbed_cloud.sdk.common._entities import InstanceFactory

        self.entities = InstanceFactory(self)

    @property
    def client(self):
        return self._client


def get_or_create_global_sdk_instance():
    global global_sdk
    if global_sdk is None:
        global_sdk = SDK()
    return global_sdk
