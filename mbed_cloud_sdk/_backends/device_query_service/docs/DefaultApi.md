# device_query_service.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_query_create**](DefaultApi.md#device_query_create) | **POST** /v3/device-queries/ | 
[**device_query_destroy**](DefaultApi.md#device_query_destroy) | **DELETE** /v3/device-queries/{query_id}/ | 
[**device_query_list**](DefaultApi.md#device_query_list) | **GET** /v3/device-queries/ | 
[**device_query_partial_update**](DefaultApi.md#device_query_partial_update) | **PATCH** /v3/device-queries/{query_id}/ | 
[**device_query_retrieve**](DefaultApi.md#device_query_retrieve) | **GET** /v3/device-queries/{query_id}/ | 
[**device_query_update**](DefaultApi.md#device_query_update) | **PUT** /v3/device-queries/{query_id}/ | 


# **device_query_create**
> DeviceQuerySerializer device_query_create(name, query, description=description, object=object, query_id=query_id)



<p>The APIs for creating and manipulating device queries.  </p> <p>Create device query</p>

### Example 
```python
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
name = 'name_example' # str | The name of the query
query = 'query_example' # str | The device query
description = 'description_example' # str | The description of the object (optional)
object = 'object_example' # str | The API resource entity (optional)
query_id = 'query_id_example' # str | DEPRECATED: The ID of the query (optional)

try: 
    api_response = api_instance.device_query_create(name, query, description=description, object=object, query_id=query_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the query | 
 **query** | **str**| The device query | 
 **description** | **str**| The description of the object | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **query_id** | **str**| DEPRECATED: The ID of the query | [optional] 

### Return type

[**DeviceQuerySerializer**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_destroy**
> DeviceQuerySerializer device_query_destroy(query_id)



<p>The APIs for creating and manipulating device queries.  </p> <p>Delete device query</p>

### Example 
```python
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 

try: 
    api_response = api_instance.device_query_destroy(query_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_destroy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 

### Return type

[**DeviceQuerySerializer**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_list**
> list[DeviceQuerySerializer] device_query_list(description=description, created_at=created_at, updated_at=updated_at, etag=etag, name=name, object=object, query=query, query_id=query_id)



<p>The APIs for creating and manipulating device queries.  </p> <p>List all device queries. The result will be paged into pages of 100.</p>

### Example 
```python
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
description = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
name = 'name_example' # str |  (optional)
object = 'object_example' # str |  (optional)
query = 'query_example' # str |  (optional)
query_id = 'query_id_example' # str |  (optional)

try: 
    api_response = api_instance.device_query_list(description=description, created_at=created_at, updated_at=updated_at, etag=etag, name=name, object=object, query=query, query_id=query_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **query_id** | **str**|  | [optional] 

### Return type

[**list[DeviceQuerySerializer]**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_partial_update**
> DeviceQuerySerializer device_query_partial_update(query_id, description=description, name=name, object=object, query=query, query_id2=query_id2)



<p>The APIs for creating and manipulating device queries.  </p> <p>Update device query fields</p>

### Example 
```python
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 
description = 'description_example' # str | The description of the object (optional)
name = 'name_example' # str | The name of the query (optional)
object = 'object_example' # str | The API resource entity (optional)
query = 'query_example' # str | The device query (optional)
query_id2 = 'query_id_example' # str | DEPRECATED: The ID of the query (optional)

try: 
    api_response = api_instance.device_query_partial_update(query_id, description=description, name=name, object=object, query=query, query_id2=query_id2)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_partial_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 
 **description** | **str**| The description of the object | [optional] 
 **name** | **str**| The name of the query | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **query** | **str**| The device query | [optional] 
 **query_id2** | **str**| DEPRECATED: The ID of the query | [optional] 

### Return type

[**DeviceQuerySerializer**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_retrieve**
> DeviceQuerySerializer device_query_retrieve(query_id)



<p>The APIs for creating and manipulating device queries.  </p> <p>Retrieve device query.</p>

### Example 
```python
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 

try: 
    api_response = api_instance.device_query_retrieve(query_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_retrieve: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 

### Return type

[**DeviceQuerySerializer**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_update**
> DeviceQuerySerializer device_query_update(query_id, name, query, description=description, object=object, query_id2=query_id2)



<p>The APIs for creating and manipulating device queries.  </p> <p>Update device query.</p>

### Example 
```python
import time
import device_query_service
from device_query_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
device_query_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# device_query_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = device_query_service.DefaultApi()
query_id = 'query_id_example' # str | 
name = 'name_example' # str | The name of the query
query = 'query_example' # str | The device query
description = 'description_example' # str | The description of the object (optional)
object = 'object_example' # str | The API resource entity (optional)
query_id2 = 'query_id_example' # str | DEPRECATED: The ID of the query (optional)

try: 
    api_response = api_instance.device_query_update(query_id, name, query, description=description, object=object, query_id2=query_id2)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 
 **name** | **str**| The name of the query | 
 **query** | **str**| The device query | 
 **description** | **str**| The description of the object | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **query_id2** | **str**| DEPRECATED: The ID of the query | [optional] 

### Return type

[**DeviceQuerySerializer**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

