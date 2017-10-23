# ---------------------------------------------------------------------------
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
"""Initialise the mbed_cloud config and BaseAPI."""
from __future__ import print_function
from __future__ import unicode_literals

from builtins import object
import datetime
from six import iteritems
from six import string_types
import sys

from six.moves import urllib

from mbed_cloud._version import __version__  # noqa
from mbed_cloud.bootstrap import Config
from mbed_cloud.exceptions import CloudValueError

config = Config()


class BaseAPI(object):
    """BaseAPI is parent class for all APIs. Ensuring config is valid and available."""

    def __init__(self, user_config={}):
        """Ensure the config is valid and has all required fields."""
        config.update(user_config)
        self.apis = []
        if "host" in config:
            # Strip leading and trailing slashes from host
            config.update({'host': config['host'].strip('/')})
            if not config["host"].startswith("https"):
                sys.stderr.write("'host' config needs to use protocol HTTPS. Ignoring.\n")
                sys.stderr.flush()
                del config["host"]
        else:
            # Host is not set. Set default host.
            config.update({'host': 'https://api.us-east-1.mbedcloud.com'})

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
        self.apis.append(api)
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

    def _verify_filters(self, kwargs, obj, encode=False):
        if kwargs.get('filters'):
            kwargs.update({'filter': kwargs.get('filters')})
            del kwargs['filters']
        if 'filter' in kwargs:
            filters = kwargs.get('filter')
            if filters and not isinstance(filters, dict):
                raise CloudValueError("'filters' parameter needs to be of type dict")
            filters = self._encode_query(filters, obj, encode)
            if encode:
                kwargs.update({'filter': filters})
            else:
                for k, v in list(filters.items()):
                    kwargs[k] = v
                del kwargs['filter']
        return kwargs

    def _encode_query(self, filters, obj, encode=True):
        updated_filters = {}
        for k, v in list(filters.items()):
            val = obj._get_attributes_map().get(k, None)
            if val is not None:
                updated_filters[val] = filters[k]
            else:
                updated_filters[k] = v
        self._set_custom_attributes(updated_filters)
        filters = self._create_filters_dict(updated_filters, encode)
        if encode:
            return urllib.parse.urlencode(sorted(filters.items()))
        else:
            return filters

    def _create_filters_dict(self, query, encode):
        filters = {}
        for k, v in list(query.items()):
            if not isinstance(v, dict):
                # Set default operator as eq
                v = {'$eq': v}
            for operator, val in list(v.items()):
                val = self._convert_filter_value(val)
                suffix = self._get_key_suffix(operator, encode)
                key = "%s%s" % (k, suffix)
                if encode:
                    if not isinstance(val, string_types):
                        val = str(val)
                    filters[key] = urllib.parse.quote(val)
                else:
                    filters[key] = val
        return filters

    def _convert_filter_value(self, value):
        if isinstance(value, datetime.datetime):
            value = value.isoformat() + "Z"
        return value

    def _set_custom_attributes(self, query):
        if "custom_attributes" in query:
            custom_attributes = query["custom_attributes"]
            del query["custom_attributes"]
            if not isinstance(custom_attributes, dict):
                raise CloudValueError("Custom attributes when creating query"
                                      "needs to be dict object")
            for k, v in list(custom_attributes.items()):
                if not k:
                    print("Ignoring custom attribute with value %r as key is empty" % (v,))
                    continue
                query['custom_attributes__' + k] = v

    def _get_key_suffix(self, operator, replace_eq=True):
        suffix = ""
        operator = operator.replace("$", "")
        if replace_eq and operator == "eq":
            suffix = ""
        elif operator == "ne":
            suffix = "__neq"
        else:
            suffix = "__%s" % (operator)
        return suffix

    def get_last_api_metadata(self):
        """Get meta data for the last Mbed Cloud API call.

        :returns: meta data of the last Mbed Cloud API call
        :rtype: ApiMetadata
        """
        last_metadata = None
        for api in self.apis:
            api_client = api.configuration.api_client
            if api_client is not None:
                metadata = api_client.get_last_metadata()
                if metadata is not None:
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
            dictionary[key] = getattr(self, key, None)
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

        # Update properties
        self._has_more = resp.has_more
        self._data = [self._lwrap_type(e) if self._lwrap_type else e for e in resp.data]
        if hasattr(resp, 'total_count'):
            self._total_count = resp.total_count
        else:
            self._total_count = len(self._data)

        if len(resp.data) > 0:
            # Update 'after' by taking the last element ID
            self._kwargs['after'] = resp.data[-1].id
        else:
            if 'after' in self._kwargs:
                del self._kwargs['after']

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
