# statistics.AccountApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_metrics_get**](AccountApi.md#v3_metrics_get) | **GET** /v3/metrics | Provides account-specific statistics for other cloud services.


# **v3_metrics_get**
> SuccessfulResponse v3_metrics_get(include, interval, authorization, start=start, end=end, period=period, limit=limit, after=after, order=order)

Provides account-specific statistics for other cloud services.

This REST API is used to get account-specific statistics.

### Example 
```python
from __future__ import print_function
import time
import statistics
from statistics.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
statistics.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# statistics.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = statistics.AccountApi()
include = 'include_example' # str | A comma-separated list of requested metrics and total_count ( if included, the response will contain total_count to specify total number of records available). Supported values are:  - `transactions` - `registered_devices` - `bootstraps_successful` - `bootstraps_failed` - `bootstraps_pending` - `handshakes_successful` - `handshakes_failed` - `device_server_rest_api_success` - `device_server_rest_api_error` - `total_count` 
interval = 'interval_example' # str | Group data by this interval in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The maximum interval cannot exceed more than one year ( 365 days ) and so the allowed ranges are 5m - 525600m / 1h - 8760h / 1d - 365d / 1w - 53w. 
authorization = 'authorization_example' # str | Bearer {Access Token}. A valid API Gateway access token. The token is validated and the associated account identifier is used to retrieve account-specific statistics. 
start = 'start_example' # str | UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year (365 days). The parameter is not mandatory, if the period is specified.  (optional)
end = 'end_example' # str | UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value.Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year ( 365 days ). The parameter is not mandatory, if the period is specified.  (optional)
period = 'period_example' # str | Period. Fetch the data for the period in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The parameter is not mandatory, if the start and end time are specified. The maximum period cannot exceed more than one year ( 365 days ) and so the allowed ranges are 5m - 525600m / 1h - 8760h / 1d - 365d / 1w - 53w.  (optional)
limit = 56 # int | The number of results to return. Default value is 50, minimum value is 2 and maximum value is 1000.  (optional)
after = 'after_example' # str | The metric ID after which to start fetching.  (optional)
order = 'order_example' # str | The order of the records to return. Available values are ASC and DESC. The default value is ASC.  (optional)

try: 
    # Provides account-specific statistics for other cloud services.
    api_response = api_instance.v3_metrics_get(include, interval, authorization, start=start, end=end, period=period, limit=limit, after=after, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->v3_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| A comma-separated list of requested metrics and total_count ( if included, the response will contain total_count to specify total number of records available). Supported values are:  - &#x60;transactions&#x60; - &#x60;registered_devices&#x60; - &#x60;bootstraps_successful&#x60; - &#x60;bootstraps_failed&#x60; - &#x60;bootstraps_pending&#x60; - &#x60;handshakes_successful&#x60; - &#x60;handshakes_failed&#x60; - &#x60;device_server_rest_api_success&#x60; - &#x60;device_server_rest_api_error&#x60; - &#x60;total_count&#x60;  | 
 **interval** | **str**| Group data by this interval in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The maximum interval cannot exceed more than one year ( 365 days ) and so the allowed ranges are 5m - 525600m / 1h - 8760h / 1d - 365d / 1w - 53w.  | 
 **authorization** | **str**| Bearer {Access Token}. A valid API Gateway access token. The token is validated and the associated account identifier is used to retrieve account-specific statistics.  | 
 **start** | **str**| UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year (365 days). The parameter is not mandatory, if the period is specified.  | [optional] 
 **end** | **str**| UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value.Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year ( 365 days ). The parameter is not mandatory, if the period is specified.  | [optional] 
 **period** | **str**| Period. Fetch the data for the period in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The parameter is not mandatory, if the start and end time are specified. The maximum period cannot exceed more than one year ( 365 days ) and so the allowed ranges are 5m - 525600m / 1h - 8760h / 1d - 365d / 1w - 53w.  | [optional] 
 **limit** | **int**| The number of results to return. Default value is 50, minimum value is 2 and maximum value is 1000.  | [optional] 
 **after** | **str**| The metric ID after which to start fetching.  | [optional] 
 **order** | **str**| The order of the records to return. Available values are ASC and DESC. The default value is ASC.  | [optional] 

### Return type

[**SuccessfulResponse**](SuccessfulResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

