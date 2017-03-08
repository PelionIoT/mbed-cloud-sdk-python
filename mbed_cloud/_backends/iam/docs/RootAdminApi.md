# iam.RootAdminApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account_certificate**](RootAdminApi.md#add_account_certificate) | **POST** /v3/accounts/{accountID}/trusted-certificates | Upload new trusted certificate.
[**add_api_keys_to_account_group**](RootAdminApi.md#add_api_keys_to_account_group) | **POST** /v3/accounts/{accountID}/policy-groups/{groupID}/api-keys | Add API keys to a group.
[**add_subjects_to_account_group**](RootAdminApi.md#add_subjects_to_account_group) | **POST** /v3/accounts/{accountID}/policy-groups/{groupID} | Add members to a group.
[**add_users_to_account_group**](RootAdminApi.md#add_users_to_account_group) | **POST** /v3/accounts/{accountID}/policy-groups/{groupID}/users | Add users to a group.
[**admin_create_account**](RootAdminApi.md#admin_create_account) | **POST** /admin/v3/accounts | Create a new account.
[**admin_delete_account**](RootAdminApi.md#admin_delete_account) | **DELETE** /admin/v3/accounts/{accountID} | Delete an existing account.
[**admin_delete_user**](RootAdminApi.md#admin_delete_user) | **DELETE** /admin/v3/users/{user-id} | Delete a user.
[**admin_get_account_info**](RootAdminApi.md#admin_get_account_info) | **GET** /admin/v3/accounts/{accountID} | Get account info.
[**admin_get_all_accounts**](RootAdminApi.md#admin_get_all_accounts) | **GET** /admin/v3/accounts | Get all accounts.
[**admin_update_account**](RootAdminApi.md#admin_update_account) | **PUT** /admin/v3/accounts/{accountID} | Update attributes of an existing account.
[**change_account_user_password**](RootAdminApi.md#change_account_user_password) | **PUT** /v3/accounts/{accountID}/users/{user-id}/password | Change the password of a user.
[**check_account_user_password**](RootAdminApi.md#check_account_user_password) | **POST** /v3/accounts/{accountID}/users/{user-id}/password | Check the password of a user.
[**create_account**](RootAdminApi.md#create_account) | **POST** /v3/accounts | Create a new account.
[**create_account_api_key**](RootAdminApi.md#create_account_api_key) | **POST** /v3/accounts/{accountID}/api-keys | Create a new API key.
[**create_account_group**](RootAdminApi.md#create_account_group) | **POST** /v3/accounts/{accountID}/policy-groups | Create a new group.
[**create_account_template**](RootAdminApi.md#create_account_template) | **POST** /admin/v3/account-templates | Create a new account template.
[**create_account_user**](RootAdminApi.md#create_account_user) | **POST** /v3/accounts/{accountID}/users | Create a new user.
[**delete_account**](RootAdminApi.md#delete_account) | **DELETE** /v3/accounts/{accountID} | Delete an existing account.
[**delete_account_api_key**](RootAdminApi.md#delete_account_api_key) | **DELETE** /v3/accounts/{accountID}/api-keys/{apiKey} | Delete the API key.
[**delete_account_certificate**](RootAdminApi.md#delete_account_certificate) | **DELETE** /v3/accounts/{accountID}/trusted-certificates/{cert-id} | Delete trusted certificate by ID.
[**delete_account_group**](RootAdminApi.md#delete_account_group) | **DELETE** /v3/accounts/{accountID}/policy-groups/{groupID} | Delete a group.
[**delete_account_template**](RootAdminApi.md#delete_account_template) | **DELETE** /admin/v3/account-templates/{template-id} | Delete account template by ID.
[**delete_account_user**](RootAdminApi.md#delete_account_user) | **DELETE** /v3/accounts/{accountID}/users/{user-id} | Delete a user.
[**get_account_api_key**](RootAdminApi.md#get_account_api_key) | **GET** /v3/accounts/{accountID}/api-keys/{apiKey} | Get API key details.
[**get_account_certificate**](RootAdminApi.md#get_account_certificate) | **GET** /v3/accounts/{accountID}/trusted-certificates/{cert-id} | Get trusted certificate by ID.
[**get_account_group_summary**](RootAdminApi.md#get_account_group_summary) | **GET** /v3/accounts/{accountID}/policy-groups/{groupID} | Get group information.
[**get_account_info**](RootAdminApi.md#get_account_info) | **GET** /v3/accounts/{accountID} | Get account info.
[**get_account_limits**](RootAdminApi.md#get_account_limits) | **GET** /internal/v1/limits/{account-id} | Get limits for account.
[**get_account_template**](RootAdminApi.md#get_account_template) | **GET** /admin/v3/account-templates/{template-id} | Get account template by ID.
[**get_account_user**](RootAdminApi.md#get_account_user) | **GET** /v3/accounts/{accountID}/users/{user-id} | Details of the user.
[**get_admin_options**](RootAdminApi.md#get_admin_options) | **GET** /admin/v3/iam/features | Get admin options.
[**get_all_account_api_keys**](RootAdminApi.md#get_all_account_api_keys) | **GET** /v3/accounts/{accountID}/api-keys | Get all API keys.
[**get_all_account_certificates**](RootAdminApi.md#get_all_account_certificates) | **GET** /v3/accounts/{accountID}/trusted-certificates | Get all trusted certificates.
[**get_all_account_groups**](RootAdminApi.md#get_all_account_groups) | **GET** /v3/accounts/{accountID}/policy-groups | Get all group information.
[**get_all_account_templates**](RootAdminApi.md#get_all_account_templates) | **GET** /admin/v3/account-templates | Get all account templates.
[**get_all_account_users**](RootAdminApi.md#get_all_account_users) | **GET** /v3/accounts/{accountID}/users | Get all user details.
[**get_all_accounts**](RootAdminApi.md#get_all_accounts) | **GET** /v3/accounts | Get all accounts.
[**get_all_accounts_all_api_keys**](RootAdminApi.md#get_all_accounts_all_api_keys) | **GET** /admin/v3/api-keys | Get all API keys from all accounts
[**get_all_accounts_all_users**](RootAdminApi.md#get_all_accounts_all_users) | **GET** /admin/v3/users | Get all users from all accounts
[**get_api_keys_of_account_group**](RootAdminApi.md#get_api_keys_of_account_group) | **GET** /v3/accounts/{accountID}/policy-groups/{groupID}/api-keys | Get API keys of a group.
[**get_users_of_account_group**](RootAdminApi.md#get_users_of_account_group) | **GET** /v3/accounts/{accountID}/policy-groups/{groupID}/users | Get users of a group.
[**manage_account**](RootAdminApi.md#manage_account) | **POST** /v3/accounts/{accountID}/manage | Manage an account.
[**remove_api_keys_from_account_group**](RootAdminApi.md#remove_api_keys_from_account_group) | **DELETE** /v3/accounts/{accountID}/policy-groups/{groupID}/api-keys | Remove API keys from a group.
[**remove_users_from_account_group**](RootAdminApi.md#remove_users_from_account_group) | **DELETE** /v3/accounts/{accountID}/policy-groups/{groupID}/users | Remove users from a group.
[**reset_account_api_key_secret**](RootAdminApi.md#reset_account_api_key_secret) | **POST** /v3/accounts/{accountID}/api-keys/{apiKey}/reset-secret | Reset the secret key.
[**reset_account_user_password**](RootAdminApi.md#reset_account_user_password) | **POST** /v3/accounts/{accountID}/users/{user-id}/reset-password | Reset the user password.
[**update_account_api_key**](RootAdminApi.md#update_account_api_key) | **PUT** /v3/accounts/{accountID}/api-keys/{apiKey} | Update API key details.
[**update_account_certificate**](RootAdminApi.md#update_account_certificate) | **PUT** /v3/accounts/{accountID}/trusted-certificates/{cert-id} | Update trusted certificate.
[**update_account_template**](RootAdminApi.md#update_account_template) | **PUT** /admin/v3/account-templates/{template-id} | Update an existing account template.
[**update_account_user**](RootAdminApi.md#update_account_user) | **PUT** /v3/accounts/{accountID}/users/{user-id} | Update user details.


# **add_account_certificate**
> TrustedCertificateResp add_account_certificate(account_id, body)

Upload new trusted certificate.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
body = iam.TrustedCertificateInternalReq() # TrustedCertificateInternalReq | A trusted certificate object with attributes, signature is optional.

try: 
    # Upload new trusted certificate.
    api_response = api_instance.add_account_certificate(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->add_account_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **body** | [**TrustedCertificateInternalReq**](TrustedCertificateInternalReq.md)| A trusted certificate object with attributes, signature is optional. | 

### Return type

[**TrustedCertificateResp**](TrustedCertificateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_api_keys_to_account_group**
> UpdatedResponse add_api_keys_to_account_group(account_id, group_id, body)

Add API keys to a group.

An endpoint for adding API keys to groups.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.SubjectList() # SubjectList | A list of API keys to be added to the group.

try: 
    # Add API keys to a group.
    api_response = api_instance.add_api_keys_to_account_group(account_id, group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->add_api_keys_to_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **add_subjects_to_account_group**
> UpdatedResponse add_subjects_to_account_group(account_id, group_id, body)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.SubjectList() # SubjectList | A list of users and API keys to be added to the group.

try: 
    # Add members to a group.
    api_response = api_instance.add_subjects_to_account_group(account_id, group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->add_subjects_to_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **add_users_to_account_group**
> UpdatedResponse add_users_to_account_group(account_id, group_id, body)

Add users to a group.

An endpoint for adding users to groups.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.SubjectList() # SubjectList | A list of users to be added to the group.

try: 
    # Add users to a group.
    api_response = api_instance.add_users_to_account_group(account_id, group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->add_users_to_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**| The ID of the group to be updated. | 
 **body** | [**SubjectList**](SubjectList.md)| A list of users to be added to the group. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_create_account**
> AccountCreationResp admin_create_account(body)

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
api_instance = iam.RootAdminApi()
body = iam.AccountCreationReq() # AccountCreationReq | Details of the account to be created.

try: 
    # Create a new account.
    api_response = api_instance.admin_create_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->admin_create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreationReq**](AccountCreationReq.md)| Details of the account to be created. | 

### Return type

[**AccountCreationResp**](AccountCreationResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_account**
> admin_delete_account(account_id)

Delete an existing account.

An endpoint for deleting an account.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | The ID of the account to be deleted.

try: 
    # Delete an existing account.
    api_instance.admin_delete_account(account_id)
except ApiException as e:
    print("Exception when calling RootAdminApi->admin_delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_user**
> admin_delete_user(user_id)

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
api_instance = iam.RootAdminApi()
user_id = 'user_id_example' # str | The ID of the user to be deleted.

try: 
    # Delete a user.
    api_instance.admin_delete_user(user_id)
except ApiException as e:
    print("Exception when calling RootAdminApi->admin_delete_user: %s\n" % e)
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

# **admin_get_account_info**
> AccountInfo admin_get_account_info(account_id)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | The ID or alias of the account to be fetched.

try: 
    # Get account info.
    api_response = api_instance.admin_get_account_info(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->admin_get_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID or alias of the account to be fetched. | 

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_all_accounts**
> AccountInfoList admin_get_all_accounts(status=status, tier=tier, parent=parent, status__eq=status__eq, tier__eq=tier__eq, parent__eq=parent__eq, filter__eq=filter__eq, template__eq=template__eq, limit=limit, after=after)

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
api_instance = iam.RootAdminApi()
status = 'status_example' # str | An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. (optional)
tier = 'tier_example' # str | An optional filter for tier level, must be 0, 1 or omitted. (optional)
parent = 'parent_example' # str | An optional filter for parent account ID. (optional)
status__eq = 'status__eq_example' # str | An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. (optional)
tier__eq = 'tier__eq_example' # str | An optional filter for tier level, must be 0, 1 or omitted. (optional)
parent__eq = 'parent__eq_example' # str | An optional filter for parent account ID. (optional)
filter__eq = 'filter__eq_example' # str | An optional filter for aggregated accounts. Supported: aggregator, subtenant. (optional)
template__eq = 'template__eq_example' # str | An optional filter for account template ID. (optional)
limit = 56 # int | The number of results to return (2-1000). By default, it is unlimited. (optional)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)

try: 
    # Get all accounts.
    api_response = api_instance.admin_get_all_accounts(status=status, tier=tier, parent=parent, status__eq=status__eq, tier__eq=tier__eq, parent__eq=parent__eq, filter__eq=filter__eq, template__eq=template__eq, limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->admin_get_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. | [optional] 
 **tier** | **str**| An optional filter for tier level, must be 0, 1 or omitted. | [optional] 
 **parent** | **str**| An optional filter for parent account ID. | [optional] 
 **status__eq** | **str**| An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. | [optional] 
 **tier__eq** | **str**| An optional filter for tier level, must be 0, 1 or omitted. | [optional] 
 **parent__eq** | **str**| An optional filter for parent account ID. | [optional] 
 **filter__eq** | **str**| An optional filter for aggregated accounts. Supported: aggregator, subtenant. | [optional] 
 **template__eq** | **str**| An optional filter for account template ID. | [optional] 
 **limit** | **int**| The number of results to return (2-1000). By default, it is unlimited. | [optional] 
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 

### Return type

[**AccountInfoList**](AccountInfoList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_account**
> AccountInfo admin_update_account(account_id, body)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | The ID of the account to be updated.
body = iam.AccountUpdateRootReq() # AccountUpdateRootReq | Details of the account to be updated.

try: 
    # Update attributes of an existing account.
    api_response = api_instance.admin_update_account(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->admin_update_account: %s\n" % e)
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

# **change_account_user_password**
> UpdatedResponse change_account_user_password(account_id, user_id, body)

Change the password of a user.

An endpoint for changing the user password. The old password is not checked.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user whose password is changed.
body = iam.PasswordChangeReq() # PasswordChangeReq | New password only.

try: 
    # Change the password of a user.
    api_response = api_instance.change_account_user_password(account_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->change_account_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user whose password is changed. | 
 **body** | [**PasswordChangeReq**](PasswordChangeReq.md)| New password only. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_account_user_password**
> check_account_user_password(account_id, user_id, body)

Check the password of a user.

An endpoint for checking user's current password.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user whose password is checked.
body = iam.PasswordChangeReq() # PasswordChangeReq | Current password only.

try: 
    # Check the password of a user.
    api_instance.check_account_user_password(account_id, user_id, body)
except ApiException as e:
    print("Exception when calling RootAdminApi->check_account_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user whose password is checked. | 
 **body** | [**PasswordChangeReq**](PasswordChangeReq.md)| Current password only. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> AccountCreationResp create_account(body)

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
api_instance = iam.RootAdminApi()
body = iam.AccountCreationReq() # AccountCreationReq | Details of the account to be created.

try: 
    # Create a new account.
    api_response = api_instance.create_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreationReq**](AccountCreationReq.md)| Details of the account to be created. | 

### Return type

[**AccountCreationResp**](AccountCreationResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_api_key**
> ApiKeyInfoResp create_account_api_key(account_id, body)

Create a new API key.

An endpoint for creating a new API key.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
body = iam.ApiKeyInfoReq() # ApiKeyInfoReq | Details of the API key to be created.

try: 
    # Create a new API key.
    api_response = api_instance.create_account_api_key(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->create_account_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **body** | [**ApiKeyInfoReq**](ApiKeyInfoReq.md)| Details of the API key to be created. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_group**
> GroupSummary create_account_group(account_id, body)

Create a new group.

An endpoint for creating a new group.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
body = iam.GroupCreationInfo() # GroupCreationInfo | Details of the group to be created.

try: 
    # Create a new group.
    api_response = api_instance.create_account_group(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->create_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **body** | [**GroupCreationInfo**](GroupCreationInfo.md)| Details of the group to be created. | 

### Return type

[**GroupSummary**](GroupSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_template**
> AccountTemplateResp create_account_template(body)

Create a new account template.

An endpoint for creating a new account template.

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
api_instance = iam.RootAdminApi()
body = iam.AccountTemplateReq() # AccountTemplateReq | Details of the account template to be created.

try: 
    # Create a new account template.
    api_response = api_instance.create_account_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->create_account_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountTemplateReq**](AccountTemplateReq.md)| Details of the account template to be created. | 

### Return type

[**AccountTemplateResp**](AccountTemplateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_user**
> UserInfoResp create_account_user(account_id, body, action=action)

Create a new user.

An endpoint for creating a new user.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
body = iam.UserInfoReq() # UserInfoReq | A user object with attributes.
action = 'create' # str | Create or invite user. (optional) (default to create)

try: 
    # Create a new user.
    api_response = api_instance.create_account_user(account_id, body, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->create_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **body** | [**UserInfoReq**](UserInfoReq.md)| A user object with attributes. | 
 **action** | **str**| Create or invite user. | [optional] [default to create]

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> delete_account(account_id)

Delete an existing account.

An endpoint for deleting an account.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | The ID of the account to be deleted.

try: 
    # Delete an existing account.
    api_instance.delete_account(account_id)
except ApiException as e:
    print("Exception when calling RootAdminApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_api_key**
> delete_account_api_key(account_id, api_key)

Delete the API key.

An endpoint for deleting an API key.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be deleted.

try: 
    # Delete the API key.
    api_instance.delete_account_api_key(account_id, api_key)
except ApiException as e:
    print("Exception when calling RootAdminApi->delete_account_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The ID of the API key to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_certificate**
> delete_account_certificate(account_id, cert_id)

Delete trusted certificate by ID.

An endpoint for deleting the trusted certificate.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be deleted.

try: 
    # Delete trusted certificate by ID.
    api_instance.delete_account_certificate(account_id, cert_id)
except ApiException as e:
    print("Exception when calling RootAdminApi->delete_account_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **cert_id** | **str**| The ID of the trusted certificate to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_group**
> delete_account_group(account_id, group_id)

Delete a group.

An endpoint for deleting a group.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be deleted.

try: 
    # Delete a group.
    api_instance.delete_account_group(account_id, group_id)
except ApiException as e:
    print("Exception when calling RootAdminApi->delete_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**| The ID of the group to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_template**
> delete_account_template(template_id)

Delete account template by ID.

An endpoint for deleting a account template by ID.

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
api_instance = iam.RootAdminApi()
template_id = 'template_id_example' # str | The ID of the account template to be deleted.

try: 
    # Delete account template by ID.
    api_instance.delete_account_template(template_id)
except ApiException as e:
    print("Exception when calling RootAdminApi->delete_account_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the account template to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_user**
> delete_account_user(account_id, user_id)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user to be deleted.

try: 
    # Delete a user.
    api_instance.delete_account_user(account_id, user_id)
except ApiException as e:
    print("Exception when calling RootAdminApi->delete_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_api_key**
> ApiKeyInfoResp get_account_api_key(account_id, api_key)

Get API key details.

An endpoint for retrieving API key details.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be retrieved.

try: 
    # Get API key details.
    api_response = api_instance.get_account_api_key(account_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_account_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The ID of the API key to be retrieved. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_certificate**
> TrustedCertificateInternalResp get_account_certificate(account_id, cert_id)

Get trusted certificate by ID.

An endpoint for retrieving a trusted certificate by ID.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
cert_id = 'cert_id_example' # str | The ID or name of the trusted certificate to be retrieved.

try: 
    # Get trusted certificate by ID.
    api_response = api_instance.get_account_certificate(account_id, cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_account_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **cert_id** | **str**| The ID or name of the trusted certificate to be retrieved. | 

### Return type

[**TrustedCertificateInternalResp**](TrustedCertificateInternalResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_group_summary**
> GroupSummary get_account_group_summary(account_id, group_id)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID or name of the group to be retrieved.

try: 
    # Get group information.
    api_response = api_instance.get_account_group_summary(account_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_account_group_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**| The ID or name of the group to be retrieved. | 

### Return type

[**GroupSummary**](GroupSummary.md)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | The ID or alias of the account to be fetched.
include = 'include_example' # str | Comma separated additional data to return. Currently supported: limits, policies, sub_accounts (optional)

try: 
    # Get account info.
    api_response = api_instance.get_account_info(account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_account_info: %s\n" % e)
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

# **get_account_limits**
> dict(str, str) get_account_limits(account_id)

Get limits for account.

Endpoint for retrieving limits by account ID.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | The ID of the account whose limits to be retrieved.

try: 
    # Get limits for account.
    api_response = api_instance.get_account_limits(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_account_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account whose limits to be retrieved. | 

### Return type

[**dict(str, str)**](dict.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_template**
> AccountTemplateResp get_account_template(template_id)

Get account template by ID.

An endpoint for retrieving a account template by ID.

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
api_instance = iam.RootAdminApi()
template_id = 'template_id_example' # str | The ID of the account template to be retrieved.

try: 
    # Get account template by ID.
    api_response = api_instance.get_account_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_account_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the account template to be retrieved. | 

### Return type

[**AccountTemplateResp**](AccountTemplateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_user**
> UserInfoResp get_account_user(account_id, user_id)

Details of the user.

An endpoint for retrieving details of the user.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID or name of the user to be retrieved.

try: 
    # Details of the user.
    api_response = api_instance.get_account_user(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID or name of the user to be retrieved. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_options**
> list[FeatureOptionsResp] get_admin_options()

Get admin options.

An endpoint for retrieving admin options.

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
api_instance = iam.RootAdminApi()

try: 
    # Get admin options.
    api_response = api_instance.get_admin_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_admin_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FeatureOptionsResp]**](FeatureOptionsResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_api_keys**
> ApiKeyInfoRespList get_all_account_api_keys(account_id, limit=limit, after=after, order=order, include=include, filter=filter, owner=owner, owner__eq=owner__eq)

Get all API keys.

An endpoint for retrieving the API keys in an array, optionally filtered by the owner.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | Filter for the query, for example filter=owner%3Duuid. (optional)
owner = 'owner_example' # str | Owner name filter. (optional)
owner__eq = 'owner__eq_example' # str | Owner name filter. (optional)

try: 
    # Get all API keys.
    api_response = api_instance.get_all_account_api_keys(account_id, limit=limit, after=after, order=order, include=include, filter=filter, owner=owner, owner__eq=owner__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_account_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **filter** | **str**| Filter for the query, for example filter&#x3D;owner%3Duuid. | [optional] 
 **owner** | **str**| Owner name filter. | [optional] 
 **owner__eq** | **str**| Owner name filter. | [optional] 

### Return type

[**ApiKeyInfoRespList**](ApiKeyInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_certificates**
> TrustedCertificateInternalRespList get_all_account_certificates(account_id, limit=limit, after=after, order=order, include=include, filter=filter, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq)

Get all trusted certificates.

An endpoint for retrieving trusted certificates in an array.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | Filter for the query, for example filter=service%3Dlwm2m,expire%3D180,device_execution_mode%3D0. (optional)
service__eq = 'service__eq_example' # str | Filter for service (optional)
expire__eq = 56 # int | Filter for expire (optional)
device_execution_mode__eq = 56 # int | Filter for developer certificates (optional)

try: 
    # Get all trusted certificates.
    api_response = api_instance.get_all_account_certificates(account_id, limit=limit, after=after, order=order, include=include, filter=filter, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_account_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **filter** | **str**| Filter for the query, for example filter&#x3D;service%3Dlwm2m,expire%3D180,device_execution_mode%3D0. | [optional] 
 **service__eq** | **str**| Filter for service | [optional] 
 **expire__eq** | **int**| Filter for expire | [optional] 
 **device_execution_mode__eq** | **int**| Filter for developer certificates | [optional] 

### Return type

[**TrustedCertificateInternalRespList**](TrustedCertificateInternalRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_groups**
> list[GroupSummary] get_all_account_groups(account_id, limit=limit, after=after, order=order, include=include)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get all group information.
    api_response = api_instance.get_all_account_groups(account_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_account_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 

### Return type

[**list[GroupSummary]**](GroupSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_templates**
> AccountTemplateRespList get_all_account_templates(limit=limit, after=after, order=order, include=include, template_type__eq=template_type__eq)

Get all account templates.

An endpoint for retrieving account templates in an array.

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
api_instance = iam.RootAdminApi()
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; default ASC. (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count. (optional)
template_type__eq = 'template_type__eq_example' # str | Filter for Account Template Type. (optional)

try: 
    # Get all account templates.
    api_response = api_instance.get_all_account_templates(limit=limit, after=after, order=order, include=include, template_type__eq=template_type__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_account_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; default ASC. | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count. | [optional] 
 **template_type__eq** | **str**| Filter for Account Template Type. | [optional] 

### Return type

[**AccountTemplateRespList**](AccountTemplateRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_users**
> UserInfoRespList get_all_account_users(account_id, limit=limit, after=after, order=order, include=include, filter=filter, status__eq=status__eq)

Get all user details.

An endpoint for retrieving details of all users.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | Filter for the query, for example filter=status%3Dactive,status%3Dreset. (optional)
status__eq = 'status__eq_example' # str | Filter for status (optional)

try: 
    # Get all user details.
    api_response = api_instance.get_all_account_users(account_id, limit=limit, after=after, order=order, include=include, filter=filter, status__eq=status__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_account_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **filter** | **str**| Filter for the query, for example filter&#x3D;status%3Dactive,status%3Dreset. | [optional] 
 **status__eq** | **str**| Filter for status | [optional] 

### Return type

[**UserInfoRespList**](UserInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> AccountInfoList get_all_accounts(status=status, tier=tier, parent=parent, status__eq=status__eq, tier__eq=tier__eq, parent__eq=parent__eq, limit=limit, after=after, include=include, filter=filter, format=format)

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
api_instance = iam.RootAdminApi()
status = 'status_example' # str | An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. (optional)
tier = 'tier_example' # str | An optional filter for tier level, must be 0, 1 or omitted. (optional)
parent = 'parent_example' # str | An optional filter for parent account ID. (optional)
status__eq = 'status__eq_example' # str | An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. (optional)
tier__eq = 'tier__eq_example' # str | An optional filter for tier level, must be 0, 1 or omitted. (optional)
parent__eq = 'parent__eq_example' # str | An optional filter for parent account ID. (optional)
limit = 56 # int | The number of results to return (2-1000). By default, it is unlimited. (optional)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count,limits (optional)
filter = 'filter_example' # str | Filter for the query, for example filter=tier%3D1, status%3DACTIVE or parent%3D{uuid}. (optional)
format = 'format_example' # str | Format information for the response to the query, supported: format=breakdown. (optional)

try: 
    # Get all accounts.
    api_response = api_instance.get_all_accounts(status=status, tier=tier, parent=parent, status__eq=status__eq, tier__eq=tier__eq, parent__eq=parent__eq, limit=limit, after=after, include=include, filter=filter, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. | [optional] 
 **tier** | **str**| An optional filter for tier level, must be 0, 1 or omitted. | [optional] 
 **parent** | **str**| An optional filter for parent account ID. | [optional] 
 **status__eq** | **str**| An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. | [optional] 
 **tier__eq** | **str**| An optional filter for tier level, must be 0, 1 or omitted. | [optional] 
 **parent__eq** | **str**| An optional filter for parent account ID. | [optional] 
 **limit** | **int**| The number of results to return (2-1000). By default, it is unlimited. | [optional] 
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count,limits | [optional] 
 **filter** | **str**| Filter for the query, for example filter&#x3D;tier%3D1, status%3DACTIVE or parent%3D{uuid}. | [optional] 
 **format** | **str**| Format information for the response to the query, supported: format&#x3D;breakdown. | [optional] 

### Return type

[**AccountInfoList**](AccountInfoList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts_all_api_keys**
> ApiKeyInfoRespList get_all_accounts_all_api_keys(limit=limit, after=after, order=order, include=include, filter=filter, owner=owner, owner__eq=owner__eq)

Get all API keys from all accounts

An endpoint for retrieving API keys from all accounts.

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
api_instance = iam.RootAdminApi()
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | A filter for the query, for example filter=owner%3Duuid. (optional)
owner = 'owner_example' # str | Owner name filter. (optional)
owner__eq = 'owner__eq_example' # str | Owner name filter. (optional)

try: 
    # Get all API keys from all accounts
    api_response = api_instance.get_all_accounts_all_api_keys(limit=limit, after=after, order=order, include=include, filter=filter, owner=owner, owner__eq=owner__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_accounts_all_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **filter** | **str**| A filter for the query, for example filter&#x3D;owner%3Duuid. | [optional] 
 **owner** | **str**| Owner name filter. | [optional] 
 **owner__eq** | **str**| Owner name filter. | [optional] 

### Return type

[**ApiKeyInfoRespList**](ApiKeyInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts_all_users**
> UserInfoRespList get_all_accounts_all_users(limit=limit, after=after, order=order, include=include, filter=filter, status__eq=status__eq)

Get all users from all accounts

Endpoint for retrieving user info from all accounts

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
api_instance = iam.RootAdminApi()
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | Filter for the query, for example filter=status%3Dactive,status%3Dreset. (optional)
status__eq = 'status__eq_example' # str | Filter for status, for example active or reset (optional)

try: 
    # Get all users from all accounts
    api_response = api_instance.get_all_accounts_all_users(limit=limit, after=after, order=order, include=include, filter=filter, status__eq=status__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_all_accounts_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **filter** | **str**| Filter for the query, for example filter&#x3D;status%3Dactive,status%3Dreset. | [optional] 
 **status__eq** | **str**| Filter for status, for example active or reset | [optional] 

### Return type

[**UserInfoRespList**](UserInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_of_account_group**
> ApiKeyInfoRespList get_api_keys_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include)

Get API keys of a group.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group whose API keys are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get API keys of a group.
    api_response = api_instance.get_api_keys_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_api_keys_of_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **get_users_of_account_group**
> UserInfoRespList get_users_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include)

Get users of a group.

An endpoint for listing users of the group with details.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group whose users are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get users of a group.
    api_response = api_instance.get_users_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->get_users_of_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **manage_account**
> UpdatedResponse manage_account(account_id, status=status, tier=tier, is_provisioning_allowed=is_provisioning_allowed)

Manage an account.

This endpoint upgrades the account from free tier to commercial, sets the new status.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | The ID of the account to be updated.
status = 'status_example' # str | New status of the account; ACTIVE, RESTRICTED or SUSPENDED (optional)
tier = 'tier_example' # str | New tier level of the account; '0': free tier, '1': commercial account. Other values are reserved for the future. (optional)
is_provisioning_allowed = 'is_provisioning_allowed_example' # str | A flag indicating whether Factory Tool is permitted to be downloaded or not, true or false. (optional)

try: 
    # Manage an account.
    api_response = api_instance.manage_account(account_id, status=status, tier=tier, is_provisioning_allowed=is_provisioning_allowed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->manage_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be updated. | 
 **status** | **str**| New status of the account; ACTIVE, RESTRICTED or SUSPENDED | [optional] 
 **tier** | **str**| New tier level of the account; &#39;0&#39;: free tier, &#39;1&#39;: commercial account. Other values are reserved for the future. | [optional] 
 **is_provisioning_allowed** | **str**| A flag indicating whether Factory Tool is permitted to be downloaded or not, true or false. | [optional] 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_api_keys_from_account_group**
> UpdatedResponse remove_api_keys_from_account_group(account_id, group_id, body=body)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | A list of API keys to be removed from the group.
body = iam.SubjectList() # SubjectList |  (optional)

try: 
    # Remove API keys from a group.
    api_response = api_instance.remove_api_keys_from_account_group(account_id, group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->remove_api_keys_from_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**| A list of API keys to be removed from the group. | 
 **body** | [**SubjectList**](SubjectList.md)|  | [optional] 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_users_from_account_group**
> UpdatedResponse remove_users_from_account_group(account_id, group_id, body=body)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | 
body = iam.SubjectList() # SubjectList |  (optional)

try: 
    # Remove users from a group.
    api_response = api_instance.remove_users_from_account_group(account_id, group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->remove_users_from_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**|  | 
 **body** | [**SubjectList**](SubjectList.md)|  | [optional] 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_account_api_key_secret**
> ApiKeyInfoResp reset_account_api_key_secret(account_id, api_key)

Reset the secret key.

An endpoint for resetting the secret key of the API key.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be reset.

try: 
    # Reset the secret key.
    api_response = api_instance.reset_account_api_key_secret(account_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->reset_account_api_key_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The ID of the API key to be reset. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_account_user_password**
> UserInfoResp reset_account_user_password(account_id, user_id)

Reset the user password.

An endpoint for resetting the user password. The new password will visible in the response.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user whose password is reset.

try: 
    # Reset the user password.
    api_response = api_instance.reset_account_user_password(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->reset_account_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user whose password is reset. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_api_key**
> ApiKeyInfoResp update_account_api_key(account_id, api_key, body)

Update API key details.

An endpoint for updating API key details.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be updated.
body = iam.RootAdminApiKeyUpdateReq() # RootAdminApiKeyUpdateReq | New API key attributes to be stored.

try: 
    # Update API key details.
    api_response = api_instance.update_account_api_key(account_id, api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->update_account_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The ID of the API key to be updated. | 
 **body** | [**RootAdminApiKeyUpdateReq**](RootAdminApiKeyUpdateReq.md)| New API key attributes to be stored. | 

### Return type

[**ApiKeyInfoResp**](ApiKeyInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_certificate**
> TrustedCertificateInternalResp update_account_certificate(account_id, cert_id, body)

Update trusted certificate.

An endpoint for updating existing trusted certificates.

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be updated.
body = iam.TrustedCertificateReq() # TrustedCertificateReq | A trusted certificate object with attributes.

try: 
    # Update trusted certificate.
    api_response = api_instance.update_account_certificate(account_id, cert_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->update_account_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **cert_id** | **str**| The ID of the trusted certificate to be updated. | 
 **body** | [**TrustedCertificateReq**](TrustedCertificateReq.md)| A trusted certificate object with attributes. | 

### Return type

[**TrustedCertificateInternalResp**](TrustedCertificateInternalResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_template**
> AccountTemplateResp update_account_template(template_id, body)

Update an existing account template.

An endpoint for updating an existing account template.

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
api_instance = iam.RootAdminApi()
template_id = 'template_id_example' # str | The ID of the account template to be updated.
body = iam.AccountTemplateReq() # AccountTemplateReq | Details of the account template to be updated.

try: 
    # Update an existing account template.
    api_response = api_instance.update_account_template(template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->update_account_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the account template to be updated. | 
 **body** | [**AccountTemplateReq**](AccountTemplateReq.md)| Details of the account template to be updated. | 

### Return type

[**AccountTemplateResp**](AccountTemplateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_user**
> UserInfoResp update_account_user(account_id, user_id, body)

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
api_instance = iam.RootAdminApi()
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user to be updated.
body = iam.RootAdminUserUpdateReq() # RootAdminUserUpdateReq | A rootadmin user object with attributes.

try: 
    # Update user details.
    api_response = api_instance.update_account_user(account_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootAdminApi->update_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user to be updated. | 
 **body** | [**RootAdminUserUpdateReq**](RootAdminUserUpdateReq.md)| A rootadmin user object with attributes. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

