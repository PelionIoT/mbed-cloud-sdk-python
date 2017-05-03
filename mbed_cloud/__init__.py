# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Initialise the mbed_cloud config and BaseAPI."""
from six import iteritems
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
            raise ValueError("api_key not found in config. Please see documentation.")

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

        # Ensure we don't encode /
        api.configuration.safe_chars = "/"

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
            kwargs.update({'filter': urllib.urlencode(kwargs.get('filter'))})
        if kwargs.get('filters'):
            kwargs.update({'filter': urllib.urlencode(kwargs.get('filters'))})
            del kwargs['filters']
        return kwargs


class BaseObject(object):
    """Base class for APIs classes."""

    def __init__(self, obj):
        """Override __init__ and allow passing in backend object."""
        if not isinstance(obj, dict):
            obj = obj.to_dict()
        for key, value in iteritems(self._get_attributes_map()):
            setattr(self, "_%s" % key, obj.get(value, None))

    @staticmethod
    def _get_attributes_map():
        """Override in child class."""
        pass

    def to_dict(self):
        """Return dictionary of object."""
        dictionary = {}
        for key, value in iteritems(self._get_attributes_map()):
            dictionary[key] = getattr(self, key, None)
        return dictionary

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())


class _FakePaginatedResponse(object):
    """Fake a summary page that is returned from API when mocking paginated response."""

    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return {
            'data': [e.to_dict() for e in self.data],
            'total_count': len(self.data),
            'has_more': False
        }


class PaginatedResponse(object):
    """Paginated response object wrapper.

    Used to access multiple pages of data, either through manually
    iterating pages or using iterators.
    """

    def __init__(self, func, lwrap_type=None, init_data=None, limit=None, **kwargs):
        """Initialize wrapper by passing in object with metadata structure.

        :param lwrap_type: Wrap each response element in type
        :param init_data: Initialize pagination object with data
        """
        self._func = func
        self._lwrap_type = lwrap_type
        self._kwargs = kwargs
        self._limit = limit
        self._data = None

        # Initial values, will be updated in first response
        self._raw_response = None
        self._has_more = False
        self._idx = 0
        if init_data is not None:
            self._data = init_data
            self._raw_response = _FakePaginatedResponse(init_data)

        # Calculate total count on initial data, if set.
        self._total_count = None if self._data is None else len(self._data)

        # Do initial request, if needed.
        if self._data is None:
            self._get_page()

    def _get_page(self):
        resp = self._func(**self._kwargs)
        self._raw_response = resp

        # Update properties
        self._has_more = resp.has_more
        self._total_count = resp.total_count
        self._data = [self._lwrap_type(e) if self._lwrap_type else e for e in resp.data]

        # Update 'after' by taking the last element ID
        if len(resp.data) > 0:
            self._kwargs['after'] = resp.data[-1].id
        else:
            if 'after' in self._kwargs:
                del self._kwargs['after']

    def _get_total_count(self):
        resp = self._func(**{'include': 'total_count', 'limit': 2})
        return resp.total_count

    def next(self):
        """Get the next element in list.

        As one can see in the example we finely control the iteration of the
        pagination and in total we would here have 50+23=73 users.
        """
        # If we've reached the limit, we stop.
        if self._limit is not None and self._idx == self._limit:
            raise StopIteration

        # If we don't have any data, then we just return.
        if self._data is None:
            raise StopIteration

        # If we have an empty data array, but more data in the pipe we
        # fetch it. If not we're done iterating.
        if len(self._data) == 0 and self.has_more:
            self._get_page()
        if len(self._data) == 0 and not self.has_more:
            raise StopIteration

        # Grab first item and return
        r_value = self._data[0]
        self._data = self._data[1:]
        self._idx += 1
        return r_value

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
        if self._total_count is None:
            return self._get_total_count()
        return self._total_count

    def to_dict(self):
        """Propagate the to_dict of the inner response for the paginated response."""
        return self._raw_response.to_dict()

    def __iter__(self):
        """Override iter, as to provide iterable interface to Pagination object.

        This was you can iterate over PaginatinatedResponse objects like so:

        .. code-block:: python

            obj = PaginatedResponse(..)
            for x in obj:
                print(x)

        """
        return self

    @property
    def has_more(self):
        """Get status of whether the paginated response has more content."""
        return self._has_more

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
