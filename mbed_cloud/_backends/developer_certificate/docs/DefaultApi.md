# developer_certificate.DefaultApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_developer_certificate_delete**](DefaultApi.md#v3_developer_certificate_delete) | **DELETE** /v3/developer-certificate | 
[**v3_developer_certificate_get**](DefaultApi.md#v3_developer_certificate_get) | **GET** /v3/developer-certificate | 
[**v3_developer_certificate_post**](DefaultApi.md#v3_developer_certificate_post) | **POST** /v3/developer-certificate | 


# **v3_developer_certificate_delete**
> v3_developer_certificate_delete(authorization)



Deletes the account's developer certificate (only one per account allowed).

### Example 
```python
from __future__ import print_statement
import time
import developer_certificate
from developer_certificate.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
developer_certificate.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# developer_certificate.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = developer_certificate.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.

try: 
    api_instance.v3_developer_certificate_delete(authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->v3_developer_certificate_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_developer_certificate_get**
> DeveloperCertificate v3_developer_certificate_get(authorization)



Gets the developer certificate of the account.

### Example 
```python
from __future__ import print_statement
import time
import developer_certificate
from developer_certificate.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
developer_certificate.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# developer_certificate.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = developer_certificate.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.

try: 
    api_response = api_instance.v3_developer_certificate_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v3_developer_certificate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 

### Return type

[**DeveloperCertificate**](DeveloperCertificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_developer_certificate_post**
> DeveloperCertificate v3_developer_certificate_post(authorization, body)



Adds a developer certificate to the account (only one per account allowed).

### Example 
```python
from __future__ import print_statement
import time
import developer_certificate
from developer_certificate.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
developer_certificate.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# developer_certificate.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = developer_certificate.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.
body = developer_certificate.Body() # Body | 

try: 
    api_response = api_instance.v3_developer_certificate_post(authorization, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v3_developer_certificate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**DeveloperCertificate**](DeveloperCertificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

