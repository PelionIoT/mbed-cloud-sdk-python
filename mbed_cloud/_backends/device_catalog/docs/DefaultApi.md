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
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ###### By device properties (all properties are filterable): ```state=[unenrolled|cloud_enrolling|bootstrapped|registered]```  ```device_class={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ###### On device custom attributes:  ```custom_attributes__{param}={value}``` ```custom_attributes__tag=TAG1```  ##### Multi-field example  ```state=bootstrapped&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded:  ```?filter=state%3Dbootstrapped%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z``` (optional)
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
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60; The examples below show the queries in *unencoded* form.  ###### By device properties (all properties are filterable): &#x60;&#x60;&#x60;state&#x3D;[unenrolled|cloud_enrolling|bootstrapped|registered]&#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;device_class&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ###### On device custom attributes:  &#x60;&#x60;&#x60;custom_attributes__{param}&#x3D;{value}&#x60;&#x60;&#x60; &#x60;&#x60;&#x60;custom_attributes__tag&#x3D;TAG1&#x60;&#x60;&#x60;  ##### Multi-field example  &#x60;&#x60;&#x60;state&#x3D;bootstrapped&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;&#x60;&#x60;  Encoded:  &#x60;&#x60;&#x60;?filter&#x3D;state%3Dbootstrapped%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&#x60;&#x60;&#x60; | [optional] 
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
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ###### By id: ```id={id}```  ###### By state change: ```state_change=[True|False]```  ###### By event type: ```event_type={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example  ```id=0158d38771f70000000000010010038c&state_change=True&date_time__gte=2016-11-30T16:25:12.1234Z```  Encoded:  ```?filter=id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z``` (optional)
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
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60; The examples below show the queries in *unencoded* form.  ###### By id: &#x60;&#x60;&#x60;id&#x3D;{id}&#x60;&#x60;&#x60;  ###### By state change: &#x60;&#x60;&#x60;state_change&#x3D;[True|False]&#x60;&#x60;&#x60;  ###### By event type: &#x60;&#x60;&#x60;event_type&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example  &#x60;&#x60;&#x60;id&#x3D;0158d38771f70000000000010010038c&amp;state_change&#x3D;True&amp;date_time__gte&#x3D;2016-11-30T16:25:12.1234Z&#x60;&#x60;&#x60;  Encoded:  &#x60;&#x60;&#x60;?filter&#x3D;id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z&#x60;&#x60;&#x60; | [optional] 
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

