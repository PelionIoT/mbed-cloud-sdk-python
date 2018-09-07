# iam.AccountAdminApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_api_key_to_groups**](AccountAdminApi.md#add_api_key_to_groups) | **POST** /v3/api-keys/{apiKey}/groups | Add API key to a list of groups.
[**add_certificate**](AccountAdminApi.md#add_certificate) | **POST** /v3/trusted-certificates | Upload a new trusted certificate.
[**add_subjects_to_group**](AccountAdminApi.md#add_subjects_to_group) | **POST** /v3/policy-groups/{groupID} | Add members to a group.
[**add_user_to_groups**](AccountAdminApi.md#add_user_to_groups) | **POST** /v3/users/{user-id}/groups | Add user to a list of groups.
[**create_group**](AccountAdminApi.md#create_group) | **POST** /v3/policy-groups | Create a new group.
[**create_invitation**](AccountAdminApi.md#create_invitation) | **POST** /v3/user-invitations | Create a user invitation.
[**create_user**](AccountAdminApi.md#create_user) | **POST** /v3/users | Create a new user.
[**delete_group**](AccountAdminApi.md#delete_group) | **DELETE** /v3/policy-groups/{groupID} | Delete a group.
[**delete_invitation**](AccountAdminApi.md#delete_invitation) | **DELETE** /v3/user-invitations/{invitation-id} | Delete a user invitation.
[**delete_user**](AccountAdminApi.md#delete_user) | **DELETE** /v3/users/{user-id} | Delete a user.
[**get_all_invitations**](AccountAdminApi.md#get_all_invitations) | **GET** /v3/user-invitations | Get the details of all the user invitations.
[**get_all_users**](AccountAdminApi.md#get_all_users) | **GET** /v3/users | Get the details of all users.
[**get_groups_of_apikey**](AccountAdminApi.md#get_groups_of_apikey) | **GET** /v3/api-keys/{apiKey}/groups | Get groups of the API key.
[**get_groups_of_user**](AccountAdminApi.md#get_groups_of_user) | **GET** /v3/users/{user-id}/groups | Get groups of the user.
[**get_invitation**](AccountAdminApi.md#get_invitation) | **GET** /v3/user-invitations/{invitation-id} | Details of a user invitation.
[**get_user**](AccountAdminApi.md#get_user) | **GET** /v3/users/{user-id} | Details of a user.
[**get_users_of_group**](AccountAdminApi.md#get_users_of_group) | **GET** /v3/policy-groups/{groupID}/users | Get users of a group.
[**remove_api_key_from_groups**](AccountAdminApi.md#remove_api_key_from_groups) | **DELETE** /v3/api-keys/{apiKey}/groups | Remove API key from groups.
[**remove_user_from_groups**](AccountAdminApi.md#remove_user_from_groups) | **DELETE** /v3/users/{user-id}/groups | Remove user from groups.
[**remove_users_from_group**](AccountAdminApi.md#remove_users_from_group) | **DELETE** /v3/policy-groups/{groupID}/users | Remove users from a group.
[**update_group_name**](AccountAdminApi.md#update_group_name) | **PUT** /v3/policy-groups/{groupID} | Update the group name.
[**update_my_account**](AccountAdminApi.md#update_my_account) | **PUT** /v3/accounts/me | Updates attributes of the account.
[**update_user**](AccountAdminApi.md#update_user) | **PUT** /v3/users/{user-id} | Update user details.


# **add_api_key_to_groups**
> UpdatedResponse add_api_key_to_groups(api_key, body)

Add API key to a list of groups.

An endpoint for adding API key to groups.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/api-keys/{apikey-id}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
api_key = 'api_key_example' # str | The ID of the API key to be added to the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Add API key to a list of groups.
    api_response = api_instance.add_api_key_to_groups(api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->add_api_key_to_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **add_certificate**
> TrustedCertificateResp add_certificate(body)

Upload a new trusted certificate.

An endpoint for uploading new trusted certificates.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/trusted-certificates -d {\"name\": \"myCert1\", \"description\": \"very important cert\", \"certificate\": \"certificate_data\", \"service\": \"lwm2m\"} -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
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

An endpoint for adding users and API keys to a group.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id} -d '{\"users\": [0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
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

# **add_user_to_groups**
> UpdatedResponse add_user_to_groups(user_id, body)

Add user to a list of groups.

An endpoint for adding user to groups.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/users/{user-id}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
user_id = 'user_id_example' # str | The ID of the user to be added to the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Add user to a list of groups.
    api_response = api_instance.add_user_to_groups(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->add_user_to_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **create_group**
> GroupSummary create_group(body)

Create a new group.

An endpoint for creating a new group.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/policy-groups -d '{\"name\": \"MyGroup1\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
body = iam.GroupCreationInfo() # GroupCreationInfo | Details of the group to be created.

try: 
    # Create a new group.
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreationInfo**](GroupCreationInfo.md)| Details of the group to be created. | 

### Return type

[**GroupSummary**](GroupSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invitation**
> UserInvitationResp create_invitation(body)

Create a user invitation.

An endpoint for inviting a new or an existing user to join the account.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/user-invitations -d {\"email\": \"myemail@company.com\"} -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
body = iam.UserInvitationReq() # UserInvitationReq | A user invitation object with attributes.

try: 
    # Create a user invitation.
    api_response = api_instance.create_invitation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->create_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserInvitationReq**](UserInvitationReq.md)| A user invitation object with attributes. | 

### Return type

[**UserInvitationResp**](UserInvitationResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserInfoResp create_user(body, action=action)

Create a new user.

An endpoint for creating or inviting a new user to the account. In case of invitation email address is used only, other attributes are set in the 2nd step.   **Example usage:** `curl -X POST https://api.us-east-1.mbedcloud.com/v3/users?action=invite -d {\"email\": \"myemail@company.com\"} -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
body = iam.UserInfoReq() # UserInfoReq | A user object with attributes.
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
 **body** | [**UserInfoReq**](UserInfoReq.md)| A user object with attributes. | 
 **action** | **str**| Action, either &#39;create&#39; or &#39;invite&#39;. | [optional] [default to create]

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Delete a group.

An endpoint for deleting a group.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
group_id = 'group_id_example' # str | The ID of the group to be deleted.

try: 
    # Delete a group.
    api_instance.delete_group(group_id)
except ApiException as e:
    print("Exception when calling AccountAdminApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invitation**
> delete_invitation(invitation_id)

Delete a user invitation.

An endpoint for deleting an active user invitation which has been sent for a new or an existing user to join the account.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/user-invitations/{invitation-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
invitation_id = 'invitation_id_example' # str | The ID of the invitation to be deleted.

try: 
    # Delete a user invitation.
    api_instance.delete_invitation(invitation_id)
except ApiException as e:
    print("Exception when calling AccountAdminApi->delete_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| The ID of the invitation to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete a user.

An endpoint for deleting a user.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/users/{user-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
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

# **get_all_invitations**
> UserInvitationRespList get_all_invitations(limit=limit, after=after, order=order)

Get the details of all the user invitations.

An endpoint for retrieving the details of all the active user invitations sent for new or existing users to join the account.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/user-invitations -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)

try: 
    # Get the details of all the user invitations.
    api_response = api_instance.get_all_invitations(limit=limit, after=after, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_all_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_all_users**
> UserInfoRespList get_all_users(limit=limit, after=after, order=order, include=include, email__eq=email__eq, status__eq=status__eq, status__in=status__in, status__nin=status__nin)

Get the details of all users.

An endpoint for retrieving the details of all users.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/users -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
email__eq = 'email__eq_example' # str | Filter for email address (optional)
status__eq = 'status__eq_example' # str | Filter for status, for example active or reset (optional)
status__in = 'status__in_example' # str | An optional filter for getting users with a specified set of statuses. (optional)
status__nin = 'status__nin_example' # str | An optional filter for excluding users with a specified set of statuses. (optional)

try: 
    # Get the details of all users.
    api_response = api_instance.get_all_users(limit=limit, after=after, order=order, include=include, email__eq=email__eq, status__eq=status__eq, status__in=status__in, status__nin=status__nin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records based on creation time, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **email__eq** | **str**| Filter for email address | [optional] 
 **status__eq** | **str**| Filter for status, for example active or reset | [optional] 
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

# **get_groups_of_apikey**
> GroupSummaryList get_groups_of_apikey(api_key, limit=limit, after=after, order=order, include=include)

Get groups of the API key.

An endpoint for retrieving groups of the API key.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/api-keys/{apikey-id}/groups -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
api_key = 'api_key_example' # str | The ID of the API key whose details are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get groups of the API key.
    api_response = api_instance.get_groups_of_apikey(api_key, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_groups_of_apikey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_groups_of_user**
> GroupSummaryList get_groups_of_user(user_id, limit=limit, after=after, order=order, include=include)

Get groups of the user.

An endpoint for retrieving groups of the user.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/users/{user-id}/groups -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
user_id = 'user_id_example' # str | The ID of the user whose details are retrieved.
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records based on creation time, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)

try: 
    # Get groups of the user.
    api_response = api_instance.get_groups_of_user(user_id, limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_groups_of_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_invitation**
> UserInvitationResp get_invitation(invitation_id)

Details of a user invitation.

An endpoint for retrieving the details of an active user invitation sent for a new or an existing user to join the account.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/user-invitations/{invitation-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
invitation_id = 'invitation_id_example' # str | The ID of the invitation to be retrieved.

try: 
    # Details of a user invitation.
    api_response = api_instance.get_invitation(invitation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| The ID of the invitation to be retrieved. | 

### Return type

[**UserInvitationResp**](UserInvitationResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserInfoResp get_user(user_id)

Details of a user.

An endpoint for retrieving the details of a user.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/users/{user-id} -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
user_id = 'user_id_example' # str | The ID of the user whose details are retrieved.

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
 **user_id** | **str**| The ID of the user whose details are retrieved. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_of_group**
> UserInfoRespList get_users_of_group(group_id, limit=limit, after=after, order=order, include=include, status__eq=status__eq, status__in=status__in, status__nin=status__nin)

Get users of a group.

An endpoint for listing the users of a group with details.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id}/users -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
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
    api_response = api_instance.get_users_of_group(group_id, limit=limit, after=after, order=order, include=include, status__eq=status__eq, status__in=status__in, status__nin=status__nin)
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

# **remove_api_key_from_groups**
> UpdatedResponse remove_api_key_from_groups(api_key, body)

Remove API key from groups.

An endpoint for removing API key from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/api-keys/{apikey-id}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
api_key = 'api_key_example' # str | The ID of the API key to be removed from the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Remove API key from groups.
    api_response = api_instance.remove_api_key_from_groups(api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->remove_api_key_from_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **remove_user_from_groups**
> UpdatedResponse remove_user_from_groups(user_id, body)

Remove user from groups.

An endpoint for removing user from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/users/{user-id}/groups -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
user_id = 'user_id_example' # str | The ID of the user to be removed from the group.
body = [iam.list[str]()] # list[str] | A list of IDs of the groups to be updated.

try: 
    # Remove user from groups.
    api_response = api_instance.remove_user_from_groups(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->remove_user_from_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **remove_users_from_group**
> UpdatedResponse remove_users_from_group(group_id, body)

Remove users from a group.

An endpoint for removing users from groups.   **Example usage:** `curl -X DELETE https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id}/users -d '[0162056a9a1586f30242590700000000,0117056a9a1586f30242590700000000]' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
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

# **update_group_name**
> UpdatedResponse update_group_name(group_id, body)

Update the group name.

An endpoint for updating a group name.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/policy-groups/{group-id} -d '{\"name\": \"TestGroup2\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
group_id = 'group_id_example' # str | The ID of the group to be updated.
body = iam.GroupUpdateInfo() # GroupUpdateInfo | Details of the group to be created.

try: 
    # Update the group name.
    api_response = api_instance.update_group_name(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->update_group_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **update_my_account**
> AccountInfo update_my_account(body)

Updates attributes of the account.

An endpoint for updating the account.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/accounts/me -d '{\"phone_number\": \"12345678\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
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

An endpoint for updating user details.   **Example usage:** `curl -X PUT https://api.us-east-1.mbedcloud.com/v3/users/{user-id} -d '{\"username\": \"myusername\"}' -H 'content-type: application/json' -H 'Authorization: Bearer API_KEY'`

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
api_instance = iam.AccountAdminApi(iam.ApiClient(configuration))
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

