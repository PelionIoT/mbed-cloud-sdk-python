# factory_tool.DefaultApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloads_mbed_factory_provisioning_package_get**](DefaultApi.md#downloads_mbed_factory_provisioning_package_get) | **GET** /downloads/mbed_factory_provisioning_package | 
[**downloads_mbed_factory_provisioning_package_info_get**](DefaultApi.md#downloads_mbed_factory_provisioning_package_info_get) | **GET** /downloads/mbed_factory_provisioning_package/info | 


# **downloads_mbed_factory_provisioning_package_get**
> file downloads_mbed_factory_provisioning_package_get(os)



Returns a specific Factory Tool package in a ZIP archive. * mbed Cloud user role must be Administrator. * mbed Cloud account must have Factory Tool downloads enabled. 

### Example 
```python
import time
import factory_tool
from factory_tool.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
factory_tool.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# factory_tool.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = factory_tool.DefaultApi()
os = 'os_example' # str | Requires Factory Tool OS name (Windows or Linux).

try: 
    api_response = api_instance.downloads_mbed_factory_provisioning_package_get(os)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->downloads_mbed_factory_provisioning_package_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| Requires Factory Tool OS name (Windows or Linux). | 

### Return type

[**file**](file.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **downloads_mbed_factory_provisioning_package_info_get**
> AListOfDownloadableFactoryToolVersions_ downloads_mbed_factory_provisioning_package_info_get()



Gets a list of downloadable Factory Tool versions. * mbed Cloud user role must be Administrator. * mbed Cloud account must have Factory Tool downloads enabled. 

### Example 
```python
import time
import factory_tool
from factory_tool.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
factory_tool.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# factory_tool.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = factory_tool.DefaultApi()

try: 
    api_response = api_instance.downloads_mbed_factory_provisioning_package_info_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->downloads_mbed_factory_provisioning_package_info_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AListOfDownloadableFactoryToolVersions_**](AListOfDownloadableFactoryToolVersions_.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

