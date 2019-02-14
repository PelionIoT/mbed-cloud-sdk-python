# mds.WebsocketApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_websocket**](WebsocketApi.md#connect_websocket) | **GET** /v2/notification/websocket-connect | Open the websocket.
[**delete_websocket**](WebsocketApi.md#delete_websocket) | **DELETE** /v2/notification/websocket | Delete websocket channel.
[**get_websocket**](WebsocketApi.md#get_websocket) | **GET** /v2/notification/websocket | Get websocket channel information.
[**register_websocket**](WebsocketApi.md#register_websocket) | **PUT** /v2/notification/websocket | Register a websocket channel


# **connect_websocket**
> connect_websocket(connection, upgrade)

Open the websocket.

Opens the websocket connection.  A websocket channel can have only one active websocket connection at a time. If a websocket connection for a channel exists and a new connection to the same channel is made the connection is accepted and the older connection will be closed.  

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
api_instance = mds.WebsocketApi(mds.ApiClient(configuration))
connection = 'Upgrade' # str |  (default to Upgrade)
upgrade = 'websocket' # str |  (default to websocket)

try: 
    # Open the websocket.
    api_instance.connect_websocket(connection, upgrade)
except ApiException as e:
    print("Exception when calling WebsocketApi->connect_websocket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | **str**|  | [default to Upgrade]
 **upgrade** | **str**|  | [default to websocket]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_websocket**
> delete_websocket()

Delete websocket channel.

To delete a notification websocket channel bound to the API key.  This is required to change the channel from websocket to another type.  **Example usage:**      curl -X DELETE https://api.us-east-1.mbedcloud.com/v2/notification/websocket -H 'authorization: Bearer {api-key}' 

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
api_instance = mds.WebsocketApi(mds.ApiClient(configuration))

try: 
    # Delete websocket channel.
    api_instance.delete_websocket()
except ApiException as e:
    print("Exception when calling WebsocketApi->delete_websocket: %s\n" % e)
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

# **get_websocket**
> WebsocketChannel get_websocket()

Get websocket channel information.

Returns 200 with websocket connection status if websocket channel exists.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/notification/websocket -H 'authorization: Bearer {api-key}' 

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
api_instance = mds.WebsocketApi(mds.ApiClient(configuration))

try: 
    # Get websocket channel information.
    api_response = api_instance.get_websocket()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketApi->get_websocket: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebsocketChannel**](WebsocketChannel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_websocket**
> WebsocketChannel register_websocket()

Register a websocket channel

Register (or update) a channel which will use websocket connection to deliver notifications. The websocket channel should be opened by client using `/v2/notification/websocket-connect` endpoint. To get notifications pushed, you also need to place  the subscriptions. For more information on notification messages, see [NotificationMessage](#NotificationMessage).  A websocket channel can have only one active websocket connection at a time. If a websocket connection for a channel exists and a new connection to the same channel is made the connection is accepted and the older connection will be closed.   **Expiration of a websocket:**  A websocket channel will be expired if the channel does not have an opened websocket connection for 24 hour period. Channel expiration means the channel will be deleted and any undelivered notifications stored in its internal queue will be removed. As long as the channel has an opened websocket connection or time between successive websocket connections is less than 24 hours, the channel is considered active, notifications are stored in its internal queue and delivered when a websocket connection is active. A channel can be also deleted explicitly by a DELETE call.  More about [notification sending logic](/docs/current/integrate-web-app/event-notification.html#notification-sending-logic).  **Example usage:**      curl -X PUT https://api.us-east-1.mbedcloud.com/v2/notification/websocket -H 'authorization: Bearer {api-key}' 

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
api_instance = mds.WebsocketApi(mds.ApiClient(configuration))

try: 
    # Register a websocket channel
    api_response = api_instance.register_websocket()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketApi->register_websocket: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebsocketChannel**](WebsocketChannel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

