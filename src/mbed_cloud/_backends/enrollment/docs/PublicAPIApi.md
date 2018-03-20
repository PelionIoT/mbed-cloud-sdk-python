# enrollment.PublicAPIApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_enrollment**](PublicAPIApi.md#create_device_enrollment) | **POST** /v3/device-enrollments | Place an enrollment claim for one or several devices.
[**delete_device_enrollment**](PublicAPIApi.md#delete_device_enrollment) | **DELETE** /v3/device-enrollments/{id} | Delete an enrollment by ID.
[**get_device_enrollment**](PublicAPIApi.md#get_device_enrollment) | **GET** /v3/device-enrollments/{id} | Get details of an enrollment by ID.
[**get_device_enrollments**](PublicAPIApi.md#get_device_enrollments) | **GET** /v3/device-enrollments | Get enrollment list.


# **create_device_enrollment**
> EnrollmentIdentity create_device_enrollment(enrollment_identity)

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
    api_response = api_instance.create_device_enrollment(enrollment_identity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->create_device_enrollment: %s\n" % e)
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

# **delete_device_enrollment**
> delete_device_enrollment(id)

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
id = 'id_example' # str | Enrollment identity internal id

try: 
    # Delete an enrollment by ID.
    api_instance.delete_device_enrollment(id)
except ApiException as e:
    print("Exception when calling PublicAPIApi->delete_device_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment identity internal id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_enrollment**
> EnrollmentIdentity get_device_enrollment(id)

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
id = 'id_example' # str | Enrollment identity internal id

try: 
    # Get details of an enrollment by ID.
    api_response = api_instance.get_device_enrollment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->get_device_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment identity internal id | 

### Return type

[**EnrollmentIdentity**](EnrollmentIdentity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_enrollments**
> EnrollmentIdentities get_device_enrollments(limit=limit, after=after, order=order, include=include)

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
include = 'include_example' # str | Comma separate additional data to return. Currently supported: total_count (optional)

try: 
    # Get enrollment list.
    api_response = api_instance.get_device_enrollments(limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->get_device_enrollments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to be returned. Between 2 and 1000, inclusive. | [optional] 
 **after** | **str**| Entity ID to fetch after. | [optional] 
 **order** | **str**| ASC or DESC | [optional] [default to ASC]
 **include** | **str**| Comma separate additional data to return. Currently supported: total_count | [optional] 

### Return type

[**EnrollmentIdentities**](EnrollmentIdentities.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

