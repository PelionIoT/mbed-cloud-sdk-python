# connector_ca.DeveloperCertificateApi

All URIs are relative to *http://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_developer_certificate**](DeveloperCertificateApi.md#create_developer_certificate) | **POST** /v3/developer-certificates | Create a new developer certificate to connect to the bootstrap server.
[**get_developer_certificate**](DeveloperCertificateApi.md#get_developer_certificate) | **GET** /v3/developer-certificates/{developerCertificateId} | Fetch an existing developer certificate to connect to the bootstrap server.


# **create_developer_certificate**
> DeveloperCertificateResponseData create_developer_certificate(authorization, body)

Create a new developer certificate to connect to the bootstrap server.

This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Note:** The number of developer certificates allowed per account is limited. Please see [Using your own certificate authority](/docs/current/mbed-cloud-deploy/instructions-for-factory-setup-and-device-provision.html#using-your-own-certificate-authority-with-mbed-cloud).  **Example usage:** curl -X POST \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" -H \"content-type: application/json\" -d \"{ \\\"name\\\": \\\"THE_CERTIFICATE_NAME\\\", \\\"description\\\": \\\"THE_CERTIFICATE_DESCRIPTION\\\"}\" 

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
api_instance = connector_ca.DeveloperCertificateApi(connector_ca.ApiClient(configuration))
authorization = 'authorization_example' # str | Bearer {Access Token}. 
body = connector_ca.DeveloperCertificateRequestData() # DeveloperCertificateRequestData | 

try: 
    # Create a new developer certificate to connect to the bootstrap server.
    api_response = api_instance.create_developer_certificate(authorization, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperCertificateApi->create_developer_certificate: %s\n" % e)
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

# **get_developer_certificate**
> DeveloperCertificateResponseData get_developer_certificate(developer_certificate_id, authorization)

Fetch an existing developer certificate to connect to the bootstrap server.

This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates/THE_CERTIFICATE_ID\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" 

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
api_instance = connector_ca.DeveloperCertificateApi(connector_ca.ApiClient(configuration))
developer_certificate_id = 'developer_certificate_id_example' # str | A unique identifier for the developer certificate. 
authorization = 'authorization_example' # str | Bearer {Access Token}. 

try: 
    # Fetch an existing developer certificate to connect to the bootstrap server.
    api_response = api_instance.get_developer_certificate(developer_certificate_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeveloperCertificateApi->get_developer_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **developer_certificate_id** | **str**| A unique identifier for the developer certificate.  | 
 **authorization** | **str**| Bearer {Access Token}.  | 

### Return type

[**DeveloperCertificateResponseData**](DeveloperCertificateResponseData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

