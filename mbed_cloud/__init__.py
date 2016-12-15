"""Initialise the mbed_cloud config and BaseAPI."""
import sys
import urllib

from mbed_cloud.bootstrap import Config

config = Config()


class BaseAPI(object):
    """BaseAPI is parent class for all APIs. Ensuring config is valid and available."""

    def __init__(self, user_config={}):
        """Ensure the config is valid and has all required fields."""
        config.update(user_config)

        if "host" in config:
            if not config["host"].startswith("https"):
                sys.stderr.write("'host' config needs to use protocol HTTPS. Ignoring.\n")
                sys.stderr.flush()
                del config["host"]

        if "api_key" not in config:
            sys.stderr.write("api_key not found in config. Please see documentation.\n")
            sys.exit(1)

    def _init_api(self, api):
        api.configuration.api_key['Authorization'] = config.get('api_key')
        api.configuration.api_key_prefix['Authorization'] = 'Bearer'
        if config.get('host'):
            api.configuration.host = config.get('host')
        return api

    def _verify_sort_options(self, kwargs):
        if kwargs.get('order'):
            order = kwargs.get('order').upper()
            if order not in ["ASC", "DESC"]:
                raise ValueError("Key 'order' needs to be either 'ASC' or 'DESC'. "
                                 "Currently: %r" % order)
            kwargs['order'] = order

        if kwargs.get('limit') is not None:
            if kwargs.get('limit') < 2 or kwargs.get('limit') > 1000:
                raise ValueError("Limit needs to be between 2 and 1000. "
                                 "Currently: %r" % kwargs.get('limit'))
        return kwargs

    def _verify_filters(self, kwargs):
        if kwargs.get('filter'):
            raise ValueError("Pass filters using dictionary and the 'filters' keyword")
        if kwargs.get('filters'):
            kwargs.update({'filter': urllib.urlencode(kwargs.get('filters'))})
            del kwargs['filters']
        return kwargs
