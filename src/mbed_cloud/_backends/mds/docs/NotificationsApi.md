# mds.NotificationsApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_long_poll_channel**](NotificationsApi.md#delete_long_poll_channel) | **DELETE** /v2/notification/pull | Delete notification Long Poll channel
[**deregister_webhook**](NotificationsApi.md#deregister_webhook) | **DELETE** /v2/notification/callback | Delete callback URL
[**get_webhook**](NotificationsApi.md#get_webhook) | **GET** /v2/notification/callback | Check callback URL
[**long_poll_notifications**](NotificationsApi.md#long_poll_notifications) | **GET** /v2/notification/pull | Get notifications using Long Poll
[**register_webhook**](NotificationsApi.md#register_webhook) | **PUT** /v2/notification/callback | Register a callback URL


# **delete_long_poll_channel**
> delete_long_poll_channel()

Delete notification Long Poll channel

To delete a notification Long Poll channel. This is required to change the channel from Long Poll to a callback. You should not make a GET `/v2/notification/pull` call for 2 minutes after channel was deleted, because it can implicitly recreate the pull channel. You can also have some random responses with payload or 410 GONE with \"CHANNEL_DELETED\" as a payload or 200/204 until the old channel is purged.  **Example usage:**     curl -X DELETE https://api.us-east-1.mbedcloud.com/v2/notification/pull -H 'authorization: Bearer {api-key}' 

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
api_instance = mds.NotificationsApi(mds.ApiClient(configuration))

try: 
    # Delete notification Long Poll channel
    api_instance.delete_long_poll_channel()
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_long_poll_channel: %s\n" % e)
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

# **deregister_webhook**
> deregister_webhook()

Delete callback URL

Deletes the callback URL.  **Example usage:**      curl -X DELETE https://api.us-east-1.mbedcloud.com/v2/notification/callback -H 'authorization: Bearer {api-key}' 

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
api_instance = mds.NotificationsApi(mds.ApiClient(configuration))

try: 
    # Delete callback URL
    api_instance.deregister_webhook()
except ApiException as e:
    print("Exception when calling NotificationsApi->deregister_webhook: %s\n" % e)
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

# **get_webhook**
> Webhook get_webhook()

Check callback URL

Shows the current callback URL if it exists.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/notification/callback -H 'authorization: Bearer {api-key}' 

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
api_instance = mds.NotificationsApi(mds.ApiClient(configuration))

try: 
    # Check callback URL
    api_response = api_instance.get_webhook()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_webhook: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Webhook**](Webhook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **long_poll_notifications**
> NotificationMessage long_poll_notifications()

Get notifications using Long Poll

In this case, notifications are delivered through HTTP long poll requests. The HTTP request is kept open until an event notification or a batch of event notifications are delivered to the client or the request times out (response code 204). In both cases, the client should open a new polling connection after the previous one closes. Only a single long polling connection per API key can be ongoing at any given time. You must have a persistent connection (Connection keep-alive header in the request) to avoid excess TLS handshakes.  The pull channel is implicitly created by the first GET call to `/v2/notification/pull`. It is refreshed on each GET call. If the channel is not polled for a long time (10 minutes) - it expires and will be deleted. This means that no notifications will stay in the queue between polls. A channel can be also deleted explicitly by a DELETE call.  **Note:** If you cannot have a public facing callback URL, for example when developing on your local machine, you can use long polling to check for new messages. However, **long polling is deprecated** and will likely be replaced in future. It is meant only for experimentation and not for commercial usage. The proper method to receive notifications is a **notification callback**. There can only be one notification channel per API key at a time in Device Management Connect. If a callback notification channel already exists, you need to delete it before creating a long poll notification channel, and vice-versa.  **Example usage:**      curl -X GET https://api.us-east-1.mbedcloud.com/v2/notification/pull -H 'authorization: Bearer {api-key}' 

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
api_instance = mds.NotificationsApi(mds.ApiClient(configuration))

try: 
    # Get notifications using Long Poll
    api_response = api_instance.long_poll_notifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->long_poll_notifications: %s\n" % e)
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

# **register_webhook**
> register_webhook(webhook)

Register a callback URL

Register a URL to which the server should deliver notifications of the subscribed resource changes. To get notifications pushed, you also need to place the subscriptions. The maximum length of the URL, header keys and values, all combined, is 400 characters. Notifications are delivered as PUT messages to the HTTP server defined by the client with a subscription server message. The given URL should be accessible and respond to the PUT request with response code of 200 or 204. Device Management Connect tests the callback URL with an empty payload when the URL is registered. For more information on callback notification, see [NotificationMessage](/docs/current/service-api-references/mbed-cloud-connect.html#models).  **Optional headers in a callback message:**  You can set optional headers to a callback in a **Webhook** object. Device Management Connect will include the header and key pairs to the notification messages send them to callback URL. As the callback URL's are API key specific also the headers are.  One possible use for the additional headers is to check the origin of a PUT request and also distinguish the application (API key) to which the notification belongs to.  **Note**: Only one callback URL per an API key can be active. If you register a new URL while another one is already active, it replaces the active one. There can be only one notification channel at a time. If the Long Poll notification is already present, you need to delete it before setting the callback URL.  **Expiration of a callback URL:**  A callback can expire when Device Management cannot deliver a notification due to a connection timeout or an error response (4xx or 5xx). After each delivery failure, Device Management sets an exponential back off time and makes a retry attempt after that. The first retry delay is 1 second, then 2s, 4s, 8s, ..., 2min, 2min. The maximum retry delay is 2 minutes. The callback URL will be removed if all retries fail withing 24 hours. More about [notification sending logic](/docs/current/integrate-web-app/event-notification.html#notification-sending-logic).  **Supported callback URL protocols:**  Currently, only HTTP and HTTPS protocols are supported.  **HTTPS callback URLs:**  When delivering a notification to an HTTPS based callback URL, Device Management Connect will present a valid client certificate to identify itself. The certificate is signed by a trusted certificate authorithy (GlobalSign) with a Common Name (CN) set to notifications.mbedcloud.com.  **Example usage:**  This example command shows how to set your callback URL and API key. It also sets an optional header authorization. When Device Management Connect calls your callback URL, the call contains the authorization header with the defined value.      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/notification/callback \\       -H 'authorization: Bearer {api-key}' \\       -H 'content-type: application/json' \\       -d '{       \"url\": \"{callback-url}\",       \"headers\": {\"authorization\" : \"f4b93d6e-4652-4874-82e4-41a3ced0cd56\"}       }' 

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
api_instance = mds.NotificationsApi(mds.ApiClient(configuration))
webhook = mds.Webhook() # Webhook | A json object that contains the optional headers and the URL to which the notifications need to be sent. 

try: 
    # Register a callback URL
    api_instance.register_webhook(webhook)
except ApiException as e:
    print("Exception when calling NotificationsApi->register_webhook: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

