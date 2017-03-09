# iam.AccountAdminApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_alias**](AccountAdminApi.md#add_alias) | **PUT** /v3/accounts/{accountID}/alias/{alias} | Add an alias.
[**add_certificate**](AccountAdminApi.md#add_certificate) | **POST** /v3/trusted-certificates | Upload a new trusted certificate.
[**add_my_account_alias**](AccountAdminApi.md#add_my_account_alias) | **PUT** /v3/accounts/me/alias/{alias} | Add an alias.
[**create_user**](AccountAdminApi.md#create_user) | **POST** /v3/users | Create a new user.
[**delete_certificate**](AccountAdminApi.md#delete_certificate) | **DELETE** /v3/trusted-certificates/{cert-id} | Delete a trusted certificate by ID.
[**delete_user**](AccountAdminApi.md#delete_user) | **DELETE** /v3/users/{user-id} | Delete a user.
[**get_all_certificates**](AccountAdminApi.md#get_all_certificates) | **GET** /v3/trusted-certificates | Get all trusted certificates.
[**get_all_users**](AccountAdminApi.md#get_all_users) | **GET** /v3/users | Get the details of all users.
[**get_certificate**](AccountAdminApi.md#get_certificate) | **GET** /v3/trusted-certificates/{cert-id} | Get trusted certificate by ID.
[**get_user**](AccountAdminApi.md#get_user) | **GET** /v3/users/{user-id} | Details of a user.
[**remove_alias**](AccountAdminApi.md#remove_alias) | **DELETE** /v3/accounts/{accountID}/alias/{alias} | Remove an alias.
[**remove_my_account_alias**](AccountAdminApi.md#remove_my_account_alias) | **DELETE** /v3/accounts/me/alias/{alias} | Remove an alias.
[**reset_user_password**](AccountAdminApi.md#reset_user_password) | **POST** /v3/users/{user-id}/reset-password | Reset the user password.
[**set_aliases**](AccountAdminApi.md#set_aliases) | **POST** /v3/accounts/{accountID}/alias | Set aliases.
[**set_my_account_aliases**](AccountAdminApi.md#set_my_account_aliases) | **POST** /v3/accounts/me/alias | Set aliases.
[**update_account**](AccountAdminApi.md#update_account) | **PUT** /v3/accounts/{accountID} | Update attributes of an existing account.
[**update_certificate**](AccountAdminApi.md#update_certificate) | **PUT** /v3/trusted-certificates/{cert-id} | Update trusted certificate.
[**update_my_account**](AccountAdminApi.md#update_my_account) | **PUT** /v3/accounts/me | Updates attributes of the account.
[**update_user**](AccountAdminApi.md#update_user) | **PUT** /v3/users/{user-id} | Update user details.


# **add_alias**
> UpdatedResponse add_alias(account_id, alias)

Add an alias.

Adds an alias to the account.

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
alias = 'alias_example' # str | The account alias to be added.

try: 
    # Add an alias.
    api_response = api_instance.add_alias(account_id, alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->add_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be updated. | 
 **alias** | **str**| The account alias to be added. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **add_my_account_alias**
> UpdatedResponse add_my_account_alias(alias)

Add an alias.

Adds an alias to the account.

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
alias = 'alias_example' # str | 

try: 
    # Add an alias.
    api_response = api_instance.add_my_account_alias(alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->add_my_account_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**|  | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserInfoResp create_user(body, action=action)

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
api_instance = iam.AccountAdminApi()
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

# **delete_certificate**
> delete_certificate(cert_id)

Delete a trusted certificate by ID.

An endpoint for deleting a trusted certificate.

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
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be deleted.

try: 
    # Delete a trusted certificate by ID.
    api_instance.delete_certificate(cert_id)
except ApiException as e:
    print("Exception when calling AccountAdminApi->delete_certificate: %s\n" % e)
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

# **get_all_certificates**
> TrustedCertificateRespList get_all_certificates(limit=limit, after=after, order=order, include=include, filter=filter, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq)

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
api_instance = iam.AccountAdminApi()
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity ID to fetch after the given one. (optional)
order = 'ASC' # str | The order of the records, ASC or DESC; by default ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separated additional data to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | Filter by service or expiring days, for example filter=service%3Dlwm2m,expire%3D180,device_execution_filter%3D0 (optional)
service__eq = 'service__eq_example' # str | Service filter, either lwm2m or bootstrap (optional)
expire__eq = 56 # int | Expire filter in days (optional)
device_execution_mode__eq = 56 # int | Device execution mode, as 1 for developer certificates or as another natural integer value (optional)

try: 
    # Get all trusted certificates.
    api_response = api_instance.get_all_certificates(limit=limit, after=after, order=order, include=include, filter=filter, service__eq=service__eq, expire__eq=expire__eq, device_execution_mode__eq=device_execution_mode__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_all_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity ID to fetch after the given one. | [optional] 
 **order** | **str**| The order of the records, ASC or DESC; by default ASC | [optional] [default to ASC]
 **include** | **str**| Comma separated additional data to return. Currently supported: total_count | [optional] 
 **filter** | **str**| Filter by service or expiring days, for example filter&#x3D;service%3Dlwm2m,expire%3D180,device_execution_filter%3D0 | [optional] 
 **service__eq** | **str**| Service filter, either lwm2m or bootstrap | [optional] 
 **expire__eq** | **int**| Expire filter in days | [optional] 
 **device_execution_mode__eq** | **int**| Device execution mode, as 1 for developer certificates or as another natural integer value | [optional] 

### Return type

[**TrustedCertificateRespList**](TrustedCertificateRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> UserInfoRespList get_all_users(limit=limit, after=after, order=order, include=include, filter=filter, status__eq=status__eq)

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
filter = 'filter_example' # str | Filter for the query, for example filter=status%3Dactive,status%3Dreset. (optional)
status__eq = 'status__eq_example' # str | Filter for status, for example active or reset (optional)

try: 
    # Get the details of all users.
    api_response = api_instance.get_all_users(limit=limit, after=after, order=order, include=include, filter=filter, status__eq=status__eq)
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

# **get_certificate**
> TrustedCertificateResp get_certificate(cert_id)

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
api_instance = iam.AccountAdminApi()
cert_id = 'cert_id_example' # str | The ID or name of the trusted certificate to be retrieved.

try: 
    # Get trusted certificate by ID.
    api_response = api_instance.get_certificate(cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| The ID or name of the trusted certificate to be retrieved. | 

### Return type

[**TrustedCertificateResp**](TrustedCertificateResp.md)

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

# **remove_alias**
> UpdatedResponse remove_alias(account_id, alias)

Remove an alias.

Removes an alias from the account.

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
alias = 'alias_example' # str | The account alias to be removed.

try: 
    # Remove an alias.
    api_response = api_instance.remove_alias(account_id, alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->remove_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be updated. | 
 **alias** | **str**| The account alias to be removed. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_my_account_alias**
> UpdatedResponse remove_my_account_alias(alias)

Remove an alias.

Removes an alias from the account.

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
alias = 'alias_example' # str | Account alias to be removed.

try: 
    # Remove an alias.
    api_response = api_instance.remove_my_account_alias(alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->remove_my_account_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Account alias to be removed. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_password**
> UserInfoResp reset_user_password(user_id)

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
api_instance = iam.AccountAdminApi()
user_id = 'user_id_example' # str | The ID of the user whose password is reset.

try: 
    # Reset the user password.
    api_response = api_instance.reset_user_password(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->reset_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose password is reset. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_aliases**
> UpdatedResponse set_aliases(account_id, body)

Set aliases.

Defines aliases of the account and overwrites the previous set of aliases.

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
body = [iam.list[str]()] # list[str] | A list of aliases to be set.

try: 
    # Set aliases.
    api_response = api_instance.set_aliases(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->set_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to be updated. | 
 **body** | **list[str]**| A list of aliases to be set. | 

### Return type

[**UpdatedResponse**](UpdatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_my_account_aliases**
> UpdatedResponse set_my_account_aliases(body)

Set aliases.

Defines the aliases of the account and overwrites the previous set of aliases.

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
body = [iam.list[str]()] # list[str] | List of aliases to be set.

try: 
    # Set aliases.
    api_response = api_instance.set_my_account_aliases(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->set_my_account_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| List of aliases to be set. | 

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

# **update_certificate**
> TrustedCertificateResp update_certificate(cert_id, body)

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
api_instance = iam.AccountAdminApi()
cert_id = 'cert_id_example' # str | The ID of the trusted certificate to be updated.
body = iam.TrustedCertificateReq() # TrustedCertificateReq | A trusted certificate object with attributes.

try: 
    # Update trusted certificate.
    api_response = api_instance.update_certificate(cert_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->update_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| The ID of the trusted certificate to be updated. | 
 **body** | [**TrustedCertificateReq**](TrustedCertificateReq.md)| A trusted certificate object with attributes. | 

### Return type

[**TrustedCertificateResp**](TrustedCertificateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_account**
> AccountInfo update_my_account(body)

Updates attributes of the account.

An endpoint for updating the account.

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

