# iam.DeveloperApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_api_keys_to_group**](DeveloperApi.md#add_api_keys_to_group) | **POST** /v3/policy-groups/{groupID}/api-keys | Add API keys to a group.
[**change_my_password**](DeveloperApi.md#change_my_password) | **PUT** /v3/users/me/password | Change the password of the current user.
[**get_account_attributes**](DeveloperApi.md#get_account_attributes) | **GET** /v3/accounts/{accountID}/attributes | Read account attributes.
[**get_aliases**](DeveloperApi.md#get_aliases) | **GET** /v3/accounts/{accountID}/alias | Get aliases.
[**get_all_groups**](DeveloperApi.md#get_all_groups) | **GET** /v3/policy-groups | Get all group information.
[**get_api_keys_of_group**](DeveloperApi.md#get_api_keys_of_group) | **GET** /v3/policy-groups/{groupID}/api-keys | Get the API keys of a group.
[**get_group_summary**](DeveloperApi.md#get_group_summary) | **GET** /v3/policy-groups/{groupID} | Get group information.
[**get_my_user**](DeveloperApi.md#get_my_user) | **GET** /v3/users/me | Details of the current user.
[**remove_api_keys_from_group**](DeveloperApi.md#remove_api_keys_from_group) | **DELETE** /v3/policy-groups/{groupID}/api-keys | Remove API keys from a group.
[**update_my_user**](DeveloperApi.md#update_my_user) | **PUT** /v3/users/me | Update user details.


# **add_api_keys_to_group**
> UpdatedResponse add_api_keys_to_group(group_id, body)

Add API keys to a group.

Ann endpoint for adding API keys to groups.

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
api_instance = iam.DeveloperApi()
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.SubjectList() # SubjectList | A list of API keys to be added to the group.

try: 
    # Add API keys to a group.
    api_response = api_instance.add_api_keys_to_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->add_api_keys_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group to be updated. | 
 **body** | [**SubjectList**](SubjectList.md)| A list of API keys to be added to the group. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_my_password**
> UpdatedResponse change_my_password(body)

Change the password of the current user.

An endpoint for changing the password of the logged in user.

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
api_instance = iam.DeveloperApi()
body = iam.PasswordChangeReq() # PasswordChangeReq | Old and new password.

try: 
    # Change the password of the current user.
    api_response = api_instance.change_my_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->change_my_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeReq**](PasswordChangeReq.md)| Old and new password. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attributes**
> dict(str, str) get_account_attributes(account_id, name=name)

Read account attributes.

Reads all account attributes as map.

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
api_instance = iam.DeveloperApi()
account_id = 'account_id_example' # str | The ID of the account to be read.
name = 'name_example' # str | A comma separated list of attribute names. (optional)

try: 
    # Read account attributes.
    api_response = api_instance.get_account_attributes(account_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_account_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be read. | 
 **name** | **str**| A comma separated list of attribute names. | [optional] 

### Return type

[**dict(str, str)**](dict.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aliases**
> list[str] get_aliases(account_id)

Get aliases.

Retrieves the aliases of the account as an array.

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
api_instance = iam.DeveloperApi()
account_id = 'account_id_example' # str | The ID of the account whose aliases are retrieved.

try: 
    # Get aliases.
    api_response = api_instance.get_aliases(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account whose aliases are retrieved. | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_groups**
> GroupSummaryList get_all_groups(limit=limit, after=after, order=order, include=include)

Get all group information.

An endpoint for retrieving all group information.

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
api_instance = iam.DeveloperApi()
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get all group information.
    api_response = api_instance.get_all_groups(limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_all_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 

### Return type

[**GroupSummaryList**](GroupSummaryList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_of_group**
> ApiKeyInfoRespList get_api_keys_of_group(group_id, limit=limit, after=after, order=order, include=include)

Get the API keys of a group.

An endpoint for listing the API keys of the group with details.

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
api_instance = iam.DeveloperApi()
group_id = 'group_id_example' # str | The ID of the group whose API keys are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
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
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 

### Return type

[**ApiKeyInfoRespList**](ApiKeyInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_summary**
> GroupSummary get_group_summary(group_id)

Get group information.

An endpoint for getting general information about the group.

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
api_instance = iam.DeveloperApi()
group_id = 'group_id_example' # str | The ID or name of the group to be retrieved.

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
 **group_id** | **str**| The ID or name of the group to be retrieved. | 

### Return type

[**GroupSummary**](GroupSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_user**
> UserInfoResp get_my_user()

Details of the current user.

An endpoint for retrieving the details of the logged in user.

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
api_instance = iam.DeveloperApi()

try: 
    # Details of the current user.
    api_response = api_instance.get_my_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->get_my_user: %s\n" % e)
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

# **remove_api_keys_from_group**
> UpdatedResponse remove_api_keys_from_group(group_id, body)

Remove API keys from a group.

An endpoint for removing API keys from groups.

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
api_instance = iam.DeveloperApi()
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

# **update_my_user**
> UserInfoResp update_my_user(body)

Update user details.

An endpoint for updating the details of the logged in user.

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
api_instance = iam.DeveloperApi()
body = iam.UserUpdateReq() # UserUpdateReq | New attributes for the logged in user.

try: 
    # Update user details.
    api_response = api_instance.update_my_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperApi->update_my_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdateReq**](UserUpdateReq.md)| New attributes for the logged in user. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

