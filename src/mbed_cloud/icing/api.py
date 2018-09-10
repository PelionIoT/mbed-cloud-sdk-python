from mbed_cloud.configuration import Config
from mbed_cloud.connect.connect import ConnectAPI


class Client(object):
    """A client for the mbed cloud APIs

    """
    def __init__(self, **kwargs):
        self.configure(**kwargs)
        self._connect = ConnectAPI(params=self.config)
        self._user = ConnectAPI(params=self.config)

    def configure(self, configuration=None, **kwargs):
        if configuration is None:
            configuration = Config(kwargs)
        self.config = configuration

    def subscribe(self, subscription_channel, **observer_params):
        return self._connect.subscribe(subscription_channel, **observer_params)
