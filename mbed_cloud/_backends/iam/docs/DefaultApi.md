# iam.DefaultApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_agreement**](DefaultApi.md#download_agreement) | **GET** /downloads/agreements/{agreement-id} | Download agreement as a document.
[**head_downloads**](DefaultApi.md#head_downloads) | **HEAD** /downloads/agreements | The heartbeat method for this API.
[**is_alive**](DefaultApi.md#is_alive) | **GET** /alive | Get alive status


# **download_agreement**
> download_agreement(agreement_id)

Download agreement as a document.

Endpoint for download limits by account ID.

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
agreement_id = 'agreement_id_example' # str | The ID of the agreement to be returned.

try: 
    # Download agreement as a document.
    api_instance.download_agreement(agreement_id)
except ApiException as e:
    print("Exception when calling DefaultApi->download_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement_id** | **str**| The ID of the agreement to be returned. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_downloads**
> head_downloads()

The heartbeat method for this API.



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

try: 
    # The heartbeat method for this API.
    api_instance.head_downloads()
except ApiException as e:
    print("Exception when calling DefaultApi->head_downloads: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

