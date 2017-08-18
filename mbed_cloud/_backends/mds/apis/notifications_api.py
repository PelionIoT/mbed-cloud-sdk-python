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


class NotificationsApi(object):
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

    def v2_notification_callback_put(self, webhook, **kwargs):
        """
        Register a callback URL
        Register a URL to which the server should deliver notifications of the subscribed resource changes. To get notifications pushed you need to also place the subscriptions.  The maximum length of URL, header keys and values, all combined, is 400 characters.  Notifications are delivered as PUT messages to the HTTP server defined by the client with a subscription server message.  The given URL should be accessible and respond to the PUT request with response code of 200 or 204. mbed Cloud Connect  tests the callback URL with an empty payload when the URL is registered. For more information on callback notification, see [NotificationMessage](/docs/v1.2/api-references/connect-api.html#notificationmessage).  **Note**: Only one callback URL per an API key can be active. If you register a new URL while another one is already active,  it replaces the active one. There can be only one notification channel at a time. If the Long Poll notification is already present  you need to delete it before setting the callback URL.  **Expiration of a callback URL:**   A callback can expire when mbed DS cannot deliver a notification due to a connection timeout or  error response (4xx or 5xx). After each delivery failure, mbed DS sets an exponential back off time and makes a retry attempt  after that. The first retry delay is 1 second, then 2s, 4s, 8s, ..., 2min, 2min. The maximum retry delay is 2 minutes.  The callback URL will be removed if all retries fail withing 24 hours. More about [notification sending logic](/docs/v1.2/device-dev/developer-guide-to-mbed-cloud-connect.html#notification-sending-logic).  **Example usage:**      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/notification/callback \\       -H 'authorization: Bearer {api-key}' \\       -H 'content-type: application/json' \\       -d '{       \"url\": \"{callback-url}\",       \"headers\": {}       }' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_callback_put(webhook, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Webhook webhook: A json object that contains the optional headers and the URL to which the notifications need to be sent.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_notification_callback_put_with_http_info(webhook, **kwargs)
        else:
            (data) = self.v2_notification_callback_put_with_http_info(webhook, **kwargs)
            return data

    def v2_notification_callback_put_with_http_info(self, webhook, **kwargs):
        """
        Register a callback URL
        Register a URL to which the server should deliver notifications of the subscribed resource changes. To get notifications pushed you need to also place the subscriptions.  The maximum length of URL, header keys and values, all combined, is 400 characters.  Notifications are delivered as PUT messages to the HTTP server defined by the client with a subscription server message.  The given URL should be accessible and respond to the PUT request with response code of 200 or 204. mbed Cloud Connect  tests the callback URL with an empty payload when the URL is registered. For more information on callback notification, see [NotificationMessage](/docs/v1.2/api-references/connect-api.html#notificationmessage).  **Note**: Only one callback URL per an API key can be active. If you register a new URL while another one is already active,  it replaces the active one. There can be only one notification channel at a time. If the Long Poll notification is already present  you need to delete it before setting the callback URL.  **Expiration of a callback URL:**   A callback can expire when mbed DS cannot deliver a notification due to a connection timeout or  error response (4xx or 5xx). After each delivery failure, mbed DS sets an exponential back off time and makes a retry attempt  after that. The first retry delay is 1 second, then 2s, 4s, 8s, ..., 2min, 2min. The maximum retry delay is 2 minutes.  The callback URL will be removed if all retries fail withing 24 hours. More about [notification sending logic](/docs/v1.2/device-dev/developer-guide-to-mbed-cloud-connect.html#notification-sending-logic).  **Example usage:**      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/notification/callback \\       -H 'authorization: Bearer {api-key}' \\       -H 'content-type: application/json' \\       -d '{       \"url\": \"{callback-url}\",       \"headers\": {}       }' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_callback_put_with_http_info(webhook, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Webhook webhook: A json object that contains the optional headers and the URL to which the notifications need to be sent.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_notification_callback_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook' is set
        if ('webhook' not in params) or (params['webhook'] is None):
            raise ValueError("Missing the required parameter `webhook` when calling `v2_notification_callback_put`")


        collection_formats = {}

        resource_path = '/v2/notification/callback'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook' in params:
            body_params = params['webhook']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PUT',
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

    def v2_notification_pull_delete(self, **kwargs):
        """
        Delete notification Long Poll channel
        To delete a notification Long Poll channel. This is required to change the channel from Long Poll to a callback.  **Example usage:**      curl -X DELETE https://api.us-east-1.mbedcloud.com/v2/notification/pull -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_pull_delete(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_notification_pull_delete_with_http_info(**kwargs)
        else:
            (data) = self.v2_notification_pull_delete_with_http_info(**kwargs)
            return data

    def v2_notification_pull_delete_with_http_info(self, **kwargs):
        """
        Delete notification Long Poll channel
        To delete a notification Long Poll channel. This is required to change the channel from Long Poll to a callback.  **Example usage:**      curl -X DELETE https://api.us-east-1.mbedcloud.com/v2/notification/pull -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_pull_delete_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_notification_pull_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/v2/notification/pull'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

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

    def v2_notification_pull_get(self, **kwargs):
        """
        Get notifications using Long Poll
        In this case, notifications are delivered through HTTP long poll requests. The HTTP request is kept open until an event notification or a batch of event notifications are delivered to the client or the request times out  (response code 204). In both cases, the client should open a new polling connection after the previous one closes. Only a single long polling connection per API key can be ongoing at any given time. You must have a persistent connection (Connection keep-alive header in the request) to avoid excess  TLS handshakes.  **Note:** If it is not possible to have a public facing callback URL, for example when developing on your local machine, you can use long polling to check for new messages. However, long polling is deprecated and will likely be replaced in future. It is meant only for experimentation and not for commercial usage. The proper method to receive notifications is via [Notification Callback](/docs/v1.2/api-references/connect-api.html#v2-notification-callback). Only a single notification channel per API key can exist in mbed Cloud Connect at a time. If a callback notification channel already exists, you need to delete it before creating a long poll notification channel, and vice-versa.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/notification/pull -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_pull_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: NotificationMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_notification_pull_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_notification_pull_get_with_http_info(**kwargs)
            return data

    def v2_notification_pull_get_with_http_info(self, **kwargs):
        """
        Get notifications using Long Poll
        In this case, notifications are delivered through HTTP long poll requests. The HTTP request is kept open until an event notification or a batch of event notifications are delivered to the client or the request times out  (response code 204). In both cases, the client should open a new polling connection after the previous one closes. Only a single long polling connection per API key can be ongoing at any given time. You must have a persistent connection (Connection keep-alive header in the request) to avoid excess  TLS handshakes.  **Note:** If it is not possible to have a public facing callback URL, for example when developing on your local machine, you can use long polling to check for new messages. However, long polling is deprecated and will likely be replaced in future. It is meant only for experimentation and not for commercial usage. The proper method to receive notifications is via [Notification Callback](/docs/v1.2/api-references/connect-api.html#v2-notification-callback). Only a single notification channel per API key can exist in mbed Cloud Connect at a time. If a callback notification channel already exists, you need to delete it before creating a long poll notification channel, and vice-versa.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/notification/pull -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_notification_pull_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: NotificationMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_notification_pull_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/v2/notification/pull'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='NotificationMessage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
