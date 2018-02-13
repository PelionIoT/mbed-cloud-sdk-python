# enrollment.PublicAPIApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_device_enrollments_get**](PublicAPIApi.md#v3_device_enrollments_get) | **GET** /v3/device-enrollments | Get enrollment list.
[**v3_device_enrollments_post**](PublicAPIApi.md#v3_device_enrollments_post) | **POST** /v3/device-enrollments | Place an enrollment claim for one or several devices.
[**v3_device_enrollmentsid_delete**](PublicAPIApi.md#v3_device_enrollmentsid_delete) | **DELETE** /v3/device-enrollments/:id | Delete an enrollment by ID.
[**v3_device_enrollmentsid_get**](PublicAPIApi.md#v3_device_enrollmentsid_get) | **GET** /v3/device-enrollments/:id | Get details of an enrollment by ID.


# **v3_device_enrollments_get**
> EnrollmentIdentities v3_device_enrollments_get(limit=limit, after=after, order=order)

Get enrollment list.

Provides a list of pending and claimed enrollments. Example usage: 

### Example 
```python
from __future__ import print_function
import time
import enrollment
from enrollment.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = enrollment.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = enrollment.PublicAPIApi(enrollment.ApiClient(configuration))
limit = 56 # int | Number of results to be returned. Between 2 and 1000, inclusive. (optional)
after = 'after_example' # str | Entity ID to fetch after. (optional)
order = 'ASC' # str | ASC or DESC (optional) (default to ASC)

try: 
    # Get enrollment list.
    api_response = api_instance.v3_device_enrollments_get(limit=limit, after=after, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->v3_device_enrollments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to be returned. Between 2 and 1000, inclusive. | [optional] 
 **after** | **str**| Entity ID to fetch after. | [optional] 
 **order** | **str**| ASC or DESC | [optional] [default to ASC]

### Return type

[**EnrollmentIdentities**](EnrollmentIdentities.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_device_enrollments_post**
> EnrollmentIdentity v3_device_enrollments_post(enrollment_identity)

Place an enrollment claim for one or several devices.

When the device connects to the bootstrap server and provides the enrollment ID, it will be assigned to your account. 

### Example 
```python
from __future__ import print_function
import time
import enrollment
from enrollment.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = enrollment.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = enrollment.PublicAPIApi(enrollment.ApiClient(configuration))
enrollment_identity = enrollment.EnrollmentId() # EnrollmentId | 

try: 
    # Place an enrollment claim for one or several devices.
    api_response = api_instance.v3_device_enrollments_post(enrollment_identity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->v3_device_enrollments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_identity** | [**EnrollmentId**](EnrollmentId.md)|  | 

### Return type

[**EnrollmentIdentity**](EnrollmentIdentity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_device_enrollmentsid_delete**
> v3_device_enrollmentsid_delete()

Delete an enrollment by ID.

To free a device from your account you can delete the enrollment claim. To bypass the device ownership, you need to delete the enrollment and do a factory reset for the device. For more information on the ownership trasfer, see [https://github.com/ARMmbed/mbed_Cloud_Docs/blob/restructure/Docs/provisioning/generic_instructions/device-ownership.md#transferring-ownership-using-first-to-claim](TODO put the right link).

### Example 
```python
from __future__ import print_function
import time
import enrollment
from enrollment.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = enrollment.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = enrollment.PublicAPIApi(enrollment.ApiClient(configuration))

try: 
    # Delete an enrollment by ID.
    api_instance.v3_device_enrollmentsid_delete()
except ApiException as e:
    print("Exception when calling PublicAPIApi->v3_device_enrollmentsid_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_device_enrollmentsid_get**
> EnrollmentIdentity v3_device_enrollmentsid_get()

Get details of an enrollment by ID.

To check the enrollment info in detail, for example claming date and expiration date.

### Example 
```python
from __future__ import print_function
import time
import enrollment
from enrollment.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = enrollment.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = enrollment.PublicAPIApi(enrollment.ApiClient(configuration))

try: 
    # Get details of an enrollment by ID.
    api_response = api_instance.v3_device_enrollmentsid_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->v3_device_enrollmentsid_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnrollmentIdentity**](EnrollmentIdentity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

