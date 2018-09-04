# billing.DefaultApi

All URIs are relative to *http://mbed-billing.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_report**](DefaultApi.md#get_billing_report) | **GET** /v3/billing-report | Get billing report.
[**get_billing_report_active_devices**](DefaultApi.md#get_billing_report_active_devices) | **GET** /v3/billing-report-active-devices | Get raw active devices billing data for the month.
[**get_billing_report_firmware_updates**](DefaultApi.md#get_billing_report_firmware_updates) | **GET** /v3/billing-report-firmware-updates | Get raw firmware updates billing data for the month.
[**get_service_package_quota**](DefaultApi.md#get_service_package_quota) | **GET** /v3/service-packages-quota | Service package quota
[**get_service_package_quota_history**](DefaultApi.md#get_service_package_quota_history) | **GET** /v3/service-packages-quota-history | Service package quota history
[**get_service_packages**](DefaultApi.md#get_service_packages) | **GET** /v3/service-packages | Get all service packages.


# **get_billing_report**
> ReportResponse get_billing_report(month)

Get billing report.

Fetch generated billing report for the currently authenticated commercial non-subtenant account. Billing reports for subtenant accounts are included in their aggregator's billing report response.

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
month = 'month_example' # str | Queried year and month of billing report

try: 
    # Get billing report.
    api_response = api_instance.get_billing_report(month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_billing_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| Queried year and month of billing report | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_report_active_devices**
> BillingReportRawDataResponse get_billing_report_active_devices(month)

Get raw active devices billing data for the month.

Fetch raw active devices billing data for the currently authenticated commercial non-subtenant account. They are supplementary data for billing report. The raw active devices billing data for subtenant accounts are included in their aggregator's raw active devices billing data. Endpoint returns the URL to download the gzipped csv file. First line of the file is the header which describes information of active devices included, e.g. active device id.

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
month = 'month_example' # str | Queried year and month of billing report

try: 
    # Get raw active devices billing data for the month.
    api_response = api_instance.get_billing_report_active_devices(month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_billing_report_active_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| Queried year and month of billing report | 

### Return type

[**BillingReportRawDataResponse**](BillingReportRawDataResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_report_firmware_updates**
> BillingReportRawDataResponse get_billing_report_firmware_updates(month)

Get raw firmware updates billing data for the month.

Fetch raw firmware updates billing data for the currently authenticated commercial non-subtenant account. They are supplementary data for billing report. The raw firmware updates billing data for subtenant accounts are included in their aggregator's raw firmware updates billing data. Endpoint returns the URL to download the gzipped csv file. First line of the file is the header which describes information of firmware updates included, e.g. firmware update device id.

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
month = 'month_example' # str | Queried year and month of billing report

try: 
    # Get raw firmware updates billing data for the month.
    api_response = api_instance.get_billing_report_firmware_updates(month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_billing_report_firmware_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| Queried year and month of billing report | 

### Return type

[**BillingReportRawDataResponse**](BillingReportRawDataResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

