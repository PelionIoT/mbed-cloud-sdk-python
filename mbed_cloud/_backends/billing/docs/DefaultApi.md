# billing.DefaultApi

All URIs are relative to *http://mbed-billing.example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_v1_build_get**](DefaultApi.md#public_v1_build_get) | **GET** /public/v1/build | Build information
[**public_v1_health_get**](DefaultApi.md#public_v1_health_get) | **GET** /public/v1/health | Service health
[**v1_accounts_get**](DefaultApi.md#v1_accounts_get) | **GET** /v1/accounts | List of accounts
[**v1_activedevices_get**](DefaultApi.md#v1_activedevices_get) | **GET** /v1/activedevices | Active devices per account
[**v1_imports_activedevices_get**](DefaultApi.md#v1_imports_activedevices_get) | **GET** /v1/imports/activedevices | Active devices
[**v1_imports_get**](DefaultApi.md#v1_imports_get) | **GET** /v1/imports | Import log
[**v1_metrics_get**](DefaultApi.md#v1_metrics_get) | **GET** /v1/metrics | System metrics
[**v1_report_activedevices_get**](DefaultApi.md#v1_report_activedevices_get) | **GET** /v1/report/activedevices | Active devices per account in reporting
[**v1_report_get**](DefaultApi.md#v1_report_get) | **GET** /v1/report | Billing report
[**v1_services_get**](DefaultApi.md#v1_services_get) | **GET** /v1/services | Known services
[**v1_stats_get**](DefaultApi.md#v1_stats_get) | **GET** /v1/stats | Account billing data
[**v1_timeseries_get**](DefaultApi.md#v1_timeseries_get) | **GET** /v1/timeseries | Known time series


# **public_v1_build_get**
> BuildInfo public_v1_build_get()

Build information

Get a full build information of the running system.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()

try: 
    # Build information
    api_response = api_instance.public_v1_build_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->public_v1_build_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BuildInfo**](BuildInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_v1_health_get**
> Health public_v1_health_get()

Service health

Check current service health

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()

try: 
    # Service health
    api_response = api_instance.public_v1_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->public_v1_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_accounts_get**
> list[str] v1_accounts_get()

List of accounts

Get a list of all accounts.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()

try: 
    # List of accounts
    api_response = api_instance.v1_accounts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_accounts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_activedevices_get**
> list[ActiveDevice] v1_activedevices_get(account, _from, to)

Active devices per account

Get active devices for an account with specified from and to timestamp. Can be used to fetch active device data for a single month (full or partial) (for example: between 01.04.2017 00:00:00.000Z (inclusive) - 01.05.2017 00:00:00.000Z (exclusive) or between 15.04.2017 15:00:00.000Z (inclusive) - 15.04.2017 16:00.00.000Z (exclusive)).

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()
account = 'account_example' # str | account id
_from = 789 # int | in epoch milliseconds, inclusive.
to = 789 # int | in epoch milliseconds, exclusive. Must be greater than 'from' parameter and be on the same calendar month as 'from' parameter (can be also the absolute beginning of the next month as this parameter is exclusive).

try: 
    # Active devices per account
    api_response = api_instance.v1_activedevices_get(account, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_activedevices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account id | 
 **_from** | **int**| in epoch milliseconds, inclusive. | 
 **to** | **int**| in epoch milliseconds, exclusive. Must be greater than &#39;from&#39; parameter and be on the same calendar month as &#39;from&#39; parameter (can be also the absolute beginning of the next month as this parameter is exclusive). | 

### Return type

[**list[ActiveDevice]**](ActiveDevice.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_imports_activedevices_get**
> list[str] v1_imports_activedevices_get(account, import_id)

Active devices

Get active devices for an account in import log

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()
account = 'account_example' # str | account id
import_id = 789 # int | import id

try: 
    # Active devices
    api_response = api_instance.v1_imports_activedevices_get(account, import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_imports_activedevices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account id | 
 **import_id** | **int**| import id | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_imports_get**
> list[ImportLog] v1_imports_get(account)

Import log

Get full import log for a single account.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()
account = 'account_example' # str | account id

try: 
    # Import log
    api_response = api_instance.v1_imports_get(account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_imports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account id | 

### Return type

[**list[ImportLog]**](ImportLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_metrics_get**
> Metrics v1_metrics_get()

System metrics

Get various internal metrics of the service.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()

try: 
    # System metrics
    api_response = api_instance.v1_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_metrics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Metrics**](Metrics.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_report_activedevices_get**
> list[ActiveDevice] v1_report_activedevices_get(account, month)

Active devices per account in reporting

Get active devices for a commercial account with specified month.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()
account = 'account_example' # str | account id
month = 'month_example' # str | year and month

try: 
    # Active devices per account in reporting
    api_response = api_instance.v1_report_activedevices_get(account, month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_report_activedevices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account id | 
 **month** | **str**| year and month | 

### Return type

[**list[ActiveDevice]**](ActiveDevice.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_report_get**
> Report v1_report_get(month, format=format)

Billing report

Generate billing report for all commercial accounts.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()
month = 'month_example' # str | year and month
format = 'json' # str | report format (optional) (default to json)

try: 
    # Billing report
    api_response = api_instance.v1_report_get(month, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| year and month | 
 **format** | **str**| report format | [optional] [default to json]

### Return type

[**Report**](Report.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_services_get**
> list[Service] v1_services_get()

Known services

Get a full list of known services and when they have last updated data to the system.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()

try: 
    # Known services
    api_response = api_instance.v1_services_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_services_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Service]**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stats_get**
> list[AccountBillingData] v1_stats_get(month, account=account)

Account billing data

Get account billing data for one or multiple accounts for a given month.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()
month = 'month_example' # str | year and month
account = 'account_example' # str | account id (optional)

try: 
    # Account billing data
    api_response = api_instance.v1_stats_get(month, account=account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| year and month | 
 **account** | **str**| account id | [optional] 

### Return type

[**list[AccountBillingData]**](AccountBillingData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_timeseries_get**
> list[ServiceTimeSeries] v1_timeseries_get()

Known time series

Get a full list of consecutive known time series grouped by service and timestamp.

### Example 
```python
from __future__ import print_statement
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = billing.DefaultApi()

try: 
    # Known time series
    api_response = api_instance.v1_timeseries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_timeseries_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServiceTimeSeries]**](ServiceTimeSeries.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

