# connector_frontend.ResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_delete**](ResourcesApi.md#v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_delete) | **DELETE** /v3/connect-synchronizer/proxy/endpoint/{endpointName}/{resourcePath} | Delete a resource
[**v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_get**](ResourcesApi.md#v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_get) | **GET** /v3/connect-synchronizer/proxy/endpoint/{endpointName}/{resourcePath} | Read from a resource
[**v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_post**](ResourcesApi.md#v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_post) | **POST** /v3/connect-synchronizer/proxy/endpoint/{endpointName}/{resourcePath} | Execute a function on a resource
[**v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_put**](ResourcesApi.md#v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_put) | **PUT** /v3/connect-synchronizer/proxy/endpoint/{endpointName}/{resourcePath} | Write to a resource


# **v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_delete**
> v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_delete(endpoint_name, _resource_path, no_resp=no_resp, pri=pri)

Delete a resource

A request to delete a resource must be handled by both mbed Client and mbed Device Connector. The resource is not deleted from mbed Device Connector until the delete is handled by mbed Client.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Device Connector. 

### Example 
```python
from __future__ import print_statement
import time
import connector_frontend
from connector_frontend.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_frontend.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_frontend.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_frontend.ResourcesApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | Resource's url. 
no_resp = true # bool | ** Non-confirmable requests **  All resource APIs have the parameter noResp. If you make a request with noResp=true, mbed Device Connector makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict.  (optional)
pri = 'pri_example' # str | Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values 0-7 are interpreted as matching to the corresponding CS value. Optional. Default: 0  (optional)

try: 
    # Delete a resource
    api_instance.v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_delete(endpoint_name, _resource_path, no_resp=no_resp, pri=pri)
except ApiException as e:
    print("Exception when calling ResourcesApi->v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| Resource&#39;s url.  | 
 **no_resp** | **bool**| ** Non-confirmable requests **  All resource APIs have the parameter noResp. If you make a request with noResp&#x3D;true, mbed Device Connector makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict.  | [optional] 
 **pri** | **str**| Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values 0-7 are interpreted as matching to the corresponding CS value. Optional. Default: 0  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_get**
> str v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_get(endpoint_name, _resource_path, cache_only=cache_only, pri=pri)

Read from a resource

Requests the resource value and when the response is available, a json object with the resource value will be returned.  Note that these APIs will only respond if the device is turned on and connected to mbed Device Connector. 

### Example 
```python
from __future__ import print_statement
import time
import connector_frontend
from connector_frontend.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_frontend.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_frontend.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_frontend.ResourcesApi()
endpoint_name = 'endpoint_name_example' # str | Unique identifier for the endpoint. Note that the endpoint name needs to be an exact match. You cannot use wildcards here.
_resource_path = '_resource_path_example' # str | Resource's url.
cache_only = true # bool | Decides if the response comes only from the cache or from the device. Default value is false. (optional)
pri = 'pri_example' # str | Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values [0 - 7 ] are interpreted as matching to the corresponding CS value. This is an optional field.  (optional)

try: 
    # Read from a resource
    api_response = api_instance.v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_get(endpoint_name, _resource_path, cache_only=cache_only, pri=pri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Unique identifier for the endpoint. Note that the endpoint name needs to be an exact match. You cannot use wildcards here. | 
 **_resource_path** | **str**| Resource&#39;s url. | 
 **cache_only** | **bool**| Decides if the response comes only from the cache or from the device. Default value is false. | [optional] 
 **pri** | **str**| Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values [0 - 7 ] are interpreted as matching to the corresponding CS value. This is an optional field.  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_post**
> v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_post(endpoint_name, _resource_path, resource_function=resource_function, no_resp=no_resp, pri=pri)

Execute a function on a resource

With this API, you can execute a function on an existing resource.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Device Connector. 

### Example 
```python
from __future__ import print_statement
import time
import connector_frontend
from connector_frontend.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_frontend.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_frontend.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_frontend.ResourcesApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | Resource's url.
resource_function = 'resource_function_example' # str | This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in mbed Client.  (optional)
no_resp = true # bool | **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp=true,mbed Device Connector makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict.  (optional)
pri = 'pri_example' # str | Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values 0-7 are interpreted as matching to the corresponding CS value. Optional. Default: 0  (optional)

try: 
    # Execute a function on a resource
    api_instance.v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_post(endpoint_name, _resource_path, resource_function=resource_function, no_resp=no_resp, pri=pri)
except ApiException as e:
    print("Exception when calling ResourcesApi->v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| Resource&#39;s url. | 
 **resource_function** | **str**| This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in mbed Client.  | [optional] 
 **no_resp** | **bool**| **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp&#x3D;true,mbed Device Connector makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict.  | [optional] 
 **pri** | **str**| Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values 0-7 are interpreted as matching to the corresponding CS value. Optional. Default: 0  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: text/plain, application/xml, application/octet-stream, application/exi, application/json, application/link-format, application/senml+json, application/nanoservice-tlv, application/vnd.oma.lwm2m+text, application/vnd.oma.lwm2m+opaq, application/vnd.oma.lwm2m+tlv, application/vnd.oma.lwm2m+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_put**
> v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_put(endpoint_name, _resource_path, resource_value, pri=pri)

Write to a resource

With this API, you can write new values to existing resources, or create new resources on the device. The resource-path does not have to exist - it can be created by the call.  Note that these APIs respond only if the device is turned on and connected to mbed Device Connector.  Also note that query parameters defined in OMA specification such as step/lt/ gt/pmax/ pmin can also be included with relvant values and will be passed to the device as they are defined. 

### Example 
```python
from __future__ import print_statement
import time
import connector_frontend
from connector_frontend.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
connector_frontend.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# connector_frontend.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_frontend.ResourcesApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here.
_resource_path = '_resource_path_example' # str | Resource's url.
resource_value = 'resource_value_example' # str | Value to be set to the resource. (Check accceptable content-types)
pri = 'pri_example' # str | Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values 0-7 are interpreted as matching to the corresponding CS value. Optional. Default: 0  (optional)

try: 
    # Write to a resource
    api_instance.v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_put(endpoint_name, _resource_path, resource_value, pri=pri)
except ApiException as e:
    print("Exception when calling ResourcesApi->v3_connect_synchronizer_proxy_endpoint_endpoint_name_resource_path_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here. | 
 **_resource_path** | **str**| Resource&#39;s url. | 
 **resource_value** | **str**| Value to be set to the resource. (Check accceptable content-types) | 
 **pri** | **str**| Priority message. Adds traffic-class for outgoing IPv6 message (only UDP). Network should this header and  Accepted values are AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, VA, EF, CS0, CS1, CS2,CS3, CS4, CS5, CS6, CS7 and DF. Numeric values 0-7 are interpreted as matching to the corresponding CS value. Optional. Default: 0  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: text/plain, application/xml, application/octet-stream, application/exi, application/json, application/link-format, application/senml+json, application/nanoservice-tlv, application/vnd.oma.lwm2m+text, application/vnd.oma.lwm2m+opaq, application/vnd.oma.lwm2m+tlv, application/vnd.oma.lwm2m+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

