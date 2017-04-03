# mds.SubscriptionsApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_subscriptions_delete**](SubscriptionsApi.md#v2_subscriptions_delete) | **DELETE** /v2/subscriptions | Remove all subscriptions
[**v2_subscriptions_endpoint_name_delete**](SubscriptionsApi.md#v2_subscriptions_endpoint_name_delete) | **DELETE** /v2/subscriptions/{endpointName} | Delete subscriptions from an endpoint
[**v2_subscriptions_endpoint_name_get**](SubscriptionsApi.md#v2_subscriptions_endpoint_name_get) | **GET** /v2/subscriptions/{endpointName} | Read endpoints subscriptions
[**v2_subscriptions_endpoint_name_resource_path_delete**](SubscriptionsApi.md#v2_subscriptions_endpoint_name_resource_path_delete) | **DELETE** /v2/subscriptions/{endpointName}/{resourcePath} | Remove a subscription
[**v2_subscriptions_endpoint_name_resource_path_get**](SubscriptionsApi.md#v2_subscriptions_endpoint_name_resource_path_get) | **GET** /v2/subscriptions/{endpointName}/{resourcePath} | Read subscription status
[**v2_subscriptions_endpoint_name_resource_path_put**](SubscriptionsApi.md#v2_subscriptions_endpoint_name_resource_path_put) | **PUT** /v2/subscriptions/{endpointName}/{resourcePath} | Subscribe to a resource path
[**v2_subscriptions_get**](SubscriptionsApi.md#v2_subscriptions_get) | **GET** /v2/subscriptions | Get pre-subscriptions
[**v2_subscriptions_put**](SubscriptionsApi.md#v2_subscriptions_put) | **PUT** /v2/subscriptions | Set pre-subscriptions


# **v2_subscriptions_delete**
> v2_subscriptions_delete()

Remove all subscriptions

Removes subscriptions from every endpoint and resource. Note that this does not remove pre-subscriptions.

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()

try: 
    # Remove all subscriptions
    api_instance.v2_subscriptions_delete()
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_subscriptions_endpoint_name_delete**
> v2_subscriptions_endpoint_name_delete(endpoint_name)

Delete subscriptions from an endpoint

Deletes all resource subscriptions in a single endpoint.

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here. 

try: 
    # Delete subscriptions from an endpoint
    api_instance.v2_subscriptions_endpoint_name_delete(endpoint_name)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_endpoint_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_subscriptions_endpoint_name_get**
> v2_subscriptions_endpoint_name_get(endpoint_name)

Read endpoints subscriptions

Lists all subscribed resources from a single endpoint.

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that endpoint name must be an exact match. You cannot use wildcards here. 

try: 
    # Read endpoints subscriptions
    api_instance.v2_subscriptions_endpoint_name_get(endpoint_name)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_endpoint_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that endpoint name must be an exact match. You cannot use wildcards here.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/uri-list

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_subscriptions_endpoint_name_resource_path_delete**
> v2_subscriptions_endpoint_name_resource_path_delete(endpoint_name, _resource_path)

Remove a subscription

To remove an existing subscription from a resource path. 

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 

try: 
    # Remove a subscription
    api_instance.v2_subscriptions_endpoint_name_resource_path_delete(endpoint_name, _resource_path)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_endpoint_name_resource_path_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_subscriptions_endpoint_name_resource_path_get**
> v2_subscriptions_endpoint_name_resource_path_get(endpoint_name, _resource_path)

Read subscription status

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 

try: 
    # Read subscription status
    api_instance.v2_subscriptions_endpoint_name_resource_path_get(endpoint_name, _resource_path)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_endpoint_name_resource_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_subscriptions_endpoint_name_resource_path_put**
> v2_subscriptions_endpoint_name_resource_path_put(endpoint_name, _resource_path)

Subscribe to a resource path

The mbed Cloud Connect eventing model consists of observable resources.  This means that endpoints can deliver updated resource content, periodically or with a more sophisticated  solution-dependent logic. The OMA LWM2M resource model including objects, object instances,  resources and resource instances is also supported.  Applications can subscribe to objects, object instances or individual resources to make the device  to provide value change notifications to mbed Cloud Connect service. An application needs to call a `/notification/callback` method to get mbed Cloud Connect to push a notification of the resource changes.  You can also use `/subscriptions` to set a pre-subscription. 

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()
endpoint_name = 'endpoint_name_example' # str | A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here. 
_resource_path = '_resource_path_example' # str | The URL of the resource. 

try: 
    # Subscribe to a resource path
    api_instance.v2_subscriptions_endpoint_name_resource_path_put(endpoint_name, _resource_path)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_endpoint_name_resource_path_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here.  | 
 **_resource_path** | **str**| The URL of the resource.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_subscriptions_get**
> v2_subscriptions_get()

Get pre-subscriptions

You can retrieve the pre-subscription data by using a GET operation. The server returns with the same JSON structure  as described above. If there are no pre-subscribed resources, it returns with an empty array. 

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()

try: 
    # Get pre-subscriptions
    api_instance.v2_subscriptions_get()
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_subscriptions_put**
> v2_subscriptions_put(presubsription)

Set pre-subscriptions

Pre-subscription is a set of rules and patterns put by the application. When an endpoint registers  and its name, type and registered resources match the pre-subscription data, mbed Cloud Connect sends  subscription requests to the device automatically. The pattern may include the endpoint name  (optionally having an `\\*` character at the end), endpoint type, a list of resources or expressions  with an `\\*` character at the end. Subscriptions based on pre-subscriptions are done when device registers or does register update. To remove the pre-subscription data, put an empty array as a rule.  ``` Example payload: [  {    endpoint-name: \"node-001\",    resource-path: [\"/dev\"]  },  {    endpoint-type: \"Light\",    resource-path: [\"/sen/*\"]  },  {    endpoint-name: \"node*\"  },  {    endpoint-type: \"Sensor\"  },  {     resource-path: [\"/dev/temp\",\"/dev/hum\"]  } ] ``` 

### Example 
```python
from __future__ import print_statement
import time
import mds
from mds.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
mds.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mds.SubscriptionsApi()
presubsription = mds.PresubscriptionArray() # PresubscriptionArray | Array of pre-subscriptions.

try: 
    # Set pre-subscriptions
    api_instance.v2_subscriptions_put(presubsription)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->v2_subscriptions_put: %s\n" % e)
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

