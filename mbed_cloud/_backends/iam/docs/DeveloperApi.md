# iam.DeveloperApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](DeveloperApi.md#create_api_key) | **POST** /v3/api-keys | Create a new API key.
[**delete_api_key**](DeveloperApi.md#delete_api_key) | **DELETE** /v3/api-keys/{apiKey} | Delete API key.
[**get_all_api_keys**](DeveloperApi.md#get_all_api_keys) | **GET** /v3/api-keys | Get all API keys
[**get_all_groups**](DeveloperApi.md#get_all_groups) | **GET** /v3/policy-groups | Get all group information.
[**get_api_key**](DeveloperApi.md#get_api_key) | **GET** /v3/api-keys/{apiKey} | Get API key details.
[**get_my_account_info**](DeveloperApi.md#get_my_account_info) | **GET** /v3/accounts/me | Get account info.
[**get_my_user**](DeveloperApi.md#get_my_user) | **GET** /v3/users/me | Details of the current user.
[**update_api_key**](DeveloperApi.md#update_api_key) | **PUT** /v3/api-keys/{apiKey} | Update API key details.
[**update_my_user**](DeveloperApi.md#update_my_user) | **PUT** /v3/users/me | Update user details.


# **create_api_key**
> ApiKeyInfoResp create_api_key(body)

Create a new API key.

Endpoint for creating the new API key.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()
body = iam.ApiKeyInfoReq() # ApiKeyInfoReq | The details of the API key to be created.

try: 
    # Create a new API key.
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->create_api_key: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKeyInfoReq**](ApiKeyInfoReq.md)| The details of the API key to be created. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(api_key)

Delete API key.

Endpoint for deleting the API key.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()
api_key = 'api_key_example' # str | The ID of the API key to be deleted.

try: 
    # Delete API key.
    api_instance.delete_api_key(api_key)
except ApiException as e:
    print "Exception when calling DeveloperApi->delete_api_key: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The ID of the API key to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_api_keys**
> ApiKeyInfoRespList get_all_api_keys(owner=owner)

Get all API keys

Endpoint for retrieving API keys in an array, optionally filtered by the owner.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()
owner = 'owner_example' # str | Owner name filter. (optional)

try: 
    # Get all API keys
    api_response = api_instance.get_all_api_keys(owner=owner)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->get_all_api_keys: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Owner name filter. | [optional] 

### Return type

[**ApiKeyInfoRespList**](ApiKeyInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_groups**
> GroupSummaryList get_all_groups()

Get all group information.

Endpoint for retrieving all group information.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()

try: 
    # Get all group information.
    api_response = api_instance.get_all_groups()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->get_all_groups: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupSummaryList**](GroupSummaryList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> ApiKeyInfoResp get_api_key(api_key)

Get API key details.

Endpoint for retrieving API key details.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()
api_key = 'api_key_example' # str | The ID of the API key to be retrieved.

try: 
    # Get API key details.
    api_response = api_instance.get_api_key(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->get_api_key: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The ID of the API key to be retrieved. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_account_info**
> AccountInfo get_my_account_info()

Get account info.

Returns detailed information about the account.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()

try: 
    # Get account info.
    api_response = api_instance.get_my_account_info()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->get_my_account_info: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_user**
> UserInfoResp get_my_user()

Details of the current user.

Endpoint for retrieving the details of the logged in user.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()

try: 
    # Details of the current user.
    api_response = api_instance.get_my_user()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->get_my_user: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiKeyInfoResp update_api_key(api_key, body)

Update API key details.

Endpoint for updating API key details.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()
api_key = 'api_key_example' # str | The ID of the API key to be updated.
body = iam.ApiKeyInfoReq() # ApiKeyInfoReq | New API key attributes to be stored.

try: 
    # Update API key details.
    api_response = api_instance.update_api_key(api_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->update_api_key: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The ID of the API key to be updated. | 
 **body** | [**ApiKeyInfoReq**](ApiKeyInfoReq.md)| New API key attributes to be stored. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_user**
> UserInfoResp update_my_user(body)

Update user details.

Endpoint for updating the details of the logged in user.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi()
body = iam.UserInfoReq() # UserInfoReq | New attributes for the logged in user.

try: 
    # Update user details.
    api_response = api_instance.update_my_user(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeveloperApi->update_my_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserInfoReq**](UserInfoReq.md)| New attributes for the logged in user. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

