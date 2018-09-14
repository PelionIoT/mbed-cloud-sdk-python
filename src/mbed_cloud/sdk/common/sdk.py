import warnings

from mbed_cloud.sdk import Config
from mbed_cloud.sdk.common.client import Client

# create a new InstanceFactory for providing access to Entities directly from this instance
from mbed_cloud.sdk._modules._factory import InstanceFactory

global_sdk = None
has_warned = None


class SDK(object):
    def __init__(self, config=None, **config_overrides):
        """Create a new SDK instance

        [Beta] this section of the SDK is at a `beta` release level
               and is subject to change without notice

        :param config: An SDK config object
        :type config: Config

        :param config_overrides: Key-value updates to apply to the config
        :type config_overrides: dict(str, str)
        """
        beta_warning(self.__class__)

        # create a new config based on those we received
        existing = config.to_dict() if config else {}
        existing.update(config_overrides)
        self._config = Config(**existing)

        # create a new client for making http calls
        self._client = Client(self._config)

        self.entities = InstanceFactory(self.client)

    @property
    def client(self):
        return self._client

    @property
    def config(self):
        return self._config


def get_or_create_global_sdk_instance():
    """For simple use cases, a single global SDK is sufficient"""
    global global_sdk
    if global_sdk is None:
        global_sdk = SDK()
    return global_sdk


def beta_warning(header, category=FutureWarning):
    global has_warned
    if not has_warned:
        warnings.warn(
            "[Beta] this section of the SDK is at a `beta` release level and is subject to change without notice: %s"
            % header,
            category=category,
            stacklevel=3,  # make the trace log from two levels above this `warnings.warn` line
        )
        has_warned = True
