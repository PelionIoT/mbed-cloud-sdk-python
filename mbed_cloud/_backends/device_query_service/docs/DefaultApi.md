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



Create device query

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



Delete device query

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



List all device queries. The result will be paged into pages of 100.

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
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data. </p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-device-query-properties-all-properties-are-filterable\">By device query properties (all properties are filterable):</h5> <p>For example: <code>description={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>query_id=0158d38771f70000000000010010038c&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>ï¿½ (optional)
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
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data. &lt;/p&gt; &lt;h4 id&#x3D;\&quot;filtering\&quot;&gt;Filtering:&lt;/h4&gt; &lt;p&gt;&lt;code&gt;?filter&#x3D;{URL encoded query string}&lt;/code&gt;&lt;/p&gt; &lt;p&gt;The query string is made up of key/value pairs separated by ampersands. So for a query of &lt;code&gt;key1&#x3D;value1&amp;amp;key2&#x3D;value2&amp;amp;key3&#x3D;value3&lt;/code&gt; this would be encoded as follows:&lt;/p&gt; &lt;p&gt;&lt;code&gt;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&lt;/code&gt;&lt;/p&gt; &lt;p&gt;The examples below show the queries in &lt;em&gt;unencoded&lt;/em&gt; form.&lt;/p&gt; &lt;h5 id&#x3D;\&quot;by-device-query-properties-all-properties-are-filterable\&quot;&gt;By device query properties (all properties are filterable):&lt;/h5&gt; &lt;p&gt;For example: &lt;code&gt;description&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;on-date-time-fields\&quot;&gt;On date-time fields:&lt;/h5&gt; &lt;p&gt;Date-time fields should be specified in UTC RFC3339 format &lt;code&gt;YYYY-MM-DDThh:mm:ss.msZ&lt;/code&gt;. There are three permitted variations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z&lt;/li&gt; &lt;li&gt;UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z&lt;/li&gt; &lt;li&gt;UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Date-time filtering supports three operators:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;equality&lt;/li&gt; &lt;li&gt;greater than or equal to &amp;ndash; field name suffixed with &lt;code&gt;__gte&lt;/code&gt;&lt;/li&gt; &lt;li&gt;less than or equal to &amp;ndash; field name suffixed with &lt;code&gt;__lte&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Lower and upper limits to a date-time range may be specified by including both the &lt;code&gt;__gte&lt;/code&gt; and &lt;code&gt;__lte&lt;/code&gt; forms in the filter.&lt;/p&gt; &lt;p&gt;&lt;code&gt;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&lt;/code&gt;&lt;/p&gt; &lt;h4 id&#x3D;\&quot;multi-field-example\&quot;&gt;Multi-field example&lt;/h4&gt; &lt;p&gt;&lt;code&gt;query_id&#x3D;0158d38771f70000000000010010038c&amp;amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&lt;/code&gt;&lt;/p&gt; &lt;p&gt;Encoded: &lt;code&gt;?filter&#x3D;query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&lt;/code&gt;&lt;/p&gt;ï¿½ | [optional] 
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



Update device query fields

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



Retrieve device query

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



Update device query

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
body = device_query_service.DeviceQueryPostPutRequest() # DeviceQueryPostPutRequest | Device query update object.

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
 **body** | [**DeviceQueryPostPutRequest**](DeviceQueryPostPutRequest.md)| Device query update object. | 

### Return type

[**DeviceQuery**](DeviceQuery.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

