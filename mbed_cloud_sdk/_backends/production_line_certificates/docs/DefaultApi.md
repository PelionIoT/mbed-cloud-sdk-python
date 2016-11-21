# production_line_certificates.DefaultApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_production_line_certificates_get**](DefaultApi.md#v3_production_line_certificates_get) | **GET** /v3/production-line-certificates | 
[**v3_production_line_certificates_muuid_delete**](DefaultApi.md#v3_production_line_certificates_muuid_delete) | **DELETE** /v3/production-line-certificates/{mUUID} | 
[**v3_production_line_certificates_muuid_get**](DefaultApi.md#v3_production_line_certificates_muuid_get) | **GET** /v3/production-line-certificates/{mUUID} | 
[**v3_production_line_certificates_muuid_put**](DefaultApi.md#v3_production_line_certificates_muuid_put) | **PUT** /v3/production-line-certificates/{mUUID} | 
[**v3_production_line_certificates_post**](DefaultApi.md#v3_production_line_certificates_post) | **POST** /v3/production-line-certificates | 


# **v3_production_line_certificates_get**
> AListOfProductionLineCertificates_ v3_production_line_certificates_get(authorization)



Gets the list of production line certificates associated with the account. 

### Example 
```python
import time
import production_line_certificates
from production_line_certificates.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
production_line_certificates.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# production_line_certificates.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = production_line_certificates.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.

try: 
    api_response = api_instance.v3_production_line_certificates_get(authorization)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->v3_production_line_certificates_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 

### Return type

[**AListOfProductionLineCertificates_**](AListOfProductionLineCertificates_.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_production_line_certificates_muuid_delete**
> ProductionLineCertificate v3_production_line_certificates_muuid_delete(authorization, m_uuid)



Deactivates the production line certificate.  There is no way to reactivate it. 

### Example 
```python
import time
import production_line_certificates
from production_line_certificates.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
production_line_certificates.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# production_line_certificates.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = production_line_certificates.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.
m_uuid = 'm_uuid_example' # str | Certificate mUUID

try: 
    api_response = api_instance.v3_production_line_certificates_muuid_delete(authorization, m_uuid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->v3_production_line_certificates_muuid_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 
 **m_uuid** | **str**| Certificate mUUID | 

### Return type

[**ProductionLineCertificate**](ProductionLineCertificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_production_line_certificates_muuid_get**
> ProductionLineCertificate v3_production_line_certificates_muuid_get(authorization, m_uuid)



Gets a single production line certificate by its mUUID. 

### Example 
```python
import time
import production_line_certificates
from production_line_certificates.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
production_line_certificates.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# production_line_certificates.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = production_line_certificates.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.
m_uuid = 'm_uuid_example' # str | Certificate mUUID.

try: 
    api_response = api_instance.v3_production_line_certificates_muuid_get(authorization, m_uuid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->v3_production_line_certificates_muuid_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 
 **m_uuid** | **str**| Certificate mUUID. | 

### Return type

[**ProductionLineCertificate**](ProductionLineCertificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_production_line_certificates_muuid_put**
> ProductionLineCertificate v3_production_line_certificates_muuid_put(authorization, m_uuid, body)



Updates the comment on a production line certificate. 

### Example 
```python
import time
import production_line_certificates
from production_line_certificates.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
production_line_certificates.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# production_line_certificates.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = production_line_certificates.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.
m_uuid = 'm_uuid_example' # str | Certificate mUUID
body = production_line_certificates.Body1() # Body1 | 

try: 
    api_response = api_instance.v3_production_line_certificates_muuid_put(authorization, m_uuid, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->v3_production_line_certificates_muuid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 
 **m_uuid** | **str**| Certificate mUUID | 
 **body** | [**Body1**](Body1.md)|  | 

### Return type

[**ProductionLineCertificate**](ProductionLineCertificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_production_line_certificates_post**
> ProductionLineCertificate v3_production_line_certificates_post(authorization, body)



Adds a new production line certificate to the account. 

### Example 
```python
import time
import production_line_certificates
from production_line_certificates.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
production_line_certificates.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# production_line_certificates.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = production_line_certificates.DefaultApi()
authorization = 'authorization_example' # str | \"Bearer\" followed by the reference token or API key.
body = production_line_certificates.Body() # Body | 

try: 
    api_response = api_instance.v3_production_line_certificates_post(authorization, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->v3_production_line_certificates_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| \&quot;Bearer\&quot; followed by the reference token or API key. | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**ProductionLineCertificate**](ProductionLineCertificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

