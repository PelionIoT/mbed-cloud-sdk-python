import os

import dotenv

from mbed_cloud import utils
from mbed_cloud.sdk.common import constants
from mbed_cloud.sdk.common import logs


class Config(object):
    _tried_dotenv = False
    api_key = None
    host = None
    user_agent = None

    def __init__(self, **kwargs):
        self._logger = logs.LOGGER.getChild(self.__class__.__name__)
        self.update(**kwargs)
        if not self.api_key and not Config._tried_dotenv:
            # mark dotenv load complete, so we don't have to do it again
            dotenv.load_dotenv(
                dotenv.find_dotenv(usecwd=True, raise_error_if_not_found=False)
            )
            Config._tried_dotenv = True
        self._set_defaults()

    def _set_defaults(self):
        """Configures any default parameters"""
        self.api_key = (
            self.api_key
            or os.getenv(constants.ENVVAR_API_KEY)
            or constants.DEFAULT_API_KEY
        )
        self.host = (
            self.host or os.getenv(constants.ENVVAR_HOST) or constants.DEFAULT_HOST
        )
        self.user_agent = utils.get_user_agent()

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value

    def update(self, *updates, **kwargs):
        for update in updates:
            self.update(**update)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}
