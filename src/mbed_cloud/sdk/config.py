"""SDK Configuration
=================

Configuration of the Pelion Device Management SDK can be provided in a number of ways. The list is ordered
such that the methods at the top of the list have the highest order of precedence and those at the bottom the lowest.

1. Parameters provided to the :class:`mbed_cloud.sdk.sdk.SDK` class on instantiation.
2. Using environment variables.
3. Environment variables configured via a `.env` file.


Configuration Parameters
------------------------

The SDK can be configured with the following parameters:

=========== ========================== =================================================================== ========
Parameter   Environment Variable       Description                                                         Optional
=========== ========================== =================================================================== ========
``api_key`` ``MBED_CLOUD_SDK_API_KEY`` The API key created in the Pelion Device Management Portal.         Required
``host``    ``MBED_CLOUD_SDK_HOST``    The fully qualified hostname (scheme, host, port) of the REST API.  Optional
=========== ========================== =================================================================== ========


Production deployment
---------------------

In a production environments, it is recommended that configuration is stored in environment variables, in a secure
manner, this is the equivalent of:

.. code-block:: console

    export MBED_CLOUD_SDK_API_KEY=ak_abcdef123


Local Development
-----------------

For a reproducible local development environment a `.env` file can be used to configure the SDK without modifying the
system's environment. The file should be named `.env` and placed at any level of the directory tree
between the project's working directory and the root. Files closer to the working directory take priority.

Example `.env` file:

.. code-block:: bash

    MBED_CLOUD_SDK_API_KEY=ak_A644VERY4745LONG64RANDOM3254STRINGW555455ITHA564miXTurOFlowercaseANDUPPERCASELETTERSIintersperseDwithNUMBER5


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

    def __init__(self, api_key=None, host=None):
        """Create a new configuration instance.

        If configuration is not supplied then the default configuration from a `.env` file or environment variables will
        be used.

        :param api_key: (optional) API Key to use for Authentication, if provided this will override all other
            configuration
        :type api_key: str
        :param host: (optional) Host of the Pelion Device Management API, if provided this will override all other
            configuration
        :type host: str
        """
        self._logger = LOGGER.getChild(self.__class__.__name__)

        config_dict = {}

        if api_key:
            config_dict["api_key"] = api_key
        if host:
            config_dict["host"] = host

        self._update(**config_dict)
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
        """The user-agent used in HTTP requests."""
        return self._user_agent

    @property
    def logger(self):
        """Instance of the logger."""
        return self._logger

    @logger.setter
    def logger(self, value):
        """Set the logger instance"""
        self._logger = value

    def _update(self, *updates, **kwargs):
        """Update the current configuration with that provided in the arguments."""
        for update in updates:
            self.update(**update)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _to_dict(self):
        """Return the current configuration as a dictionary."""
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}
