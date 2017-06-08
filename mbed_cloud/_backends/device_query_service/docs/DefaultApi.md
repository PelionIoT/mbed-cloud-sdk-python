# device_query_service.DefaultApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

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



Create device query.

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



Delete device query.

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
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ###### By device query properties (all properties are filterable): For example: ```description={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example  ```query_id=0158d38771f70000000000010010038c&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded:  ```filter=query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z``` (optional)
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
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60; The examples below show the queries in *unencoded* form.  ###### By device query properties (all properties are filterable): For example: &#x60;&#x60;&#x60;description&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example  &#x60;&#x60;&#x60;query_id&#x3D;0158d38771f70000000000010010038c&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;&#x60;&#x60;  Encoded:  &#x60;&#x60;&#x60;filter&#x3D;query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&#x60;&#x60;&#x60; | [optional] 
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



Update device query fields.

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



Retrieve device query.

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



Update device query.

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

