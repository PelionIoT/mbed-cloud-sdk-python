# connector_ca.ExternalAPIApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_developer_certificates_muuid_get**](ExternalAPIApi.md#v3_developer_certificates_muuid_get) | **GET** /v3/developer-certificates/{muuid} | Fetch an existing developer certificate to connect to the bootstrap server.
[**v3_developer_certificates_post**](ExternalAPIApi.md#v3_developer_certificates_post) | **POST** /v3/developer-certificates | Create a new developer certificate to connect to the bootstrap server.
[**v3_server_credentials_bootstrap_get**](ExternalAPIApi.md#v3_server_credentials_bootstrap_get) | **GET** /v3/server-credentials/bootstrap | Fetch bootstrap server credentials.
[**v3_server_credentials_lwm2m_get**](ExternalAPIApi.md#v3_server_credentials_lwm2m_get) | **GET** /v3/server-credentials/lwm2m | Fetch LWM2M server credentials.


# **v3_developer_certificates_muuid_get**
> DeveloperCertificateResponseData v3_developer_certificates_muuid_get(muuid, authorization)

Fetch an existing developer certificate to connect to the bootstrap server.

This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server). 

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
api_instance = connector_ca.ExternalAPIApi(connector_ca.ApiClient(configuration))
muuid = 'muuid_example' # str | A unique identifier for the developer certificate. 
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch an existing developer certificate to connect to the bootstrap server.
    api_response = api_instance.v3_developer_certificates_muuid_get(muuid, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_developer_certificates_muuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muuid** | **str**| A unique identifier for the developer certificate.  | 
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**DeveloperCertificateResponseData**](DeveloperCertificateResponseData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_developer_certificates_post**
> DeveloperCertificateResponseData v3_developer_certificates_post(authorization, body)

Create a new developer certificate to connect to the bootstrap server.

This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  Limitations:    - One developer certificate allows up to 100 devices to connect to bootstrap server.   - Only 10 developer certificates are allowed per account. 

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
api_instance = connector_ca.ExternalAPIApi(connector_ca.ApiClient(configuration))
authorization = 'authorization_example' # str | Bearer {Access Token}. 
body = connector_ca.DeveloperCertificateRequestData() # DeveloperCertificateRequestData | 

try: 
    # Create a new developer certificate to connect to the bootstrap server.
    api_response = api_instance.v3_developer_certificates_post(authorization, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_developer_certificates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer {Access Token}.  | 
 **body** | [**DeveloperCertificateRequestData**](DeveloperCertificateRequestData.md)|  | 

### Return type

[**DeveloperCertificateResponseData**](DeveloperCertificateResponseData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_server_credentials_bootstrap_get**
> ServerCredentialsResponseData v3_server_credentials_bootstrap_get(authorization)

Fetch bootstrap server credentials.

This REST API is intended to be used by customers to fetch bootstrap server credentials that they need to use with their clients to connect to bootstrap server. 

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
api_instance = connector_ca.ExternalAPIApi(connector_ca.ApiClient(configuration))
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch bootstrap server credentials.
    api_response = api_instance.v3_server_credentials_bootstrap_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_server_credentials_bootstrap_get: %s\n" % e)
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

# **v3_server_credentials_lwm2m_get**
> ServerCredentialsResponseData v3_server_credentials_lwm2m_get(authorization)

Fetch LWM2M server credentials.

This REST API is intended to be used by customers to fetch LWM2M server credentials that they need to use with their clients to connect to LWM2M server. 

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
api_instance = connector_ca.ExternalAPIApi(connector_ca.ApiClient(configuration))
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch LWM2M server credentials.
    api_response = api_instance.v3_server_credentials_lwm2m_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAPIApi->v3_server_credentials_lwm2m_get: %s\n" % e)
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

