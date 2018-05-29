# billing.DefaultApi

All URIs are relative to *http://mbed-billing.example.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_package_quota**](DefaultApi.md#get_service_package_quota) | **GET** /service-packages-quota | Service package quota
[**get_service_package_quota_history**](DefaultApi.md#get_service_package_quota_history) | **GET** /service-packages-quota-history | Service package quota history
[**get_service_packages**](DefaultApi.md#get_service_packages) | **GET** /service-packages | Get all service packages.


# **get_service_package_quota**
> ServicePackageQuota get_service_package_quota()

Service package quota

Get the available firmware update quota for the currently authenticated commercial acount.

### Example 
```python
from __future__ import print_function
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = billing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi(billing.ApiClient(configuration))

try: 
    # Service package quota
    api_response = api_instance.get_service_package_quota()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_package_quota: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServicePackageQuota**](ServicePackageQuota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_package_quota_history**
> ServicePackageQuotaHistoryResponse get_service_package_quota_history(limit=limit, after=after)

Service package quota history

Get your quota usage history. This API is available for commercial accounts. Aggregator accounts can see own and subtenant quota usage data. History data is ordered in ascending order based on the added timestamp. 

### Example 
```python
from __future__ import print_function
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = billing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi(billing.ApiClient(configuration))
limit = 56 # int | Maximum amount of quota history entries contained in one paged response. (optional)
after = 'after_example' # str | To fetch after which quota history id. The results will contain entries after specified entry. (optional)

try: 
    # Service package quota history
    api_response = api_instance.get_service_package_quota_history(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_package_quota_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum amount of quota history entries contained in one paged response. | [optional] 
 **after** | **str**| To fetch after which quota history id. The results will contain entries after specified entry. | [optional] 

### Return type

[**ServicePackageQuotaHistoryResponse**](ServicePackageQuotaHistoryResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_packages**
> ServicePackagesResponse get_service_packages()

Get all service packages.

Get information of all service packages for currently authenticated commercial account. The response is returned with descending order by service package created timestamp, listing first pending service package, then active service package, and previous service packages at last.

### Example 
```python
from __future__ import print_function
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = billing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi(billing.ApiClient(configuration))

try: 
    # Get all service packages.
    api_response = api_instance.get_service_packages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_packages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServicePackagesResponse**](ServicePackagesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

