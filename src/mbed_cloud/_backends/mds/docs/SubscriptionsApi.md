# mds.SubscriptionsApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resource_subscription**](SubscriptionsApi.md#add_resource_subscription) | **PUT** /v2/subscriptions/{device-id}/{resourcePath} | Subscribe to a resource path
[**check_resource_subscription**](SubscriptionsApi.md#check_resource_subscription) | **GET** /v2/subscriptions/{device-id}/{resourcePath} | Read subscription status
[**delete_endpoint_subscriptions**](SubscriptionsApi.md#delete_endpoint_subscriptions) | **DELETE** /v2/subscriptions/{device-id} | Delete subscriptions from an endpoint
[**delete_pre_subscriptions**](SubscriptionsApi.md#delete_pre_subscriptions) | **DELETE** /v2/subscriptions | Remove pre-subscriptions
[**delete_resource_subscription**](SubscriptionsApi.md#delete_resource_subscription) | **DELETE** /v2/subscriptions/{device-id}/{resourcePath} | Remove a subscription
[**get_endpoint_subscriptions**](SubscriptionsApi.md#get_endpoint_subscriptions) | **GET** /v2/subscriptions/{device-id} | Read endpoints subscriptions
[**get_pre_subscriptions**](SubscriptionsApi.md#get_pre_subscriptions) | **GET** /v2/subscriptions | Get pre-subscriptions
[**update_pre_subscriptions**](SubscriptionsApi.md#update_pre_subscriptions) | **PUT** /v2/subscriptions | Set pre-subscriptions


# **add_resource_subscription**
> add_resource_subscription(device_id, _resource_path)

Subscribe to a resource path

The Device Management Connect eventing model consists of observable resources.  This means that endpoints can deliver updated resource content, periodically or with a more sophisticated solution-dependent logic. The OMA LwM2M resource model including objects, object instances, resources and resource instances is also supported.  Applications can subscribe to objects, object instances or individual resources to make the device to provide value change notifications to Device Management Connect service. An application needs to call a `/notification/callback` method to get Device Management Connect to push notifications of the resource changes.  **Notification rules**  A web application can place dynamic observation rules for individual Object Instances and Resources to define when the device sends observations. More information in [Notification rules](/docs/current/connecting/resource-change-webapp.html).  All manual subscriptions are removed during a full device registration and applications need to re-subscribe at that point. To avoid this, you can use `/subscriptions` to set a pre-subscription.  **Example usage:**      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/subscriptions/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 

try: 
    # Subscribe to a resource path
    api_instance.add_resource_subscription(device_id, _resource_path)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_resource_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_resource_subscription**
> check_resource_subscription(device_id, _resource_path)

Read subscription status

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 

try: 
    # Read subscription status
    api_instance.check_resource_subscription(device_id, _resource_path)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->check_resource_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint_subscriptions**
> delete_endpoint_subscriptions(device_id)

Delete subscriptions from an endpoint

Deletes all resource subscriptions in a single endpoint.  **Example usage:**      curl -X DELETE \\       https://api.us-east-1.mbedcloud.com/v2/subscriptions/{device-id} \\       -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here. 

try: 
    # Delete subscriptions from an endpoint
    api_instance.delete_endpoint_subscriptions(device_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_endpoint_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pre_subscriptions**
> delete_pre_subscriptions()

Remove pre-subscriptions

Removes pre-subscriptions.  **Example usage:**      curl -X DELETE https://api.us-east-1.mbedcloud.com/v2/subscriptions -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))

try: 
    # Remove pre-subscriptions
    api_instance.delete_pre_subscriptions()
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_pre_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_subscription**
> delete_resource_subscription(device_id, _resource_path)

Remove a subscription

To remove an existing subscription from a resource path.  **Example usage:**      curl -X DELETE \\       https://api.us-east-1.mbedcloud.com/v2/subscriptions/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 

try: 
    # Remove a subscription
    api_instance.delete_resource_subscription(device_id, _resource_path)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_resource_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_subscriptions**
> str get_endpoint_subscriptions(device_id)

Read endpoints subscriptions

Lists all subscribed resources from a single endpoint.  **Example usage:**      curl -X GET \\       https://api.us-east-1.mbedcloud.com/v2/subscriptions/{device-id} \\       -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))
device_id = 'device_id_example' # str | A unique Device Management device ID for the endpoint. Note that ID must be an exact match. You cannot use wildcards here. 

try: 
    # Read endpoints subscriptions
    api_response = api_instance.get_endpoint_subscriptions(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_endpoint_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| A unique Device Management device ID for the endpoint. Note that ID must be an exact match. You cannot use wildcards here.  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/uri-list

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_subscriptions**
> PresubscriptionArray get_pre_subscriptions()

Get pre-subscriptions

You can retrieve the pre-subscription data with the GET operation. The server returns with the same JSON structure as described above. If there are no pre-subscribed resources, it returns with an empty array.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/subscriptions -H 'authorization: Bearer {api-key}' 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))

try: 
    # Get pre-subscriptions
    api_response = api_instance.get_pre_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_pre_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PresubscriptionArray**](PresubscriptionArray.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pre_subscriptions**
> update_pre_subscriptions(presubsription)

Set pre-subscriptions

Pre-subscription is a set of rules and patterns put by the application. When an endpoint registers and its ID, type and registered resources match the pre-subscription data, Device Management Connect sends subscription requests to the device automatically. The pattern may include the endpoint ID (optionally having an `*` character at the end), endpoint type, a list of resources or expressions with an `*` character at the end. Subscriptions based on pre-subscriptions are done when device registers or does register update. To remove the pre-subscription data, put an empty array as a rule.  **Notification rules**  A web application can place dynamic observation rules for individual Object Instances and Resources to define when the device sends observations. More information in [Notification rules](/docs/current/connecting/resource-change-webapp.html).  **Limits**:  - The maximum length of the endpoint name and endpoint type is 64 characters. - The maximum length of the resource path is 128 characters. - You can listen to 256 separate resource paths. - The maximum number of pre-subscription entries is 1024.  **Example request:**  ``` curl -X PUT \\   https://api.us-east-1.mbedcloud.com/v2/subscriptions \\   -H 'authorization: Bearer {api-key}' \\   -H 'content-type: application/json' \\   -d '[          {            \"endpoint-name\": \"node-001\",            \"resource-path\": [\"/dev\"]          },          {            \"endpoint-type\": \"Light\",            \"resource-path\": [\"/sen/*\"]          },          {            \"endpoint-name\": \"node*\"          },          {            \"endpoint-type\": \"Sensor\"          },          {            \"resource-path\": [\"/dev/temp\",\"/dev/hum\"]          }       ]' ```  - Subscribe to `/dev` resource of endpoint named `node-001`. - Subscribe to `Light` type of endpoints and their resources prefixed with `/sen/`. - Subscribe to all observable resources of endpoint names prefixed with `node`. - Subscribe to all observable resources of `Sensor` type endpoints. - Subscribe to `/dev/temp` and `/dev/hum` resources of all endpoints.  **Note**: For efficiency reasons, you should use resource path patterns in the pre-subscription data. This prevents the notification flow from unwanted resources. 

### Example 
```python
from __future__ import print_function
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = mds.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi(mds.ApiClient(configuration))
presubsription = mds.PresubscriptionArray() # PresubscriptionArray | Array of pre-subscriptions.

try: 
    # Set pre-subscriptions
    api_instance.update_pre_subscriptions(presubsription)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->update_pre_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presubsription** | [**PresubscriptionArray**](PresubscriptionArray.md)| Array of pre-subscriptions. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

