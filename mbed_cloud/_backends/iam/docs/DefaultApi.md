# iam.DefaultApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](DefaultApi.md#activate_user) | **PUT** /auth/invitations/{invitation-id} | Accept invitation.
[**apply_password_recovery**](DefaultApi.md#apply_password_recovery) | **PUT** /auth/recover | Apply password recovery.
[**get_invited_user**](DefaultApi.md#get_invited_user) | **GET** /auth/invitations/{invitation-id} | Get invited user.
[**get_self_enrolling_user**](DefaultApi.md#get_self_enrolling_user) | **GET** /auth/register/{signup-id} | Get registering user.
[**register_account**](DefaultApi.md#register_account) | **PUT** /auth/register/{signup-id} | Register a new account.
[**request_password_recovery**](DefaultApi.md#request_password_recovery) | **POST** /auth/recover | Request password recovery.
[**signup**](DefaultApi.md#signup) | **POST** /auth/register | Sign up for a new account.
[**verify_self_enrollment**](DefaultApi.md#verify_self_enrollment) | **POST** /auth/register/{signup-id} | Verify self-enrollment code and aliases.


# **activate_user**
> UserInfoResp activate_user(invitation_id, body)

Accept invitation.

Accepting pending invitation and providing missing details.

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
api_instance = iam.DefaultApi()
invitation_id = 'invitation_id_example' # str | Invitation ID received in email.
body = iam.UserUpdateReq() # UserUpdateReq | Details of the user accepting the invitation.

try: 
    # Accept invitation.
    api_response = api_instance.activate_user(invitation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->activate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| Invitation ID received in email. | 
 **body** | [**UserUpdateReq**](UserUpdateReq.md)| Details of the user accepting the invitation. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_password_recovery**
> apply_password_recovery(body, x_forwarded_for=x_forwarded_for)

Apply password recovery.

Applying password recovery by providing a secret hash code.

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
api_instance = iam.DefaultApi()
body = iam.PasswordRecoveryReq() # PasswordRecoveryReq | Hash received by email and new password.
x_forwarded_for = 'x_forwarded_for_example' # str |  (optional)

try: 
    # Apply password recovery.
    api_instance.apply_password_recovery(body, x_forwarded_for=x_forwarded_for)
except ApiException as e:
    print("Exception when calling DefaultApi->apply_password_recovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordRecoveryReq**](PasswordRecoveryReq.md)| Hash received by email and new password. | 
 **x_forwarded_for** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invited_user**
> UserInfoResp get_invited_user(invitation_id)

Get invited user.

Returns information about the user being invited.

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
api_instance = iam.DefaultApi()
invitation_id = 'invitation_id_example' # str | Invitation ID received in email.

try: 
    # Get invited user.
    api_response = api_instance.get_invited_user(invitation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_invited_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| Invitation ID received in email. | 

### Return type

[**UserInfoResp**](UserInfoResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_enrolling_user**
> AccountSignupResp get_self_enrolling_user(signup_id)

Get registering user.

Retrieving the details of a user to register.

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
api_instance = iam.DefaultApi()
signup_id = 'signup_id_example' # str | ID received while signing up.

try: 
    # Get registering user.
    api_response = api_instance.get_self_enrolling_user(signup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_self_enrolling_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_id** | **str**| ID received while signing up. | 

### Return type

[**AccountSignupResp**](AccountSignupResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_account**
> AccountEnrollmentResp register_account(signup_id, body)

Register a new account.

An endpoint for registering a new account.

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
api_instance = iam.DefaultApi()
signup_id = 'signup_id_example' # str | ID received while signing up.
body = iam.AccountEnrollmentReq() # AccountEnrollmentReq | Details of the account to be created.

try: 
    # Register a new account.
    api_response = api_instance.register_account(signup_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->register_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_id** | **str**| ID received while signing up. | 
 **body** | [**AccountEnrollmentReq**](AccountEnrollmentReq.md)| Details of the account to be created. | 

### Return type

[**AccountEnrollmentResp**](AccountEnrollmentResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_recovery**
> request_password_recovery(body, x_forwarded_for=x_forwarded_for)

Request password recovery.

Requesting password recovery by email address.

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
api_instance = iam.DefaultApi()
body = iam.PasswordResetReq() # PasswordResetReq | Email address of the user whose password needs to be recovered.
x_forwarded_for = 'x_forwarded_for_example' # str |  (optional)

try: 
    # Request password recovery.
    api_instance.request_password_recovery(body, x_forwarded_for=x_forwarded_for)
except ApiException as e:
    print("Exception when calling DefaultApi->request_password_recovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordResetReq**](PasswordResetReq.md)| Email address of the user whose password needs to be recovered. | 
 **x_forwarded_for** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup**
> AccountSignupResp signup(body)

Sign up for a new account.

Signing up for a new free tier account with email address.

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
api_instance = iam.DefaultApi()
body = iam.AccountSignupReq() # AccountSignupReq | Email address of the user to be signed up.

try: 
    # Sign up for a new account.
    api_response = api_instance.signup(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->signup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountSignupReq**](AccountSignupReq.md)| Email address of the user to be signed up. | 

### Return type

[**AccountSignupResp**](AccountSignupResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_self_enrollment**
> verify_self_enrollment(signup_id, body=body)

Verify self-enrollment code and aliases.

Verifying whether the code received by email is valid. Optionally, it also verifies whether an account with the given aliases exists.

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
api_instance = iam.DefaultApi()
signup_id = 'signup_id_example' # str | ID received while signing up.
body = iam.AccountSignupVerify() # AccountSignupVerify | Verification code received by email and aliases to be checked. (optional)

try: 
    # Verify self-enrollment code and aliases.
    api_instance.verify_self_enrollment(signup_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->verify_self_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_id** | **str**| ID received while signing up. | 
 **body** | [**AccountSignupVerify**](AccountSignupVerify.md)| Verification code received by email and aliases to be checked. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

