# iam.AggregatorAccountAdminApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account_api_key_to_groups**](AggregatorAccountAdminApi.md#add_account_api_key_to_groups) | **POST** /v3/accounts/{accountID}/api-keys/{apiKey}/groups | Add API key to a list of groups.
[**add_account_certificate**](AggregatorAccountAdminApi.md#add_account_certificate) | **POST** /v3/accounts/{accountID}/trusted-certificates | Upload new trusted certificate.
[**add_account_user_to_groups**](AggregatorAccountAdminApi.md#add_account_user_to_groups) | **POST** /v3/accounts/{accountID}/users/{user-id}/groups | Add user to a list of groups.
[**add_subjects_to_account_group**](AggregatorAccountAdminApi.md#add_subjects_to_account_group) | **POST** /v3/accounts/{accountID}/policy-groups/{groupID} | Add members to a group.
[**check_account_api_key**](AggregatorAccountAdminApi.md#check_account_api_key) | **POST** /v3/accounts/{accountID}/api-keys/{apiKey} | Check the API key.
[**create_account**](AggregatorAccountAdminApi.md#create_account) | **POST** /v3/accounts | Create a new account.
[**create_account_api_key**](AggregatorAccountAdminApi.md#create_account_api_key) | **POST** /v3/accounts/{accountID}/api-keys | Create a new API key.
[**create_account_group**](AggregatorAccountAdminApi.md#create_account_group) | **POST** /v3/accounts/{accountID}/policy-groups | Create a new group.
[**create_account_invitation**](AggregatorAccountAdminApi.md#create_account_invitation) | **POST** /v3/accounts/{account-id}/user-invitations | Create a user invitation.
[**create_account_user**](AggregatorAccountAdminApi.md#create_account_user) | **POST** /v3/accounts/{accountID}/users | Create a new user.
[**delete_account_api_key**](AggregatorAccountAdminApi.md#delete_account_api_key) | **DELETE** /v3/accounts/{accountID}/api-keys/{apiKey} | Delete the API key.
[**delete_account_certificate**](AggregatorAccountAdminApi.md#delete_account_certificate) | **DELETE** /v3/accounts/{accountID}/trusted-certificates/{cert-id} | Delete trusted certificate by ID.
[**delete_account_group**](AggregatorAccountAdminApi.md#delete_account_group) | **DELETE** /v3/accounts/{accountID}/policy-groups/{groupID} | Delete a group.
[**delete_account_invitation**](AggregatorAccountAdminApi.md#delete_account_invitation) | **DELETE** /v3/accounts/{account-id}/user-invitations/{invitation-id} | Delete a user invitation.
[**delete_account_user**](AggregatorAccountAdminApi.md#delete_account_user) | **DELETE** /v3/accounts/{accountID}/users/{user-id} | Delete a user.
[**get_account_api_key**](AggregatorAccountAdminApi.md#get_account_api_key) | **GET** /v3/accounts/{accountID}/api-keys/{apiKey} | Get API key details.
[**get_account_certificate**](AggregatorAccountAdminApi.md#get_account_certificate) | **GET** /v3/accounts/{accountID}/trusted-certificates/{cert-id} | Get trusted certificate by ID.
[**get_account_group_summary**](AggregatorAccountAdminApi.md#get_account_group_summary) | **GET** /v3/accounts/{accountID}/policy-groups/{groupID} | Get group information.
[**get_account_info**](AggregatorAccountAdminApi.md#get_account_info) | **GET** /v3/accounts/{accountID} | Get account info.
[**get_account_invitation**](AggregatorAccountAdminApi.md#get_account_invitation) | **GET** /v3/accounts/{account-id}/user-invitations/{invitation-id} | Details of a user invitation.
[**get_account_user**](AggregatorAccountAdminApi.md#get_account_user) | **GET** /v3/accounts/{accountID}/users/{user-id} | Details of the user.
[**get_all_account_api_keys**](AggregatorAccountAdminApi.md#get_all_account_api_keys) | **GET** /v3/accounts/{accountID}/api-keys | Get all API keys.
[**get_all_account_certificates**](AggregatorAccountAdminApi.md#get_all_account_certificates) | **GET** /v3/accounts/{accountID}/trusted-certificates | Get all trusted certificates.
[**get_all_account_groups**](AggregatorAccountAdminApi.md#get_all_account_groups) | **GET** /v3/accounts/{accountID}/policy-groups | Get all group information.
[**get_all_account_invitations**](AggregatorAccountAdminApi.md#get_all_account_invitations) | **GET** /v3/accounts/{account-id}/user-invitations | Get the details of all the user invitations.
[**get_all_account_users**](AggregatorAccountAdminApi.md#get_all_account_users) | **GET** /v3/accounts/{accountID}/users | Get all user details.
[**get_all_accounts**](AggregatorAccountAdminApi.md#get_all_accounts) | **GET** /v3/accounts | Get all accounts.
[**get_api_keys_of_account_group**](AggregatorAccountAdminApi.md#get_api_keys_of_account_group) | **GET** /v3/accounts/{accountID}/policy-groups/{groupID}/api-keys | Get API keys of a group.
[**get_groups_of_account_apikey**](AggregatorAccountAdminApi.md#get_groups_of_account_apikey) | **GET** /v3/accounts/{accountID}/api-keys/{apiKey}/groups | Get groups of the API key.
[**get_groups_of_account_user**](AggregatorAccountAdminApi.md#get_groups_of_account_user) | **GET** /v3/accounts/{accountID}/users/{user-id}/groups | Get groups of the user.
[**get_users_of_account_group**](AggregatorAccountAdminApi.md#get_users_of_account_group) | **GET** /v3/accounts/{accountID}/policy-groups/{groupID}/users | Get users of a group.
[**remove_account_api_key_from_groups**](AggregatorAccountAdminApi.md#remove_account_api_key_from_groups) | **DELETE** /v3/accounts/{accountID}/api-keys/{apiKey}/groups | Remove API key from groups.
[**remove_account_user_from_groups**](AggregatorAccountAdminApi.md#remove_account_user_from_groups) | **DELETE** /v3/accounts/{accountID}/users/{user-id}/groups | Remove user from groups.
[**remove_api_keys_from_account_group**](AggregatorAccountAdminApi.md#remove_api_keys_from_account_group) | **DELETE** /v3/accounts/{accountID}/policy-groups/{groupID}/api-keys | Remove API keys from a group.
[**remove_users_from_account_group**](AggregatorAccountAdminApi.md#remove_users_from_account_group) | **DELETE** /v3/accounts/{accountID}/policy-groups/{groupID}/users | Remove users from a group.
[**reset_account_api_key_secret**](AggregatorAccountAdminApi.md#reset_account_api_key_secret) | **POST** /v3/accounts/{accountID}/api-keys/{apiKey}/reset-secret | Reset the secret key.
[**update_account**](AggregatorAccountAdminApi.md#update_account) | **PUT** /v3/accounts/{accountID} | Update attributes of an existing account.
[**update_account_api_key**](AggregatorAccountAdminApi.md#update_account_api_key) | **PUT** /v3/accounts/{accountID}/api-keys/{apiKey} | Update API key details.
[**update_account_certificate**](AggregatorAccountAdminApi.md#update_account_certificate) | **PUT** /v3/accounts/{accountID}/trusted-certificates/{cert-id} | Update trusted certificate.
[**update_account_group_name**](AggregatorAccountAdminApi.md#update_account_group_name) | **PUT** /v3/accounts/{accountID}/policy-groups/{groupID} | Update the group name.
[**update_account_user**](AggregatorAccountAdminApi.md#update_account_user) | **PUT** /v3/accounts/{accountID}/users/{user-id} | Update user details.
[**validate_account_user_email**](AggregatorAccountAdminApi.md#validate_account_user_email) | **POST** /v3/accounts/{accountID}/users/{user-id}/validate-email | Validate the user email.


# **add_account_api_key_to_groups**
> UpdatedResponse add_account_api_key_to_groups(account_id, api_key, body)

Add API key to a list of groups.

An endpoint for adding API key to groups.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apikey}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be added to the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Add API key to a list of groups.
    api_response = api_instance.add_account_api_key_to_groups(account_id, api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->add_account_api_key_to_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The ID of the API key to be added to the group. | 
 **body** | **list[str]**| A list of IDs of the groups to be updated. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_account_certificate**
> TrustedCertificateResp add_account_certificate(account_id, body)

Upload new trusted certificate.

An endpoint for uploading new trusted certificates.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/trusted-certificates -d {\"name\": \"myCert1\", \"description\": \"very important cert\", \"certificate\": \"certificate_data\", \"service\": \"lwm2m\"} -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
body = iam.TrustedCertificateRootReq() # TrustedCertificateRootReq | A trusted certificate object with attributes, signature is optional.

try: 
    # Upload new trusted certificate.
    api_response = api_instance.add_account_certificate(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->add_account_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **body** | [**TrustedCertificateRootReq**](TrustedCertificateRootReq.md)| A trusted certificate object with attributes, signature is optional. | 

### Return type

[**TrustedCertificateResp**](TrustedCertificateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_account_user_to_groups**
> UpdatedResponse add_account_user_to_groups(account_id, user_id, body)

Add user to a list of groups.

An endpoint for adding user to groups.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user to be added to the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Add user to a list of groups.
    api_response = api_instance.add_account_user_to_groups(account_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->add_account_user_to_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user to be added to the group. | 
 **body** | **list[str]**| A list of IDs of the groups to be updated. | 

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

An endpoint for adding users and API keys to groups.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID} -d '{\"users\": [0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.SubjectList() # SubjectList | A list of users and API keys to be added to the group.

try: 
    # Add members to a group.
    api_response = api_instance.add_subjects_to_account_group(account_id, group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->add_subjects_to_account_group: %s\n" % e)
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

# **check_account_api_key**
> check_account_api_key(account_id, api_key)

Check the API key.

An endpoint for checking API key.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apiKey} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The API key to be checked.

try: 
    # Check the API key.
    api_instance.check_account_api_key(account_id, api_key)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->check_account_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The API key to be checked. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> AccountCreationResp create_account(body, action=action)

Create a new account.

An endpoint for creating a new account.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts -d '{\"display_name\": \"MyAccount1\", \"admin_name\": \"accountAdmin1\", \"email\": \"example_admin@myaccount.info\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
body = iam.AccountCreationReq() # AccountCreationReq | Details of the account to be created.
action = 'create' # str | Action, either 'create' or 'enroll'. <ul><li>'create' creates the account where its admin user has ACTIVE status if admin_password was defined in the request, or RESET status if no admin_password was defined. If the user already exists, its status is not modified. </li><li>'enroll' creates the account where its admin user has ENROLLING status. If the user already exists, its status is not modified. Email to finish the enrollment or to notify the existing user about the new account is sent to the admin_email defined in the request. </li></ul> (optional) (default to create)

try: 
    # Create a new account.
    api_response = api_instance.create_account(body, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreationReq**](AccountCreationReq.md)| Details of the account to be created. | 
 **action** | **str**| Action, either &#39;create&#39; or &#39;enroll&#39;. &lt;ul&gt;&lt;li&gt;&#39;create&#39; creates the account where its admin user has ACTIVE status if admin_password was defined in the request, or RESET status if no admin_password was defined. If the user already exists, its status is not modified. &lt;/li&gt;&lt;li&gt;&#39;enroll&#39; creates the account where its admin user has ENROLLING status. If the user already exists, its status is not modified. Email to finish the enrollment or to notify the existing user about the new account is sent to the admin_email defined in the request. &lt;/li&gt;&lt;/ul&gt; | [optional] [default to create]

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

An endpoint for creating a new API key. There is no default value for the owner ID and it must be from the same account where the new API key is created.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys -d '{\"name\": \"MyKey1\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
body = iam.ApiKeyInfoReq() # ApiKeyInfoReq | Details of the API key to be created.

try: 
    # Create a new API key.
    api_response = api_instance.create_account_api_key(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->create_account_api_key: %s\n" % e)
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

An endpoint for creating a new group.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups -d '{\"name\": \"MyGroup1\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
body = iam.GroupCreationInfo() # GroupCreationInfo | Details of the group to be created.

try: 
    # Create a new group.
    api_response = api_instance.create_account_group(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->create_account_group: %s\n" % e)
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

# **create_account_invitation**
> UserInvitationResp create_account_invitation(account_id, body)

Create a user invitation.

An endpoint for inviting a new or an existing user to join the account.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accouns/{account-id}/user-invitations -d {\"email\": \"myemail@company.com\"} -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
body = iam.UserInvitationReq() # UserInvitationReq | A user invitation object with attributes.

try: 
    # Create a user invitation.
    api_response = api_instance.create_account_invitation(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->create_account_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **body** | [**UserInvitationReq**](UserInvitationReq.md)| A user invitation object with attributes. | 

### Return type

[**UserInvitationResp**](UserInvitationResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_user**
> UserInfoResp create_account_user(account_id, body, action=action)

Create a new user.

An endpoint for creating or inviting a new user to the account. In case of invitation email address is used only, other attributes are set in the 2nd step.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users -d {\"email\": \"myemail@company.com\"} -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
body = iam.UserInfoReq() # UserInfoReq | A user object with attributes.
action = 'create' # str | Create or invite user. (optional) (default to create)

try: 
    # Create a new user.
    api_response = api_instance.create_account_user(account_id, body, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->create_account_user: %s\n" % e)
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

# **delete_account_api_key**
> delete_account_api_key(account_id, api_key)

Delete the API key.

An endpoint for deleting an API key.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apikey} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be deleted.

try: 
    # Delete the API key.
    api_instance.delete_account_api_key(account_id, api_key)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->delete_account_api_key: %s\n" % e)
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

An endpoint for deleting the trusted certificate.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/trusted-certificates/{cert-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be deleted.

try: 
    # Delete trusted certificate by ID.
    api_instance.delete_account_certificate(account_id, cert_id)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->delete_account_certificate: %s\n" % e)
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

An endpoint for deleting a group.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be deleted.

try: 
    # Delete a group.
    api_instance.delete_account_group(account_id, group_id)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->delete_account_group: %s\n" % e)
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

# **delete_account_invitation**
> delete_account_invitation(account_id, invitation_id)

Delete a user invitation.

An endpoint for deleting an active user invitation which has been sent for a new or an existing user to join the account.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{account-id}/user-invitations/{invitation-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
invitation_id = 'invitation_id_example' # str | The ID of the invitation to be deleted.

try: 
    # Delete a user invitation.
    api_instance.delete_account_invitation(account_id, invitation_id)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->delete_account_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **invitation_id** | **str**| The ID of the invitation to be deleted. | 

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

An endpoint for deleting a user.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user to be deleted.

try: 
    # Delete a user.
    api_instance.delete_account_user(account_id, user_id)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->delete_account_user: %s\n" % e)
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

An endpoint for retrieving API key details.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apiKey} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be retrieved.

try: 
    # Get API key details.
    api_response = api_instance.get_account_api_key(account_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_account_api_key: %s\n" % e)
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

An endpoint for retrieving a trusted certificate by ID.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/trusted-certificates/{cert-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be retrieved.

try: 
    # Get trusted certificate by ID.
    api_response = api_instance.get_account_certificate(account_id, cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_account_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **cert_id** | **str**| The ID of the trusted certificate to be retrieved. | 

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

An endpoint for getting general information about the group.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be retrieved.

try: 
    # Get group information.
    api_response = api_instance.get_account_group_summary(account_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_account_group_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**| The ID of the group to be retrieved. | 

### Return type

[**GroupSummary**](GroupSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_info**
> AccountInfo get_account_info(account_id, include=include, properties=properties)

Get account info.

Returns detailed information about the account.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{account-id} -H 'Authorization: Bearer API_KEY'`.

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | The ID of the account to be fetched.
include = 'include_example' # str | Comma separated additional data to return. Currently supported: limits, policies, sub_accounts (optional)
properties = 'properties_example' # str | Property name to be returned from account specific properties. (optional)

try: 
    # Get account info.
    api_response = api_instance.get_account_info(account_id, include=include, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be fetched. | 
 **include** | **str**| Comma separated additional data to return. Currently supported: limits, policies, sub_accounts | [optional] 
 **properties** | **str**| Property name to be returned from account specific properties. | [optional] 

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_invitation**
> UserInvitationResp get_account_invitation(account_id, invitation_id)

Details of a user invitation.

An endpoint for retrieving the details of an active user invitation sent for a new or an existing user to join the account.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{account-id}/user-invitations/{invitation-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
invitation_id = 'invitation_id_example' # str | The ID of the invitation to be retrieved.

try: 
    # Details of a user invitation.
    api_response = api_instance.get_account_invitation(account_id, invitation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_account_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **invitation_id** | **str**| The ID of the invitation to be retrieved. | 

### Return type

[**UserInvitationResp**](UserInvitationResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_user**
> UserInfoResp get_account_user(account_id, user_id)

Details of the user.

An endpoint for retrieving details of the user.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{userID} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user to be retrieved.

try: 
    # Details of the user.
    api_response = api_instance.get_account_user(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user to be retrieved. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_api_keys**
> ApiKeyInfoRespList get_all_account_api_keys(account_id, limit=limit, after=after, order=order, include=include, key__eq=key__eq, owner__eq=owner__eq)

Get all API keys.

An endpoint for retrieving the API keys in an array, optionally filtered by the owner.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
key__eq = 'key__eq_example' # str | API key filter. (optional)
owner__eq = 'owner__eq_example' # str | Owner name filter. (optional)

try: 
    # Get all API keys.
    api_response = api_instance.get_all_account_api_keys(account_id, limit=limit, after=after, order=order, include=include, key__eq=key__eq, owner__eq=owner__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_all_account_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **get_all_account_certificates**
> TrustedCertificateInternalRespList get_all_account_certificates(account_id, limit=limit, after=after, order=order, include=include, name__eq=name__eq, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq, device_execution_mode__neq=device_execution_mode__neq, owner__eq=owner__eq, enrollment_mode__eq=enrollment_mode__eq, issuer__like=issuer__like, subject__like=subject__like)

Get all trusted certificates.

An endpoint for retrieving trusted certificates in an array.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/trusted-certificates -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
name__eq = 'name__eq_example' # str | Filter for certificate name (optional)
service__eq = 'service__eq_example' # str | Filter for service (optional)
expire__eq = 56 # int | Filter for expire (optional)
device_execution_mode__eq = 56 # int | Filter for developer certificates (optional)
device_execution_mode__neq = 56 # int | Filter for not developer certificates (optional)
owner__eq = 'owner__eq_example' # str | Owner name filter (optional)
enrollment_mode__eq = true # bool | Enrollment mode filter (optional)
issuer__like = 'issuer__like_example' # str | Filter for issuer. Finds all matches where the filter value is a case insensitive substring of the result. Example: issuer__like=cn=iss matches CN=issuer. (optional)
subject__like = 'subject__like_example' # str | Filter for subject. Finds all matches where the filter value is a case insensitive substring of the result. Example: subject__like=cn=su matches CN=subject. (optional)

try: 
    # Get all trusted certificates.
    api_response = api_instance.get_all_account_certificates(account_id, limit=limit, after=after, order=order, include=include, name__eq=name__eq, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq, device_execution_mode__neq=device_execution_mode__neq, owner__eq=owner__eq, enrollment_mode__eq=enrollment_mode__eq, issuer__like=issuer__like, subject__like=subject__like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_all_account_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **name__eq** | **str**| Filter for certificate name | [optional] 
 **service__eq** | **str**| Filter for service | [optional] 
 **expire__eq** | **int**| Filter for expire | [optional] 
 **device_execution_mode__eq** | **int**| Filter for developer certificates | [optional] 
 **device_execution_mode__neq** | **int**| Filter for not developer certificates | [optional] 
 **owner__eq** | **str**| Owner name filter | [optional] 
 **enrollment_mode__eq** | **bool**| Enrollment mode filter | [optional] 
 **issuer__like** | **str**| Filter for issuer. Finds all matches where the filter value is a case insensitive substring of the result. Example: issuer__like&#x3D;cn&#x3D;iss matches CN&#x3D;issuer. | [optional] 
 **subject__like** | **str**| Filter for subject. Finds all matches where the filter value is a case insensitive substring of the result. Example: subject__like&#x3D;cn&#x3D;su matches CN&#x3D;subject. | [optional] 

### Return type

[**TrustedCertificateInternalRespList**](TrustedCertificateInternalRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_groups**
> GroupSummaryList get_all_account_groups(account_id, limit=limit, after=after, order=order, include=include, name__eq=name__eq)

Get all group information.

An endpoint for retrieving all group information.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
name__eq = 'name__eq_example' # str | Filter for group name (optional)

try: 
    # Get all group information.
    api_response = api_instance.get_all_account_groups(account_id, limit=limit, after=after, order=order, include=include, name__eq=name__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_all_account_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **get_all_account_invitations**
> UserInvitationRespList get_all_account_invitations(account_id, limit=limit, after=after, order=order)

Get the details of all the user invitations.

An endpoint for retrieving the details of all the active user invitations sent for new or existing users to join the account.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{account-id}/user-invitations -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)

try: 
    # Get the details of all the user invitations.
    api_response = api_instance.get_all_account_invitations(account_id, limit=limit, after=after, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_all_account_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]

### Return type

[**UserInvitationRespList**](UserInvitationRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_users**
> UserInfoRespList get_all_account_users(account_id, limit=limit, after=after, order=order, include=include, email__eq=email__eq, status__eq=status__eq, status__in=status__in, status__nin=status__nin)

Get all user details.

An endpoint for retrieving details of all users.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
email__eq = 'email__eq_example' # str | Filter for email address (optional)
status__eq = 'status__eq_example' # str | Filter for status (optional)
status__in = 'status__in_example' # str | An optional filter for getting users with a specified set of statuses. (optional)
status__nin = 'status__nin_example' # str | An optional filter for excluding users with a specified set of statuses. (optional)

try: 
    # Get all user details.
    api_response = api_instance.get_all_account_users(account_id, limit=limit, after=after, order=order, include=include, email__eq=email__eq, status__eq=status__eq, status__in=status__in, status__nin=status__nin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_all_account_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **email__eq** | **str**| Filter for email address | [optional] 
 **status__eq** | **str**| Filter for status | [optional] 
 **status__in** | **str**| An optional filter for getting users with a specified set of statuses. | [optional] 
 **status__nin** | **str**| An optional filter for excluding users with a specified set of statuses. | [optional] 

### Return type

[**UserInfoRespList**](UserInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> AccountInfoList get_all_accounts(status__eq=status__eq, status__in=status__in, status__nin=status__nin, tier__eq=tier__eq, parent__eq=parent__eq, end_market__eq=end_market__eq, country__like=country__like, limit=limit, after=after, order=order, include=include, format=format, properties=properties)

Get all accounts.

Returns an array of account objects, optionally filtered by status and tier level.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts -H 'Authorization: Bearer API_KEY'`.

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
status__eq = 'status__eq_example' # str | An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. (optional)
status__in = 'status__in_example' # str | An optional filter for getting accounts with a specified set of statuses. (optional)
status__nin = 'status__nin_example' # str | An optional filter for excluding accounts with a specified set of statuses. (optional)
tier__eq = 'tier__eq_example' # str | An optional filter for tier level, must be 0, 1, 2, 98, 99 or omitted. (optional)
parent__eq = 'parent__eq_example' # str | An optional filter for parent account ID. (optional)
end_market__eq = 'end_market__eq_example' # str | An optional filter for account end market. (optional)
country__like = 'country__like_example' # str | An optional filter for account country. Finds all matches where the filter value is a case insensitive substring of the result. Example: country__like=LAND matches Ireland. (optional)
limit = 1000 # int | The number of results to return (2-1000), default is 1000. (optional) (default to 1000)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC. Default value is ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: limits, policies, sub_accounts (optional)
format = 'format_example' # str | Format information for the response to the query, supported: format=breakdown. (optional)
properties = 'properties_example' # str | Property name to be returned from account specific properties. (optional)

try: 
    # Get all accounts.
    api_response = api_instance.get_all_accounts(status__eq=status__eq, status__in=status__in, status__nin=status__nin, tier__eq=tier__eq, parent__eq=parent__eq, end_market__eq=end_market__eq, country__like=country__like, limit=limit, after=after, order=order, include=include, format=format, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status__eq** | **str**| An optional filter for account status, ENROLLING, ACTIVE, RESTRICTED or SUSPENDED. | [optional] 
 **status__in** | **str**| An optional filter for getting accounts with a specified set of statuses. | [optional] 
 **status__nin** | **str**| An optional filter for excluding accounts with a specified set of statuses. | [optional] 
 **tier__eq** | **str**| An optional filter for tier level, must be 0, 1, 2, 98, 99 or omitted. | [optional] 
 **parent__eq** | **str**| An optional filter for parent account ID. | [optional] 
 **end_market__eq** | **str**| An optional filter for account end market. | [optional] 
 **country__like** | **str**| An optional filter for account country. Finds all matches where the filter value is a case insensitive substring of the result. Example: country__like&#x3D;LAND matches Ireland. | [optional] 
 **limit** | **int**| The number of results to return (2-1000), default is 1000. | [optional] [default to 1000]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC. Default value is ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: limits, policies, sub_accounts | [optional] 
 **format** | **str**| Format information for the response to the query, supported: format&#x3D;breakdown. | [optional] 
 **properties** | **str**| Property name to be returned from account specific properties. | [optional] 

### Return type

[**AccountInfoList**](AccountInfoList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_of_account_group**
> ApiKeyInfoRespList get_api_keys_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include)

Get API keys of a group.

An endpoint for listing the API keys of the group with details.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID}/api-keys -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group whose API keys are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get API keys of a group.
    api_response = api_instance.get_api_keys_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_api_keys_of_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **get_groups_of_account_apikey**
> GroupSummaryList get_groups_of_account_apikey(account_id, api_key, limit=limit, after=after, order=order, include=include)

Get groups of the API key.

An endpoint for retrieving groups of the API key.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apiKey}/groups -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key whose details are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get groups of the API key.
    api_response = api_instance.get_groups_of_account_apikey(account_id, api_key, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_groups_of_account_apikey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The ID of the API key whose details are retrieved. | 
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

# **get_groups_of_account_user**
> GroupSummaryList get_groups_of_account_user(account_id, user_id, limit=limit, after=after, order=order, include=include)

Get groups of the user.

An endpoint for retrieving groups of the user.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id}/groups -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user whose details are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get groups of the user.
    api_response = api_instance.get_groups_of_account_user(account_id, user_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_groups_of_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user whose details are retrieved. | 
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

# **get_users_of_account_group**
> UserInfoRespList get_users_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include, status__eq=status__eq, status__in=status__in, status__nin=status__nin)

Get users of a group.

An endpoint for listing users of the group with details.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID}/users -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group whose users are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
status__eq = 'status__eq_example' # str | An optional filter for getting users by status. (optional)
status__in = 'status__in_example' # str | An optional filter for getting users with a specified set of statuses. (optional)
status__nin = 'status__nin_example' # str | An optional filter for excluding users with a specified set of statuses. (optional)

try: 
    # Get users of a group.
    api_response = api_instance.get_users_of_account_group(account_id, group_id, limit=limit, after=after, order=order, include=include, status__eq=status__eq, status__in=status__in, status__nin=status__nin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->get_users_of_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**| The ID of the group whose users are retrieved. | 
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **status__eq** | **str**| An optional filter for getting users by status. | [optional] 
 **status__in** | **str**| An optional filter for getting users with a specified set of statuses. | [optional] 
 **status__nin** | **str**| An optional filter for excluding users with a specified set of statuses. | [optional] 

### Return type

[**UserInfoRespList**](UserInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_account_api_key_from_groups**
> UpdatedResponse remove_account_api_key_from_groups(account_id, api_key, body)

Remove API key from groups.

An endpoint for removing API key from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apiKey}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be removed from the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Remove API key from groups.
    api_response = api_instance.remove_account_api_key_from_groups(account_id, api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->remove_account_api_key_from_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **api_key** | **str**| The ID of the API key to be removed from the group. | 
 **body** | **list[str]**| A list of IDs of the groups to be updated. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_account_user_from_groups**
> UpdatedResponse remove_account_user_from_groups(account_id, user_id, body)

Remove user from groups.

An endpoint for removing user from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user to be removed from the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Remove user from groups.
    api_response = api_instance.remove_account_user_from_groups(account_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->remove_account_user_from_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user to be removed from the group. | 
 **body** | **list[str]**| A list of IDs of the groups to be updated. | 

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

An endpoint for removing API keys from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID}/api-keys -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | A list of API keys to be removed from the group.
body = iam.SubjectList() # SubjectList |  (optional)

try: 
    # Remove API keys from a group.
    api_response = api_instance.remove_api_keys_from_account_group(account_id, group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->remove_api_keys_from_account_group: %s\n" % e)
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

An endpoint for removing users from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID}/users -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | 
body = iam.SubjectList() # SubjectList |  (optional)

try: 
    # Remove users from a group.
    api_response = api_instance.remove_users_from_account_group(account_id, group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->remove_users_from_account_group: %s\n" % e)
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

An endpoint for resetting the secret key of the API key.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apiKey}/reset-secret -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be reset.

try: 
    # Reset the secret key.
    api_response = api_instance.reset_account_api_key_secret(account_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->reset_account_api_key_secret: %s\n" % e)
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

# **update_account**
> AccountInfo update_account(account_id, body)

Update attributes of an existing account.

An endpoint for updating an account.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/accounts/{account-id} -d '{\"phone_number\": \"12345678\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | The ID of the account to be updated.
body = iam.AccountUpdateRootReq() # AccountUpdateRootReq | Details of the account to be updated.

try: 
    # Update attributes of an existing account.
    api_response = api_instance.update_account(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->update_account: %s\n" % e)
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

# **update_account_api_key**
> ApiKeyInfoResp update_account_api_key(account_id, api_key, body)

Update API key details.

An endpoint for updating API key details.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/api-keys/{apiKey} -d '{\"name\": \"TestApiKey25\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
api_key = 'api_key_example' # str | The ID of the API key to be updated.
body = iam.ApiKeyUpdateReq() # ApiKeyUpdateReq | New API key attributes to be stored.

try: 
    # Update API key details.
    api_response = api_instance.update_account_api_key(account_id, api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->update_account_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
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

# **update_account_certificate**
> TrustedCertificateInternalResp update_account_certificate(account_id, cert_id, body)

Update trusted certificate.

An endpoint for updating existing trusted certificates.

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be updated.
body = iam.TrustedCertificateUpdateReq() # TrustedCertificateUpdateReq | A trusted certificate object with attributes.

try: 
    # Update trusted certificate.
    api_response = api_instance.update_account_certificate(account_id, cert_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->update_account_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **cert_id** | **str**| The ID of the trusted certificate to be updated. | 
 **body** | [**TrustedCertificateUpdateReq**](TrustedCertificateUpdateReq.md)| A trusted certificate object with attributes. | 

### Return type

[**TrustedCertificateInternalResp**](TrustedCertificateInternalResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_group_name**
> UpdatedResponse update_account_group_name(account_id, group_id, body)

Update the group name.

An endpoint for updating a group name.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/policy-groups/{groupID}/ -d '{\"name\": \"TestGroup2\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.GroupUpdateInfo() # GroupUpdateInfo | Details of the group to be created.

try: 
    # Update the group name.
    api_response = api_instance.update_account_group_name(account_id, group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->update_account_group_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **group_id** | **str**| The ID of the group to be updated. | 
 **body** | [**GroupUpdateInfo**](GroupUpdateInfo.md)| Details of the group to be created. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_user**
> UserInfoResp update_account_user(account_id, user_id, body)

Update user details.

An endpoint for updating user details.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id} -d '{\"username\": \"myusername\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user to be updated.
body = iam.UserUpdateReq() # UserUpdateReq | A user object with attributes.

try: 
    # Update user details.
    api_response = api_instance.update_account_user(account_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->update_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user to be updated. | 
 **body** | [**UserUpdateReq**](UserUpdateReq.md)| A user object with attributes. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_account_user_email**
> validate_account_user_email(account_id, user_id)

Validate the user email.

An endpoint for validating the user email.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id}/validate-email -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AggregatorAccountAdminApi(iam.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID.
user_id = 'user_id_example' # str | The ID of the user whose email is validated.

try: 
    # Validate the user email.
    api_instance.validate_account_user_email(account_id, user_id)
except ApiException as e:
    print("Exception when calling AggregatorAccountAdminApi->validate_account_user_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | 
 **user_id** | **str**| The ID of the user whose email is validated. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

