# statistics.StatisticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_metrics_get**](StatisticsApi.md#v3_metrics_get) | **GET** /v3/metrics | provides account specific statistics for other cloud services
[**v3_metrics_global_get**](StatisticsApi.md#v3_metrics_global_get) | **GET** /v3/metrics/global | provides global statistics for other cloud services


# **v3_metrics_get**
> SuccessfulResponse v3_metrics_get(include, start, end, period, interval, authorization)

provides account specific statistics for other cloud services

This REST API will be used to get account specific statistics

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
api_instance = statistics.StatisticsApi()
include = 'include_example' # str | Comma-separated list of requested metrics. Supported values are bootstraps_successful, bootstraps_failed, bootstraps_pending, bootstrap_certificate_create, bootstrap_certificate_delete, connector_certificate_create,  connector_certificate_delete, bootstrap_credentials_get, bootstrap_full_credentials_get, connector_credentials_get, connector_full_credentials_get, connector_ca_rest_api_count, connector_ca_rest_api_error_count
start = 'start_example' # str | UTC time/year/date in RFC3339 format. Fetch data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The parameter is not mandatory, if period specified. 
end = 'end_example' # str | UTC time / year / date in RFC3339 format. Fetch data with timestamp less than this value.Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207.The parameter is not mandatory, if period specified. 
period = 'period_example' # str | Period. Fetch data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if start and end time are specified. 
interval = 'interval_example' # str | Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d. 
authorization = 'authorization_example' # str | Bearer {Access Token}. A valid ApiGateway access token. The token is validated and the associated account identifier is used to retrieve account specific statistics. 

try: 
    # provides account specific statistics for other cloud services
    api_response = api_instance.v3_metrics_get(include, start, end, period, interval, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->v3_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Comma-separated list of requested metrics. Supported values are bootstraps_successful, bootstraps_failed, bootstraps_pending, bootstrap_certificate_create, bootstrap_certificate_delete, connector_certificate_create,  connector_certificate_delete, bootstrap_credentials_get, bootstrap_full_credentials_get, connector_credentials_get, connector_full_credentials_get, connector_ca_rest_api_count, connector_ca_rest_api_error_count | 
 **start** | **str**| UTC time/year/date in RFC3339 format. Fetch data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The parameter is not mandatory, if period specified.  | 
 **end** | **str**| UTC time / year / date in RFC3339 format. Fetch data with timestamp less than this value.Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207.The parameter is not mandatory, if period specified.  | 
 **period** | **str**| Period. Fetch data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if start and end time are specified.  | 
 **interval** | **str**| Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d.  | 
 **authorization** | **str**| Bearer {Access Token}. A valid ApiGateway access token. The token is validated and the associated account identifier is used to retrieve account specific statistics.  | 

### Return type

[**SuccessfulResponse**](SuccessfulResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_metrics_global_get**
> SuccessfulResponse v3_metrics_global_get(include, start, end, period, interval, authorization)

provides global statistics for other cloud services

This REST API will be used to get global statistics

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
api_instance = statistics.StatisticsApi()
include = 'include_example' # str | Comma-separated list of requested metrics. Supported values are bootstraps_successful, bootstraps_failed, bootstraps_pending, bootstrap_certificate_create, bootstrap_certificate_delete, connector_certificate_create,  connector_certificate_delete, bootstrap_credentials_get, bootstrap_full_credentials_get, connector_credentials_get, connector_full_credentials_get, connector_ca_rest_api_count, connector_ca_rest_api_error_count
start = 'start_example' # str | UTC time/year/date in RFC3339 format. Fetch data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The parameter is not mandatory, if period specified. 
end = 'end_example' # str | UTC time / year / date in RFC3339 format. Fetch data with timestamp less than this value.Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207.The parameter is not mandatory, if period specified. 
period = 'period_example' # str | Period. Fetch data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if start and end time are specified. 
interval = 'interval_example' # str | Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d. 
authorization = 'authorization_example' # str | Bearer {Access Token}. A valid ApiGateway access token. The token is validated and the associated account identifier is used to retrieve account specific statistics. 

try: 
    # provides global statistics for other cloud services
    api_response = api_instance.v3_metrics_global_get(include, start, end, period, interval, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->v3_metrics_global_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Comma-separated list of requested metrics. Supported values are bootstraps_successful, bootstraps_failed, bootstraps_pending, bootstrap_certificate_create, bootstrap_certificate_delete, connector_certificate_create,  connector_certificate_delete, bootstrap_credentials_get, bootstrap_full_credentials_get, connector_credentials_get, connector_full_credentials_get, connector_ca_rest_api_count, connector_ca_rest_api_error_count | 
 **start** | **str**| UTC time/year/date in RFC3339 format. Fetch data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The parameter is not mandatory, if period specified.  | 
 **end** | **str**| UTC time / year / date in RFC3339 format. Fetch data with timestamp less than this value.Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207.The parameter is not mandatory, if period specified.  | 
 **period** | **str**| Period. Fetch data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if start and end time are specified.  | 
 **interval** | **str**| Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d.  | 
 **authorization** | **str**| Bearer {Access Token}. A valid ApiGateway access token. The token is validated and the associated account identifier is used to retrieve account specific statistics.  | 

### Return type

[**SuccessfulResponse**](SuccessfulResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

