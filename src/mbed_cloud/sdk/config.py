"""SDK Configuration
=================

Configuration of the Pelion Device Management SDK can be provided in a number of ways. The list is ordered
such that the methods at the top of the list have the highest order of precedence and those at the bottom the lowest.

1. Parameters provided to the :class:`mbed_cloud.sdk.sdk.SDK` class on instantiation.
2. Environment variables;
  - `MBED_CLOUD_SDK_API_KEY` - API Key
  - `MBED_CLOUD_SDK_HOST` - Pelion Device Management API Hostname
3. From a `.env` file.

Example `.env` file:

.. code-block:: bash

    MBED_CLOUD_SDK_API_KEY=ak_A644VERY4745LONG64RANDOM3254STRINGW555455ITHA564miXTurOFlowercaseANDUPPERCASELETTERSIintersperseDwithNUMBER5

.. note::
    The order of precedence does not indicate the method preference. For example, in a production environments, it is
    recommended that configuration is stored in environment variables.

.. warning::
    Take care to exclude `.env` files from your version control. Otherwise, you risk exposing your API keys to anyone
    with read access to your repository.

------------
"""
import os
import logging
import dotenv

from mbed_cloud import utils
from mbed_cloud.sdk import constants

LOGGER = logging.getLogger(__file__)


class Config(object):
    """Configuration object for SDK"""
    _tried_dotenv = False
    api_key = None
    host = None
    _user_agent = None

    def __init__(self, **kwargs):
        self._logger = LOGGER.getChild(self.__class__.__name__)
        self._update(**kwargs)
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
        self._user_agent = utils.get_user_agent()

    @property
    def user_agent(self):
        return self._user_agent

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value

    def _update(self, *updates, **kwargs):
        for update in updates:
            self.update(**update)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}
