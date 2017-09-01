# iam.AccountAdminApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_certificate**](AccountAdminApi.md#add_certificate) | **POST** /v3/trusted-certificates | Upload a new trusted certificate.
[**add_subjects_to_group**](AccountAdminApi.md#add_subjects_to_group) | **POST** /v3/policy-groups/{groupID} | Add members to a group.
[**create_account**](AccountAdminApi.md#create_account) | **POST** /v3/accounts | Create a new account.
[**create_user**](AccountAdminApi.md#create_user) | **POST** /v3/users | Create a new user.
[**delete_user**](AccountAdminApi.md#delete_user) | **DELETE** /v3/users/{user-id} | Delete a user.
[**get_account_info**](AccountAdminApi.md#get_account_info) | **GET** /v3/accounts/{accountID} | Get account info.
[**get_all_accounts**](AccountAdminApi.md#get_all_accounts) | **GET** /v3/accounts | Get all accounts.
[**get_all_users**](AccountAdminApi.md#get_all_users) | **GET** /v3/users | Get the details of all users.
[**get_user**](AccountAdminApi.md#get_user) | **GET** /v3/users/{user-id} | Details of a user.
[**get_users_of_group**](AccountAdminApi.md#get_users_of_group) | **GET** /v3/policy-groups/{groupID}/users | Get users of a group.
[**remove_users_from_group**](AccountAdminApi.md#remove_users_from_group) | **DELETE** /v3/policy-groups/{groupID}/users | Remove users from a group.
[**update_account**](AccountAdminApi.md#update_account) | **PUT** /v3/accounts/{accountID} | Update attributes of an existing account.
[**update_my_account**](AccountAdminApi.md#update_my_account) | **PUT** /v3/accounts/me | Updates attributes of the account.
[**update_user**](AccountAdminApi.md#update_user) | **PUT** /v3/users/{user-id} | Update user details.


# **add_certificate**
> TrustedCertificateResp add_certificate(body)

Upload a new trusted certificate.

An endpoint for uploading new trusted certificates.

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
api_instance = iam.AccountAdminApi()
body = iam.TrustedCertificateReq() # TrustedCertificateReq | A trusted certificate object with attributes.

try: 
    # Upload a new trusted certificate.
    api_response = api_instance.add_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->add_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrustedCertificateReq**](TrustedCertificateReq.md)| A trusted certificate object with attributes. | 

### Return type

[**TrustedCertificateResp**](TrustedCertificateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_subjects_to_group**
> UpdatedResponse add_subjects_to_group(group_id, body)

Add members to a group.

An endpoint for adding users and API keys to groups.

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
api_instance = iam.AccountAdminApi()
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.SubjectList() # SubjectList | A list of users and API keys to be added to the group.

try: 
    # Add members to a group.
    api_response = api_instance.add_subjects_to_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->add_subjects_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group to be updated. | 
 **body** | [**SubjectList**](SubjectList.md)| A list of users and API keys to be added to the group. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> AccountCreationResp create_account(body, action=action)

Create a new account.

An endpoint for creating a new account.

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
api_instance = iam.AccountAdminApi()
body = iam.AccountCreationReq() # AccountCreationReq | Details of the account to be created.
action = 'create' # str | Action, either 'create' or 'enroll'. (optional) (default to create)

try: 
    # Create a new account.
    api_response = api_instance.create_account(body, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreationReq**](AccountCreationReq.md)| Details of the account to be created. | 
 **action** | **str**| Action, either &#39;create&#39; or &#39;enroll&#39;. | [optional] [default to create]

### Return type

[**AccountCreationResp**](AccountCreationResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserInfoResp create_user(body, action=action)

Create a new user.

An endpoint for creating or inviting a new user to the account. In case of invitation email address is used only, other attributes are set in the 2nd step.

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
api_instance = iam.AccountAdminApi()
body = iam.UserCreationReq() # UserCreationReq | A user object with attributes.
action = 'create' # str | Action, either 'create' or 'invite'. (optional) (default to create)

try: 
    # Create a new user.
    api_response = api_instance.create_user(body, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreationReq**](UserCreationReq.md)| A user object with attributes. | 
 **action** | **str**| Action, either &#39;create&#39; or &#39;invite&#39;. | [optional] [default to create]

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete a user.

An endpoint for deleting a user.

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
api_instance = iam.AccountAdminApi()
user_id = 'user_id_example' # str | The ID of the user to be deleted.

try: 
    # Delete a user.
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling AccountAdminApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_info**
> AccountInfo get_account_info(account_id, include=include)

Get account info.

Returns detailed information about the account.

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
api_instance = iam.AccountAdminApi()
account_id = 'account_id_example' # str | The ID or alias of the account to be fetched.
include = 'include_example' # str | Comma separated additional data to return. Currently supported: limits, policies, sub_accounts (optional)

try: 
    # Get account info.
    api_response = api_instance.get_account_info(account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID or alias of the account to be fetched. | 
 **include** | **str**| Comma separated additional data to return. Currently supported: limits, policies, sub_accounts | [optional] 

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> AccountInfoList get_all_accounts(status__eq=status__eq, tier__eq=tier__eq, parent__eq=parent__eq, end_market__eq=end_market__eq, limit=limit, after=after, include=include, format=format)

Get all accounts.

Returns an array of account objects, optionally filtered by status and tier level.

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
api_instance = iam.AccountAdminApi()
status__eq = 'status__eq_example' # str | An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. (optional)
tier__eq = 'tier__eq_example' # str | An optional filter for tier level, must be 0, 1 or omitted. (optional)
parent__eq = 'parent__eq_example' # str | An optional filter for parent account ID. (optional)
end_market__eq = 'end_market__eq_example' # str | An optional filter for account end market. (optional)
limit = 1000 # int | The number of results to return (2-1000), default is 1000. (optional) (default to 1000)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count,limits (optional)
format = 'format_example' # str | Format information for the response to the query, supported: format=breakdown. (optional)

try: 
    # Get all accounts.
    api_response = api_instance.get_all_accounts(status__eq=status__eq, tier__eq=tier__eq, parent__eq=parent__eq, end_market__eq=end_market__eq, limit=limit, after=after, include=include, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status__eq** | **str**| An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. | [optional] 
 **tier__eq** | **str**| An optional filter for tier level, must be 0, 1 or omitted. | [optional] 
 **parent__eq** | **str**| An optional filter for parent account ID. | [optional] 
 **end_market__eq** | **str**| An optional filter for account end market. | [optional] 
 **limit** | **int**| The number of results to return (2-1000), default is 1000. | [optional] [default to 1000]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count,limits | [optional] 
 **format** | **str**| Format information for the response to the query, supported: format&#x3D;breakdown. | [optional] 

### Return type

[**AccountInfoList**](AccountInfoList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> UserInfoRespList get_all_users(limit=limit, after=after, order=order, include=include, status__eq=status__eq)

Get the details of all users.

An endpoint for retrieving the details of all users.

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
api_instance = iam.AccountAdminApi()
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
status__eq = 'status__eq_example' # str | Filter for status, for example active or reset (optional)

try: 
    # Get the details of all users.
    api_response = api_instance.get_all_users(limit=limit, after=after, order=order, include=include, status__eq=status__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **status__eq** | **str**| Filter for status, for example active or reset | [optional] 

### Return type

[**UserInfoRespList**](UserInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserInfoResp get_user(user_id)

Details of a user.

An endpoint for retrieving the details of a user.

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
api_instance = iam.AccountAdminApi()
user_id = 'user_id_example' # str | The ID or name of the user whose details are retrieved.

try: 
    # Details of a user.
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID or name of the user whose details are retrieved. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_of_group**
> UserInfoRespList get_users_of_group(group_id, limit=limit, after=after, order=order, include=include)

Get users of a group.

An endpoint for listing the users of a group with details.

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
api_instance = iam.AccountAdminApi()
group_id = 'group_id_example' # str | The ID of the group whose users are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get users of a group.
    api_response = api_instance.get_users_of_group(group_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_users_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group whose users are retrieved. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 

### Return type

[**UserInfoRespList**](UserInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_users_from_group**
> UpdatedResponse remove_users_from_group(group_id, body)

Remove users from a group.

An endpoint for removing users from groups.

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
api_instance = iam.AccountAdminApi()
group_id = 'group_id_example' # str | The ID of the group whose users are removed.
body = iam.SubjectList() # SubjectList | A list of users to be removed from the group.

try: 
    # Remove users from a group.
    api_response = api_instance.remove_users_from_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->remove_users_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group whose users are removed. | 
 **body** | [**SubjectList**](SubjectList.md)| A list of users to be removed from the group. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> AccountInfo update_account(account_id, body)

Update attributes of an existing account.

An endpoint for updating an account.

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
api_instance = iam.AccountAdminApi()
account_id = 'account_id_example' # str | The ID of the account to be updated.
body = iam.AccountUpdateRootReq() # AccountUpdateRootReq | Details of the account to be updated.

try: 
    # Update attributes of an existing account.
    api_response = api_instance.update_account(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be updated. | 
 **body** | [**AccountUpdateRootReq**](AccountUpdateRootReq.md)| Details of the account to be updated. | 

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_account**
> AccountInfo update_my_account(body)

Updates attributes of the account.

An endpoint for updating the account. Example usage: curl -X PUT https://api.us-east-1.mbedcloud.com/v3/accounts/me -d '{\"phone_number\": \"12345678\"}' -H 'content-type: application/json' -H 'Authorization: Bearer AUTH_TOKEN' 

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
api_instance = iam.AccountAdminApi()
body = iam.AccountUpdateReq() # AccountUpdateReq | Details of the account to be updated.

try: 
    # Updates attributes of the account.
    api_response = api_instance.update_my_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->update_my_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountUpdateReq**](AccountUpdateReq.md)| Details of the account to be updated. | 

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserInfoResp update_user(user_id, body)

Update user details.

An endpoint for updating user details.

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
api_instance = iam.AccountAdminApi()
user_id = 'user_id_example' # str | The ID of the user whose details are updated.
body = iam.UserUpdateReq() # UserUpdateReq | A user object with attributes.

try: 
    # Update user details.
    api_response = api_instance.update_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose details are updated. | 
 **body** | [**UserUpdateReq**](UserUpdateReq.md)| A user object with attributes. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

