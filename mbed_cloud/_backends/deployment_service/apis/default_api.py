# coding: utf-8

"""
    Deployment Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 0.1
    
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

    def update_campaign_create(self, campaign, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Create update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_create(campaign, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateCampaignPostRequest campaign: Update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_create_with_http_info(campaign, **kwargs)
        else:
            (data) = self.update_campaign_create_with_http_info(campaign, **kwargs)
            return data

    def update_campaign_create_with_http_info(self, campaign, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Create update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_create_with_http_info(campaign, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateCampaignPostRequest campaign: Update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign' is set
        if ('campaign' not in params) or (params['campaign'] is None):
            raise ValueError("Missing the required parameter `campaign` when calling `update_campaign_create`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'campaign' in params:
            body_params = params['campaign']
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaign',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_destroy(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Delete update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_destroy(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_destroy_with_http_info(campaign_id, **kwargs)
        else:
            (data) = self.update_campaign_destroy_with_http_info(campaign_id, **kwargs)
            return data

    def update_campaign_destroy_with_http_info(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Delete update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_destroy_with_http_info(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_destroy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_destroy`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

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
                                        response_type='UpdateCampaign',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_list(self, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>List all update campaigns.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-campaign-properties-all-properties-are-filterable\">By campaign properties (all properties are filterable):</h5> <p>For example: <code>state=[draft|scheduled|devicefectch|devicecopy|devicecopycomplete|publishing|deploying|deployed|manifestremoved|expired]</code></p> <p><code>root_manifest_id=43217771234242e594ddb433816c498a</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>state=deployed&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: how many objects to retrieve in the page
        :param str order: ASC or DESC
        :param str after: the ID of the the item after which to retrieve the next page
        :param str filter: URL encoded query string parameter to filter returned data
        :param str include: Comma separated list of data fields to return. Currently supported: total_count
        :param str created_at:
        :param str created_at__lte:
        :param str created_at__gte:
        :param str description:
        :param str device_filter:
        :param str etag:
        :param str etag__lte:
        :param str etag__gte:
        :param str finished:
        :param str finished__lte:
        :param str finished__gte:
        :param str id:
        :param str name:
        :param str object:
        :param str root_manifest_id:
        :param str root_manifest_url:
        :param str started_at:
        :param str started_at__lte:
        :param str stated_at__gte:
        :param str state:
        :param str when:
        :param str when__lte:
        :param str when_gte:
        :return: UpdateCampaignPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_list_with_http_info(**kwargs)
        else:
            (data) = self.update_campaign_list_with_http_info(**kwargs)
            return data

    def update_campaign_list_with_http_info(self, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>List all update campaigns.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-campaign-properties-all-properties-are-filterable\">By campaign properties (all properties are filterable):</h5> <p>For example: <code>state=[draft|scheduled|devicefectch|devicecopy|devicecopycomplete|publishing|deploying|deployed|manifestremoved|expired]</code></p> <p><code>root_manifest_id=43217771234242e594ddb433816c498a</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>state=deployed&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: how many objects to retrieve in the page
        :param str order: ASC or DESC
        :param str after: the ID of the the item after which to retrieve the next page
        :param str filter: URL encoded query string parameter to filter returned data
        :param str include: Comma separated list of data fields to return. Currently supported: total_count
        :param str created_at:
        :param str created_at__lte:
        :param str created_at__gte:
        :param str description:
        :param str device_filter:
        :param str etag:
        :param str etag__lte:
        :param str etag__gte:
        :param str finished:
        :param str finished__lte:
        :param str finished__gte:
        :param str id:
        :param str name:
        :param str object:
        :param str root_manifest_id:
        :param str root_manifest_url:
        :param str started_at:
        :param str started_at__lte:
        :param str stated_at__gte:
        :param str state:
        :param str when:
        :param str when__lte:
        :param str when_gte:
        :return: UpdateCampaignPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'order', 'after', 'filter', 'include', 'created_at', 'created_at__lte', 'created_at__gte', 'description', 'device_filter', 'etag', 'etag__lte', 'etag__gte', 'finished', 'finished__lte', 'finished__gte', 'id', 'name', 'object', 'root_manifest_id', 'root_manifest_url', 'started_at', 'started_at__lte', 'stated_at__gte', 'state', 'when', 'when__lte', 'when_gte']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v3/update-campaigns/'.replace('{format}', 'json')
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
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'created_at__lte' in params:
            query_params['created_at__lte'] = params['created_at__lte']
        if 'created_at__gte' in params:
            query_params['created_at__gte'] = params['created_at__gte']
        if 'description' in params:
            query_params['description'] = params['description']
        if 'device_filter' in params:
            query_params['device_filter'] = params['device_filter']
        if 'etag' in params:
            query_params['etag'] = params['etag']
        if 'etag__lte' in params:
            query_params['etag__lte'] = params['etag__lte']
        if 'etag__gte' in params:
            query_params['etag__gte'] = params['etag__gte']
        if 'finished' in params:
            query_params['finished'] = params['finished']
        if 'finished__lte' in params:
            query_params['finished__lte'] = params['finished__lte']
        if 'finished__gte' in params:
            query_params['finished__gte'] = params['finished__gte']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'object' in params:
            query_params['object'] = params['object']
        if 'root_manifest_id' in params:
            query_params['root_manifest_id'] = params['root_manifest_id']
        if 'root_manifest_url' in params:
            query_params['root_manifest_url'] = params['root_manifest_url']
        if 'started_at' in params:
            query_params['started_at'] = params['started_at']
        if 'started_at__lte' in params:
            query_params['started_at__lte'] = params['started_at__lte']
        if 'stated_at__gte' in params:
            query_params['stated_at__gte'] = params['stated_at__gte']
        if 'state' in params:
            query_params['state'] = params['state']
        if 'when' in params:
            query_params['when'] = params['when']
        if 'when__lte' in params:
            query_params['when__lte'] = params['when__lte']
        if 'when_gte' in params:
            query_params['when_gte'] = params['when_gte']

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
                                        response_type='UpdateCampaignPage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_partial_update(self, campaign_id, campaign, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign fields</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_partial_update(campaign_id, campaign, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: (required)
        :param UpdateCampaignPatchRequest campaign: Update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_partial_update_with_http_info(campaign_id, campaign, **kwargs)
        else:
            (data) = self.update_campaign_partial_update_with_http_info(campaign_id, campaign, **kwargs)
            return data

    def update_campaign_partial_update_with_http_info(self, campaign_id, campaign, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign fields</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_partial_update_with_http_info(campaign_id, campaign, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: (required)
        :param UpdateCampaignPatchRequest campaign: Update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'campaign']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_partial_update`")
        # verify the required parameter 'campaign' is set
        if ('campaign' not in params) or (params['campaign'] is None):
            raise ValueError("Missing the required parameter `campaign` when calling `update_campaign_partial_update`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'campaign' in params:
            body_params = params['campaign']
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaign',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_retrieve(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Retrieve campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_retrieve(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_retrieve_with_http_info(campaign_id, **kwargs)
        else:
            (data) = self.update_campaign_retrieve_with_http_info(campaign_id, **kwargs)
            return data

    def update_campaign_retrieve_with_http_info(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Retrieve campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_retrieve_with_http_info(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_retrieve`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

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
                                        response_type='UpdateCampaign',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_update(self, campaign_id, campaign, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_update(campaign_id, campaign, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: (required)
        :param UpdateCampaignPutRequest campaign: Update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_update_with_http_info(campaign_id, campaign, **kwargs)
        else:
            (data) = self.update_campaign_update_with_http_info(campaign_id, campaign, **kwargs)
            return data

    def update_campaign_update_with_http_info(self, campaign_id, campaign, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_update_with_http_info(campaign_id, campaign, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: (required)
        :param UpdateCampaignPutRequest campaign: Update campaign (required)
        :return: UpdateCampaign
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'campaign']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_update`")
        # verify the required parameter 'campaign' is set
        if ('campaign' not in params) or (params['campaign'] is None):
            raise ValueError("Missing the required parameter `campaign` when calling `update_campaign_update`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'campaign' in params:
            body_params = params['campaign']
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaign',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
