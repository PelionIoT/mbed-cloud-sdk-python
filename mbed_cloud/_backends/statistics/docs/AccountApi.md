# statistics.AccountApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_metrics_get**](AccountApi.md#v3_metrics_get) | **GET** /v3/metrics | Provides account-specific statistics for other cloud services.


# **v3_metrics_get**
> SuccessfulResponse v3_metrics_get(include, interval, authorization, start=start, end=end, period=period)

Provides account-specific statistics for other cloud services.

This REST API is used to get account-specific statistics.

### Example 
```python
from __future__ import print_statement
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
include = 'include_example' # str | A comma-separated list of requested metrics. Supported values are:  - `transactions` - `registered_devices` - `bootstraps_successful` - `bootstraps_failed` - `bootstraps_pending` - `handshakes_successful` - `handshakes_failed` - `device_server_rest_api_success` - `device_server_rest_api_error` 
interval = 'interval_example' # str | Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d. Maximum allowed interval is 9999[h/w/d]. 
authorization = 'authorization_example' # str | Bearer {Access Token}. A valid API Gateway access token. The token is validated and the associated account identifier is used to retrieve account-specific statistics. 
start = 'start_example' # str | UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207. The parameter is not mandatory, if the period is specified.  (optional)
end = 'end_example' # str | UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value.Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.The parameter is not mandatory, if the period is specified.  (optional)
period = 'period_example' # str | Period. Fetch the data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if the start and end time are specified. Maximum allowed period is 9999[h/w/d].  (optional)

try: 
    # Provides account-specific statistics for other cloud services.
    api_response = api_instance.v3_metrics_get(include, interval, authorization, start=start, end=end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->v3_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| A comma-separated list of requested metrics. Supported values are:  - &#x60;transactions&#x60; - &#x60;registered_devices&#x60; - &#x60;bootstraps_successful&#x60; - &#x60;bootstraps_failed&#x60; - &#x60;bootstraps_pending&#x60; - &#x60;handshakes_successful&#x60; - &#x60;handshakes_failed&#x60; - &#x60;device_server_rest_api_success&#x60; - &#x60;device_server_rest_api_error&#x60;  | 
 **interval** | **str**| Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d. Maximum allowed interval is 9999[h/w/d].  | 
 **authorization** | **str**| Bearer {Access Token}. A valid API Gateway access token. The token is validated and the associated account identifier is used to retrieve account-specific statistics.  | 
 **start** | **str**| UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207. The parameter is not mandatory, if the period is specified.  | [optional] 
 **end** | **str**| UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value.Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.The parameter is not mandatory, if the period is specified.  | [optional] 
 **period** | **str**| Period. Fetch the data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if the start and end time are specified. Maximum allowed period is 9999[h/w/d].  | [optional] 

### Return type

[**SuccessfulResponse**](SuccessfulResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

