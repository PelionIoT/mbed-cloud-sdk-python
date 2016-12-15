# provisioning_certificate.DefaultApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_provisioning_certificate_get**](DefaultApi.md#v3_provisioning_certificate_get) | **GET** /v3/provisioning-certificate | 


# **v3_provisioning_certificate_get**
> ProvisioningCertificate v3_provisioning_certificate_get(authorization)



Gets the account's provisioning certificate.

### Example 
```python
import time
import provisioning_certificate
from provisioning_certificate.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
provisioning_certificate.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# provisioning_certificate.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = provisioning_certificate.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.

try: 
    api_response = api_instance.v3_provisioning_certificate_get(authorization)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->v3_provisioning_certificate_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 

### Return type

[**ProvisioningCertificate**](ProvisioningCertificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

