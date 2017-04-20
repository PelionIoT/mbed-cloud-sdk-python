# device_query_service.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_query_create**](DefaultApi.md#device_query_create) | **POST** /v3/device-queries/ | 
[**device_query_destroy**](DefaultApi.md#device_query_destroy) | **DELETE** /v3/device-queries/{query_id}/ | 
[**device_query_list**](DefaultApi.md#device_query_list) | **GET** /v3/device-queries/ | 
[**device_query_partial_update**](DefaultApi.md#device_query_partial_update) | **PATCH** /v3/device-queries/{query_id}/ | 
[**device_query_retrieve**](DefaultApi.md#device_query_retrieve) | **GET** /v3/device-queries/{query_id}/ | 
[**device_query_update**](DefaultApi.md#device_query_update) | **PUT** /v3/device-queries/{query_id}/ | 


# **device_query_create**
> DeviceQuery device_query_create(device)



<p>The APIs for creating and manipulating device queries.  </p> <p>Create device query</p>

### Example 
```python
from __future__ import print_statement
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
device = device_query_service.DeviceQueryPostPutRequest() # DeviceQueryPostPutRequest | 

try: 
    api_response = api_instance.device_query_create(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_query_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceQueryPostPutRequest**](DeviceQueryPostPutRequest.md)|  | 

### Return type

[**DeviceQuery**](DeviceQuery.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_destroy**
> device_query_destroy(query_id)



<p>The APIs for creating and manipulating device queries.  </p> <p>Delete device query</p>

### Example 
```python
from __future__ import print_statement
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 

try: 
    api_instance.device_query_destroy(query_id)
except ApiException as e:
    print("Exception when calling DefaultApi->device_query_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_list**
> DeviceQueryPage device_query_list(limit=limit, order=order, after=after, filter=filter, include=include)



<p>The APIs for creating and manipulating device queries.  </p> <p>List all device queries. The result will be paged into pages of 100.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-device-query-properties-all-properties-are-filterable\">By device query properties (all properties are filterable):</h5> <p>For example: <code>description={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>query_id=0158d38771f70000000000010010038c&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>

### Example 
```python
from __future__ import print_statement
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
limit = 56 # int | how many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | the ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data (optional)
include = 'include_example' # str | Comma separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.device_query_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_query_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| how many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| the ID of the the item after which to retrieve the next page | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data | [optional] 
 **include** | **str**| Comma separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**DeviceQueryPage**](DeviceQueryPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_partial_update**
> DeviceQuery device_query_partial_update(query_id, device_query)



<p>The APIs for creating and manipulating device queries.  </p> <p>Update device query fields</p>

### Example 
```python
from __future__ import print_statement
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 
device_query = device_query_service.DeviceQueryPatchRequest() # DeviceQueryPatchRequest | 

try: 
    api_response = api_instance.device_query_partial_update(query_id, device_query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_query_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 
 **device_query** | [**DeviceQueryPatchRequest**](DeviceQueryPatchRequest.md)|  | 

### Return type

[**DeviceQuery**](DeviceQuery.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_retrieve**
> DeviceQuery device_query_retrieve(query_id)



<p>The APIs for creating and manipulating device queries.  </p> <p>Retrieve device query.</p>

### Example 
```python
from __future__ import print_statement
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 

try: 
    api_response = api_instance.device_query_retrieve(query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_query_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 

### Return type

[**DeviceQuery**](DeviceQuery.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_update**
> DeviceQuery device_query_update(query_id, body)



<p>The APIs for creating and manipulating device queries.  </p> <p>Update device query.</p>

### Example 
```python
from __future__ import print_statement
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 
body = device_query_service.DeviceQueryPostPutRequest() # DeviceQueryPostPutRequest | Device query update object

try: 
    api_response = api_instance.device_query_update(query_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_query_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 
 **body** | [**DeviceQueryPostPutRequest**](DeviceQueryPostPutRequest.md)| Device query update object | 

### Return type

[**DeviceQuery**](DeviceQuery.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

