# bootstrap.PreSharedKeysApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_a_pre_shared_key**](PreSharedKeysApi.md#delete_a_pre_shared_key) | **DELETE** /v2/device-shared-keys/{endpoint_name} | Remove a pre-shared key.
[**get_a_pre_shared_key**](PreSharedKeysApi.md#get_a_pre_shared_key) | **GET** /v2/device-shared-keys/{endpoint_name} | Get a pre-shared key.
[**upload_a_pre_shared_key**](PreSharedKeysApi.md#upload_a_pre_shared_key) | **POST** /v2/device-shared-keys | Upload a pre-shared key to Mbed Cloud.


# **delete_a_pre_shared_key**
> delete_a_pre_shared_key(endpoint_name)

Remove a pre-shared key.

Remove a pre-shared key.

### Example 
```python
from __future__ import print_function
import time
import bootstrap
from bootstrap.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bootstrap.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bootstrap.PreSharedKeysApi(bootstrap.ApiClient(configuration))
endpoint_name = 'endpoint_name_example' # str | The endpoint name. A unique identifier of the pre-shared key. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded.

try: 
    # Remove a pre-shared key.
    api_instance.delete_a_pre_shared_key(endpoint_name)
except ApiException as e:
    print("Exception when calling PreSharedKeysApi->delete_a_pre_shared_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| The endpoint name. A unique identifier of the pre-shared key. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_pre_shared_key**
> PreSharedKeyWithoutSecret get_a_pre_shared_key(endpoint_name)

Get a pre-shared key.

Check if a pre-shared key for an endpoint exists or not. The response does not contain the secret itself. 

### Example 
```python
from __future__ import print_function
import time
import bootstrap
from bootstrap.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bootstrap.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bootstrap.PreSharedKeysApi(bootstrap.ApiClient(configuration))
endpoint_name = 'endpoint_name_example' # str | The endpoint name. A unique identifier of the pre-shared key. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded.

try: 
    # Get a pre-shared key.
    api_response = api_instance.get_a_pre_shared_key(endpoint_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreSharedKeysApi->get_a_pre_shared_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| The endpoint name. A unique identifier of the pre-shared key. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded. | 

### Return type

[**PreSharedKeyWithoutSecret**](PreSharedKeyWithoutSecret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_a_pre_shared_key**
> upload_a_pre_shared_key(body)

Upload a pre-shared key to Mbed Cloud.

Upload a pre-shared key (PSK) for an endpoint to allow it to bootstrap. The existing key will not be overwritten but needs to be deleted first in case of re-setting PSK for an endpoint.  **Note**: The PSK APIs are available only to accounts that have this feature enabled.  ``` Example payloads: {\"endpoint_name\": \"myEndpoint\", \"secret_hex\": \"4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a\" } {\"endpoint_name\": \"myEndpoint\", \"secret_hex\": \"0x4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a\" } ``` 

### Example 
```python
from __future__ import print_function
import time
import bootstrap
from bootstrap.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bootstrap.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bootstrap.PreSharedKeysApi(bootstrap.ApiClient(configuration))
body = bootstrap.PreSharedKey() # PreSharedKey | Pre-shared key to be uploaded.

try: 
    # Upload a pre-shared key to Mbed Cloud.
    api_instance.upload_a_pre_shared_key(body)
except ApiException as e:
    print("Exception when calling PreSharedKeysApi->upload_a_pre_shared_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreSharedKey**](PreSharedKey.md)| Pre-shared key to be uploaded. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

