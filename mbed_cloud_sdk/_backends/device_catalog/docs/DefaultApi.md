# device_catalog.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_create**](DefaultApi.md#device_create) | **POST** /v3/devices/ | Create device
[**device_destroy**](DefaultApi.md#device_destroy) | **DELETE** /v3/devices/{device_id}/ | Delete device
[**device_list**](DefaultApi.md#device_list) | **GET** /v3/devices/ | List all update devices
[**device_log_create**](DefaultApi.md#device_log_create) | **POST** /v3/devicelog/ | The APIs for creating and manipulating devices
[**device_log_destroy**](DefaultApi.md#device_log_destroy) | **DELETE** /v3/devicelog/{device_log_id}/ | The APIs for creating and manipulating devices
[**device_log_list**](DefaultApi.md#device_log_list) | **GET** /v3/devicelog/ | List all device logs
[**device_log_partial_update**](DefaultApi.md#device_log_partial_update) | **PATCH** /v3/devicelog/{device_log_id}/ | The APIs for creating and manipulating devices
[**device_log_retrieve**](DefaultApi.md#device_log_retrieve) | **GET** /v3/devicelog/{device_log_id}/ | Retrieve device log
[**device_log_update**](DefaultApi.md#device_log_update) | **PUT** /v3/devicelog/{device_log_id}/ | The APIs for creating and manipulating devices
[**device_partial_update**](DefaultApi.md#device_partial_update) | **PATCH** /v3/devices/{device_id}/ | Update device fields
[**device_retrieve**](DefaultApi.md#device_retrieve) | **GET** /v3/devices/{device_id}/ | Retrieve device
[**device_update**](DefaultApi.md#device_update) | **PUT** /v3/devices/{device_id}/ | Update device


# **device_create**
> DeviceSerializer device_create()

Create device

<p>The APIs for creating and manipulating devices.  </p> <p>Create device</p>

### Example 
```python
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

try: 
    # Create device
    api_response = api_instance.device_create()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_create: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceSerializer**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_destroy**
> DeviceSerializer device_destroy(device_id)

Delete device

<p>The APIs for creating and manipulating devices.  </p> <p>Delete device</p>

### Example 
```python
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
    # Delete device
    api_response = api_instance.device_destroy(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_destroy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceSerializer**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_list**
> list[DeviceSerializer] device_list(created_at=created_at, updated_at=updated_at, auto_update=auto_update, bootstrapped_timestamp=bootstrapped_timestamp, deployed_state=deployed_state, deployment=deployment, description=description, device_class=device_class, device_id=device_id, etag=etag, manifest=manifest, mechanism=mechanism, mechanism_url=mechanism_url, name=name, object=object, provision_key=provision_key, serial_number=serial_number, state=state, trust_class=trust_class, trust_level=trust_level, vendor_id=vendor_id)

List all update devices

<p>The APIs for creating and manipulating devices.  </p> <p>List all update devices. The result is paged into pages of 100.</p>

### Example 
```python
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
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
auto_update = 'auto_update_example' # str |  (optional)
bootstrapped_timestamp = 'bootstrapped_timestamp_example' # str |  (optional)
deployed_state = 'deployed_state_example' # str |  (optional)
deployment = 'deployment_example' # str |  (optional)
description = 'description_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
manifest = 'manifest_example' # str |  (optional)
mechanism = 'mechanism_example' # str |  (optional)
mechanism_url = 'mechanism_url_example' # str |  (optional)
name = 'name_example' # str |  (optional)
object = 'object_example' # str |  (optional)
provision_key = 'provision_key_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)
state = 'state_example' # str |  (optional)
trust_class = 'trust_class_example' # str |  (optional)
trust_level = 'trust_level_example' # str |  (optional)
vendor_id = 'vendor_id_example' # str |  (optional)

try: 
    # List all update devices
    api_response = api_instance.device_list(created_at=created_at, updated_at=updated_at, auto_update=auto_update, bootstrapped_timestamp=bootstrapped_timestamp, deployed_state=deployed_state, deployment=deployment, description=description, device_class=device_class, device_id=device_id, etag=etag, manifest=manifest, mechanism=mechanism, mechanism_url=mechanism_url, name=name, object=object, provision_key=provision_key, serial_number=serial_number, state=state, trust_class=trust_class, trust_level=trust_level, vendor_id=vendor_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **auto_update** | **str**|  | [optional] 
 **bootstrapped_timestamp** | **str**|  | [optional] 
 **deployed_state** | **str**|  | [optional] 
 **deployment** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **manifest** | **str**|  | [optional] 
 **mechanism** | **str**|  | [optional] 
 **mechanism_url** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **provision_key** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **trust_class** | **str**|  | [optional] 
 **trust_level** | **str**|  | [optional] 
 **vendor_id** | **str**|  | [optional] 

### Return type

[**list[DeviceSerializer]**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_create**
> DeviceLogSerializer device_log_create(date_time, device_log_id=device_log_id, event_type=event_type, state_change=state_change, date_time2=date_time2, device_id=device_id, device_log_id2=device_log_id2, event_type2=event_type2, state_change2=state_change2)

The APIs for creating and manipulating devices

<p>The APIs for creating and manipulating devices.</p>

### Example 
```python
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
date_time = '2013-10-20T19:20:30+01:00' # datetime | 
device_log_id = 'device_log_id_example' # str |  (optional)
event_type = 'event_type_example' # str |  (optional)
state_change = true # bool |  (optional)
date_time2 = 'date_time_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device_log_id2 = 'device_log_id_example' # str |  (optional)
event_type2 = 'event_type_example' # str |  (optional)
state_change2 = 'state_change_example' # str |  (optional)

try: 
    # The APIs for creating and manipulating devices
    api_response = api_instance.device_log_create(date_time, device_log_id=device_log_id, event_type=event_type, state_change=state_change, date_time2=date_time2, device_id=device_id, device_log_id2=device_log_id2, event_type2=event_type2, state_change2=state_change2)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_log_create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_time** | **datetime**|  | 
 **device_log_id** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **state_change** | **bool**|  | [optional] 
 **date_time2** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_log_id2** | **str**|  | [optional] 
 **event_type2** | **str**|  | [optional] 
 **state_change2** | **str**|  | [optional] 

### Return type

[**DeviceLogSerializer**](DeviceLogSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_destroy**
> DeviceLogSerializer device_log_destroy(device_log_id, date_time=date_time, device_id=device_id, device_log_id2=device_log_id2, event_type=event_type, state_change=state_change)

The APIs for creating and manipulating devices

<p>The APIs for creating and manipulating devices.</p>

### Example 
```python
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
date_time = 'date_time_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device_log_id2 = 'device_log_id_example' # str |  (optional)
event_type = 'event_type_example' # str |  (optional)
state_change = 'state_change_example' # str |  (optional)

try: 
    # The APIs for creating and manipulating devices
    api_response = api_instance.device_log_destroy(device_log_id, date_time=date_time, device_id=device_id, device_log_id2=device_log_id2, event_type=event_type, state_change=state_change)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_log_destroy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_log_id** | **str**|  | 
 **date_time** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_log_id2** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **state_change** | **str**|  | [optional] 

### Return type

[**DeviceLogSerializer**](DeviceLogSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_list**
> list[DeviceLogSerializer] device_log_list(date_time=date_time, device_id=device_id, device_log_id=device_log_id, event_type=event_type, state_change=state_change)

List all device logs

<p>The APIs for creating and manipulating devices.  </p> <p>List all device logs.</p>

### Example 
```python
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
date_time = 'date_time_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device_log_id = 'device_log_id_example' # str |  (optional)
event_type = 'event_type_example' # str |  (optional)
state_change = 'state_change_example' # str |  (optional)

try: 
    # List all device logs
    api_response = api_instance.device_log_list(date_time=date_time, device_id=device_id, device_log_id=device_log_id, event_type=event_type, state_change=state_change)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_log_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_time** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_log_id** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **state_change** | **str**|  | [optional] 

### Return type

[**list[DeviceLogSerializer]**](DeviceLogSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_partial_update**
> DeviceLogSerializer device_log_partial_update(device_log_id, date_time=date_time, device_log_id2=device_log_id2, event_type=event_type, state_change=state_change, date_time2=date_time2, device_id=device_id, device_log_id3=device_log_id3, event_type2=event_type2, state_change2=state_change2)

The APIs for creating and manipulating devices

<p>The APIs for creating and manipulating devices.</p>

### Example 
```python
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
date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
device_log_id2 = 'device_log_id_example' # str |  (optional)
event_type = 'event_type_example' # str |  (optional)
state_change = true # bool |  (optional)
date_time2 = 'date_time_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device_log_id3 = 'device_log_id_example' # str |  (optional)
event_type2 = 'event_type_example' # str |  (optional)
state_change2 = 'state_change_example' # str |  (optional)

try: 
    # The APIs for creating and manipulating devices
    api_response = api_instance.device_log_partial_update(device_log_id, date_time=date_time, device_log_id2=device_log_id2, event_type=event_type, state_change=state_change, date_time2=date_time2, device_id=device_id, device_log_id3=device_log_id3, event_type2=event_type2, state_change2=state_change2)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_log_partial_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_log_id** | **str**|  | 
 **date_time** | **datetime**|  | [optional] 
 **device_log_id2** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **state_change** | **bool**|  | [optional] 
 **date_time2** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_log_id3** | **str**|  | [optional] 
 **event_type2** | **str**|  | [optional] 
 **state_change2** | **str**|  | [optional] 

### Return type

[**DeviceLogSerializer**](DeviceLogSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_retrieve**
> DeviceLogSerializer device_log_retrieve(device_log_id)

Retrieve device log

<p>The APIs for creating and manipulating devices.  </p> <p>Retrieve device log.</p>

### Example 
```python
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
    # Retrieve device log
    api_response = api_instance.device_log_retrieve(device_log_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_log_retrieve: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_log_id** | **str**|  | 

### Return type

[**DeviceLogSerializer**](DeviceLogSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_update**
> DeviceLogSerializer device_log_update(device_log_id, date_time, device_log_id2=device_log_id2, event_type=event_type, state_change=state_change, date_time2=date_time2, device_id=device_id, device_log_id3=device_log_id3, event_type2=event_type2, state_change2=state_change2)

The APIs for creating and manipulating devices

<p>The APIs for creating and manipulating devices.</p>

### Example 
```python
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
date_time = '2013-10-20T19:20:30+01:00' # datetime | 
device_log_id2 = 'device_log_id_example' # str |  (optional)
event_type = 'event_type_example' # str |  (optional)
state_change = true # bool |  (optional)
date_time2 = 'date_time_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device_log_id3 = 'device_log_id_example' # str |  (optional)
event_type2 = 'event_type_example' # str |  (optional)
state_change2 = 'state_change_example' # str |  (optional)

try: 
    # The APIs for creating and manipulating devices
    api_response = api_instance.device_log_update(device_log_id, date_time, device_log_id2=device_log_id2, event_type=event_type, state_change=state_change, date_time2=date_time2, device_id=device_id, device_log_id3=device_log_id3, event_type2=event_type2, state_change2=state_change2)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_log_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_log_id** | **str**|  | 
 **date_time** | **datetime**|  | 
 **device_log_id2** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **state_change** | **bool**|  | [optional] 
 **date_time2** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_log_id3** | **str**|  | [optional] 
 **event_type2** | **str**|  | [optional] 
 **state_change2** | **str**|  | [optional] 

### Return type

[**DeviceLogSerializer**](DeviceLogSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_partial_update**
> DeviceSerializer device_partial_update(device_id)

Update device fields

<p>The APIs for creating and manipulating devices.  </p> <p>Update device fields</p>

### Example 
```python
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

try: 
    # Update device fields
    api_response = api_instance.device_partial_update(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_partial_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The ID of the device | 

### Return type

[**DeviceSerializer**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_retrieve**
> DeviceSerializer device_retrieve(device_id)

Retrieve device

<p>The APIs for creating and manipulating devices.  </p> <p>Retrieve device.</p>

### Example 
```python
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
    # Retrieve device
    api_response = api_instance.device_retrieve(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_retrieve: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceSerializer**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> DeviceSerializer device_update(device_id)

Update device

<p>The APIs for creating and manipulating devices.  </p> <p>Update device.</p>

### Example 
```python
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

try: 
    # Update device
    api_response = api_instance.device_update(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The ID of the device | 

### Return type

[**DeviceSerializer**](DeviceSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

