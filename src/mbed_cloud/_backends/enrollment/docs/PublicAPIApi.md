# enrollment.PublicAPIApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_device_enrollment**](PublicAPIApi.md#create_bulk_device_enrollment) | **POST** /v3/device-enrollments-bulk-uploads | Bulk upload
[**create_device_enrollment**](PublicAPIApi.md#create_device_enrollment) | **POST** /v3/device-enrollments | Place an enrollment claim for one or several devices.
[**delete_bulk_device_enrollment**](PublicAPIApi.md#delete_bulk_device_enrollment) | **POST** /v3/device-enrollments-bulk-deletes | Bulk delete
[**delete_device_enrollment**](PublicAPIApi.md#delete_device_enrollment) | **DELETE** /v3/device-enrollments/{id} | Delete an enrollment by ID.
[**get_bulk_device_enrollment**](PublicAPIApi.md#get_bulk_device_enrollment) | **GET** /v3/device-enrollments-bulk-uploads/{id} | Get bulk upload entity
[**get_bulk_device_enrollment_delete**](PublicAPIApi.md#get_bulk_device_enrollment_delete) | **GET** /v3/device-enrollments-bulk-deletes/{id} | Get bulk delete entity
[**get_device_enrollment**](PublicAPIApi.md#get_device_enrollment) | **GET** /v3/device-enrollments/{id} | Get details of an enrollment by ID.
[**get_device_enrollments**](PublicAPIApi.md#get_device_enrollments) | **GET** /v3/device-enrollments | Get enrollment list.


# **create_bulk_device_enrollment**
> BulkResponse create_bulk_device_enrollment(enrollment_identities)

Bulk upload

With bulk upload, you can upload a `CSV` file containing a number of enrollment IDs.  **Example usage:** ``` curl -X POST \\ -H 'Authorization: Bearer <valid access token>' \\ -F 'enrollment_identities=@/path/to/enrollments/enrollments.csv' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-uploads  ``` **An example `CSV` file:** 1. The first line is assumed to be the header. The content of the header is not validated. 2. Each line can contain comma-separated values, where the first value is always assumed to be the Enrollment ID. 3. Only one enrollment ID is expected per line. 4. Valid enrollments begin with A followed by a - and 95 characters in the format as below. 5. Valid enrollment identities may be enclosed within quotes. 6. UTF-8 encoding is expected.  ``` \"enrollment_identity\" \"A-4E:63:2D:AE:14:BC:D1:09:77:21:95:44:ED:34:06:57:1E:03:B1:EF:0E:F2:59:44:71:93:23:22:15:43:23:12\", \"A-4E:63:2D:AE:14:BC:D1:09:77:21:95:44:ED:34:06:57:1E:03:B1:EF:0E:F2:59:25:48:44:71:22:15:43:23:12\",  ``` 

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
enrollment_identities = '/path/to/file.txt' # file | The `CSV` file containing the enrollment IDs. The maximum file size is 10MB. 

try: 
    # Bulk upload
    api_response = api_instance.create_bulk_device_enrollment(enrollment_identities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->create_bulk_device_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_identities** | **file**| The &#x60;CSV&#x60; file containing the enrollment IDs. The maximum file size is 10MB.  | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_enrollment**
> EnrollmentIdentity create_device_enrollment(enrollment_identity)

Place an enrollment claim for one or several devices.

When the device connects to the bootstrap server and provides the enrollment ID, it will be assigned to your account. <br> **Example usage:** ``` curl -X POST \\ -H 'Authorization: Bearer <valid access token>' \\ -H 'content-type: application/json' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments \\ -d '{\"enrollment_identity\": \"A-35:e7:72:8a:07:50:3b:3d:75:96:57:52:72:41:0d:78:cc:c6:e5:53:48:c6:65:58:5b:fa:af:4d:2d:73:95:c5\"}' ``` 

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

# **delete_bulk_device_enrollment**
> BulkResponse delete_bulk_device_enrollment(enrollment_identities)

Bulk delete

With bulk delete, you can upload a `CSV` file containing a number of enrollment IDs to be deleted.  **Example usage:** ``` curl -X POST \\ -H 'Authorization: Bearer <valid access token>' \\ -F 'enrollment_identities=@/path/to/enrollments/enrollments.csv' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-deletes  ``` **An example `CSV` file:** 1. The first line is assumed to be the header. The content of the header is not validated. 2. Each line can contain comma-separated values, where the first value is always assumed to be the Enrollment ID. 3. Only one enrollment ID is expected per line. 4. Valid enrollments begin with A followed by a - and 95 characters in the format as below. 5. Valid enrollment identities may be enclosed within quotes. 6. UTF-8 encoding is expected.  ``` \"enrollment_identity\" \"A-4E:63:2D:AE:14:BC:D1:09:77:21:95:44:ED:34:06:57:1E:03:B1:EF:0E:F2:59:44:71:93:23:22:15:43:23:12\", \"A-4E:63:2D:AE:14:BC:D1:09:77:21:95:44:ED:34:06:57:1E:03:B1:EF:0E:F2:59:25:48:44:71:22:15:43:23:12\",  ``` 

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
enrollment_identities = '/path/to/file.txt' # file | The `CSV` file containing the enrollment IDs. The maximum file size is 10MB. 

try: 
    # Bulk delete
    api_response = api_instance.delete_bulk_device_enrollment(enrollment_identities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->delete_bulk_device_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_identities** | **file**| The &#x60;CSV&#x60; file containing the enrollment IDs. The maximum file size is 10MB.  | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_enrollment**
> delete_device_enrollment(id)

Delete an enrollment by ID.

To free a device from your account you can delete the enrollment claim. To bypass the device ownership, you need to delete the enrollment and do a factory reset for the device. For more information, see [Transferring the ownership using First-to-Claim](/docs/current/connecting/device-ownership.html). <br> **Example usage:** ``` curl -X DELETE \\ -H 'Authorization: Bearer <valid access token>' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments/{id} ``` 

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
id = 'id_example' # str | Enrollment identity.

try: 
    # Delete an enrollment by ID.
    api_instance.delete_device_enrollment(id)
except ApiException as e:
    print("Exception when calling PublicAPIApi->delete_device_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment identity. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_device_enrollment**
> BulkResponse get_bulk_device_enrollment(id)

Get bulk upload entity

Provides information on bulk upload for the given ID. For example, the bulk status and the number of processed enrollment identities. Also links to the bulk upload reports are provided. **Example usage:** ``` curl -X GET \\ -H 'Authorization: Bearer <valid access token>' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-uploads/{id} ``` 

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
id = 'id_example' # str | Bulk create task entity ID

try: 
    # Get bulk upload entity
    api_response = api_instance.get_bulk_device_enrollment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->get_bulk_device_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bulk create task entity ID | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_device_enrollment_delete**
> BulkResponse get_bulk_device_enrollment_delete(id)

Get bulk delete entity

Provides information on bulk delete for the given ID. For example, the bulk status and the number of processed enrollment identities. Also links to the bulk delete reports are provided. **Example usage:** ``` curl -X GET \\ -H 'Authorization: Bearer <valid access token>' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-deletes/{id} ``` 

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
id = 'id_example' # str | Bulk delete task entity ID

try: 
    # Get bulk delete entity
    api_response = api_instance.get_bulk_device_enrollment_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAPIApi->get_bulk_device_enrollment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bulk delete task entity ID | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_enrollment**
> EnrollmentIdentity get_device_enrollment(id)

Get details of an enrollment by ID.

To check the enrollment info in detail, for example date of claim and expiration date. **Example usage:** ``` curl -X GET \\ -H 'Authorization: Bearer <valid access token>' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments/{id} ``` 

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
id = 'id_example' # str | Enrollment identity.

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
 **id** | **str**| Enrollment identity. | 

### Return type

[**EnrollmentIdentity**](EnrollmentIdentity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_enrollments**
> EnrollmentIdentities get_device_enrollments(limit=limit, after=after, order=order, include=include)

Get enrollment list.

Provides a list of pending and claimed enrollments. **Example usage:** ``` curl -X GET \\ -H 'Authorization: Bearer <valid access token>' \\ https://api.us-east-1.mbedcloud.com/v3/device-enrollments ``` With query parameters: ``` curl -X GET \\ -H 'Authorization: Bearer <valid access token>' \\ 'https://api.us-east-1.mbedcloud.com/v3/device-enrollments?limit=10' ``` 

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
include = 'include_example' # str | Comma-separated additional data to return. Currently supported: total_count. (optional)

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
 **include** | **str**| Comma-separated additional data to return. Currently supported: total_count. | [optional] 

### Return type

[**EnrollmentIdentities**](EnrollmentIdentities.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

