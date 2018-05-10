# iam.DeveloperApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_my_api_key_to_groups**](DeveloperApi.md#add_my_api_key_to_groups) | **POST** /v3/api-keys/me/groups | Add API key to a list of groups.
[**create_api_key**](DeveloperApi.md#create_api_key) | **POST** /v3/api-keys | Create a new API key.
[**delete_api_key**](DeveloperApi.md#delete_api_key) | **DELETE** /v3/api-keys/{apiKey} | Delete API key.
[**delete_certificate**](DeveloperApi.md#delete_certificate) | **DELETE** /v3/trusted-certificates/{cert-id} | Delete a trusted certificate by ID.
[**get_all_api_keys**](DeveloperApi.md#get_all_api_keys) | **GET** /v3/api-keys | Get all API keys
[**get_all_certificates**](DeveloperApi.md#get_all_certificates) | **GET** /v3/trusted-certificates | Get all trusted certificates.
[**get_all_groups**](DeveloperApi.md#get_all_groups) | **GET** /v3/policy-groups | Get all group information.
[**get_api_key**](DeveloperApi.md#get_api_key) | **GET** /v3/api-keys/{apiKey} | Get API key details.
[**get_api_keys_of_group**](DeveloperApi.md#get_api_keys_of_group) | **GET** /v3/policy-groups/{groupID}/api-keys | Get the API keys of a group.
[**get_certificate**](DeveloperApi.md#get_certificate) | **GET** /v3/trusted-certificates/{cert-id} | Get trusted certificate by ID.
[**get_group_summary**](DeveloperApi.md#get_group_summary) | **GET** /v3/policy-groups/{groupID} | Get group information.
[**get_groups_of_my_api_key**](DeveloperApi.md#get_groups_of_my_api_key) | **GET** /v3/api-keys/me/groups | Get groups of the API key.
[**get_my_account_info**](DeveloperApi.md#get_my_account_info) | **GET** /v3/accounts/me | Get account info.
[**get_my_api_key**](DeveloperApi.md#get_my_api_key) | **GET** /v3/api-keys/me | Get API key details.
[**remove_api_keys_from_group**](DeveloperApi.md#remove_api_keys_from_group) | **DELETE** /v3/policy-groups/{groupID}/api-keys | Remove API keys from a group.
[**remove_my_api_key_from_groups**](DeveloperApi.md#remove_my_api_key_from_groups) | **DELETE** /v3/api-keys/me/groups | Remove API key from groups.
[**update_api_key**](DeveloperApi.md#update_api_key) | **PUT** /v3/api-keys/{apiKey} | Update API key details.
[**update_certificate**](DeveloperApi.md#update_certificate) | **PUT** /v3/trusted-certificates/{cert-id} | Update trusted certificate.
[**update_my_api_key**](DeveloperApi.md#update_my_api_key) | **PUT** /v3/api-keys/me | Update API key details.


# **add_my_api_key_to_groups**
> UpdatedResponse add_my_api_key_to_groups(body)

Add API key to a list of groups.

An endpoint for adding API key to groups.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/api-keys/me/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Add API key to a list of groups.
    api_response = api_instance.add_my_api_key_to_groups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->add_my_api_key_to_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| A list of IDs of the groups to be updated. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> ApiKeyInfoResp create_api_key(body)

Create a new API key.

An endpoint for creating a new API key.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/api-keys -d '{\"name\": \"MyKey1\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
body = iam.ApiKeyInfoReq() # ApiKeyInfoReq | The details of the API key to be created.

try: 
    # Create a new API key.
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->create_api_key: %s\n" % e)
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

An endpoint for deleting the API key.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/api-keys/{apikey-id} -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
api_key = 'api_key_example' # str | The ID of the API key to be deleted.

try: 
    # Delete API key.
    api_instance.delete_api_key(api_key)
except ApiException as e:
    print("Exception when calling DeveloperApi->delete_api_key: %s\n" % e)
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

# **delete_certificate**
> delete_certificate(cert_id)

Delete a trusted certificate by ID.

An endpoint for deleting a trusted certificate.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/trusted-certificates/{cert-id} -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be deleted.

try: 
    # Delete a trusted certificate by ID.
    api_instance.delete_certificate(cert_id)
except ApiException as e:
    print("Exception when calling DeveloperApi->delete_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| The ID of the trusted certificate to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_api_keys**
> ApiKeyInfoRespList get_all_api_keys(limit=limit, after=after, order=order, include=include, key__eq=key__eq, owner__eq=owner__eq)

Get all API keys

An endpoint for retrieving API keys in an array, optionally filtered by the owner.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/api-keys -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
key__eq = 'key__eq_example' # str | API key filter. (optional)
owner__eq = 'owner__eq_example' # str | Owner name filter. (optional)

try: 
    # Get all API keys
    api_response = api_instance.get_all_api_keys(limit=limit, after=after, order=order, include=include, key__eq=key__eq, owner__eq=owner__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_all_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **key__eq** | **str**| API key filter. | [optional] 
 **owner__eq** | **str**| Owner name filter. | [optional] 

### Return type

[**ApiKeyInfoRespList**](ApiKeyInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_certificates**
> TrustedCertificateRespList get_all_certificates(limit=limit, after=after, order=order, include=include, name__eq=name__eq, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq, device_execution_mode__neq=device_execution_mode__neq, owner__eq=owner__eq, enrollment_mode__eq=enrollment_mode__eq, issuer__like=issuer__like, subject__like=subject__like)

Get all trusted certificates.

An endpoint for retrieving trusted certificates in an array.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/trusted-certificates -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
name__eq = 'name__eq_example' # str | Filter for certificate name (optional)
service__eq = 'service__eq_example' # str | Service filter, either lwm2m or bootstrap (optional)
expire__eq = 56 # int | Expire filter in days (optional)
device_execution_mode__eq = 56 # int | Device execution mode, as 1 for developer certificates or as another natural integer value (optional)
device_execution_mode__neq = 56 # int | Device execution mode not equals filter (optional)
owner__eq = 'owner__eq_example' # str | Owner name filter (optional)
enrollment_mode__eq = true # bool | Enrollment mode filter (optional)
issuer__like = 'issuer__like_example' # str | Issuer filter. Finds all matches where the filter value is a case insensitive substring of the result. Example: issuer__like=cn=iss matches CN=issuer. (optional)
subject__like = 'subject__like_example' # str | Subject filter. Finds all matches where the filter value is a case insensitive substring of the result. Example: subject__like=cn=su matches CN=subject. (optional)

try: 
    # Get all trusted certificates.
    api_response = api_instance.get_all_certificates(limit=limit, after=after, order=order, include=include, name__eq=name__eq, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq, device_execution_mode__neq=device_execution_mode__neq, owner__eq=owner__eq, enrollment_mode__eq=enrollment_mode__eq, issuer__like=issuer__like, subject__like=subject__like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_all_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **name__eq** | **str**| Filter for certificate name | [optional] 
 **service__eq** | **str**| Service filter, either lwm2m or bootstrap | [optional] 
 **expire__eq** | **int**| Expire filter in days | [optional] 
 **device_execution_mode__eq** | **int**| Device execution mode, as 1 for developer certificates or as another natural integer value | [optional] 
 **device_execution_mode__neq** | **int**| Device execution mode not equals filter | [optional] 
 **owner__eq** | **str**| Owner name filter | [optional] 
 **enrollment_mode__eq** | **bool**| Enrollment mode filter | [optional] 
 **issuer__like** | **str**| Issuer filter. Finds all matches where the filter value is a case insensitive substring of the result. Example: issuer__like&#x3D;cn&#x3D;iss matches CN&#x3D;issuer. | [optional] 
 **subject__like** | **str**| Subject filter. Finds all matches where the filter value is a case insensitive substring of the result. Example: subject__like&#x3D;cn&#x3D;su matches CN&#x3D;subject. | [optional] 

### Return type

[**TrustedCertificateRespList**](TrustedCertificateRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_groups**
> GroupSummaryList get_all_groups(limit=limit, after=after, order=order, include=include, name__eq=name__eq)

Get all group information.

An endpoint for retrieving all group information.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/policy-groups -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
name__eq = 'name__eq_example' # str | Filter for group name (optional)

try: 
    # Get all group information.
    api_response = api_instance.get_all_groups(limit=limit, after=after, order=order, include=include, name__eq=name__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_all_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **name__eq** | **str**| Filter for group name | [optional] 

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

An endpoint for retrieving API key details.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/api-keys/{apikey-id} -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
api_key = 'api_key_example' # str | The ID of the API key to be retrieved.

try: 
    # Get API key details.
    api_response = api_instance.get_api_key(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_api_key: %s\n" % e)
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

# **get_api_keys_of_group**
> ApiKeyInfoRespList get_api_keys_of_group(group_id, limit=limit, after=after, order=order, include=include)

Get the API keys of a group.

An endpoint for listing the API keys of the group with details.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id}/api-keys -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
group_id = 'group_id_example' # str | The ID of the group whose API keys are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get the API keys of a group.
    api_response = api_instance.get_api_keys_of_group(group_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_api_keys_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group whose API keys are retrieved. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 

### Return type

[**ApiKeyInfoRespList**](ApiKeyInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate**
> TrustedCertificateResp get_certificate(cert_id)

Get trusted certificate by ID.

An endpoint for retrieving a trusted certificate by ID.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/trusted-certificates/{cert-id} -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be retrieved.

try: 
    # Get trusted certificate by ID.
    api_response = api_instance.get_certificate(cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| The ID of the trusted certificate to be retrieved. | 

### Return type

[**TrustedCertificateResp**](TrustedCertificateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_summary**
> GroupSummary get_group_summary(group_id)

Get group information.

An endpoint for getting general information about the group.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id} -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
group_id = 'group_id_example' # str | The ID of the group to be retrieved.

try: 
    # Get group information.
    api_response = api_instance.get_group_summary(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_group_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group to be retrieved. | 

### Return type

[**GroupSummary**](GroupSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_of_my_api_key**
> GroupSummaryList get_groups_of_my_api_key(limit=limit, after=after, order=order, include=include)

Get groups of the API key.

An endpoint for retrieving groups of the API key.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/api-keys/me/groups -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get groups of the API key.
    api_response = api_instance.get_groups_of_my_api_key(limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_groups_of_my_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 

### Return type

[**GroupSummaryList**](GroupSummaryList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_account_info**
> AccountInfo get_my_account_info(include=include, properties=properties)

Get account info.

Returns detailed information about the account.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/me?include=policies -H 'Authorization: Bearer API_KEY'`.

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
include = 'include_example' # str | Comma separated additional data to return. Currently supported: limits, policies, sub_accounts. (optional)
properties = 'properties_example' # str | Property name to be returned from account specific properties. (optional)

try: 
    # Get account info.
    api_response = api_instance.get_my_account_info(include=include, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_my_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Comma separated additional data to return. Currently supported: limits, policies, sub_accounts. | [optional] 
 **properties** | **str**| Property name to be returned from account specific properties. | [optional] 

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_api_key**
> ApiKeyInfoResp get_my_api_key()

Get API key details.

An endpoint for retrieving API key details.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/api-keys/me -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))

try: 
    # Get API key details.
    api_response = api_instance.get_my_api_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_my_api_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_api_keys_from_group**
> UpdatedResponse remove_api_keys_from_group(group_id, body)

Remove API keys from a group.

An endpoint for removing API keys from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id}/api-keys -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
group_id = 'group_id_example' # str | The ID of the group whose API keys are removed.
body = iam.SubjectList() # SubjectList | A list of API keys to be removed from the group.

try: 
    # Remove API keys from a group.
    api_response = api_instance.remove_api_keys_from_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->remove_api_keys_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group whose API keys are removed. | 
 **body** | [**SubjectList**](SubjectList.md)| A list of API keys to be removed from the group. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_my_api_key_from_groups**
> UpdatedResponse remove_my_api_key_from_groups(body)

Remove API key from groups.

An endpoint for removing API key from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/api-keys/me/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Remove API key from groups.
    api_response = api_instance.remove_my_api_key_from_groups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->remove_my_api_key_from_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| A list of IDs of the groups to be updated. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiKeyInfoResp update_api_key(api_key, body)

Update API key details.

An endpoint for updating API key details.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/api-keys/{apikey-id} -d '{\"name\": \"TestApiKey25\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
api_key = 'api_key_example' # str | The ID of the API key to be updated.
body = iam.ApiKeyUpdateReq() # ApiKeyUpdateReq | New API key attributes to be stored.

try: 
    # Update API key details.
    api_response = api_instance.update_api_key(api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The ID of the API key to be updated. | 
 **body** | [**ApiKeyUpdateReq**](ApiKeyUpdateReq.md)| New API key attributes to be stored. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate**
> TrustedCertificateResp update_certificate(cert_id, body)

Update trusted certificate.

An endpoint for updating existing trusted certificates.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/trusted-certificates/{cert-id} -d {\"description\": \"very important cert\"} -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be updated.
body = iam.TrustedCertificateUpdateReq() # TrustedCertificateUpdateReq | A trusted certificate object with attributes.

try: 
    # Update trusted certificate.
    api_response = api_instance.update_certificate(cert_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->update_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| The ID of the trusted certificate to be updated. | 
 **body** | [**TrustedCertificateUpdateReq**](TrustedCertificateUpdateReq.md)| A trusted certificate object with attributes. | 

### Return type

[**TrustedCertificateResp**](TrustedCertificateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_api_key**
> ApiKeyInfoResp update_my_api_key(body)

Update API key details.

An endpoint for updating API key details.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/api-keys/me -d '{\"name\": \"TestApiKey25\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

### Example 
```python
from __future__ import print_function
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = iam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.DeveloperApi(iam.ApiClient(configuration))
body = iam.ApiKeyUpdateReq() # ApiKeyUpdateReq | New API key attributes to be stored.

try: 
    # Update API key details.
    api_response = api_instance.update_my_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->update_my_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKeyUpdateReq**](ApiKeyUpdateReq.md)| New API key attributes to be stored. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

