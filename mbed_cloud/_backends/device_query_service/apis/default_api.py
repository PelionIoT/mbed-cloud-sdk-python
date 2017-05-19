# coding: utf-8

"""
    Device Query Service API

    This is the API Documentation for the mbed device query service update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def device_query_create(self, device, **kwargs):
        """
        Create device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_create(device, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeviceQueryPostPutRequest device: (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_create_with_http_info(device, **kwargs)
        else:
            (data) = self.device_query_create_with_http_info(device, **kwargs)
            return data

    def device_query_create_with_http_info(self, device, **kwargs):
        """
        Create device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_create_with_http_info(device, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeviceQueryPostPutRequest device: (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device' is set
        if ('device' not in params) or (params['device'] is None):
            raise ValueError("Missing the required parameter `device` when calling `device_query_create`")


        collection_formats = {}

        resource_path = '/v3/device-queries/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'device' in params:
            body_params = params['device']
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceQuery',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def device_query_destroy(self, query_id, **kwargs):
        """
        Delete device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_destroy(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_destroy_with_http_info(query_id, **kwargs)
        else:
            (data) = self.device_query_destroy_with_http_info(query_id, **kwargs)
            return data

    def device_query_destroy_with_http_info(self, query_id, **kwargs):
        """
        Delete device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_destroy_with_http_info(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_destroy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_destroy`")


        collection_formats = {}

        resource_path = '/v3/device-queries/{query_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def device_query_list(self, **kwargs):
        """
        List all device queries. The result will be paged into pages of 100.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: How many objects to retrieve in the page.
        :param str order: ASC or DESC
        :param str after: The ID of the the item after which to retrieve the next page.
        :param str filter: URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ###### By device query properties (all properties are filterable): For example: ```description={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example  ```query_id=0158d38771f70000000000010010038c&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded:  ```filter=query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z```
        :param str include: Comma separated list of data fields to return. Currently supported: total_count
        :return: DeviceQueryPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_list_with_http_info(**kwargs)
        else:
            (data) = self.device_query_list_with_http_info(**kwargs)
            return data

    def device_query_list_with_http_info(self, **kwargs):
        """
        List all device queries. The result will be paged into pages of 100.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: How many objects to retrieve in the page.
        :param str order: ASC or DESC
        :param str after: The ID of the the item after which to retrieve the next page.
        :param str filter: URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ###### By device query properties (all properties are filterable): For example: ```description={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example  ```query_id=0158d38771f70000000000010010038c&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded:  ```filter=query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z```
        :param str include: Comma separated list of data fields to return. Currently supported: total_count
        :return: DeviceQueryPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'order', 'after', 'filter', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v3/device-queries/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'order' in params:
            query_params['order'] = params['order']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceQueryPage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def device_query_partial_update(self, query_id, device_query, **kwargs):
        """
        Update device query fields.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_partial_update(query_id, device_query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :param DeviceQueryPatchRequest device_query: (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_partial_update_with_http_info(query_id, device_query, **kwargs)
        else:
            (data) = self.device_query_partial_update_with_http_info(query_id, device_query, **kwargs)
            return data

    def device_query_partial_update_with_http_info(self, query_id, device_query, **kwargs):
        """
        Update device query fields.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_partial_update_with_http_info(query_id, device_query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :param DeviceQueryPatchRequest device_query: (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'device_query']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_partial_update`")
        # verify the required parameter 'device_query' is set
        if ('device_query' not in params) or (params['device_query'] is None):
            raise ValueError("Missing the required parameter `device_query` when calling `device_query_partial_update`")


        collection_formats = {}

        resource_path = '/v3/device-queries/{query_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'device_query' in params:
            body_params = params['device_query']
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceQuery',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def device_query_retrieve(self, query_id, **kwargs):
        """
        Retrieve device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_retrieve(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_retrieve_with_http_info(query_id, **kwargs)
        else:
            (data) = self.device_query_retrieve_with_http_info(query_id, **kwargs)
            return data

    def device_query_retrieve_with_http_info(self, query_id, **kwargs):
        """
        Retrieve device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_retrieve_with_http_info(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_retrieve`")


        collection_formats = {}

        resource_path = '/v3/device-queries/{query_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceQuery',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def device_query_update(self, query_id, body, **kwargs):
        """
        Update device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_update(query_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :param DeviceQueryPostPutRequest body: Device query update object. (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_update_with_http_info(query_id, body, **kwargs)
        else:
            (data) = self.device_query_update_with_http_info(query_id, body, **kwargs)
            return data

    def device_query_update_with_http_info(self, query_id, body, **kwargs):
        """
        Update device query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_update_with_http_info(query_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id: (required)
        :param DeviceQueryPostPutRequest body: Device query update object. (required)
        :return: DeviceQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_update`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `device_query_update`")


        collection_formats = {}

        resource_path = '/v3/device-queries/{query_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceQuery',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
