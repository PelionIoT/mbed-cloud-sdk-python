# device_catalog.DefaultApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_create**](DefaultApi.md#device_create) | **POST** /v3/devices/ | 
[**device_destroy**](DefaultApi.md#device_destroy) | **DELETE** /v3/devices/{id}/ | 
[**device_list**](DefaultApi.md#device_list) | **GET** /v3/devices/ | 
[**device_log_list**](DefaultApi.md#device_log_list) | **GET** /v3/devicelog/ | 
[**device_log_retrieve**](DefaultApi.md#device_log_retrieve) | **GET** /v3/devicelog/{device_log_id}/ | 
[**device_partial_update**](DefaultApi.md#device_partial_update) | **PATCH** /v3/devices/{id}/ | 
[**device_retrieve**](DefaultApi.md#device_retrieve) | **GET** /v3/devices/{id}/ | 
[**device_update**](DefaultApi.md#device_update) | **PUT** /v3/devices/{id}/ | 


# **device_create**
> DeviceData device_create(device)



Create device

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
device = device_catalog.DeviceDataPostRequest() # DeviceDataPostRequest | 

try: 
    api_response = api_instance.device_create(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceDataPostRequest**](DeviceDataPostRequest.md)|  | 

### Return type

[**DeviceData**](DeviceData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_destroy**
> device_destroy(id)



Delete device

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
id = 'id_example' # str | 

try: 
    api_instance.device_destroy(id)
except ApiException as e:
    print("Exception when calling DefaultApi->device_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_list**
> DevicePage device_list(limit=limit, order=order, after=after, filter=filter, include=include)



List all devices.

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | <p>URL encoded query string parameter to filter returned data.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-device-properties-all-properties-are-filterable\">By device properties (all properties are filterable):</h5> <p><code>state=[unenrolled|cloud_enrolling|bootstrapped|registered]</code></p> <p><code>device_class={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h5 id=\"on-device-custom-attributes\">On device custom attributes:</h5> <p><code>custom_attributes__{param}={value}</code></p> <p><code>custom_attributes__tag=TAG1</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>state=bootstrapped&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=state%3Dbootstrapped%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p> (optional)
include = 'include_example' # str | Comma separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.device_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page. | [optional] 
 **filter** | **str**| &lt;p&gt;URL encoded query string parameter to filter returned data.&lt;/p&gt; &lt;h4 id&#x3D;\&quot;filtering\&quot;&gt;Filtering:&lt;/h4&gt; &lt;p&gt;&lt;code&gt;?filter&#x3D;{URL encoded query string}&lt;/code&gt;&lt;/p&gt; &lt;p&gt;The query string is made up of key/value pairs separated by ampersands. So for a query of &lt;code&gt;key1&#x3D;value1&amp;amp;key2&#x3D;value2&amp;amp;key3&#x3D;value3&lt;/code&gt; this would be encoded as follows:&lt;/p&gt; &lt;p&gt;&lt;code&gt;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&lt;/code&gt;&lt;/p&gt; &lt;p&gt;The examples below show the queries in &lt;em&gt;unencoded&lt;/em&gt; form.&lt;/p&gt; &lt;h5 id&#x3D;\&quot;by-device-properties-all-properties-are-filterable\&quot;&gt;By device properties (all properties are filterable):&lt;/h5&gt; &lt;p&gt;&lt;code&gt;state&#x3D;[unenrolled|cloud_enrolling|bootstrapped|registered]&lt;/code&gt;&lt;/p&gt; &lt;p&gt;&lt;code&gt;device_class&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;on-date-time-fields\&quot;&gt;On date-time fields:&lt;/h5&gt; &lt;p&gt;Date-time fields should be specified in UTC RFC3339 format &lt;code&gt;YYYY-MM-DDThh:mm:ss.msZ&lt;/code&gt;. There are three permitted variations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z&lt;/li&gt; &lt;li&gt;UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z&lt;/li&gt; &lt;li&gt;UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Date-time filtering supports three operators:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;equality&lt;/li&gt; &lt;li&gt;greater than or equal to &amp;ndash; field name suffixed with &lt;code&gt;__gte&lt;/code&gt;&lt;/li&gt; &lt;li&gt;less than or equal to &amp;ndash; field name suffixed with &lt;code&gt;__lte&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Lower and upper limits to a date-time range may be specified by including both the &lt;code&gt;__gte&lt;/code&gt; and &lt;code&gt;__lte&lt;/code&gt; forms in the filter.&lt;/p&gt; &lt;p&gt;&lt;code&gt;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;on-device-custom-attributes\&quot;&gt;On device custom attributes:&lt;/h5&gt; &lt;p&gt;&lt;code&gt;custom_attributes__{param}&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;p&gt;&lt;code&gt;custom_attributes__tag&#x3D;TAG1&lt;/code&gt;&lt;/p&gt; &lt;h4 id&#x3D;\&quot;multi-field-example\&quot;&gt;Multi-field example&lt;/h4&gt; &lt;p&gt;&lt;code&gt;state&#x3D;bootstrapped&amp;amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&lt;/code&gt;&lt;/p&gt; &lt;p&gt;Encoded: &lt;code&gt;?filter&#x3D;state%3Dbootstrapped%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&lt;/code&gt;&lt;/p&gt; | [optional] 
 **include** | **str**| Comma separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**DevicePage**](DevicePage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_list**
> DeviceLogPage device_log_list(limit=limit, order=order, after=after, filter=filter, include=include)



List all device logs.

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | <p>URL encoded query string parameter to filter returned data.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-device95id\">By id:</h5> <p><code>id={id}</code></p> <h5 id=\"by-state-change\">By state change:</h5> <p><code>state_change=[True|False]</code></p> <h5 id=\"by-event-type\">By event type:</h5> <p><code>event_type={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h5 id=\"on-device-custom-attributes\">On device custom attributes:</h5> <p><code>device__custom_attributes__{param}={value}</code></p> <p><code>device__custom_attributes__tag=TAG1</code></p> <h5 id=\"by-device-attributes\">By Device attributes:</h5> <p><code>device__deployed_state={value}</code></p> <p><code>device__device_class={value}</code></p> <p><code>device__name={value}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>id=0158d38771f70000000000010010038c&amp;state_change=True&amp;date_time__gte=2016-11-30T16:25:12.1234Z</code></p> <p>Encoded: <code>?filter=id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z</code></p> (optional)
include = 'include_example' # str | Comma separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.device_log_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page. | [optional] 
 **filter** | **str**| &lt;p&gt;URL encoded query string parameter to filter returned data.&lt;/p&gt; &lt;h4 id&#x3D;\&quot;filtering\&quot;&gt;Filtering:&lt;/h4&gt; &lt;p&gt;&lt;code&gt;?filter&#x3D;{URL encoded query string}&lt;/code&gt;&lt;/p&gt; &lt;p&gt;The query string is made up of key/value pairs separated by ampersands. So for a query of &lt;code&gt;key1&#x3D;value1&amp;amp;key2&#x3D;value2&amp;amp;key3&#x3D;value3&lt;/code&gt; this would be encoded as follows:&lt;/p&gt; &lt;p&gt;&lt;code&gt;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&lt;/code&gt;&lt;/p&gt; &lt;p&gt;The examples below show the queries in &lt;em&gt;unencoded&lt;/em&gt; form.&lt;/p&gt; &lt;h5 id&#x3D;\&quot;by-device95id\&quot;&gt;By id:&lt;/h5&gt; &lt;p&gt;&lt;code&gt;id&#x3D;{id}&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;by-state-change\&quot;&gt;By state change:&lt;/h5&gt; &lt;p&gt;&lt;code&gt;state_change&#x3D;[True|False]&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;by-event-type\&quot;&gt;By event type:&lt;/h5&gt; &lt;p&gt;&lt;code&gt;event_type&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;on-date-time-fields\&quot;&gt;On date-time fields:&lt;/h5&gt; &lt;p&gt;Date-time fields should be specified in UTC RFC3339 format &lt;code&gt;YYYY-MM-DDThh:mm:ss.msZ&lt;/code&gt;. There are three permitted variations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z&lt;/li&gt; &lt;li&gt;UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z&lt;/li&gt; &lt;li&gt;UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Date-time filtering supports three operators:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;equality&lt;/li&gt; &lt;li&gt;greater than or equal to &amp;ndash; field name suffixed with &lt;code&gt;__gte&lt;/code&gt;&lt;/li&gt; &lt;li&gt;less than or equal to &amp;ndash; field name suffixed with &lt;code&gt;__lte&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Lower and upper limits to a date-time range may be specified by including both the &lt;code&gt;__gte&lt;/code&gt; and &lt;code&gt;__lte&lt;/code&gt; forms in the filter.&lt;/p&gt; &lt;p&gt;&lt;code&gt;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;on-device-custom-attributes\&quot;&gt;On device custom attributes:&lt;/h5&gt; &lt;p&gt;&lt;code&gt;device__custom_attributes__{param}&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;p&gt;&lt;code&gt;device__custom_attributes__tag&#x3D;TAG1&lt;/code&gt;&lt;/p&gt; &lt;h5 id&#x3D;\&quot;by-device-attributes\&quot;&gt;By Device attributes:&lt;/h5&gt; &lt;p&gt;&lt;code&gt;device__deployed_state&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;p&gt;&lt;code&gt;device__device_class&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;p&gt;&lt;code&gt;device__name&#x3D;{value}&lt;/code&gt;&lt;/p&gt; &lt;h4 id&#x3D;\&quot;multi-field-example\&quot;&gt;Multi-field example&lt;/h4&gt; &lt;p&gt;&lt;code&gt;id&#x3D;0158d38771f70000000000010010038c&amp;amp;state_change&#x3D;True&amp;amp;date_time__gte&#x3D;2016-11-30T16:25:12.1234Z&lt;/code&gt;&lt;/p&gt; &lt;p&gt;Encoded: &lt;code&gt;?filter&#x3D;id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z&lt;/code&gt;&lt;/p&gt; | [optional] 
 **include** | **str**| Comma separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**DeviceLogPage**](DeviceLogPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_retrieve**
> DeviceLogData device_log_retrieve(device_log_id)



Retrieve device log

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
device_log_id = 'device_log_id_example' # str | 

try: 
    api_response = api_instance.device_log_retrieve(device_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_log_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_log_id** | **str**|  | 

### Return type

[**DeviceLogData**](DeviceLogData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_partial_update**
> DeviceData device_partial_update(id, device)



Update device fields

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
id = 'id_example' # str | The ID of the device.
device = device_catalog.DeviceDataPatchRequest() # DeviceDataPatchRequest | 

try: 
    api_response = api_instance.device_partial_update(id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the device. | 
 **device** | [**DeviceDataPatchRequest**](DeviceDataPatchRequest.md)|  | 

### Return type

[**DeviceData**](DeviceData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_retrieve**
> DeviceData device_retrieve(id)



Retrieve device

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.device_retrieve(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DeviceData**](DeviceData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> DeviceData device_update(id, device)



Update device

### Example 
```python
from __future__ import print_statement
import time
import device_catalog
from device_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_catalog.DefaultApi()
id = 'id_example' # str | The ID of the device.
device = device_catalog.DeviceDataPutRequest() # DeviceDataPutRequest | 

try: 
    api_response = api_instance.device_update(id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the device. | 
 **device** | [**DeviceDataPutRequest**](DeviceDataPutRequest.md)|  | 

### Return type

[**DeviceData**](DeviceData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

