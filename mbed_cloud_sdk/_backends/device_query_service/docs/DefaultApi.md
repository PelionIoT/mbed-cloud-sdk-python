# device_query_service.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_query_create**](DefaultApi.md#device_query_create) | **POST** /v3/device-queries/ | Create device query
[**device_query_destroy**](DefaultApi.md#device_query_destroy) | **DELETE** /v3/device-queries/{query_id}/ | Delete device query
[**device_query_list**](DefaultApi.md#device_query_list) | **GET** /v3/device-queries/ | List all device queries
[**device_query_partial_update**](DefaultApi.md#device_query_partial_update) | **PATCH** /v3/device-queries/{query_id}/ | Update device query fields
[**device_query_retrieve**](DefaultApi.md#device_query_retrieve) | **GET** /v3/device-queries/{query_id}/ | Retrieve device query
[**device_query_update**](DefaultApi.md#device_query_update) | **PUT** /v3/device-queries/{query_id}/ | Update device query


# **device_query_create**
> DeviceQuerySerializer device_query_create(name, query, description=description, id=id, object=object, query_id=query_id)

Create device query

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
id = 'id_example' # str | The ID of the query entity (optional)
object = 'object_example' # str | The API resource entity (optional)
query_id = 'query_id_example' # str | The ID of the query (optional)

try: 
    # Create device query
    api_response = api_instance.device_query_create(name, query, description=description, id=id, object=object, query_id=query_id)
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
 **id** | **str**| The ID of the query entity | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **query_id** | **str**| The ID of the query | [optional] 

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

Delete device query

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
    # Delete device query
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
> list[DeviceQuerySerializer] device_query_list(description=description, created_at=created_at, updated_at=updated_at, etag=etag, object=object, name=name, query=query)

List all device queries

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
description = 'description_example' # str | Description (optional)
created_at = 'created_at_example' # str | Created at (optional)
updated_at = 'updated_at_example' # str | Updated at (optional)
etag = 'etag_example' # str | Etag (optional)
object = 'object_example' # str | Object (optional)
name = 'name_example' # str | Name (optional)
query = 'query_example' # str | Query (optional)

try: 
    # List all device queries
    api_response = api_instance.device_query_list(description=description, created_at=created_at, updated_at=updated_at, etag=etag, object=object, name=name, query=query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| Description | [optional] 
 **created_at** | **str**| Created at | [optional] 
 **updated_at** | **str**| Updated at | [optional] 
 **etag** | **str**| Etag | [optional] 
 **object** | **str**| Object | [optional] 
 **name** | **str**| Name | [optional] 
 **query** | **str**| Query | [optional] 

### Return type

[**list[DeviceQuerySerializer]**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query_partial_update**
> DeviceQuerySerializer device_query_partial_update(query_id, description=description, id=id, name=name, object=object, query=query, query_id2=query_id2)

Update device query fields

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
id = 'id_example' # str | The ID of the query entity (optional)
name = 'name_example' # str | The name of the query (optional)
object = 'object_example' # str | The API resource entity (optional)
query = 'query_example' # str | The device query (optional)
query_id2 = 'query_id_example' # str | The ID of the query (optional)

try: 
    # Update device query fields
    api_response = api_instance.device_query_partial_update(query_id, description=description, id=id, name=name, object=object, query=query, query_id2=query_id2)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->device_query_partial_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 
 **description** | **str**| The description of the object | [optional] 
 **id** | **str**| The ID of the query entity | [optional] 
 **name** | **str**| The name of the query | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **query** | **str**| The device query | [optional] 
 **query_id2** | **str**| The ID of the query | [optional] 

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

Retrieve device query

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
    # Retrieve device query
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
> DeviceQuerySerializer device_query_update(query_id, name, query, description=description, id=id, object=object, query_id2=query_id2)

Update device query

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
id = 'id_example' # str | The ID of the query entity (optional)
object = 'object_example' # str | The API resource entity (optional)
query_id2 = 'query_id_example' # str | The ID of the query (optional)

try: 
    # Update device query
    api_response = api_instance.device_query_update(query_id, name, query, description=description, id=id, object=object, query_id2=query_id2)
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
 **id** | **str**| The ID of the query entity | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **query_id2** | **str**| The ID of the query | [optional] 

### Return type

[**DeviceQuerySerializer**](DeviceQuerySerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

