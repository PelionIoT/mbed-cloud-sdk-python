# mds.EndpointsApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_endpoints_device_id_get**](EndpointsApi.md#v2_endpoints_device_id_get) | **GET** /v2/endpoints/{device-id} | List the resources on an endpoint
[**v2_endpoints_get**](EndpointsApi.md#v2_endpoints_get) | **GET** /v2/endpoints | (DEPRECATED) List registered endpoints. The number of returned endpoints is currently limited to 200.


# **v2_endpoints_device_id_get**
> list[Resource] v2_endpoints_device_id_get(device_id)

List the resources on an endpoint

The list of resources is cached by Mbed Cloud Connect, so this call does not create a message to the device.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id} -H 'authorization: Bearer {api-key}'      

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
api_instance = mds.EndpointsApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Mbed Cloud device ID for an endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here. 

try: 
    # List the resources on an endpoint
    api_response = api_instance.v2_endpoints_device_id_get(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->v2_endpoints_device_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Mbed Cloud device ID for an endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  | 

### Return type

[**list[Resource]**](Resource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_endpoints_get**
> list[Endpoint] v2_endpoints_get(type=type)

(DEPRECATED) List registered endpoints. The number of returned endpoints is currently limited to 200.

Endpoints are physical devices having valid registration to Mbed Cloud Connect. All devices regardless of registration status can be requested from Device Directory API ['/v3/devices/`](/docs/v1.2/service-api-references/device-directory-api.html#v3-devices).  **Note:** This endpoint is deprecated and will be removed 1Q/18. You should use the Device Directory API [`/v3/devices/`](/docs/v1.2/service-api-references/device-directory-api.html#v3-devices). To list only the registered devices, use filter `/v3/devices/?filter=state%3Dregistered`.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/endpoints -H 'authorization: Bearer {api-key}'      

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
api_instance = mds.EndpointsApi(mds.ApiClient(configuration))
type = 'type_example' # str | Filter endpoints by endpoint-type. (optional)

try: 
    # (DEPRECATED) List registered endpoints. The number of returned endpoints is currently limited to 200.
    api_response = api_instance.v2_endpoints_get(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->v2_endpoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter endpoints by endpoint-type. | [optional] 

### Return type

[**list[Endpoint]**](Endpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

