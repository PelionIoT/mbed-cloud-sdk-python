# statistics.StatisticsApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](StatisticsApi.md#get_metrics) | **GET** /v3/metrics | Provides account-specific statistics for other cloud services.


# **get_metrics**
> SuccessfulResponse get_metrics(include, interval, start=start, end=end, period=period, limit=limit, after=after, order=order)

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
configuration = statistics.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = statistics.StatisticsApi(statistics.ApiClient(configuration))
include = 'include_example' # str | A comma-separated list of requested metrics and total_count (if included, the response will contain total_count to specify the total number of records available). Supported values are:  - `transactions` - `full_registrations` - `registration_updates` - `deleted_registrations` - `expired_registrations` - `bootstraps_successful` - `bootstraps_failed` - `bootstraps_pending` - `handshakes_successful` - `connect_rest_api_success` - `connect_rest_api_error` - `device_proxy_request_success` - `device_proxy_request_error` - `device_subscription_request_success` - `device_subscription_request_error` - `device_observations` - `total_count`  **Note:**  The metrics device_proxy_request_success, device_proxy_request_error, device_subscription_request_success, device_subscription_request_error and device_observations monitor only the response from the device to Mbed Cloud Connect and they do not confirm that the response is delivered to client callback URLs used when you try to access device resources using  [Connect API](/docs/current/service-api-references/mbed-cloud-connect.html) endpoints. New metrics will be added to monitor the response delivery to client callback URLs later.  **Example usage:**  ``` curl  -X GET \\       -H \"Authorization : Bearer <valid access Token>\"        'https://api.us-east-1.mbedcloud.com/v3/metrics?include=transactions,total_count&start=20170207&end=20170407&interval=1d'  {     \"object\": \"list\",     \"limit\": 20,     \"total_count\": 54,     \"after\": \"2017-07-26T00:00:00Z\",     \"has_more\": true,     \"data\": [         {             \"id\": \"015d8157c800015e306fffff005374617473000\",             \"timestamp\": \"2017-07-27T00:00:00Z\",             \"transactions\": 27366         },         {             \"id\": \"015d867e2400015e306fffff005374617473000\",             \"timestamp\": \"2017-07-28T00:00:00Z\",             \"transactions\": 27480         }     ] } ``` 
interval = 'interval_example' # str | Group the data by this interval in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The maximum interval cannot exceed one year (365 days). The allowed ranges are 5m-525600m/1h-8760h/1d-365d/1w-53w. 
start = '2013-10-20' # date | UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year (365 days). The parameter is not mandatory, if the period is specified.  (optional)
end = '2013-10-20' # date | UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year (365 days). The parameter is not mandatory, if the period is specified.  (optional)
period = 'period_example' # str | Period. Fetch the data for the period in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The parameter is not mandatory, if the start and end time are specified. The maximum period cannot exceed one year (365 days). The allowed ranges are 5m-525600m/1h-8760h/1d-365d/1w-53w.  (optional)
limit = 56 # int | The number of results to return. The default value is 50, minimum 2 and maximum 1000.  (optional)
after = 'after_example' # str | The metric ID after which to start fetching. This also can be used for pagination as follows.  **Example usage:**  ``` curl  -X GET \\       -H \"Authorization : Bearer <valid access Token>\"        'https://api.us-east-1.mbedcloud.com/v3/metrics?include=transactions,total_count&start=20170707&end=20170829&interval=1d&limit=20' {    \"object\": \"list\",    \"limit\": 20,    \"total_count\": 54,    \"has_more\": true,    \"data\": [        {            \"id\": \"015d1a589800015e306fffff005374617473000\",            \"timestamp\": \"2017-07-07T00:00:00Z\",            \"transactions\": 26381        },        .        .        .        {            \"id\": \"015d7c316c00015e306fffff005374617473000\",            \"timestamp\": \"2017-07-26T00:00:00Z\",            \"transactions\": 25569        }    ] } ```  If the parameter “has more” is true, it indicates that the list is not complete and more values are available. You can give the last ID of the list as the value of the “after” query parameter, and you get the next page of values. You can keep doing this until “has more” is false. ``` curl -X GET \\      -H \"Authorization : Bearer <valid access Token>\"      'https://api.us-east-1.mbedcloud.com/v3/metrics?include=transactions,total_count&start=20170707&end=20170829&interval=1d&limit=20&after=015d7c316c00015e306fffff005374617473000'  {    \"object\": \"list\",    \"limit\": 20,    \"total_count\": 54,    \"after\": \"2017-07-26T00:00:00Z\",    \"has_more\": true,    \"data\": [        {            \"id\": \"015d8157c800015e306fffff005374617473000\",            \"timestamp\": \"2017-07-27T00:00:00Z\",            \"transactions\": 27366        },      .      .      .        {            \"id\": \"015de3309c00015e306fffff005374617473000\",            \"timestamp\": \"2017-08-15T00:00:00Z\",            \"transactions\": 24707        }    ] } ```  (optional)
order = 'order_example' # str | The order of the records to return. Available values are ASC and DESC. The default value is ASC.  (optional)

try: 
    # Provides account-specific statistics for other cloud services.
    api_response = api_instance.get_metrics(include, interval, start=start, end=end, period=period, limit=limit, after=after, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| A comma-separated list of requested metrics and total_count (if included, the response will contain total_count to specify the total number of records available). Supported values are:  - &#x60;transactions&#x60; - &#x60;full_registrations&#x60; - &#x60;registration_updates&#x60; - &#x60;deleted_registrations&#x60; - &#x60;expired_registrations&#x60; - &#x60;bootstraps_successful&#x60; - &#x60;bootstraps_failed&#x60; - &#x60;bootstraps_pending&#x60; - &#x60;handshakes_successful&#x60; - &#x60;connect_rest_api_success&#x60; - &#x60;connect_rest_api_error&#x60; - &#x60;device_proxy_request_success&#x60; - &#x60;device_proxy_request_error&#x60; - &#x60;device_subscription_request_success&#x60; - &#x60;device_subscription_request_error&#x60; - &#x60;device_observations&#x60; - &#x60;total_count&#x60;  **Note:**  The metrics device_proxy_request_success, device_proxy_request_error, device_subscription_request_success, device_subscription_request_error and device_observations monitor only the response from the device to Mbed Cloud Connect and they do not confirm that the response is delivered to client callback URLs used when you try to access device resources using  [Connect API](/docs/current/service-api-references/mbed-cloud-connect.html) endpoints. New metrics will be added to monitor the response delivery to client callback URLs later.  **Example usage:**  &#x60;&#x60;&#x60; curl  -X GET \\       -H \&quot;Authorization : Bearer &lt;valid access Token&gt;\&quot;        &#39;https://api.us-east-1.mbedcloud.com/v3/metrics?include&#x3D;transactions,total_count&amp;start&#x3D;20170207&amp;end&#x3D;20170407&amp;interval&#x3D;1d&#39;  {     \&quot;object\&quot;: \&quot;list\&quot;,     \&quot;limit\&quot;: 20,     \&quot;total_count\&quot;: 54,     \&quot;after\&quot;: \&quot;2017-07-26T00:00:00Z\&quot;,     \&quot;has_more\&quot;: true,     \&quot;data\&quot;: [         {             \&quot;id\&quot;: \&quot;015d8157c800015e306fffff005374617473000\&quot;,             \&quot;timestamp\&quot;: \&quot;2017-07-27T00:00:00Z\&quot;,             \&quot;transactions\&quot;: 27366         },         {             \&quot;id\&quot;: \&quot;015d867e2400015e306fffff005374617473000\&quot;,             \&quot;timestamp\&quot;: \&quot;2017-07-28T00:00:00Z\&quot;,             \&quot;transactions\&quot;: 27480         }     ] } &#x60;&#x60;&#x60;  | 
 **interval** | **str**| Group the data by this interval in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The maximum interval cannot exceed one year (365 days). The allowed ranges are 5m-525600m/1h-8760h/1d-365d/1w-53w.  | 
 **start** | **date**| UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year (365 days). The parameter is not mandatory, if the period is specified.  | [optional] 
 **end** | **date**| UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value. Sample values: 20170207T092056990Z / 2017-02-07T09:20:56.990Z / 2017 / 20170207. The maximum time between start and end parameters cannot exceed more than one year (365 days). The parameter is not mandatory, if the period is specified.  | [optional] 
 **period** | **str**| Period. Fetch the data for the period in minutes, hours, days or weeks. Sample values: 5m, 2h, 3d, 4w. The parameter is not mandatory, if the start and end time are specified. The maximum period cannot exceed one year (365 days). The allowed ranges are 5m-525600m/1h-8760h/1d-365d/1w-53w.  | [optional] 
 **limit** | **int**| The number of results to return. The default value is 50, minimum 2 and maximum 1000.  | [optional] 
 **after** | **str**| The metric ID after which to start fetching. This also can be used for pagination as follows.  **Example usage:**  &#x60;&#x60;&#x60; curl  -X GET \\       -H \&quot;Authorization : Bearer &lt;valid access Token&gt;\&quot;        &#39;https://api.us-east-1.mbedcloud.com/v3/metrics?include&#x3D;transactions,total_count&amp;start&#x3D;20170707&amp;end&#x3D;20170829&amp;interval&#x3D;1d&amp;limit&#x3D;20&#39; {    \&quot;object\&quot;: \&quot;list\&quot;,    \&quot;limit\&quot;: 20,    \&quot;total_count\&quot;: 54,    \&quot;has_more\&quot;: true,    \&quot;data\&quot;: [        {            \&quot;id\&quot;: \&quot;015d1a589800015e306fffff005374617473000\&quot;,            \&quot;timestamp\&quot;: \&quot;2017-07-07T00:00:00Z\&quot;,            \&quot;transactions\&quot;: 26381        },        .        .        .        {            \&quot;id\&quot;: \&quot;015d7c316c00015e306fffff005374617473000\&quot;,            \&quot;timestamp\&quot;: \&quot;2017-07-26T00:00:00Z\&quot;,            \&quot;transactions\&quot;: 25569        }    ] } &#x60;&#x60;&#x60;  If the parameter “has more” is true, it indicates that the list is not complete and more values are available. You can give the last ID of the list as the value of the “after” query parameter, and you get the next page of values. You can keep doing this until “has more” is false. &#x60;&#x60;&#x60; curl -X GET \\      -H \&quot;Authorization : Bearer &lt;valid access Token&gt;\&quot;      &#39;https://api.us-east-1.mbedcloud.com/v3/metrics?include&#x3D;transactions,total_count&amp;start&#x3D;20170707&amp;end&#x3D;20170829&amp;interval&#x3D;1d&amp;limit&#x3D;20&amp;after&#x3D;015d7c316c00015e306fffff005374617473000&#39;  {    \&quot;object\&quot;: \&quot;list\&quot;,    \&quot;limit\&quot;: 20,    \&quot;total_count\&quot;: 54,    \&quot;after\&quot;: \&quot;2017-07-26T00:00:00Z\&quot;,    \&quot;has_more\&quot;: true,    \&quot;data\&quot;: [        {            \&quot;id\&quot;: \&quot;015d8157c800015e306fffff005374617473000\&quot;,            \&quot;timestamp\&quot;: \&quot;2017-07-27T00:00:00Z\&quot;,            \&quot;transactions\&quot;: 27366        },      .      .      .        {            \&quot;id\&quot;: \&quot;015de3309c00015e306fffff005374617473000\&quot;,            \&quot;timestamp\&quot;: \&quot;2017-08-15T00:00:00Z\&quot;,            \&quot;transactions\&quot;: 24707        }    ] } &#x60;&#x60;&#x60;  | [optional] 
 **order** | **str**| The order of the records to return. Available values are ASC and DESC. The default value is ASC.  | [optional] 

### Return type

[**SuccessfulResponse**](SuccessfulResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

