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
> DeviceDetail device_create(mechanism, provision_key, account_id=account_id, auto_update=auto_update, bootstrapped_timestamp=bootstrapped_timestamp, created_at=created_at, custom_attributes=custom_attributes, deployed_state=deployed_state, deployment=deployment, description=description, device_class=device_class, device_id=device_id, etag=etag, id=id, manifest=manifest, mechanism_url=mechanism_url, name=name, object=object, serial_number=serial_number, state=state, trust_class=trust_class, trust_level=trust_level, updated_at=updated_at, vendor_id=vendor_id)



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
mechanism = 'mechanism_example' # str | The ID of the channel used to communicate with the device
provision_key = 'provision_key_example' # str | The key used to provision the device
account_id = 'account_id_example' # str | The owning IAM account ID (optional)
auto_update = true # bool | Mark this device for auto firmware update (optional)
bootstrapped_timestamp = 'bootstrapped_timestamp_example' # str |  (optional)
created_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
custom_attributes = {'key': 'custom_attributes_example'} # dict(str, str) | Up to 5 custom JSON attributes (optional)
deployed_state = 'deployed_state_example' # str | The state of the device's deployment (optional)
deployment = 'deployment_example' # str | The last deployment used on the device (optional)
description = 'description_example' # str | The description of the object (optional)
device_class = 'device_class_example' # str |  (optional)
device_id = 'device_id_example' # str | DEPRECATED: The ID of the device (optional)
etag = '2013-10-20T19:20:30+01:00' # datetime | The entity instance signature (optional)
id = 'id_example' # str | The ID of the device (optional)
manifest = 'manifest_example' # str | URL for the current device manifest (optional)
mechanism_url = 'mechanism_url_example' # str | The address of the connector to use (optional)
name = 'name_example' # str | The name of the object (optional)
object = 'object_example' # str | The API resource entity (optional)
serial_number = 'serial_number_example' # str | The serial number of the device (optional)
state = 'state_example' # str | The current state of the device (optional)
trust_class = 789 # int | The device trust class (optional)
trust_level = 789 # int | The device trust level (optional)
updated_at = '2013-10-20T19:20:30+01:00' # datetime | The time the object was updated (optional)
vendor_id = 'vendor_id_example' # str | The device vendor ID (optional)

try: 
    api_response = api_instance.device_create(mechanism, provision_key, account_id=account_id, auto_update=auto_update, bootstrapped_timestamp=bootstrapped_timestamp, created_at=created_at, custom_attributes=custom_attributes, deployed_state=deployed_state, deployment=deployment, description=description, device_class=device_class, device_id=device_id, etag=etag, id=id, manifest=manifest, mechanism_url=mechanism_url, name=name, object=object, serial_number=serial_number, state=state, trust_class=trust_class, trust_level=trust_level, updated_at=updated_at, vendor_id=vendor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mechanism** | **str**| The ID of the channel used to communicate with the device | 
 **provision_key** | **str**| The key used to provision the device | 
 **account_id** | **str**| The owning IAM account ID | [optional] 
 **auto_update** | **bool**| Mark this device for auto firmware update | [optional] 
 **bootstrapped_timestamp** | **str**|  | [optional] 
 **created_at** | **datetime**|  | [optional] 
 **custom_attributes** | [**dict(str, str)**](str.md)| Up to 5 custom JSON attributes | [optional] 
 **deployed_state** | **str**| The state of the device&#39;s deployment | [optional] 
 **deployment** | **str**| The last deployment used on the device | [optional] 
 **description** | **str**| The description of the object | [optional] 
 **device_class** | **str**|  | [optional] 
 **device_id** | **str**| DEPRECATED: The ID of the device | [optional] 
 **etag** | **datetime**| The entity instance signature | [optional] 
 **id** | **str**| The ID of the device | [optional] 
 **manifest** | **str**| URL for the current device manifest | [optional] 
 **mechanism_url** | **str**| The address of the connector to use | [optional] 
 **name** | **str**| The name of the object | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **serial_number** | **str**| The serial number of the device | [optional] 
 **state** | **str**| The current state of the device | [optional] 
 **trust_class** | **int**| The device trust class | [optional] 
 **trust_level** | **int**| The device trust level | [optional] 
 **updated_at** | **datetime**| The time the object was updated | [optional] 
 **vendor_id** | **str**| The device vendor ID | [optional] 

### Return type

[**DeviceDetail**](DeviceDetail.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_destroy**
> DeviceListResp device_destroy(device_id)



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

[**DeviceListResp**](DeviceListResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_list**
> DeviceListResp device_list(limit=limit, order=order, after=after, filter=filter, include=include)



<p>The APIs for creating and manipulating devices.  </p> <p>List all update devices. The result is paged into pages of 100.</p>

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
limit = 56 # int |  (optional)
order = 'order_example' # str |  (optional)
after = 'after_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
include = 'include_example' # str |  (optional)

try: 
    api_response = api_instance.device_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **include** | **str**|  | [optional] 

### Return type

[**DeviceListResp**](DeviceListResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_list**
> DeviceLogSerializer device_log_list(limit=limit, order=order, after=after, filter=filter, include=include)



<p>The APIs for creating and manipulating devices.  </p> <p>List all device logs.</p>

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
limit = 56 # int |  (optional)
order = 'order_example' # str |  (optional)
after = 'after_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
include = 'include_example' # str |  (optional)

try: 
    api_response = api_instance.device_log_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **include** | **str**|  | [optional] 

### Return type

[**DeviceLogSerializer**](DeviceLogSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_log_retrieve**
> DeviceLogSerializerData device_log_retrieve(device_log_id)



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

[**DeviceLogSerializerData**](DeviceLogSerializerData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_partial_update**
> DeviceListResp device_partial_update(device_id)



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

try: 
    api_response = api_instance.device_partial_update(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The ID of the device | 

### Return type

[**DeviceListResp**](DeviceListResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_retrieve**
> DeviceListResp device_retrieve(device_id)



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

[**DeviceListResp**](DeviceListResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> DeviceDetail device_update(device_id, body)



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
body = device_catalog.DeviceUpdateDetail() # DeviceUpdateDetail | Device object to update

try: 
    api_response = api_instance.device_update(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The ID of the device | 
 **body** | [**DeviceUpdateDetail**](DeviceUpdateDetail.md)| Device object to update | 

### Return type

[**DeviceDetail**](DeviceDetail.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

