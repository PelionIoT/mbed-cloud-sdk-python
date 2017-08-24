# coding: utf-8

"""
    Connect API

    mbed Cloud Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. mbed Cloud Connect makes connectivity to devices easy by queuing requests and caching resource values.

    OpenAPI spec version: 2
    
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


class EndpointsApi(object):
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

    def v2_endpoints_device_id_get(self, device_id, **kwargs):
        """
        List the resources on an endpoint
        The list of resources is cached by mbed Cloud Connect, so this call does not create a message to the device.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id} -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_device_id_get(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: A unique mbed Cloud device ID for an endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  (required)
        :return: list[Resource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_endpoints_device_id_get_with_http_info(device_id, **kwargs)
        else:
            (data) = self.v2_endpoints_device_id_get_with_http_info(device_id, **kwargs)
            return data

    def v2_endpoints_device_id_get_with_http_info(self, device_id, **kwargs):
        """
        List the resources on an endpoint
        The list of resources is cached by mbed Cloud Connect, so this call does not create a message to the device.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id} -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_device_id_get_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: A unique mbed Cloud device ID for an endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  (required)
        :return: list[Resource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_device_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `v2_endpoints_device_id_get`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/link-format'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v2/endpoints/{device-id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Resource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def v2_endpoints_get(self, **kwargs):
        """
        List registered endpoints. The number of endpoints is currently limited to 200.
        Endpoints are physical devices having valid registration to mbed Cloud Connect. All devices despite the registration status can be requested from Device Directory API ['/v3/devices/ ](/docs/v1.2/api-references/device-directory-api.html#v3-devices).  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/endpoints -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type: Filter endpoints by endpoint-type.
        :return: list[Endpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_endpoints_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_endpoints_get_with_http_info(**kwargs)
            return data

    def v2_endpoints_get_with_http_info(self, **kwargs):
        """
        List registered endpoints. The number of endpoints is currently limited to 200.
        Endpoints are physical devices having valid registration to mbed Cloud Connect. All devices despite the registration status can be requested from Device Directory API ['/v3/devices/ ](/docs/v1.2/api-references/device-directory-api.html#v3-devices).  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/endpoints -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type: Filter endpoints by endpoint-type.
        :return: list[Endpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/link-format'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v2/endpoints', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Endpoint]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
