# device_directory.DefaultApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_create**](DefaultApi.md#device_create) | **POST** /v3/devices/ | Create a device
[**device_destroy**](DefaultApi.md#device_destroy) | **DELETE** /v3/devices/{id}/ | Delete a device.
[**device_event_list**](DefaultApi.md#device_event_list) | **GET** /v3/device-events/ | List all device events.
[**device_event_retrieve**](DefaultApi.md#device_event_retrieve) | **GET** /v3/device-events/{device_event_id}/ | Retrieve a device event.
[**device_list**](DefaultApi.md#device_list) | **GET** /v3/devices/ | List all devices.
[**device_log_list**](DefaultApi.md#device_log_list) | **GET** /v3/devicelog/ | DEPRECATED: List all device events.
[**device_log_retrieve**](DefaultApi.md#device_log_retrieve) | **GET** /v3/devicelog/{device_event_id}/ | DEPRECATED: Retrieve a device event.
[**device_query_create**](DefaultApi.md#device_query_create) | **POST** /v3/device-queries/ | Create a device query
[**device_query_destroy**](DefaultApi.md#device_query_destroy) | **DELETE** /v3/device-queries/{query_id}/ | Delete a device query
[**device_query_list**](DefaultApi.md#device_query_list) | **GET** /v3/device-queries/ | List device queries.
[**device_query_retrieve**](DefaultApi.md#device_query_retrieve) | **GET** /v3/device-queries/{query_id}/ | Retrieve a device query.
[**device_query_update**](DefaultApi.md#device_query_update) | **PUT** /v3/device-queries/{query_id}/ | Update a device query
[**device_retrieve**](DefaultApi.md#device_retrieve) | **GET** /v3/devices/{id}/ | Get a devices
[**device_update**](DefaultApi.md#device_update) | **PUT** /v3/devices/{id}/ | Update a device


# **device_create**
> DeviceData device_create(device)

Create a device

Create a new device.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
device = device_directory.DeviceDataPostRequest() # DeviceDataPostRequest | 

try: 
    # Create a device
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_destroy**
> device_destroy(id)

Delete a device.

Delete device. Only available for devices with a developer certificate. Attempts to delete a device with a production certicate will return a 400 response.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
id = 'id_example' # str | 

try: 
    # Delete a device.
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_event_list**
> DeviceEventPage device_event_list(limit=limit, order=order, after=after, filter=filter, include=include)

List all device events.

List all device events for an account.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | The order of the records based on creation time, `ASC` or `DESC`; by default `ASC`. (optional)
after = 'after_example' # str | The ID of The item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3```  ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  |     Field    | = / __eq / __neq | __in /  __nin | __lte / __gte | |:------------:|:----------------:|:-------------:|:-------------:| |   date_time  |         ✓        |       ✓       |       ✓       | |  description |         ✓        |       ✓       |               | |      id      |         ✓        |       ✓       |               | |   device_id  |         ✓        |       ✓       |               | |  event_type  |         ✓        |       ✓       |               | | state_change |         ✓        |       ✓       |               |  The examples below show the queries in *unencoded* form.  ###### By id: ```id={id}```  ###### By state change: ```state_change=[True|False]```  ###### By event type: ```event_type={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example  ```id=0158d38771f70000000000010010038c&state_change=True&date_time__gte=2016-11-30T16:25:12.1234Z```  Encoded:  ```?filter=id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z```  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `event_type__in=update.device.device-created,update.device.device-updated` (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: `total_count` (optional)

try: 
    # List all device events.
    api_response = api_instance.device_event_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| The order of the records based on creation time, &#x60;ASC&#x60; or &#x60;DESC&#x60;; by default &#x60;ASC&#x60;. | [optional] 
 **after** | **str**| The ID of The item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60;  ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  |     Field    | &#x3D; / __eq / __neq | __in /  __nin | __lte / __gte | |:------------:|:----------------:|:-------------:|:-------------:| |   date_time  |         ✓        |       ✓       |       ✓       | |  description |         ✓        |       ✓       |               | |      id      |         ✓        |       ✓       |               | |   device_id  |         ✓        |       ✓       |               | |  event_type  |         ✓        |       ✓       |               | | state_change |         ✓        |       ✓       |               |  The examples below show the queries in *unencoded* form.  ###### By id: &#x60;&#x60;&#x60;id&#x3D;{id}&#x60;&#x60;&#x60;  ###### By state change: &#x60;&#x60;&#x60;state_change&#x3D;[True|False]&#x60;&#x60;&#x60;  ###### By event type: &#x60;&#x60;&#x60;event_type&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example  &#x60;&#x60;&#x60;id&#x3D;0158d38771f70000000000010010038c&amp;state_change&#x3D;True&amp;date_time__gte&#x3D;2016-11-30T16:25:12.1234Z&#x60;&#x60;&#x60;  Encoded:  &#x60;&#x60;&#x60;?filter&#x3D;id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z&#x60;&#x60;&#x60;  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;event_type__in&#x3D;update.device.device-created,update.device.device-updated&#x60; | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: &#x60;total_count&#x60; | [optional] 

### Return type

[**DeviceEventPage**](DeviceEventPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_event_retrieve**
> DeviceEventData device_event_retrieve(device_event_id)

Retrieve a device event.

Retrieve a specific device event.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
device_event_id = 'device_event_id_example' # str | 

try: 
    # Retrieve a device event.
    api_response = api_instance.device_event_retrieve(device_event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_event_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_event_id** | **str**|  | 

### Return type

[**DeviceEventData**](DeviceEventData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_list**
> DevicePage device_list(limit=limit, order=order, after=after, filter=filter, include=include)

List all devices.

List all devices.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | The order of the records based on creation time, `ASC` or `DESC`; by default `ASC`. (optional)
after = 'after_example' # str | The ID of The item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3```  ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  |           Field           | = / __eq / __neq | __in /  __nin | __lte / __gte | |:-------------------------:|:----------------:|:-------------:|:-------------:| |         account_id        |         ✓        |       ✓       |               | |        auto_update        |         ✓        |       ✓       |               | | bootstrap_expiration_date |         ✓        |       ✓       |       ✓       | |   bootstrapped_timestamp  |         ✓        |       ✓       |       ✓       | |           ca_id           |         ✓        |       ✓       |               | | connector_expiration_date |         ✓        |       ✓       |       ✓       | |         created_at        |         ✓        |       ✓       |       ✓       | |     custom_attributes     |         ✓        |               |               | |       deployed_state      |         ✓        |       ✓       |               | |         deployment        |         ✓        |       ✓       |               | |        description        |         ✓        |       ✓       |               | |        device_class       |         ✓        |       ✓       |               | |   device_execution_mode   |         ✓        |       ✓       |               | |         device_key        |         ✓        |       ✓       |               | |       endpoint_name       |         ✓        |       ✓       |               | |       endpoint_type       |         ✓        |       ✓       |               | |  enrolment_list_timestamp |         ✓        |       ✓       |       ✓       | |            etag           |         ✓        |       ✓       |       ✓       | |     firmware_checksum     |         ✓        |       ✓       |               | |        host_gateway       |         ✓        |       ✓       |               | |             id            |         ✓        |       ✓       |               | |          manifest         |         ✓        |       ✓       |               | |     manifest_timestamp    |         ✓        |       ✓       |       ✓       | |         mechanism         |         ✓        |       ✓       |               | |       mechanism_url       |         ✓        |       ✓       |               | |            name           |         ✓        |       ✓       |               | |       serial_number       |         ✓        |       ✓       |               | |           state           |         ✓        |       ✓       |               | |         updated_at        |         ✓        |       ✓       |       ✓       | |         vendor_id         |         ✓        |       ✓       |               |   The examples below show the queries in *unencoded* form.  ###### By device properties (all properties are filterable): ```state=[unenrolled|cloud_enrolling|bootstrapped|registered]```  ```device_class={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ###### On device custom attributes:  ```custom_attributes__{param}={value}``` ```custom_attributes__tag=TAG1```  ##### Multi-field example  ```state=bootstrapped&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded:  ```?filter=state%3Dbootstrapped%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z```  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `state__nin=unenrolled,dergistered` (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: `total_count`. (optional)

try: 
    # List all devices.
    api_response = api_instance.device_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| The order of the records based on creation time, &#x60;ASC&#x60; or &#x60;DESC&#x60;; by default &#x60;ASC&#x60;. | [optional] 
 **after** | **str**| The ID of The item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60;  ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  |           Field           | &#x3D; / __eq / __neq | __in /  __nin | __lte / __gte | |:-------------------------:|:----------------:|:-------------:|:-------------:| |         account_id        |         ✓        |       ✓       |               | |        auto_update        |         ✓        |       ✓       |               | | bootstrap_expiration_date |         ✓        |       ✓       |       ✓       | |   bootstrapped_timestamp  |         ✓        |       ✓       |       ✓       | |           ca_id           |         ✓        |       ✓       |               | | connector_expiration_date |         ✓        |       ✓       |       ✓       | |         created_at        |         ✓        |       ✓       |       ✓       | |     custom_attributes     |         ✓        |               |               | |       deployed_state      |         ✓        |       ✓       |               | |         deployment        |         ✓        |       ✓       |               | |        description        |         ✓        |       ✓       |               | |        device_class       |         ✓        |       ✓       |               | |   device_execution_mode   |         ✓        |       ✓       |               | |         device_key        |         ✓        |       ✓       |               | |       endpoint_name       |         ✓        |       ✓       |               | |       endpoint_type       |         ✓        |       ✓       |               | |  enrolment_list_timestamp |         ✓        |       ✓       |       ✓       | |            etag           |         ✓        |       ✓       |       ✓       | |     firmware_checksum     |         ✓        |       ✓       |               | |        host_gateway       |         ✓        |       ✓       |               | |             id            |         ✓        |       ✓       |               | |          manifest         |         ✓        |       ✓       |               | |     manifest_timestamp    |         ✓        |       ✓       |       ✓       | |         mechanism         |         ✓        |       ✓       |               | |       mechanism_url       |         ✓        |       ✓       |               | |            name           |         ✓        |       ✓       |               | |       serial_number       |         ✓        |       ✓       |               | |           state           |         ✓        |       ✓       |               | |         updated_at        |         ✓        |       ✓       |       ✓       | |         vendor_id         |         ✓        |       ✓       |               |   The examples below show the queries in *unencoded* form.  ###### By device properties (all properties are filterable): &#x60;&#x60;&#x60;state&#x3D;[unenrolled|cloud_enrolling|bootstrapped|registered]&#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;device_class&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ###### On device custom attributes:  &#x60;&#x60;&#x60;custom_attributes__{param}&#x3D;{value}&#x60;&#x60;&#x60; &#x60;&#x60;&#x60;custom_attributes__tag&#x3D;TAG1&#x60;&#x60;&#x60;  ##### Multi-field example  &#x60;&#x60;&#x60;state&#x3D;bootstrapped&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;&#x60;&#x60;  Encoded:  &#x60;&#x60;&#x60;?filter&#x3D;state%3Dbootstrapped%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&#x60;&#x60;&#x60;  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;state__nin&#x3D;unenrolled,dergistered&#x60; | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: &#x60;total_count&#x60;. | [optional] 

### Return type

[**DevicePage**](DevicePage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_list**
> DeviceEventPage device_log_list(limit=limit, order=order, after=after, filter=filter, include=include)

DEPRECATED: List all device events.

DEPRECATED: List all device events. Use `/v3/device-events/` instead.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | The order of the records based on creation time, `ASC` or `DESC`; by default `ASC`. (optional)
after = 'after_example' # str | The ID of The item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3```  ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  |     Field    | = / __eq / __neq | __in /  __nin | __lte / __gte | |:------------:|:----------------:|:-------------:|:-------------:| |   date_time  |         ✓        |       ✓       |       ✓       | |  description |         ✓        |       ✓       |               | |      id      |         ✓        |       ✓       |               | |   device_id  |         ✓        |       ✓       |               | |  event_type  |         ✓        |       ✓       |               | | state_change |         ✓        |       ✓       |               |  The examples below show the queries in *unencoded* form.  ###### By id: ```id={id}```  ###### By state change: ```state_change=[True|False]```  ###### By event type: ```event_type={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example  ```id=0158d38771f70000000000010010038c&state_change=True&date_time__gte=2016-11-30T16:25:12.1234Z```  Encoded:  ```?filter=id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z```  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `event_type__in=update.device.device-created,update.device.device-updated` (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: `total_count`. (optional)

try: 
    # DEPRECATED: List all device events.
    api_response = api_instance.device_log_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| The order of the records based on creation time, &#x60;ASC&#x60; or &#x60;DESC&#x60;; by default &#x60;ASC&#x60;. | [optional] 
 **after** | **str**| The ID of The item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60;  ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  |     Field    | &#x3D; / __eq / __neq | __in /  __nin | __lte / __gte | |:------------:|:----------------:|:-------------:|:-------------:| |   date_time  |         ✓        |       ✓       |       ✓       | |  description |         ✓        |       ✓       |               | |      id      |         ✓        |       ✓       |               | |   device_id  |         ✓        |       ✓       |               | |  event_type  |         ✓        |       ✓       |               | | state_change |         ✓        |       ✓       |               |  The examples below show the queries in *unencoded* form.  ###### By id: &#x60;&#x60;&#x60;id&#x3D;{id}&#x60;&#x60;&#x60;  ###### By state change: &#x60;&#x60;&#x60;state_change&#x3D;[True|False]&#x60;&#x60;&#x60;  ###### By event type: &#x60;&#x60;&#x60;event_type&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example  &#x60;&#x60;&#x60;id&#x3D;0158d38771f70000000000010010038c&amp;state_change&#x3D;True&amp;date_time__gte&#x3D;2016-11-30T16:25:12.1234Z&#x60;&#x60;&#x60;  Encoded:  &#x60;&#x60;&#x60;?filter&#x3D;id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z&#x60;&#x60;&#x60;  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;event_type__in&#x3D;update.device.device-created,update.device.device-updated&#x60; | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: &#x60;total_count&#x60;. | [optional] 

### Return type

[**DeviceEventPage**](DeviceEventPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_retrieve**
> DeviceEventData device_log_retrieve(device_event_id)

DEPRECATED: Retrieve a device event.

Retrieve device event (deprecated, use /v3/device-events/{device_event_id}/ instead)

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
device_event_id = 'device_event_id_example' # str | 

try: 
    # DEPRECATED: Retrieve a device event.
    api_response = api_instance.device_log_retrieve(device_event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_log_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_event_id** | **str**|  | 

### Return type

[**DeviceEventData**](DeviceEventData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_create**
> DeviceQuery device_query_create(device)

Create a device query

Create a new device query.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
device = device_directory.DeviceQueryPostPutRequest() # DeviceQueryPostPutRequest | 

try: 
    # Create a device query
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_destroy**
> device_query_destroy(query_id)

Delete a device query

Delete a device query.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
query_id = 'query_id_example' # str | 

try: 
    # Delete a device query
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_list**
> DeviceQueryPage device_query_list(limit=limit, order=order, after=after, filter=filter, include=include)

List device queries.

List all device queries. The result will be paged into pages of 100.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | The order of the records based on creation time, `ASC` or `DESC`; by default `ASC`. (optional)
after = 'after_example' # str | The ID of The item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3```  The below table lists all the fields that can be filtered on with certain filters:  |    Field   | = / __eq / __neq | __in /  __nin | __lte / __gte | |:----------:|:----------------:|:-------------:|:-------------:| | created_at |         ✓        |       ✓       |       ✓       | |    etag    |         ✓        |       ✓       |       ✓       | |     id     |         ✓        |       ✓       |               | |    name    |         ✓        |       ✓       |               | |    query   |         ✓        |       ✓       |               | | updated_at |         ✓        |       ✓       |       ✓       |   The examples below show the queries in *unencoded* form.  ###### By device query properties (all properties are filterable): For example: ```description={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example  ```query_id=0158d38771f70000000000010010038c&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded:  ```filter=query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z```  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `name__nin=query1,query2` (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: `total_count`. (optional)

try: 
    # List device queries.
    api_response = api_instance.device_query_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_query_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| The order of the records based on creation time, &#x60;ASC&#x60; or &#x60;DESC&#x60;; by default &#x60;ASC&#x60;. | [optional] 
 **after** | **str**| The ID of The item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60;  The below table lists all the fields that can be filtered on with certain filters:  |    Field   | &#x3D; / __eq / __neq | __in /  __nin | __lte / __gte | |:----------:|:----------------:|:-------------:|:-------------:| | created_at |         ✓        |       ✓       |       ✓       | |    etag    |         ✓        |       ✓       |       ✓       | |     id     |         ✓        |       ✓       |               | |    name    |         ✓        |       ✓       |               | |    query   |         ✓        |       ✓       |               | | updated_at |         ✓        |       ✓       |       ✓       |   The examples below show the queries in *unencoded* form.  ###### By device query properties (all properties are filterable): For example: &#x60;&#x60;&#x60;description&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example  &#x60;&#x60;&#x60;query_id&#x3D;0158d38771f70000000000010010038c&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;&#x60;&#x60;  Encoded:  &#x60;&#x60;&#x60;filter&#x3D;query_id%3D0158d38771f70000000000010010038c%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&#x60;&#x60;&#x60;  ##### Filtering with filter operators  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;name__nin&#x3D;query1,query2&#x60; | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: &#x60;total_count&#x60;. | [optional] 

### Return type

[**DeviceQueryPage**](DeviceQueryPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_retrieve**
> DeviceQuery device_query_retrieve(query_id)

Retrieve a device query.

Retrieve a specific device query.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
query_id = 'query_id_example' # str | 

try: 
    # Retrieve a device query.
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_update**
> DeviceQuery device_query_update(query_id, body)

Update a device query

Update a specifc device query.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
query_id = 'query_id_example' # str | 
body = device_directory.DeviceQueryPostPutRequest() # DeviceQueryPostPutRequest | Device query update object.

try: 
    # Update a device query
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_retrieve**
> DeviceData device_retrieve(id)

Get a devices

Retrieve information about a specific device.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
id = 'id_example' # str | 

try: 
    # Get a devices
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> DeviceData device_update(id, device)

Update a device

Update a specific device.

### Example 
```python
from __future__ import print_function
import time
import device_directory
from device_directory.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = device_directory.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_directory.DefaultApi(device_directory.ApiClient(configuration))
id = 'id_example' # str | The ID of the device.
device = device_directory.DeviceDataPutRequest() # DeviceDataPutRequest | 

try: 
    # Update a device
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

