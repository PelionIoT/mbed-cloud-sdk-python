# coding: utf-8

"""
    Connect CA API

    Connect CA API provides methods to create and get Developer certificate. Also Connect CA provides server-credentials for Bootstarp and LWM2M Server.

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


class DeveloperCertificateApi(object):
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

    def v3_developer_certificates_id_get(self, id, authorization, **kwargs):
        """
        Fetch an existing developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificates_id_get(id, authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: A unique identifier for the developer certificate.  (required)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_developer_certificates_id_get_with_http_info(id, authorization, **kwargs)
        else:
            (data) = self.v3_developer_certificates_id_get_with_http_info(id, authorization, **kwargs)
            return data

    def v3_developer_certificates_id_get_with_http_info(self, id, authorization, **kwargs):
        """
        Fetch an existing developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificates_id_get_with_http_info(id, authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: A unique identifier for the developer certificate.  (required)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_developer_certificates_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v3_developer_certificates_id_get`")
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_developer_certificates_id_get`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v3/developer-certificates/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeveloperCertificateResponseData',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def v3_developer_certificates_post(self, authorization, body, **kwargs):
        """
        Create a new developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  Limitations:    - One developer certificate allows up to 100 devices to connect to bootstrap server.   - Only 10 developer certificates are allowed per account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificates_post(authorization, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Bearer {Access Token}.  (required)
        :param DeveloperCertificateRequestData body: (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_developer_certificates_post_with_http_info(authorization, body, **kwargs)
        else:
            (data) = self.v3_developer_certificates_post_with_http_info(authorization, body, **kwargs)
            return data

    def v3_developer_certificates_post_with_http_info(self, authorization, body, **kwargs):
        """
        Create a new developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  Limitations:    - One developer certificate allows up to 100 devices to connect to bootstrap server.   - Only 10 developer certificates are allowed per account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificates_post_with_http_info(authorization, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Bearer {Access Token}.  (required)
        :param DeveloperCertificateRequestData body: (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_developer_certificates_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_developer_certificates_post`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v3_developer_certificates_post`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v3/developer-certificates', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeveloperCertificateResponseData',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
