# billing.DefaultApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_report**](DefaultApi.md#get_billing_report) | **GET** /v3/billing-report | Get billing report.
[**get_billing_report_active_devices**](DefaultApi.md#get_billing_report_active_devices) | **GET** /v3/billing-report-active-devices | Get raw billing data of the active devices for the month.
[**get_billing_report_firmware_updates**](DefaultApi.md#get_billing_report_firmware_updates) | **GET** /v3/billing-report-firmware-updates | Get raw billing data of the firmware updates for the month.
[**get_service_package_quota**](DefaultApi.md#get_service_package_quota) | **GET** /v3/service-packages-quota | Service package quota.
[**get_service_package_quota_history**](DefaultApi.md#get_service_package_quota_history) | **GET** /v3/service-packages-quota-history | Service package quota history.
[**get_service_packages**](DefaultApi.md#get_service_packages) | **GET** /v3/service-packages | Get all service packages.


# **get_billing_report**
> ReportResponse get_billing_report(month)

Get billing report.

Fetch the billing report generated for the currently authenticated commercial non-subtenant account. Billing reports for subtenant accounts are included in their aggregator's billing report response.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v3/billing-report?month=2018-07 -H 'authorization: Bearer {api-key}'

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
month = 'month_example' # str | Queried year and month of billing report.

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
 **month** | **str**| Queried year and month of billing report. | 

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

Get raw billing data of the active devices for the month.

Fetch the raw billing data of the active devices for the currently authenticated commercial non-subtenant account. This is supplementary data for the billing report. The raw billing data of the active devices for subtenant accounts are included in their aggregator's raw billing data of the active devices. The endpoint returns the URL to download the gzipped CSV file. The first line is the header providing information on the active devices. For example, the ID of an active device.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v3/billing-report-active-devices?month=2018-07 -H 'authorization: Bearer {api-key}'

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
month = 'month_example' # str | Queried year and month of billing report.

try: 
    # Get raw billing data of the active devices for the month.
    api_response = api_instance.get_billing_report_active_devices(month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_billing_report_active_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| Queried year and month of billing report. | 

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

Get raw billing data of the firmware updates for the month.

Fetch raw billing data of the firmware updates for the currently authenticated commercial non-subtenant account. This is supplementary data for the billing report. The raw billing data of the firmware updates for subtenant accounts are included in their aggregator's raw billing data of the firmware updates. The endpoint returns the URL to download the gzipped CSV file. The first line is the header providing information on the firmware updates. For example, the ID of an firmware update.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v3/billing-report-firmware-updates?month=2018-07 -H 'authorization: Bearer {api-key}'

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
month = 'month_example' # str | Queried year and month of billing report.

try: 
    # Get raw billing data of the firmware updates for the month.
    api_response = api_instance.get_billing_report_firmware_updates(month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_billing_report_firmware_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| Queried year and month of billing report. | 

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

Service package quota.

Get the available firmware update quota for the currently authenticated commercial account.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v3/service-packages-quota -H 'authorization: Bearer {api-key}' 

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
    # Service package quota.
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

Service package quota history.

Get your quota usage history. This API is available for commercial accounts. Aggregator accounts can see own and subtenant quota usage data. History data is ordered in ascending order based on the added timestamp.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v3/service-packages-quota-history -H 'authorization: Bearer {api-key}' 

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
after = 'after_example' # str | To fetch after which quota history ID. The results will contain entries after specified entry. (optional)

try: 
    # Service package quota history.
    api_response = api_instance.get_service_package_quota_history(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_package_quota_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum amount of quota history entries contained in one paged response. | [optional] 
 **after** | **str**| To fetch after which quota history ID. The results will contain entries after specified entry. | [optional] 

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

Get information of all service packages for the currently authenticated commercial account. The response is returned in descending order by service package created timestamp, listing first the pending service package, then the active service package and finally the previous service packages.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v3/service-packages -H 'authorization: Bearer {api-key}'

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

