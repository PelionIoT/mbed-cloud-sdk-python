# mds.NotificationsApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_notification_callback_put**](NotificationsApi.md#v2_notification_callback_put) | **PUT** /v2/notification/callback | Register a callback URL
[**v2_notification_pull_delete**](NotificationsApi.md#v2_notification_pull_delete) | **DELETE** /v2/notification/pull | Delete notification Long Poll channel
[**v2_notification_pull_get**](NotificationsApi.md#v2_notification_pull_get) | **GET** /v2/notification/pull | Get notifications using Long Poll


# **v2_notification_callback_put**
> v2_notification_callback_put(webhook)

Register a callback URL

Register a URL to which the server should deliver notifications of the subscribed resource changes. To get notifications pushed you need to also place the subscriptions.  The maximum length of URL, header keys and values, all combined, is 400 characters.  Notifications are delivered as PUT messages to the HTTP server defined by the client with a subscription server message.  The given URL should be accessible and respond to the PUT request with response code of 200 or 204. mbed Cloud Connect  tests the callback URL with an empty payload when the URL is registered. For more information on callback notification, see [NotificationData](api-references#notificationdata).  **Note**: Only one callback URL per an API key can be active. If you register a new URL while another one is already active,  it replaces the active one. There can be only one notification channel at a time. If the Long Poll notification is already present  you need to delete it before setting the callback URL.  **Expiration of a callback URL:**   A callback can expire when mbed DS cannot deliver a notification due to a connection timeout or  error response (4xx or 5xx). After each delivery failure, mbed DS sets an exponential back off time and makes a retry attempt  after that. The first retry delay is 1 second, then 2s, 4s, 8s, ..., 2min, 2min. The maximum retry delay is 2 minutes.  The callback URL will be removed if all retries fail withing 60 minutes. 

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
api_instance = mds.NotificationsApi()
webhook = mds.Webhook() # Webhook | A json object that contains the optional headers and the URL to which the notifications need to be sent. 

try: 
    # Register a callback URL
    api_instance.v2_notification_callback_put(webhook)
except ApiException as e:
    print("Exception when calling NotificationsApi->v2_notification_callback_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)| A json object that contains the optional headers and the URL to which the notifications need to be sent.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_notification_pull_delete**
> v2_notification_pull_delete()

Delete notification Long Poll channel

To delete a notification Long Poll channel. This is required to change the channel from Long Poll to a callback. 

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
api_instance = mds.NotificationsApi()

try: 
    # Delete notification Long Poll channel
    api_instance.v2_notification_pull_delete()
except ApiException as e:
    print("Exception when calling NotificationsApi->v2_notification_pull_delete: %s\n" % e)
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

# **v2_notification_pull_get**
> NotificationMessage v2_notification_pull_get()

Get notifications using Long Poll

In this case, notifications are delivered through HTTP long-poll requests. The HTTP request is kept open  until an event notification or a batch of event notifications are delivered to the client or the request times out  (response code 204). In both cases, the client should open a new polling connection after the previous one closes.  You must have a persistent connection (Connection keep-alive header in the request) to avoid excess  TLS handshakes.  **Note:** If it is not possible to have a public facing callback URL, for example when developing on your local machine,  you can use Long Polling to check for new messages. However, to reduce network traffic and to increase performance  we recommend that you use callback URLs (webhooks) whenever possible. There can be only one notification channel at a time.  If the callback URL notification channel is already present you need to delete it before creating a Long Poll channel. 

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
api_instance = mds.NotificationsApi()

try: 
    # Get notifications using Long Poll
    api_response = api_instance.v2_notification_pull_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->v2_notification_pull_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationMessage**](NotificationMessage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

