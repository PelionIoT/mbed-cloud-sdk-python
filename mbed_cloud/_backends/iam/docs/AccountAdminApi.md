# iam.AccountAdminApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_certificate**](AccountAdminApi.md#add_certificate) | **POST** /v3/ca-certificates | Upload a new CA certificate.
[**create_user**](AccountAdminApi.md#create_user) | **POST** /v3/users | Create a new user.
[**delete_certificate**](AccountAdminApi.md#delete_certificate) | **DELETE** /v3/ca-certificates/{ca-cert-id} | Delete a CA certificate by ID.
[**delete_user**](AccountAdminApi.md#delete_user) | **DELETE** /v3/users/{user-id} | Delete a user.
[**get_all_certificates**](AccountAdminApi.md#get_all_certificates) | **GET** /v3/ca-certificates | Get all CA certificates.
[**get_all_users**](AccountAdminApi.md#get_all_users) | **GET** /v3/users | Get the details of all users.
[**get_certificate**](AccountAdminApi.md#get_certificate) | **GET** /v3/ca-certificates/{ca-cert-id} | Get CA certificate by ID.
[**get_user**](AccountAdminApi.md#get_user) | **GET** /v3/users/{user-id} | Details of a user.
[**update_certificate**](AccountAdminApi.md#update_certificate) | **PUT** /v3/ca-certificates/{ca-cert-id} | Update CA certificate.
[**update_my_account**](AccountAdminApi.md#update_my_account) | **PUT** /v3/accounts/me | Updates attributes of the account.
[**update_user**](AccountAdminApi.md#update_user) | **PUT** /v3/users/{user-id} | Update user details.


# **add_certificate**
> CACertificateResp add_certificate(body)

Upload a new CA certificate.

An endpoint for uploading new CA certificates.

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
body = iam.CACertificateReq() # CACertificateReq | A CA certificate object with attributes.

try: 
    # Upload a new CA certificate.
    api_response = api_instance.add_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->add_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CACertificateReq**](CACertificateReq.md)| A CA certificate object with attributes. | 

### Return type

[**CACertificateResp**](CACertificateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
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
> delete_certificate(ca_cert_id)

Delete a CA certificate by ID.

An endpoint for deleting a CA certificate.

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
ca_cert_id = 'ca_cert_id_example' # str | The ID of the CA certificate to be deleted.

try: 
    # Delete a CA certificate by ID.
    api_instance.delete_certificate(ca_cert_id)
except ApiException as e:
    print("Exception when calling AccountAdminApi->delete_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_cert_id** | **str**| The ID of the CA certificate to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id, force=force)

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
force = 'force_example' # str | A flag indicating that the user is forced to be deleted. (optional)

try: 
    # Delete a user.
    api_instance.delete_user(user_id, force=force)
except ApiException as e:
    print("Exception when calling AccountAdminApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to be deleted. | 
 **force** | **str**| A flag indicating that the user is forced to be deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_certificates**
> CACertificateRespList get_all_certificates(limit=limit, after=after, order=order, include=include, filter=filter)

Get all CA certificates.

An endpoint for retrieving CA certificates in an array.

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
filter = 'filter_example' # str | Filter by service or expiring days, for example filter=service%3Dlwm2m,expire%3D180 (optional)

try: 
    # Get all CA certificates.
    api_response = api_instance.get_all_certificates(limit=limit, after=after, order=order, include=include, filter=filter)
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
 **filter** | **str**| Filter by service or expiring days, for example filter&#x3D;service%3Dlwm2m,expire%3D180 | [optional] 

### Return type

[**CACertificateRespList**](CACertificateRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> UserInfoRespList get_all_users(limit=limit, after=after, order=order, include=include, filter=filter)

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

try: 
    # Get the details of all users.
    api_response = api_instance.get_all_users(limit=limit, after=after, order=order, include=include, filter=filter)
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

### Return type

[**UserInfoRespList**](UserInfoRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate**
> CACertificateResp get_certificate(ca_cert_id)

Get CA certificate by ID.

An endpoint for retrieving a CA certificate by ID.

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
ca_cert_id = 'ca_cert_id_example' # str | The ID or name of the CA certificate to be retrieved.

try: 
    # Get CA certificate by ID.
    api_response = api_instance.get_certificate(ca_cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->get_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_cert_id** | **str**| The ID or name of the CA certificate to be retrieved. | 

### Return type

[**CACertificateResp**](CACertificateResp.md)

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

# **update_certificate**
> CACertificateResp update_certificate(ca_cert_id, body)

Update CA certificate.

An endpoint for updating existing CA certificates.

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
ca_cert_id = 'ca_cert_id_example' # str | The ID of the CA certificate to be updated.
body = iam.CACertificateReq() # CACertificateReq | A CA certificate object with attributes.

try: 
    # Update CA certificate.
    api_response = api_instance.update_certificate(ca_cert_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAdminApi->update_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_cert_id** | **str**| The ID of the CA certificate to be updated. | 
 **body** | [**CACertificateReq**](CACertificateReq.md)| A CA certificate object with attributes. | 

### Return type

[**CACertificateResp**](CACertificateResp.md)

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

