# iam.DefaultApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_alive**](DefaultApi.md#is_alive) | **GET** /alive | Get alive status


# **is_alive**
> is_alive(deepalive=deepalive)

Get alive status



### Example 
```python
from __future__ import print_statement
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DefaultApi()
deepalive = true # bool | An optional parameter for getting deep aliveness. Must be true or false. (optional)

try: 
    # Get alive status
    api_instance.is_alive(deepalive=deepalive)
except ApiException as e:
    print("Exception when calling DefaultApi->is_alive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deepalive** | **bool**| An optional parameter for getting deep aliveness. Must be true or false. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

