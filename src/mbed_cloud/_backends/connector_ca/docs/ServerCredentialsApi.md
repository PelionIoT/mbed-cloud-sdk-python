# connector_ca.ServerCredentialsApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_server_credentials**](ServerCredentialsApi.md#get_all_server_credentials) | **GET** /v3/server-credentials | Fetch all (Bootstrap and LwM2M) server credentials.
[**get_bootstrap_server_credentials**](ServerCredentialsApi.md#get_bootstrap_server_credentials) | **GET** /v3/server-credentials/bootstrap | Fetch bootstrap server credentials.
[**get_l2_m2_m_server_credentials**](ServerCredentialsApi.md#get_l2_m2_m_server_credentials) | **GET** /v3/server-credentials/lwm2m | Fetch LwM2M server credentials.


# **get_all_server_credentials**
> AllServerCredentialsResponseData get_all_server_credentials(authorization)

Fetch all (Bootstrap and LwM2M) server credentials.

This REST API is intended to be used by customers to fetch all (Bootstrap and LwM2M) server credentials that they will need to use with their clients to connect to bootstrap or LwM2M server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" 

### Example 
```python
from __future__ import print_function
import time
import connector_ca
from connector_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = connector_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_ca.ServerCredentialsApi(connector_ca.ApiClient(configuration))
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch all (Bootstrap and LwM2M) server credentials.
    api_response = api_instance.get_all_server_credentials(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerCredentialsApi->get_all_server_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**AllServerCredentialsResponseData**](AllServerCredentialsResponseData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bootstrap_server_credentials**
> ServerCredentialsResponseData get_bootstrap_server_credentials(authorization)

Fetch bootstrap server credentials.

This REST API is intended to be used by customers to fetch bootstrap server credentials that they will need to use with their clients to connect to bootstrap server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials/bootstrap\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" 

### Example 
```python
from __future__ import print_function
import time
import connector_ca
from connector_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = connector_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_ca.ServerCredentialsApi(connector_ca.ApiClient(configuration))
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch bootstrap server credentials.
    api_response = api_instance.get_bootstrap_server_credentials(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerCredentialsApi->get_bootstrap_server_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**ServerCredentialsResponseData**](ServerCredentialsResponseData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_m2_m_server_credentials**
> ServerCredentialsResponseData get_l2_m2_m_server_credentials(authorization)

Fetch LwM2M server credentials.

This REST API is intended to be used by customers to fetch LwM2M server credentials that they will need to use with their clients to connect to LwM2M server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials/lwm2m\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" 

### Example 
```python
from __future__ import print_function
import time
import connector_ca
from connector_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = connector_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = connector_ca.ServerCredentialsApi(connector_ca.ApiClient(configuration))
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch LwM2M server credentials.
    api_response = api_instance.get_l2_m2_m_server_credentials(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerCredentialsApi->get_l2_m2_m_server_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**ServerCredentialsResponseData**](ServerCredentialsResponseData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

