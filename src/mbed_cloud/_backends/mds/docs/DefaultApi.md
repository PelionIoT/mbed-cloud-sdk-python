# mds.DefaultApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_notification_callback_delete**](DefaultApi.md#v2_notification_callback_delete) | **DELETE** /v2/notification/callback | Delete callback URL
[**v2_notification_callback_get**](DefaultApi.md#v2_notification_callback_get) | **GET** /v2/notification/callback | Check callback URL


# **v2_notification_callback_delete**
> v2_notification_callback_delete()

Delete callback URL

Deletes the callback URL.  **Example usage:**      curl -X DELETE https://api.us-east-1.mbedcloud.com/v2/notification/callback -H 'authorization: Bearer {api-key}'      

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
api_instance = mds.DefaultApi(mds.ApiClient(configuration))

try: 
    # Delete callback URL
    api_instance.v2_notification_callback_delete()
except ApiException as e:
    print("Exception when calling DefaultApi->v2_notification_callback_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_notification_callback_get**
> Webhook v2_notification_callback_get()

Check callback URL

Shows the current callback URL if it exists.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/notification/callback -H 'authorization: Bearer {api-key}'      

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
api_instance = mds.DefaultApi(mds.ApiClient(configuration))

try: 
    # Check callback URL
    api_response = api_instance.v2_notification_callback_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v2_notification_callback_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Webhook**](Webhook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

