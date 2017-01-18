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

    def __init__(self, func, lwrap_type=None, init_data=[], **kwargs):
        """Initialize wrapper by passing in object with metadata structure.

        :param lwrap_type: Wrap each response element in type
        :param init_data: Initialize pagination object with data
        """
        self._func = func
        self._lwrap_type = lwrap_type
        self._kwargs = kwargs
        self._idx = 0

        # Initial values, will be updated in first response
        self.has_more = False
        self._data = init_data
        self.total_count = None if not self._data else len(self._data)

        # Do initial request, if needed.
        if not self._data:
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

        .. code-block:: python

            >>> for elem, idx in api.list_users().iteritems():
            >>>    print(idx, elem)
            1,<Object #1>
            2,<Object #2>
            ...

        :returns: Yields tuples of (`element`, `idx`).
        :rtype: tuple
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

    def as_list(self):
        """Return the paginated response as a list containing all elements.

        Warning: if the list contains many pages this might block for a long time
        and consume a lot of memory. Do investigate if using more fine grained control
        functions such as `iteritems` and `next` is more suited for your needs.

        .. code-block:: python

            >>> len(api.list_users().as_list())
            13

        :returns: The paginated response as a Python list
        :rtype: list
        """
        return [d for d, idx in self.iteritems()]

    def next(self):
        """Get the next page of content.

        .. code-block:: python

            >>> p = api.list_users()
            >>> len(p.data)
            50
            >>> p.next()
            >>> len(p.data)
            23

        As one can see in the example we finely control the iteration of the
        pagination and in total we would here have 50+23=73 users.

        """
        self._get_page()

    def count(self):
        """Get the total count from the meta data.

        As the count, due to backend cost, doesn't always respond with the
        total count of elements we can explicitly request the total of elements
        that will be returned by a paginated request.

        .. code-block:: python

            # Will only do 1-2 requests, regardless of how many pages of users
            # there are. If initial page respons contains the total count it will
            # only require one request.
            >>> api.list_users().count()
            73
        """
        if not self.total_count:
            return self._get_total_count()
        return self.total_count

    @property
    def data(self):
        """The current data from doing last paginated request.

        .. code-block:: python

            >>> api.list_users().data[0].full_name
            "David Bowie"
        """
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
