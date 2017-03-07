# deployment_service.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_campaign_create**](DefaultApi.md#update_campaign_create) | **POST** /v3/update-campaigns/ | 
[**update_campaign_destroy**](DefaultApi.md#update_campaign_destroy) | **DELETE** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_list**](DefaultApi.md#update_campaign_list) | **GET** /v3/update-campaigns/ | 
[**update_campaign_partial_update**](DefaultApi.md#update_campaign_partial_update) | **PATCH** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_retrieve**](DefaultApi.md#update_campaign_retrieve) | **GET** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_update**](DefaultApi.md#update_campaign_update) | **PUT** /v3/update-campaigns/{campaign_id}/ | 


# **update_campaign_create**
> UpdateCampaign update_campaign_create(device_filter, name, campaign_id=campaign_id, description=description, finished=finished, object=object, root_manifest_id=root_manifest_id, state=state, when=when)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Create update campaign</p>

### Example 
```python
from __future__ import print_statement
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
device_filter = 'device_filter_example' # str | The filter for the devices the campaign will target
name = 'name_example' # str | A name for this campaign
campaign_id = 'campaign_id_example' # str | DEPRECATED: The ID of the campaign (optional)
description = 'description_example' # str | An optional description of the campaign (optional)
finished = '2013-10-20T19:20:30+01:00' # datetime | The timestamp when the update campaign finished (optional)
object = 'object_example' # str | The API resource entity (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str | The state of the campaign (optional)
when = '2013-10-20T19:20:30+01:00' # datetime | The timestamp at which update campaign scheduled to start (optional)

try: 
    api_response = api_instance.update_campaign_create(device_filter, name, campaign_id=campaign_id, description=description, finished=finished, object=object, root_manifest_id=root_manifest_id, state=state, when=when)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_filter** | **str**| The filter for the devices the campaign will target | 
 **name** | **str**| A name for this campaign | 
 **campaign_id** | **str**| DEPRECATED: The ID of the campaign | [optional] 
 **description** | **str**| An optional description of the campaign | [optional] 
 **finished** | **datetime**| The timestamp when the update campaign finished | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**| The state of the campaign | [optional] 
 **when** | **datetime**| The timestamp at which update campaign scheduled to start | [optional] 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_destroy**
> UpdateCampaign update_campaign_destroy(campaign_id, root_manifest_id=root_manifest_id, updating_request_id=updating_request_id, finished=finished, finished__gte=finished__gte, finished__lte=finished__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, when=when, when__gte=when__gte, when__lte=when__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, object=object, state=state, name=name, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, device_filter=device_filter, campaigndevicemetadata=campaigndevicemetadata, description=description, attempts=attempts)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Delete update campaign</p>

### Example 
```python
from __future__ import print_statement
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The ID of the update campaign
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
finished = 'finished_example' # str |  (optional)
finished__gte = 'finished__gte_example' # str |  (optional)
finished__lte = 'finished__lte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
when = 'when_example' # str |  (optional)
when__gte = 'when__gte_example' # str |  (optional)
when__lte = 'when__lte_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
object = 'object_example' # str |  (optional)
state = 'state_example' # str |  (optional)
name = 'name_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
device_filter = 'device_filter_example' # str |  (optional)
campaigndevicemetadata = 'campaigndevicemetadata_example' # str |  (optional)
description = 'description_example' # str |  (optional)
attempts = 'attempts_example' # str |  (optional)

try: 
    api_response = api_instance.update_campaign_destroy(campaign_id, root_manifest_id=root_manifest_id, updating_request_id=updating_request_id, finished=finished, finished__gte=finished__gte, finished__lte=finished__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, when=when, when__gte=when__gte, when__lte=when__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, object=object, state=state, name=name, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, device_filter=device_filter, campaigndevicemetadata=campaigndevicemetadata, description=description, attempts=attempts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the update campaign | 
 **root_manifest_id** | **str**|  | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **finished** | **str**|  | [optional] 
 **finished__gte** | **str**|  | [optional] 
 **finished__lte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **when** | **str**|  | [optional] 
 **when__gte** | **str**|  | [optional] 
 **when__lte** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **device_filter** | **str**|  | [optional] 
 **campaigndevicemetadata** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **attempts** | **str**|  | [optional] 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_list**
> UpdateCampaignPage update_campaign_list(limit=limit, order=order, after=after, filter=filter)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>List all update campaigns.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-campaign-properties-all-properties-are-filterable\">By campaign properties (all properties are filterable):</h5> <p>For example: <code>state=[draft|scheduled|devicefectch|devicecopy|devicecopycomplete|publishing|deploying|deployed|manifestremoved|expired]</code></p> <p><code>root_manifest_id=43217771234242e594ddb433816c498a</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>state=deployed&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>

### Example 
```python
from __future__ import print_statement
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
limit = 56 # int | how many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | the ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data (optional)

try: 
    api_response = api_instance.update_campaign_list(limit=limit, order=order, after=after, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| how many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| the ID of the the item after which to retrieve the next page | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data | [optional] 

### Return type

[**UpdateCampaignPage**](UpdateCampaignPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_partial_update**
> UpdateCampaign update_campaign_partial_update(campaign_id, campaign_id2=campaign_id2, description=description, device_filter=device_filter, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign fields</p>

### Example 
```python
from __future__ import print_statement
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | 
campaign_id2 = 'campaign_id_example' # str | DEPRECATED: The ID of the campaign (optional)
description = 'description_example' # str | An optional description of the campaign (optional)
device_filter = 'device_filter_example' # str | The filter for the devices the campaign will target (optional)
finished = '2013-10-20T19:20:30+01:00' # datetime | The timestamp when the update campaign finished (optional)
name = 'name_example' # str | A name for this campaign (optional)
object = 'object_example' # str | The API resource entity (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str | The state of the campaign (optional)
when = '2013-10-20T19:20:30+01:00' # datetime | The timestamp at which update campaign scheduled to start (optional)

try: 
    api_response = api_instance.update_campaign_partial_update(campaign_id, campaign_id2=campaign_id2, description=description, device_filter=device_filter, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**|  | 
 **campaign_id2** | **str**| DEPRECATED: The ID of the campaign | [optional] 
 **description** | **str**| An optional description of the campaign | [optional] 
 **device_filter** | **str**| The filter for the devices the campaign will target | [optional] 
 **finished** | **datetime**| The timestamp when the update campaign finished | [optional] 
 **name** | **str**| A name for this campaign | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**| The state of the campaign | [optional] 
 **when** | **datetime**| The timestamp at which update campaign scheduled to start | [optional] 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_retrieve**
> UpdateCampaign update_campaign_retrieve(campaign_id)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Retrieve campaign</p>

### Example 
```python
from __future__ import print_statement
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The ID of the campaign

try: 
    api_response = api_instance.update_campaign_retrieve(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign | 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_update**
> UpdateCampaign update_campaign_update(campaign_id, device_filter, name, campaign_id2=campaign_id2, description=description, finished=finished, object=object, root_manifest_id=root_manifest_id, state=state, when=when)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign</p>

### Example 
```python
from __future__ import print_statement
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | 
device_filter = 'device_filter_example' # str | The filter for the devices the campaign will target
name = 'name_example' # str | A name for this campaign
campaign_id2 = 'campaign_id_example' # str | DEPRECATED: The ID of the campaign (optional)
description = 'description_example' # str | An optional description of the campaign (optional)
finished = '2013-10-20T19:20:30+01:00' # datetime | The timestamp when the update campaign finished (optional)
object = 'object_example' # str | The API resource entity (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str | The state of the campaign (optional)
when = '2013-10-20T19:20:30+01:00' # datetime | The timestamp at which update campaign scheduled to start (optional)

try: 
    api_response = api_instance.update_campaign_update(campaign_id, device_filter, name, campaign_id2=campaign_id2, description=description, finished=finished, object=object, root_manifest_id=root_manifest_id, state=state, when=when)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**|  | 
 **device_filter** | **str**| The filter for the devices the campaign will target | 
 **name** | **str**| A name for this campaign | 
 **campaign_id2** | **str**| DEPRECATED: The ID of the campaign | [optional] 
 **description** | **str**| An optional description of the campaign | [optional] 
 **finished** | **datetime**| The timestamp when the update campaign finished | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**| The state of the campaign | [optional] 
 **when** | **datetime**| The timestamp at which update campaign scheduled to start | [optional] 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

