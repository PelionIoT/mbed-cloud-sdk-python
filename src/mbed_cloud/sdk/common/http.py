from mbed_cloud import utils
from mbed_cloud.sdk.common.config import Config

import requests


class Client(object):
    def __init__(self, config):
        """An http client container

        :param config:
        :type config: Config
        """
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": "Bearer %s" % self.config.api_key,
                "UserAgent": utils.get_user_agent(),
            }
        )
