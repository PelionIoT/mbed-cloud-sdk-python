# mds.ResourcesApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_resource_path**](ResourcesApi.md#delete_resource_path) | **DELETE** /v2/endpoints/{device-id}/{resourcePath} | Delete a resource path
[**execute_or_create_resource**](ResourcesApi.md#execute_or_create_resource) | **POST** /v2/endpoints/{device-id}/{resourcePath} | Execute a function on a Resource or create new Object instance
[**get_resource_value**](ResourcesApi.md#get_resource_value) | **GET** /v2/endpoints/{device-id}/{resourcePath} | Read from a resource
[**update_resource_value**](ResourcesApi.md#update_resource_value) | **PUT** /v2/endpoints/{device-id}/{resourcePath} | Write to a resource or use write-attributes for a resource


# **delete_resource_path**
> AsyncID delete_resource_path(device_id, _resource_path, no_resp=no_resp)

Delete a resource path

A request to delete a resource path must be handled by both Device Management Client and Device Management Connect.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  **Example usage:**      curl -X DELETE \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.ResourcesApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 
no_resp = true # bool | <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`.  (optional)

try: 
    # Delete a resource path
    api_response = api_instance.delete_resource_path(device_id, _resource_path, no_resp=no_resp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->delete_resource_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 
 **no_resp** | **bool**| &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Non-confirmable requests&lt;/b&gt;&lt;br/&gt;  All resource APIs have the parameter noResp. If you make a request with &#x60;noResp&#x3D;true&#x60;, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code &#x60;204 No Content&#x60;. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code &#x60;409 Conflict&#x60;.  | [optional] 

### Return type

[**AsyncID**](AsyncID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_or_create_resource**
> AsyncID execute_or_create_resource(device_id, _resource_path, resource_function=resource_function, no_resp=no_resp)

Execute a function on a Resource or create new Object instance

With this API, you can [execute a function](/docs/current/connecting/handle-resource-webapp.html#the-execute-operation) on an existing resource and create new Object instance to the device. The resource-path does not have to exist - it can be created by the call. The maximum length of resource-path is 255 characters.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  Supported content types depend on the device and its resource. Device Management translates HTTP to equivalent CoAP content type.  **Example usage:**  This example resets the min and max values of the [temperature sensor](http://www.openmobilealliance.org/tech/profiles/lwm2m/3303.xml) instance 0 by executing the Resource 5605 'Reset Min and Max Measured Values'.      curl -X POST \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3303/0/5605 \\       -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.ResourcesApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource.
resource_function = 'resource_function_example' # str | This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in Device Management Client.  (optional)
no_resp = true # bool | <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`.  (optional)

try: 
    # Execute a function on a Resource or create new Object instance
    api_response = api_instance.execute_or_create_resource(device_id, _resource_path, resource_function=resource_function, no_resp=no_resp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->execute_or_create_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource. | 
 **resource_function** | **str**| This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in Device Management Client.  | [optional] 
 **no_resp** | **bool**| &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Non-confirmable requests&lt;/b&gt;&lt;br/&gt;  All resource APIs have the parameter noResp. If you make a request with &#x60;noResp&#x3D;true&#x60;, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code &#x60;204 No Content&#x60;. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code &#x60;409 Conflict&#x60;.  | [optional] 

### Return type

[**AsyncID**](AsyncID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: text/plain, application/xml, application/octet-stream, application/exi, application/json, application/link-format, application/senml+json, application/nanoservice-tlv, application/vnd.oma.lwm2m+text, application/vnd.oma.lwm2m+opaq, application/vnd.oma.lwm2m+tlv, application/vnd.oma.lwm2m+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_value**
> get_resource_value(device_id, _resource_path, cache_only=cache_only, no_resp=no_resp)

Read from a resource

Requests the resource value and when the response is available, an `AsyncIDResponse` json object is received in the notification channel. The preferred way to get resource values is to use the **subscribe** and **callback** methods.  All resource APIs are asynchronous. These APIs only respond if the device is turned on and connected to Device Management.  Please refer to [Lightweight Machine to Machine Technical specification](http://www.openmobilealliance.org/release/LightweightM2M/V1_0-20170208-A/OMA-TS-LightweightM2M-V1_0-20170208-A.pdf) for more inforamtion.  **Example usage:**      curl -X GET \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.ResourcesApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique Device Management device ID for the endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 
cache_only = true # bool | If true, the response comes only from the cache. Default: false. Device Management Connect caches the received resource values for the time of [max_age](/docs/current/connecting/working-with-the-resources.html) defined in the client side.  (optional)
no_resp = true # bool | <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter `noResp`. If a request is made with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`.  (optional)

try: 
    # Read from a resource
    api_instance.get_resource_value(device_id, _resource_path, cache_only=cache_only, no_resp=no_resp)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique Device Management device ID for the endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 
 **cache_only** | **bool**| If true, the response comes only from the cache. Default: false. Device Management Connect caches the received resource values for the time of [max_age](/docs/current/connecting/working-with-the-resources.html) defined in the client side.  | [optional] 
 **no_resp** | **bool**| &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Non-confirmable requests&lt;/b&gt;&lt;br/&gt;  All resource APIs have the parameter &#x60;noResp&#x60;. If a request is made with &#x60;noResp&#x3D;true&#x60;, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code &#x60;204 No Content&#x60;. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code &#x60;409 Conflict&#x60;.  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_value**
> AsyncID update_resource_value(device_id, _resource_path, resource_value, no_resp=no_resp)

Write to a resource or use write-attributes for a resource

With this API, you can [write a new value to existing resources](/docs/current/connecting/handle-resource-webapp.html) or [use the write-attributes](/docs/current/connecting/resource-change-webapp.html) for a resource.  This API can also be used to transfer files to the device. Device Management Connect LwM2M server implements the Option 1 from RFC7959. The maximum block size is 1024 bytes. The block size versus transferred file size is something to note in low quality networks. The customer application needs to know what type of file is transferred (for example txt) and the payload can be encrypted by the customer. The maximum size of payload is 1048576 bytes.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  Supported content types depend on the device and its resource. Device Management translates HTTP to equivalent CoAP content type.  **Example usage:**  This example sets the alarm on a buzzer. The command writes the [Buzzer](http://www.openmobilealliance.org/tech/profiles/lwm2m/3338.xml) instance 0, \"On/Off\" boolean resource to '1'.      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3338/0/5850 -H \"content-type: text/plain\" \\       -H 'authorization: Bearer {api-key}' -d '1' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.ResourcesApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | Resource URL.
resource_value = 'resource_value_example' # str | The value to be set to the resource. 
no_resp = true # bool | <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`.  (optional)

try: 
    # Write to a resource or use write-attributes for a resource
    api_response = api_instance.update_resource_value(device_id, _resource_path, resource_value, no_resp=no_resp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->update_resource_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| Resource URL. | 
 **resource_value** | **str**| The value to be set to the resource.  | 
 **no_resp** | **bool**| &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Non-confirmable requests&lt;/b&gt;&lt;br/&gt;  All resource APIs have the parameter noResp. If you make a request with &#x60;noResp&#x3D;true&#x60;, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code &#x60;204 No Content&#x60;. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code &#x60;409 Conflict&#x60;.  | [optional] 

### Return type

[**AsyncID**](AsyncID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: text/plain, application/xml, application/octet-stream, application/exi, application/json, application/link-format, application/senml+json, application/nanoservice-tlv, application/vnd.oma.lwm2m+text, application/vnd.oma.lwm2m+opaq, application/vnd.oma.lwm2m+tlv, application/vnd.oma.lwm2m+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

