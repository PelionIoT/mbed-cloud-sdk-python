# --------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Core functionality for the SDK"""

from __future__ import print_function
from __future__ import unicode_literals

import datetime

from mbed_cloud.configuration import Config
from mbed_cloud import filters

from builtins import object
from six.moves import urllib

from six import iteritems


class BaseAPI(object):
    """BaseAPI is parent class for all APIs. Ensuring config is valid and available."""

    api_structure = {}

    def __init__(self, params=None):
        """Ensure the config is valid and has all required fields."""
        self.config = Config(params)
        self.apis = {}
        self.api_clients = {}
        for api_parent_class, child_classes in self.api_structure.items():
            self._init_api(api_parent_class, child_classes)

    def _get_api(self, api_class):
        return self.apis.get(api_class, None)

    def _init_api(self, api_parent_class, apis):
        api_client = api_parent_class.ApiClient()
        self.api_clients[api_parent_class] = api_client

        api_client.configuration.__class__._default = None  # disable codegen's singleton behaviour
        api_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
        api_client.configuration.safe_chars_for_path_param = "/"  # don't encode (resource paths)
        self._update_api_client(api_parent_class)

        self.apis.update({api_cls: api_cls(api_client) for api_cls in apis})

    def _update_api_client(self, api_parent_class=None):
        """Updates the ApiClient object of specified parent api (or all of them)"""
        clients = ([self.api_clients[api_parent_class]]
                   if api_parent_class else self.api_clients.values())

        for api_client in clients:
            api_client.configuration.host = (self.config.get('host') or
                                             api_client.configuration.host)
            api_client.configuration.api_key['Authorization'] = self.config['api_key']

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

    def _verify_filters(self, kwargs, obj, encode=False):
        """Legacy entrypoint with 'encode' flag"""
        return (filters.legacy_filter_formatter if encode else filters.filter_formatter)(
            kwargs,
            obj._get_attributes_map()
        )

    def get_last_api_metadata(self):
        """Get meta data for the last Mbed Cloud API call.

        :returns: meta data of the last Mbed Cloud API call
        :rtype: ApiMetadata
        """
        last_metadata = None
        for key, api in iteritems(self.apis):
            api_client = api.api_client
            if api_client is not None:
                metadata = api_client.get_last_metadata()
                if metadata is not None and metadata.get('timestamp', None) is not None:
                    if last_metadata is None:
                        last_metadata = metadata
                    elif metadata["timestamp"] >= last_metadata["timestamp"]:
                        last_metadata = metadata
        if last_metadata is not None:
            last_metadata = ApiMetadata(last_metadata.get("url"),
                                        last_metadata.get("method"),
                                        last_metadata.get("response", None),
                                        last_metadata.get("return_data", None),
                                        last_metadata.get("exception", None))
        return last_metadata


class BaseObject(object):
    """Base class for APIs classes."""

    def __init__(self, dictionary):
        """Initialize object."""
        self.update_attributes(dictionary)

    def update_attributes(self, dictionary):
        """Update attributes."""
        if not isinstance(dictionary, dict):
            dictionary = dictionary.to_dict()
        for key, value in iteritems(self._get_attributes_map()):
            if value in dictionary and not hasattr(self, "_%s" % key):
                setattr(self, "_%s" % key, dictionary.get(value, None))

    @staticmethod
    def _get_attributes_map():
        """Override in child class."""
        pass

    @classmethod
    def _create_request_map(obj, input_map):
        """Create request map."""
        request_map = {}
        attributes_map = obj._get_attributes_map()
        for key, value in iteritems(input_map):
            val = attributes_map.get(key, None)
            if val is not None:
                request_map[val] = value
        return request_map

    def to_dict(self):
        """Return dictionary of object."""
        dictionary = {}
        for key, value in iteritems(self._get_attributes_map()):
            dictionary[key] = getattr(self, str(key), None)
        return dictionary

    def _get_operator(self, key):
        operator = ""
        if key.endswith("__eq"):
            operator = "eq"
        elif key.endswith("__neq"):
            operator = "neq"
        elif key.endswith("__lte"):
            operator = "lte"
        elif key.endswith("__gte"):
            operator = "gte"
        return operator

    def _decode_query(self, query):
        qs = urllib.parse.parse_qs(urllib.parse.unquote(query))
        query = {}
        for (key, value) in list(qs.items()):
            operator = self._get_operator(key)
            if operator is not "":
                key = key.replace("__%s" % (operator), "")
            else:
                operator = "eq"
            if key.startswith("custom_attributes"):
                key = key.replace("custom_attributes__", "")
                if "custom_attributes" not in query:
                    query["custom_attributes"] = {}
                val = query["custom_attributes"].get(key, {})
                val["$%s" % (operator)] = value[0]
                query["custom_attributes"][key] = val
            else:
                val = query.get(key, {})
                val["$%s" % (operator)] = value[0]
                query[key] = val
        return query

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

    def __init__(self, func, lwrap_type=None, init_data=None, **kwargs):
        """Initialize wrapper by passing in object with metadata structure.

        :param lwrap_type: Wrap each response element in type
        :param init_data: Initialize pagination object with data
        """
        self._func = func
        self._lwrap_type = lwrap_type
        self._kwargs = kwargs
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
        data_stream = resp.data or []

        # Update properties
        self._has_more = resp.has_more
        self._data = [self._lwrap_type(e) if self._lwrap_type else e for e in data_stream]
        self._total_count = getattr(resp, 'total_count', len(self._data))

        if len(data_stream) > 0:
            # Update 'after' by taking the last element ID
            self._kwargs['after'] = data_stream[-1].id
        else:
            self._kwargs.pop('after', None)

    def _get_total_count(self):
        resp = self._func(**{'include': 'total_count', 'limit': 2})
        if hasattr(resp, 'total_count'):
            return resp.total_count
        return 0

    def next(self):
        """Get the next element in response list.

        It will make call to get next page with data if there is still data to retrieve.
        """
        return self.__next__()

    def __next__(self):
        """Get the next element in list."""
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
        total count of elements, you can explicitly request the total of elements
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


class ApiMetadata(object):
    """Api meta data."""

    def __init__(self, url, method, response=None, response_data=None, exception=None):
        """Initialise new api metadata object."""
        self._url = url
        self._method = method
        self._status_code = 400
        self._headers = []
        self._request_id = ""
        self._object = None
        self._etag = ""
        self._error_message = ""
        self._date = datetime.datetime.utcnow()
        if exception is not None:
            self._set_exception(exception)
            self._set_headers(exception)
        else:
            self._set_response(response, response_data)
            self._set_headers(response)

    def _set_headers(self, obj):
        if hasattr(obj, 'getheaders'):
            self._headers = obj.getheaders()
            self._date = self._headers.get("date", datetime.datetime.utcnow())
            self._request_id = self._headers.get("x-request-id", "")
        elif hasattr(obj, 'headers'):
            self._headers = getattr(obj, "headers")
            self._date = self._headers.get("date", datetime.datetime.utcnow())
            self._request_id = self._headers.get("x-request-id", "")

    def _set_exception(self, exception):
        if hasattr(exception, 'status'):
            self._status_code = getattr(exception, 'status')
        if hasattr(exception, 'reason'):
            self._error_message = getattr(exception, 'reason')
        else:
            self._error_message = str(exception) or ''
        if hasattr(exception, 'body'):
            self._set_response(getattr(exception, 'body'))

    def _set_response(self, response=None, response_data=None):
        if response is not None:
            if hasattr(response, 'status'):
                self._status_code = getattr(response, 'status')
            self._set_headers(response)
        if response_data is not None:
            if hasattr(response_data, 'object'):
                self._object = getattr(response_data, 'object')
            if hasattr(response_data, 'etag'):
                self._etag = getattr(response_data, 'etag')

    @property
    def url(self):
        """URL of the API request.

        :rtype: str
        """
        return self._url

    @property
    def method(self):
        """Method of the API request.

        :rtype: str
        """
        return self._method

    @property
    def status_code(self):
        """HTTP Status code of the API response.

        :rtype: int
        """
        return self._status_code

    @property
    def date(self):
        """Date of the API response.

        :rtype: datetime
        """
        return self._date

    @property
    def headers(self):
        """Headers in the API response.

        :rtype: list
        """
        return self._headers

    @property
    def request_id(self):
        """Request ID of the transaction.

        :rtype: str
        """
        return self._request_id

    @property
    def object(self):
        """Object type of the returned data.

        :rtype: str
        """
        return self._object

    @property
    def etag(self):
        """Etag of the returned data.

        :rtype: str
        """
        return self._etag

    @property
    def error_message(self):
        """Error message.

        :rtype: str
        """
        return self._error_message

    def to_dict(self):
        """Return dictionary of object."""
        dictionary = {}
        for key, value in iteritems(self.__dict__):
            property_name = key[1:]
            if hasattr(self, property_name):
                dictionary.update({property_name: getattr(self, property_name, None)})
        return dictionary

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())
