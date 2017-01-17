"""Initialise the mbed_cloud config and BaseAPI."""
from six import string_types
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

        # Ensure URL is base string, not unicode (Issue22231)
        url = api.configuration.host
        if not isinstance(url, string_types):
            url = '%s' % url
        if not isinstance(url, str):
            url = url.encode('utf-8')
        api.configuration.host = url

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


class PaginatedResponse(object):
    """Paginated response object wrapper.

    Used to access multiple pages of data, either through manually
    iterating pages or using iterators.
    """

    def __init__(self, func, lwrap_type=None, **kwargs):
        """Initialize wrapper by passing in object with metadata structure."""
        self._func = func
        self._lwrap_type = lwrap_type
        self._kwargs = kwargs
        self._idx = 0

        # Initial values, will be updated in first response
        self.has_more = False
        self.total_count = None
        self.data = []

        # Do initial request
        self._get_page()

    def _get_page(self):
        resp = self._func(**self._kwargs)

        # Update properties
        self.has_more = resp.has_more
        self.total_count = resp.total_count
        self.data = [self._lwrap_type(e) if self._lwrap_type else e for e in resp.data]

        # Update 'after' by taking the last element ID
        if len(resp.data) > 0:
            self._kwargs['after'] = resp.data[-1].id
        else:
            if 'after' in self._kwargs:
                del self._kwargs['after']

    def _get_total_count(self):
        resp = self._func(**{'include': 'total_count', 'limit': 2})
        return resp.total_count

    def iteritems(self):
        """Iterate through elements of the paginated resonse.

        This will get the next page where required. As a consequence,
        do take not that this method might do multiple calls in the background.
        """
        while True:
            # Yield the data elements one by one
            for e in self.data:
                yield e, self._idx
                self._idx += 1

            # Check if there's more data to get
            if not self.has_more:
                break

            # It is, so let's make the request
            self.next()

    def next(self):
        """Get the next page of content."""
        self._get_page()

    def count(self):
        """Get the total count from the meta data."""
        if not self.total_count:
            return self._get_total_count()
        return self.total_count
