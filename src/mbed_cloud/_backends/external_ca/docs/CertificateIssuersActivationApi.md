# external_ca.CertificateIssuersActivationApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_issuer_config**](CertificateIssuersActivationApi.md#create_certificate_issuer_config) | **POST** /v3/certificate-issuer-configurations | Create certificate issuer configuration.
[**delete_certificate_issuer_config_by_id**](CertificateIssuersActivationApi.md#delete_certificate_issuer_config_by_id) | **DELETE** /v3/certificate-issuer-configurations/{certificate-issuer-configuration-id} | Delete certificate issuer configuration.
[**get_certificate_issuer_config**](CertificateIssuersActivationApi.md#get_certificate_issuer_config) | **GET** /v3/certificate-issuer-configurations/lwm2m | Get certificate issuer configuration.
[**get_certificate_issuer_config_by_id**](CertificateIssuersActivationApi.md#get_certificate_issuer_config_by_id) | **GET** /v3/certificate-issuer-configurations/{certificate-issuer-configuration-id} | Get certificate issuer configuration.
[**get_certificate_issuer_configs**](CertificateIssuersActivationApi.md#get_certificate_issuer_configs) | **GET** /v3/certificate-issuer-configurations | Get certificate issuer configurations.
[**update_certificate_issuer_config**](CertificateIssuersActivationApi.md#update_certificate_issuer_config) | **PUT** /v3/certificate-issuer-configurations/lwm2m | Update certificate issuer configuration.
[**update_certificate_issuer_config_by_id**](CertificateIssuersActivationApi.md#update_certificate_issuer_config_by_id) | **PUT** /v3/certificate-issuer-configurations/{certificate-issuer-configuration-id} | Update certificate issuer configuration.


# **create_certificate_issuer_config**
> CertificateIssuerConfigResponse create_certificate_issuer_config(create_certificate_issuer_config)

Create certificate issuer configuration.

Configure the certificate issuer to be used when creating the device custom certificates. <br> **Example usage:**  ``` curl -X POST \\ -H 'authorization: <valid access token>' \\ -H 'content-type: application/json;charset=UTF-8' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuer-configurations \\ -d '{   \"reference\": \"customer.dlms\",   \"certificate_issuer_id\": \"01621a36719d507b9d48a91b00000000\" }' ``` 

### Example 
```python
from __future__ import print_function
import time
import external_ca
from external_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = external_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = external_ca.CertificateIssuersActivationApi(external_ca.ApiClient(configuration))
create_certificate_issuer_config = external_ca.CreateCertificateIssuerConfig() # CreateCertificateIssuerConfig | Certificate issuer configuration request

try: 
    # Create certificate issuer configuration.
    api_response = api_instance.create_certificate_issuer_config(create_certificate_issuer_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersActivationApi->create_certificate_issuer_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_certificate_issuer_config** | [**CreateCertificateIssuerConfig**](CreateCertificateIssuerConfig.md)| Certificate issuer configuration request | 

### Return type

[**CertificateIssuerConfigResponse**](CertificateIssuerConfigResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate_issuer_config_by_id**
> delete_certificate_issuer_config_by_id(certificate_issuer_configuration_id)

Delete certificate issuer configuration.

Delete the configured certificate issuer configuration. You can only delete the configurations of custom certificates. 

### Example 
```python
from __future__ import print_function
import time
import external_ca
from external_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = external_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = external_ca.CertificateIssuersActivationApi(external_ca.ApiClient(configuration))
certificate_issuer_configuration_id = 'certificate_issuer_configuration_id_example' # str | The ID of the certificate issuer configuration. 

try: 
    # Delete certificate issuer configuration.
    api_instance.delete_certificate_issuer_config_by_id(certificate_issuer_configuration_id)
except ApiException as e:
    print("Exception when calling CertificateIssuersActivationApi->delete_certificate_issuer_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_configuration_id** | **str**| The ID of the certificate issuer configuration.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_issuer_config**
> CertificateIssuerConfigResponse get_certificate_issuer_config()

Get certificate issuer configuration.

Provides the configured certificate issuer to be used when creating device certificates for LwM2M communication.<br> 

### Example 
```python
from __future__ import print_function
import time
import external_ca
from external_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = external_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = external_ca.CertificateIssuersActivationApi(external_ca.ApiClient(configuration))

try: 
    # Get certificate issuer configuration.
    api_response = api_instance.get_certificate_issuer_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersActivationApi->get_certificate_issuer_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateIssuerConfigResponse**](CertificateIssuerConfigResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_issuer_config_by_id**
> CertificateIssuerConfigResponse get_certificate_issuer_config_by_id(certificate_issuer_configuration_id)

Get certificate issuer configuration.

Provides the configured certificate issuer. 

### Example 
```python
from __future__ import print_function
import time
import external_ca
from external_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = external_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = external_ca.CertificateIssuersActivationApi(external_ca.ApiClient(configuration))
certificate_issuer_configuration_id = 'certificate_issuer_configuration_id_example' # str | The ID of the certificate issuer configuration. 

try: 
    # Get certificate issuer configuration.
    api_response = api_instance.get_certificate_issuer_config_by_id(certificate_issuer_configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersActivationApi->get_certificate_issuer_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_configuration_id** | **str**| The ID of the certificate issuer configuration.  | 

### Return type

[**CertificateIssuerConfigResponse**](CertificateIssuerConfigResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_issuer_configs**
> CertificateIssuerConfigListResponse get_certificate_issuer_configs(reference__eq=reference__eq)

Get certificate issuer configurations.

Get certificate issuer configurations, optionally filtered by reference. <br> **Example usage:**  ``` curl \\ -H 'authorization: <valid access token>' \\ -H 'content-type: application/json;charset=UTF-8' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuer-configurations \\ ``` ``` curl \\ -H 'authorization: <valid access token>' \\ -H 'content-type: application/json;charset=UTF-8' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuer-configurations?reference__eq=dlms \\ ``` 

### Example 
```python
from __future__ import print_function
import time
import external_ca
from external_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = external_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = external_ca.CertificateIssuersActivationApi(external_ca.ApiClient(configuration))
reference__eq = 'reference__eq_example' # str | The certificate name to which the certificate issuer configuration applies. (optional)

try: 
    # Get certificate issuer configurations.
    api_response = api_instance.get_certificate_issuer_configs(reference__eq=reference__eq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersActivationApi->get_certificate_issuer_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference__eq** | **str**| The certificate name to which the certificate issuer configuration applies. | [optional] 

### Return type

[**CertificateIssuerConfigListResponse**](CertificateIssuerConfigListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_issuer_config**
> CertificateIssuerConfigResponse update_certificate_issuer_config(certificate_issuer_config_request)

Update certificate issuer configuration.

Configure the certificate issuer to be used when creating device certificates for LwM2M communication. <br> **Example usage:**  ``` curl -X PUT \\ -H 'authorization: <valid access token>' \\ -H 'content-type: application/json;charset=UTF-8' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuer-configurations/lwm2m \\ -d '{   \"certificate_issuer_id\": \"01621a36719d507b9d48a91b00000000\" }' ``` 

### Example 
```python
from __future__ import print_function
import time
import external_ca
from external_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = external_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = external_ca.CertificateIssuersActivationApi(external_ca.ApiClient(configuration))
certificate_issuer_config_request = external_ca.CertificateIssuerConfigRequest() # CertificateIssuerConfigRequest | Certificate Issuer Configuration Request

try: 
    # Update certificate issuer configuration.
    api_response = api_instance.update_certificate_issuer_config(certificate_issuer_config_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersActivationApi->update_certificate_issuer_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_config_request** | [**CertificateIssuerConfigRequest**](CertificateIssuerConfigRequest.md)| Certificate Issuer Configuration Request | 

### Return type

[**CertificateIssuerConfigResponse**](CertificateIssuerConfigResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_issuer_config_by_id**
> CertificateIssuerConfigResponse update_certificate_issuer_config_by_id(certificate_issuer_configuration_id, certificate_issuer_config_request)

Update certificate issuer configuration.

Update the configured certificate issuer configuration. 

### Example 
```python
from __future__ import print_function
import time
import external_ca
from external_ca.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = external_ca.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = external_ca.CertificateIssuersActivationApi(external_ca.ApiClient(configuration))
certificate_issuer_configuration_id = 'certificate_issuer_configuration_id_example' # str | The ID of the certificate issuer configuration. 
certificate_issuer_config_request = external_ca.CertificateIssuerConfigRequest() # CertificateIssuerConfigRequest | Certificate issuer configuration request

try: 
    # Update certificate issuer configuration.
    api_response = api_instance.update_certificate_issuer_config_by_id(certificate_issuer_configuration_id, certificate_issuer_config_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersActivationApi->update_certificate_issuer_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_configuration_id** | **str**| The ID of the certificate issuer configuration.  | 
 **certificate_issuer_config_request** | [**CertificateIssuerConfigRequest**](CertificateIssuerConfigRequest.md)| Certificate issuer configuration request | 

### Return type

[**CertificateIssuerConfigResponse**](CertificateIssuerConfigResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

