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
import platform
import threading

from mbed_cloud import __version__
from mbed_cloud.configuration import Config
from mbed_cloud import filters

from builtins import object
from six.moves import urllib

from six import iteritems

_codegen_singleton_protection = threading.Lock()


class BaseAPI(object):
    """BaseAPI is parent class for all APIs. Ensuring config is valid and available."""

    api_structure = {}

    def __init__(self, params=None):
        """A module to access this section of the Mbed Cloud API.

        :param params: Dictionary to override configuration values
        """
        self.config = Config(params)
        self.apis = {}
        self.api_clients = {}
        for api_parent_class, child_classes in self.api_structure.items():
            self._init_api(api_parent_class, child_classes)

    def _get_api(self, api_class):
        return self.apis.get(api_class, None)

    def _init_api(self, api_parent_class, apis):
        with _codegen_singleton_protection:
            api_client = api_parent_class.ApiClient()
            self.api_clients[api_parent_class] = api_client
            # disable codegen's singleton behaviour
            # otherwise `TypeWithDefault` will try copying the config details
            api_client.configuration.__class__._default = None

        api_client.user_agent = "mbed-cloud-sdk-python/{sdk_ver} ({pfm}) Python/{py_ver}".format(
            sdk_ver=__version__,
            pfm=platform.platform(),
            py_ver=platform.python_version())
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


class StubAPI(BaseAPI):
    """Used in test framework"""

    def __init__(self, params):
        """For use in test verification"""
        # because we take a positional dictionary rather than **kwargs
        # we have to be careful to replicate this for the testrunner
        self.kwargs = params

    def exception(self):
        """Raises an exception"""
        raise ValueError('just a test')

    def success(self, **kwargs):
        """Returns all arguments received in init and this method call"""
        response = {'success': True}
        # check dates can be manipulated
        response.update(kwargs)
        response.update(self.kwargs)
        response['test_argument3'] = datetime.timedelta(days=1) + response['test_argument3']
        return response


class BaseObject(object):
    """Base class for APIs classes."""

    def __init__(self, dictionary):
        """Initialize object."""
        self.update_attributes(dictionary)

    def update_attributes(self, updates):
        """Update attributes."""
        if not isinstance(updates, dict):
            updates = updates.to_dict()
        for sdk_key, spec_key in self._get_attributes_map().items():
            attr = '_%s' % sdk_key
            if spec_key in updates and not hasattr(self, attr):
                setattr(self, attr, updates[spec_key])

    @staticmethod
    def _get_attributes_map():
        """Override in child class."""
        pass

    @classmethod
    def _create_request_map(cls, input_map):
        """Create request map."""
        field_map = cls._get_attributes_map()
        return {field_map[k]: v for k, v in input_map.items() if k in field_map}

    def to_dict(self):
        """Return dictionary of object."""
        return {sdk_key: getattr(self, sdk_key, None) for sdk_key in self._get_attributes_map()}

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
            if operator != "":
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
