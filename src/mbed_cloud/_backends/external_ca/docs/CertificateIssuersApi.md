# external_ca.CertificateIssuersApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_issuer**](CertificateIssuersApi.md#create_certificate_issuer) | **POST** /v3/certificate-issuers | Create certificate issuer.
[**delete_certificate_issuer**](CertificateIssuersApi.md#delete_certificate_issuer) | **DELETE** /v3/certificate-issuers/{certificate-issuer-id} | Delete certificate issuer.
[**get_certificate_issuer**](CertificateIssuersApi.md#get_certificate_issuer) | **GET** /v3/certificate-issuers/{certificate-issuer-id} | Get certificate issuer by ID.
[**get_certificate_issuers**](CertificateIssuersApi.md#get_certificate_issuers) | **GET** /v3/certificate-issuers | Get certificate issuers list.
[**update_certificate_issuer**](CertificateIssuersApi.md#update_certificate_issuer) | **PUT** /v3/certificate-issuers/{certificate-issuer-id} | Update certificate issuer.
[**verify_certificate_issuer**](CertificateIssuersApi.md#verify_certificate_issuer) | **POST** /v3/certificate-issuers/{certificate-issuer-id}/verify | Verify certificate issuer.


# **create_certificate_issuer**
> CertificateIssuerInfo create_certificate_issuer(certificate_issuer_request)

Create certificate issuer.

Create a certificate issuer. The maximum number of issuers is limited to 20 per account. Multiple certificate issuers of the same issuer type can be created, provided they have a different name. This allows verification of the certificate issuer configuration before activating it. <br> **Example usage:**  ``` curl -X POST \\ -H 'authorization: Bearer <valid access token>' \\ -H 'content-type: application/json;charset=UTF-8' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuers \\ -d '{   \"issuer_type\": \"GLOBAL_SIGN\",   \"name\": \"GS Issuer\",   \"description\": \"Sample GlobalSign certificate issuer\",   \"issuer_attributes\": null,   \"issuer_credentials\": {       \"api_key\": \"e510e289e6cd8947\",       \"api_secret\": \"a477a8393d17a55ecb2ba6a61f58feb84770b621\",       \"client_certificate\": \"-----BEGIN CERTIFICATE-----MIIC7zCCAdegAwIBAgIJANTlU4x5S74VMA0GCSqGSIb3DQEBCwUAMA4xDDAKBgNVBAoMA0FybTAeFw0xODAzMTExMzE5MTFaFw0xOTAzMTExMzE5MTFaMA4xDDAKBgNVBAoMA0FybTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJWLStsVMJULZtxdieK9qocM4ymDXMaAusmd9TZLzBgznKQe/CW2yxyA8C8K5e6MmvMYGeKDd4Lkw/ezOj2OsUj2xzNIltUxpGi/GhsNYiN/khNJa/Y1SllLoihJAPm/xbMywOBRu/dM88PiJsNZccOk0I8DYvvyAs9wCTkbKLnfHygl98DCRqXw7nBCplU6F03qpUd/4BUtMtugyqt7yboGH+4YewnUh4Yh4QNOJIvE93Ob++eKjO3pIOYEhQmUxzOLaLNuWXlv2l1WuN281hUP4XBcV8mCzRQfTBBDYTWt+5BEWoLOUkXjW0Um6EAaN3usph1IKDEH6Ia5VHP4Pj0CAwEAAaNQME4wHQYDVR0OBBYEFLsfYZxFcQTjPJKYMjHI2In316fmMB8GA1UdIwQYMBaAFLsfYZxFcQTjPJKYMjHI2In316fmMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAFl08GFsIkkUs6M7QgCWmsnwP6PtD8V87wM1GAqQQlOOeztaeRR2TEOeYiKRZQugYszJ/FVfVp4ggqzepJMn6UZ42j5nmSJs+6t79i23QAzX1zNQ354lr/t7kt3fMdhuL3AP0oZGzdy+EnXXiWeAD22UwzvVmLt38ypJIl+pmTsx9jJy4PN7yoRgtP9k+50m3X6oDxVruehC/JPSeTvEhqyLW3fLcG6IoJMX3vIwfO9uXbFJumTowQeViNJJ9duWvD2KBXn/muOOBe97TPuvAms1gOtMmmPT9/jpo9b4+NsfFiAN6bMici81aIKZzLC+lLGOUmR2fFJyM5OsVLxKsko=-----END CERTIFICATE-----\",         \"private_key\":\"-----BEGIN RSA PRIVATE KEY-----\\nProc-Type: 4,ENCRYPTED\\nDEK-Info: DES-EDE3-CBC,CCAC26A4133947CB\\n\\np3KJ4FI3wcz3I0MtiLkrznkjWFvprVmoNywySUGb5IqZViJZqCMEsyU9a9iDsSfP\\nZ07cg9GviV21WYIPSxZOQrpy1g1VWILzFnH+J6z8dSH4mxXh0PwdOzYgAeqkrIVM\\nJ7KRm6t222dZFjjXK3eEcLmBLGo29XwVJxKHx+l4++gU1LZmeHZR5M8fJ4jejUly\\n7sqzPlmRF0N3I4lwKVj+PfQTVz43QoCnpxOjuSEL4liBrc2agY2xH1O0PFyHimz9\\n3XM9HR/iuPHW0N2D+NPjXlWKacerupH9d4i9IYIagzB+HTgej8limdo03GmmxcZ6\\nYNa58n5yQSaqu0TPRU9DsrKeGjadHTlZQGdzfq1SWsROCnHLrXFKE2ozIG3+hxA5\\nujBF/QWpX5+inXUwDJhBxp8isHbPEnBEUUd6ZRzCTjvN0jaUti5B9yFhO2G6mbE8\\nCvhyzQK8oJqsjZXnlcpPf95LP+9XbcCDjLSIaWJstzXO9tPiv6+x1MVWmivtRHcC\\nSTzpx8jAGCiG6ejLqWB87ZXiZm7ujlCBheHSf5RHwNHhUvoP2JEYalDDRxjcDMSx\\n4uV42Np4yJlIQEDlGHcBlXoL7vEukFpuWgkYdpcZy/Ou9qz8mXrpLcu8C8MhLmSC\\nixGoR5iRhV7cxoHLyuCzj87eYEA73Xu238DQorSEEuiVFnLzQ2+PJMs4qoI14q/L\\notlBDz+Ko6DrU/EZROYmiqMkLKXR2sx9zNAJwPYRs6nSH08tZ3dwqzZbgtP3Wazi\\nhLWHt5/En7wQRA5a+/dDEHXSoLvvSQ9jvhclhWf+eCYuq2eH+g54oyJGRSY+8GV7\\nujhLxkzl/3OZdhZPWoz4U13KpbSTcNWu5Y7oGDoabw19UbvqmLf1PJkpDH/tQgzB\\nxYtsLBRUcofpYoeIiIxfAA4do5WilJc8xqrGhkE4WcHfY24HXAiOvsjbxV+BRprX\\n1jtgJpV/9nJESMap+8PxipGUFRGjB83/uwJaa6mLftEKflX8i4MZ+HnqraXERsqA\\nWRUcDHIWmFfpzIB3iNuxawVvPH8NdCSPmQ9qTb8Cozl0AuOK2E9S+ke8oiYQScWR\\nLdu+zhej7GjuQ9R+Ub+wPWqvOA5qLXejqnCexVScDUuN+z9JWM3N2FG1MwxhAzhP\\ndEfoQHoBn6uyOmrVGP6fosV3chqhPoec42KeOAm1xDvx692isaIy1jPgIyPxeqhm\\n2Tw4E+02R7dlP8Ljf7JzfLm4oKpWHWlcHeqg24x6lY/wXU1RBcWaTa0AQUwoGm2m\\nIQCPfIqOEv/QC2HpO7SVCYkl65KwR0oTd1AzYxdxEq3xHQbh69EL0FGZPVxVCPI+\\nhEAyifKy1/tm3l91Rf/kGpHY7nIQKCXH49tmFwix8gke2nZJmRgX7/zAdMOAKeKH\\nAaIl4nQtv14EbaasMgnn9qgaDYnWzaReEob2QlQ/WYlTor61+KFpGtcf9jAkgudT\\n2op+4CF7wT2+aTXdtkVWfmv++iB8GnlqZdxLvyG1cTYjjYHVFbMSWQnxzQqiE2ms\\nQgp+byjWCumpsWTMdTO+d9NkDOo80vDpaRxEgebmhJ0MbX+eFjBgVg==\\n-----END RSA PRIVATE KEY-----\",       \"passphrase\": \"helloworld\"   } }' ``` 

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
api_instance = external_ca.CertificateIssuersApi(external_ca.ApiClient(configuration))
certificate_issuer_request = external_ca.CertificateIssuerRequest() # CertificateIssuerRequest | Certificate issuer request.

try: 
    # Create certificate issuer.
    api_response = api_instance.create_certificate_issuer(certificate_issuer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersApi->create_certificate_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_request** | [**CertificateIssuerRequest**](CertificateIssuerRequest.md)| Certificate issuer request. | 

### Return type

[**CertificateIssuerInfo**](CertificateIssuerInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate_issuer**
> delete_certificate_issuer(certificate_issuer_id)

Delete certificate issuer.

Delete a certificate issuer by ID. <br> **Example usage:**  ``` curl -X DELETE \\ -H 'authorization: <valid access token>' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuers/0162155dc77d507b9d48a91b00000000 ``` 

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
api_instance = external_ca.CertificateIssuersApi(external_ca.ApiClient(configuration))
certificate_issuer_id = 'certificate_issuer_id_example' # str | Certificate issuer ID. <br> The ID of the certificate issuer. An active certificate issuer may not be deleted. 

try: 
    # Delete certificate issuer.
    api_instance.delete_certificate_issuer(certificate_issuer_id)
except ApiException as e:
    print("Exception when calling CertificateIssuersApi->delete_certificate_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_id** | **str**| Certificate issuer ID. &lt;br&gt; The ID of the certificate issuer. An active certificate issuer may not be deleted.  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_issuer**
> CertificateIssuerInfo get_certificate_issuer(certificate_issuer_id)

Get certificate issuer by ID.

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
api_instance = external_ca.CertificateIssuersApi(external_ca.ApiClient(configuration))
certificate_issuer_id = 'certificate_issuer_id_example' # str | Certificate issuer ID. The ID of the certificate issuer. 

try: 
    # Get certificate issuer by ID.
    api_response = api_instance.get_certificate_issuer(certificate_issuer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersApi->get_certificate_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_id** | **str**| Certificate issuer ID. The ID of the certificate issuer.  | 

### Return type

[**CertificateIssuerInfo**](CertificateIssuerInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_issuers**
> CertificateIssuerInfoListResponse get_certificate_issuers()

Get certificate issuers list.

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
api_instance = external_ca.CertificateIssuersApi(external_ca.ApiClient(configuration))

try: 
    # Get certificate issuers list.
    api_response = api_instance.get_certificate_issuers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersApi->get_certificate_issuers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateIssuerInfoListResponse**](CertificateIssuerInfoListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_issuer**
> CertificateIssuerInfo update_certificate_issuer(certificate_issuer_id, certificate_issuer_update_request)

Update certificate issuer.

Update a certificate issuer. <br> **Example usage:**  ``` curl -X PUT \\ -H 'authorization: <valid access token>' \\ -H 'content-type: application/json;charset=UTF-8' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuers/01621560be51507b9d48a91b00000000 \\ -d '{   \"description\": \"Sample GlobalSign certificate issuer - updated.\",   \"name\": \"GlobalSign Issuer\" }' ``` 

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
api_instance = external_ca.CertificateIssuersApi(external_ca.ApiClient(configuration))
certificate_issuer_id = 'certificate_issuer_id_example' # str | Certificate issuer ID. <br> The ID of the certificate issuer. 
certificate_issuer_update_request = external_ca.CertificateIssuerUpdateRequest() # CertificateIssuerUpdateRequest | Certificate issuer update request.

try: 
    # Update certificate issuer.
    api_response = api_instance.update_certificate_issuer(certificate_issuer_id, certificate_issuer_update_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersApi->update_certificate_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_id** | **str**| Certificate issuer ID. &lt;br&gt; The ID of the certificate issuer.  | 
 **certificate_issuer_update_request** | [**CertificateIssuerUpdateRequest**](CertificateIssuerUpdateRequest.md)| Certificate issuer update request. | 

### Return type

[**CertificateIssuerInfo**](CertificateIssuerInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_certificate_issuer**
> CertificateIssuerVerifyResponse verify_certificate_issuer(certificate_issuer_id)

Verify certificate issuer.

A utility API that can be used to validate the user configuration before activating a certificate issuer. Verifies that the certificate issuer is accessible and can be used to generate certificates by Device Management. <br> **Note:** The API requests the 3rd party CA to sign a test certificate. For some 3rd party CAs, this operation may make use of the account quota. <br> **Example usage:**  ``` curl -X POST \\ -H 'authorization: <valid access token>' \\ -H 'content-type: application/json;charset=UTF-8' \\ https://api.us-east-1.mbedcloud.com/v3/certificate-issuers/01621a36719d507b9d48a91b00000000/verify ``` 

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
api_instance = external_ca.CertificateIssuersApi(external_ca.ApiClient(configuration))
certificate_issuer_id = 'certificate_issuer_id_example' # str | Certificate issuer ID. <br> The ID of the certificate issuer. 

try: 
    # Verify certificate issuer.
    api_response = api_instance.verify_certificate_issuer(certificate_issuer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateIssuersApi->verify_certificate_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_issuer_id** | **str**| Certificate issuer ID. &lt;br&gt; The ID of the certificate issuer.  | 

### Return type

[**CertificateIssuerVerifyResponse**](CertificateIssuerVerifyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

