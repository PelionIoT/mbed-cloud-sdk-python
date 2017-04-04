# device_catalog.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_create**](DefaultApi.md#device_create) | **POST** /v3/devices/ | 
[**device_destroy**](DefaultApi.md#device_destroy) | **DELETE** /v3/devices/{device_id}/ | 
[**device_list**](DefaultApi.md#device_list) | **GET** /v3/devices/ | 
[**device_log_list**](DefaultApi.md#device_log_list) | **GET** /v3/devicelog/ | 
[**device_log_retrieve**](DefaultApi.md#device_log_retrieve) | **GET** /v3/devicelog/{device_log_id}/ | 
[**device_partial_update**](DefaultApi.md#device_partial_update) | **PATCH** /v3/devices/{device_id}/ | 
[**device_retrieve**](DefaultApi.md#device_retrieve) | **GET** /v3/devices/{device_id}/ | 
[**device_update**](DefaultApi.md#device_update) | **PUT** /v3/devices/{device_id}/ | 


# **device_create**
> DeviceData device_create(device)



<p>The APIs for creating and manipulating devices.  </p> <p>Create device</p>

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
device = device_catalog.DeviceData() # DeviceData | 

try: 
    api_response = api_instance.device_create(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceData**](DeviceData.md)|  | 

### Return type

[**DeviceData**](DeviceData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_destroy**
> object device_destroy(device_id)



<p>The APIs for creating and manipulating devices.  </p> <p>Delete device</p>

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
device_id = 'device_id_example' # str | 

try: 
    api_response = api_instance.device_destroy(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_list**
> DevicePage device_list(ca_id, device_key, limit=limit, order=order, after=after, filter=filter, include=include, account_id=account_id, attestation_method=attestation_method, auto_update=auto_update, bootstrap_expiration_date=bootstrap_expiration_date, bootstrap_expiration_date__lte=bootstrap_expiration_date__lte, bootstrap_expiration_date__gte=bootstrap_expiration_date__gte, bootstrapped_timestamp=bootstrapped_timestamp, bootstrapped_timestamp__lte=bootstrapped_timestamp__lte, bootstrapped_timestamp__gte=bootstrapped_timestamp__gte, connector_expiration_date=connector_expiration_date, connector_expiration_date__lte=connector_expiration_date__lte, connector_expiration_date__gte=connector_expiration_date__gte, created_at=created_at, created_at__lte=created_at__lte, created_at__gte=created_at__gte, custom_attributes=custom_attributes, deployed_state=deployed_state, deployment=deployment, description=description, device_class=device_class, device_id=device_id, endpoint_name=endpoint_name, etag=etag, etag__lte=etag__lte, etag__gte=etag__gte, firmware_checksum=firmware_checksum, manifest=manifest, manifest_timestamp=manifest_timestamp, manifest_timestamp__lte=manifest_timestamp__lte, manifest_timestamp__gte=manifest_timestamp__gte, mechanism=mechanism, mechanism_url=mechanism_url, name=name, object=object, serial_number=serial_number, state=state, trust_class=trust_class, trust_level=trust_level, updated_at=updated_at, updated_at__lte=updated_at__lte, updated_at__gte=updated_at__gte, vendor_id=vendor_id)



<p>The APIs for creating and manipulating devices.  </p> <p>List all update devices.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-device-properties-all-properties-are-filterable\">By device properties (all properties are filterable):</h5> <p><code>state=[unenrolled|cloud_enrolling|bootstrapped|registered]</code></p> <p><code>device_class={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h5 id=\"on-device-custom-attributes\">On device custom attributes:</h5> <p><code>custom_attributes__{param}={value}</code></p> <p><code>custom_attributes__tag=TAG1</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>state=bootstrapped&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=state%3Dbootstrapped%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>

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
ca_id = 'ca_id_example' # str | 
device_key = 'device_key_example' # str | 
limit = 56 # int | how many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | the ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data (optional)
include = 'include_example' # str | Comma separated list of data fields to return. Currently supported: total_count (optional)
account_id = 'account_id_example' # str |  (optional)
attestation_method = 56 # int |  (optional)
auto_update = true # bool |  (optional)
bootstrap_expiration_date = 'bootstrap_expiration_date_example' # str |  (optional)
bootstrap_expiration_date__lte = 'bootstrap_expiration_date__lte_example' # str |  (optional)
bootstrap_expiration_date__gte = 'bootstrap_expiration_date__gte_example' # str |  (optional)
bootstrapped_timestamp = 'bootstrapped_timestamp_example' # str |  (optional)
bootstrapped_timestamp__lte = 'bootstrapped_timestamp__lte_example' # str |  (optional)
bootstrapped_timestamp__gte = 'bootstrapped_timestamp__gte_example' # str |  (optional)
connector_expiration_date = 'connector_expiration_date_example' # str |  (optional)
connector_expiration_date__lte = 'connector_expiration_date__lte_example' # str |  (optional)
connector_expiration_date__gte = 'connector_expiration_date__gte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
custom_attributes = 'custom_attributes_example' # str |  (optional)
deployed_state = 'deployed_state_example' # str |  (optional)
deployment = 'deployment_example' # str |  (optional)
description = 'description_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
endpoint_name = 'endpoint_name_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
firmware_checksum = 'firmware_checksum_example' # str |  (optional)
manifest = 'manifest_example' # str |  (optional)
manifest_timestamp = 'manifest_timestamp_example' # str |  (optional)
manifest_timestamp__lte = 'manifest_timestamp__lte_example' # str |  (optional)
manifest_timestamp__gte = 'manifest_timestamp__gte_example' # str |  (optional)
mechanism = 'mechanism_example' # str |  (optional)
mechanism_url = 'mechanism_url_example' # str |  (optional)
name = 'name_example' # str |  (optional)
object = 'object_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)
state = 'state_example' # str |  (optional)
trust_class = 'trust_class_example' # str |  (optional)
trust_level = 'trust_level_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
vendor_id = 'vendor_id_example' # str |  (optional)

try: 
    api_response = api_instance.device_list(ca_id, device_key, limit=limit, order=order, after=after, filter=filter, include=include, account_id=account_id, attestation_method=attestation_method, auto_update=auto_update, bootstrap_expiration_date=bootstrap_expiration_date, bootstrap_expiration_date__lte=bootstrap_expiration_date__lte, bootstrap_expiration_date__gte=bootstrap_expiration_date__gte, bootstrapped_timestamp=bootstrapped_timestamp, bootstrapped_timestamp__lte=bootstrapped_timestamp__lte, bootstrapped_timestamp__gte=bootstrapped_timestamp__gte, connector_expiration_date=connector_expiration_date, connector_expiration_date__lte=connector_expiration_date__lte, connector_expiration_date__gte=connector_expiration_date__gte, created_at=created_at, created_at__lte=created_at__lte, created_at__gte=created_at__gte, custom_attributes=custom_attributes, deployed_state=deployed_state, deployment=deployment, description=description, device_class=device_class, device_id=device_id, endpoint_name=endpoint_name, etag=etag, etag__lte=etag__lte, etag__gte=etag__gte, firmware_checksum=firmware_checksum, manifest=manifest, manifest_timestamp=manifest_timestamp, manifest_timestamp__lte=manifest_timestamp__lte, manifest_timestamp__gte=manifest_timestamp__gte, mechanism=mechanism, mechanism_url=mechanism_url, name=name, object=object, serial_number=serial_number, state=state, trust_class=trust_class, trust_level=trust_level, updated_at=updated_at, updated_at__lte=updated_at__lte, updated_at__gte=updated_at__gte, vendor_id=vendor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_id** | **str**|  | 
 **device_key** | **str**|  | 
 **limit** | **int**| how many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| the ID of the the item after which to retrieve the next page | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data | [optional] 
 **include** | **str**| Comma separated list of data fields to return. Currently supported: total_count | [optional] 
 **account_id** | **str**|  | [optional] 
 **attestation_method** | **int**|  | [optional] 
 **auto_update** | **bool**|  | [optional] 
 **bootstrap_expiration_date** | **str**|  | [optional] 
 **bootstrap_expiration_date__lte** | **str**|  | [optional] 
 **bootstrap_expiration_date__gte** | **str**|  | [optional] 
 **bootstrapped_timestamp** | **str**|  | [optional] 
 **bootstrapped_timestamp__lte** | **str**|  | [optional] 
 **bootstrapped_timestamp__gte** | **str**|  | [optional] 
 **connector_expiration_date** | **str**|  | [optional] 
 **connector_expiration_date__lte** | **str**|  | [optional] 
 **connector_expiration_date__gte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **custom_attributes** | **str**|  | [optional] 
 **deployed_state** | **str**|  | [optional] 
 **deployment** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **endpoint_name** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **firmware_checksum** | **str**|  | [optional] 
 **manifest** | **str**|  | [optional] 
 **manifest_timestamp** | **str**|  | [optional] 
 **manifest_timestamp__lte** | **str**|  | [optional] 
 **manifest_timestamp__gte** | **str**|  | [optional] 
 **mechanism** | **str**|  | [optional] 
 **mechanism_url** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **trust_class** | **str**|  | [optional] 
 **trust_level** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **vendor_id** | **str**|  | [optional] 

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



<p>The APIs for creating and manipulating devices.  </p> <p>List all device logs.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-device95id\">By device_id:</h5> <p><code>device_id={id}</code></p> <h5 id=\"by-state-change\">By state change:</h5> <p><code>state_change=[True|False]</code></p> <h5 id=\"by-event-type\">By event type:</h5> <p><code>event_type={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h5 id=\"on-device-custom-attributes\">On device custom attributes:</h5> <p><code>device__custom_attributes__{param}={value}</code></p> <p><code>device__custom_attributes__tag=TAG1</code></p> <h5 id=\"by-device-attributes\">By Device attributes:</h5> <p><code>device__deployed_state={value}</code></p> <p><code>device__device_class={value}</code></p> <p><code>device__name={value}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>device_id=0158d38771f70000000000010010038c&amp;state_change=True&amp;date_time__gte=2016-11-30T16:25:12.1234Z</code></p> <p>Encoded: <code>?filter=device_id%3D0158d38771f70000000000010010038c%26state_change%3DTrue%26date_time__gte%3D2016-11-30T16%3A25%3A12.1234Z</code></p>

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
limit = 56 # int | how many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | the ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data (optional)
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
 **limit** | **int**| how many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| the ID of the the item after which to retrieve the next page | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data | [optional] 
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



<p>The APIs for creating and manipulating devices.  </p> <p>Retrieve device log.</p>

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
> DeviceSerializer device_partial_update(device_id, device)



<p>The APIs for creating and manipulating devices.  </p> <p>Update device fields</p>

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
device_id = 'device_id_example' # str | The ID of the device
device = device_catalog.DeviceData() # DeviceData | 

try: 
    api_response = api_instance.device_partial_update(device_id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The ID of the device | 
 **device** | [**DeviceData**](DeviceData.md)|  | 

### Return type

[**DeviceSerializer**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_retrieve**
> DeviceData device_retrieve(device_id)



<p>The APIs for creating and manipulating devices.  </p> <p>Retrieve device.</p>

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
device_id = 'device_id_example' # str | 

try: 
    api_response = api_instance.device_retrieve(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceData**](DeviceData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> DeviceSerializer device_update(device_id, device)



<p>The APIs for creating and manipulating devices.  </p> <p>Update device.</p>

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
device_id = 'device_id_example' # str | The ID of the device
device = device_catalog.DeviceData() # DeviceData | 

try: 
    api_response = api_instance.device_update(device_id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The ID of the device | 
 **device** | [**DeviceData**](DeviceData.md)|  | 

### Return type

[**DeviceSerializer**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

