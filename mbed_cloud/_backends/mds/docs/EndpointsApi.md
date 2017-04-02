# mds.EndpointsApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_endpoints_endpoint_name_get**](EndpointsApi.md#v2_endpoints_endpoint_name_get) | **GET** /v2/endpoints/{endpointName} | List the resources on an endpoint
[**v2_endpoints_get**](EndpointsApi.md#v2_endpoints_get) | **GET** /v2/endpoints | List endpoints. The number of endpoints is currently limited to 200.


# **v2_endpoints_endpoint_name_get**
> list[Resource] v2_endpoints_endpoint_name_get(endpoint_name)

List the resources on an endpoint

The list of resources is cached by mbed Cloud Connect, so this call does not create a message to the device. 

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.EndpointsApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for an endpoint. Note that the endpoint name needs to be an exact match. You cannot use wildcards here. 

try: 
    # List the resources on an endpoint
    api_response = api_instance.v2_endpoints_endpoint_name_get(endpoint_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->v2_endpoints_endpoint_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for an endpoint. Note that the endpoint name needs to be an exact match. You cannot use wildcards here.  | 

### Return type

[**list[Resource]**](Resource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/link-format

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_endpoints_get**
> list[Endpoint] v2_endpoints_get(type=type)

List endpoints. The number of endpoints is currently limited to 200.

Endpoints are physical devices running mbed Cloud Client. 

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.EndpointsApi()
type = 'type_example' # str | Filter endpoints by endpoint-type. (optional)

try: 
    # List endpoints. The number of endpoints is currently limited to 200.
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
 - **Accept**: application/json, application/link-format

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

