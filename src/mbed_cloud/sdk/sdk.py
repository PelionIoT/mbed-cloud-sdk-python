"""SDK Interface
=============

This provides a single point of entry to use the Primary, Foundation and Client interfaces. It allows the configuration
and other context information to be shared between instances.

This is the preferred method of creating Foundation Entity instances and using the Client Interface:

- :mod:`mbed_cloud.client.client.Client`
- :mod:`mbed_cloud.foundation`

------------
"""
import warnings
import ssl
import re

from mbed_cloud.sdk import Config
from mbed_cloud.client.client import Client
from mbed_cloud.foundation.entities.entity_factory import EntityFactory

global_sdk = None


class SDK(object):
    """SDK Interface for interacting with Primary, Foundation and Client interfaces."""

    def __init__(self, config=None, api_key=None, host=None):
        """Create a new SDK instance

        If configuration is not supplied then the default configuration from a `.env` file or environment variables will
        be used. For more information please see :mod:`mbed_cloud.sdk.config`.

        :param config: (optional) An SDK configuration object, this will override settings in environment variables or
            `.env` files.
        :type config: mbed_cloud.sdk.config.Config
        :param api_key: (optional) API Key to use for Authentication, if provided this will override all other
            configuration
        :type api_key: str
        :param host: (optional) Host of the Pelion Device Management API, if provided this will override all other
            configuration
        :type host: str
        """
        check_openssl_version()

        # create a new config based on those we received
        existing = config._to_dict() if config else {}
        if api_key:
            existing["api_key"] = api_key
        if host:
            existing["host"] = host
        self._config = Config(**existing)

        # create a new client for making http calls
        self._client = Client(self._config)

        self._entities = EntityFactory(self.client)

    @property
    def client(self):
        """Client Interface, which can be use for direct communication with the Pelion Device Management API

        :return: Client Interface.
        :rtype: mbed_cloud.client.client.Client
        """
        return self._client

    @property
    def config(self):
        """Configuration in use by SDK instance.

        :return: Configuration object.
        :rtype: mbed_cloud.sdk.config.Config
        """
        return self._config

    @property
    def foundation(self):
        """Foundation Interface Entities

        This provides access to all Entities in the Foundation Interface via the returned factory class.

        :return: Foundation Interface entity factory.
        :rtype: mbed_cloud.foundation.entities.entity_factory.EntityFactory
        """
        return self._entities


def get_or_create_global_sdk_instance():
    """For simple use cases, a single global SDK is sufficient"""
    global global_sdk
    if global_sdk is None:
        global_sdk = SDK()
    return global_sdk


def check_openssl_version():
    """Utility function to check that the OpenSSL version is recent enough"""
    version = ssl.OPENSSL_VERSION

    match = re.match(r'OpenSSL ((\d+)\.(\d+)\.(\d+))', ssl.OPENSSL_VERSION)
    if not match:
        # Ignore the missing SSL package
        return

    major = int(match.group(2))
    minor = int(match.group(3))
    patch = int(match.group(4))

    if major >= 1 and minor >= 0 and patch >= 2:
        return  # all ok

    warnings.warn("""
The Python interpreter being used has an old version of SSL. The recommended
minimum version for the SDK is 1.0.2, however security best practice is to use the latest
available version of SSL, which can be found at https://www.openssl.org.
Reported SSL version is '""" + version + "'")
