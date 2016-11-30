# firmware_catalog.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_info_get**](DefaultApi.md#deploy_info_get) | **GET** /v3/fc_deploy_info | 
[**firmware_image_create**](DefaultApi.md#firmware_image_create) | **POST** /v3/firmware/images/ | 
[**firmware_image_destroy**](DefaultApi.md#firmware_image_destroy) | **DELETE** /v3/firmware/images/{image_id}/ | 
[**firmware_image_list**](DefaultApi.md#firmware_image_list) | **GET** /v3/firmware/images/ | 
[**firmware_image_retrieve**](DefaultApi.md#firmware_image_retrieve) | **GET** /v3/firmware/images/{image_id}/ | 
[**firmware_manifest_create**](DefaultApi.md#firmware_manifest_create) | **POST** /v3/firmware/manifests/ | 
[**firmware_manifest_destroy**](DefaultApi.md#firmware_manifest_destroy) | **DELETE** /v3/firmware/manifests/{manifest_id}/ | 
[**firmware_manifest_list**](DefaultApi.md#firmware_manifest_list) | **GET** /v3/firmware/manifests/ | 
[**firmware_manifest_retrieve**](DefaultApi.md#firmware_manifest_retrieve) | **GET** /v3/firmware/manifests/{manifest_id}/ | 


# **deploy_info_get**
> object deploy_info_get()



<p>Reads the deploy_info.json file and returns the Build and Git ID to the caller.</p> <p>Will return a 500 error if the file is missing, cannot be parsed or the keys are missing.</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()

try: 
    api_response = api_instance.deploy_info_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deploy_info_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_create**
> FirmwareImageSerializer firmware_image_create(datafile, name, description=description, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name2=name2, description2=description2, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, image_id=image_id, object=object)



<p>The APIs for creating and manipulating firmware images.  </p> <p>Create firmware image</p><pre>YAMLError:  while scanning a simple key   in \"<unicode string>\", line 16, column 9:             Cannot validate the data used to ...              ^ could not find expected ':'   in \"<unicode string>\", line 17, column 5:         - code: 401         ^</pre>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
datafile = 'datafile_example' # str | The binary file of firmware image
name = 'name_example' # str | The name of the object
description = 'description_example' # str | The description of the object (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name2 = 'name_example' # str |  (optional)
description2 = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
image_id = 'image_id_example' # str |  (optional)
object = 'object_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_image_create(datafile, name, description=description, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name2=name2, description2=description2, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, image_id=image_id, object=object)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_image_create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **str**| The binary file of firmware image | 
 **name** | **str**| The name of the object | 
 **description** | **str**| The description of the object | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name2** | **str**|  | [optional] 
 **description2** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **image_id** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 

### Return type

[**FirmwareImageSerializer**](FirmwareImageSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_destroy**
> FirmwareImageSerializer firmware_image_destroy(image_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, object=object)



<p>The APIs for creating and manipulating firmware images.  </p> <p>Delete firmware image</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
image_id = 56 # int | The ID of the firmware image
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
object = 'object_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_image_destroy(image_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, object=object)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_image_destroy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **int**| The ID of the firmware image | 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 

### Return type

[**FirmwareImageSerializer**](FirmwareImageSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_list**
> list[FirmwareImageSerializer] firmware_image_list(updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, image_id=image_id, object=object, page=page)



<p>The APIs for creating and manipulating firmware images.  </p> <p>List all firmware images. The result will be paged into pages of 100.</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
image_id = 'image_id_example' # str |  (optional)
object = 'object_example' # str |  (optional)
page = 56 # int | The page number to retrieve. If not given, then defaults to first page.  (optional)

try: 
    api_response = api_instance.firmware_image_list(updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, image_id=image_id, object=object, page=page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_image_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **image_id** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **page** | **int**| The page number to retrieve. If not given, then defaults to first page.  | [optional] 

### Return type

[**list[FirmwareImageSerializer]**](FirmwareImageSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_retrieve**
> FirmwareImageSerializer firmware_image_retrieve(image_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, object=object)



<p>The APIs for creating and manipulating firmware images.  </p> <p>Retrieve firmware image</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
image_id = 56 # int | The ID of the firmware image
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
object = 'object_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_image_retrieve(image_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, etag=etag, object=object)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_image_retrieve: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **int**| The ID of the firmware image | 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 

### Return type

[**FirmwareImageSerializer**](FirmwareImageSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_create**
> FirmwareManifestSerializer firmware_manifest_create(datafile, name, description=description, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name2=name2, description2=description2, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, manifest_id=manifest_id, object=object, timestamp=timestamp)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>Create firmware manifest</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
datafile = 'datafile_example' # str | The manifest file to create
name = 'name_example' # str | The name of the object
description = 'description_example' # str | The description of the object (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name2 = 'name_example' # str |  (optional)
description2 = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
manifest_id = 'manifest_id_example' # str |  (optional)
object = 'object_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_manifest_create(datafile, name, description=description, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name2=name2, description2=description2, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, manifest_id=manifest_id, object=object, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_manifest_create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **str**| The manifest file to create | 
 **name** | **str**| The name of the object | 
 **description** | **str**| The description of the object | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name2** | **str**|  | [optional] 
 **description2** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **manifest_id** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 

### Return type

[**FirmwareManifestSerializer**](FirmwareManifestSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_destroy**
> FirmwareManifestSerializer firmware_manifest_destroy(manifest_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, object=object, timestamp=timestamp)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>Delete firmware manifest</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
manifest_id = 56 # int | The ID of the firmware manifest
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
object = 'object_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_manifest_destroy(manifest_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, object=object, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_manifest_destroy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **int**| The ID of the firmware manifest | 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 

### Return type

[**FirmwareManifestSerializer**](FirmwareManifestSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_list**
> list[FirmwareManifestSerializer] firmware_manifest_list(updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, manifest_id=manifest_id, object=object, timestamp=timestamp, page=page)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>List all firmware manifests</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
manifest_id = 'manifest_id_example' # str |  (optional)
object = 'object_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)
page = 56 # int | The page number to retrieve. If not given, then defaults to first page.  (optional)

try: 
    api_response = api_instance.firmware_manifest_list(updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, manifest_id=manifest_id, object=object, timestamp=timestamp, page=page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_manifest_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **manifest_id** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **page** | **int**| The page number to retrieve. If not given, then defaults to first page.  | [optional] 

### Return type

[**list[FirmwareManifestSerializer]**](FirmwareManifestSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_retrieve**
> FirmwareManifestSerializer firmware_manifest_retrieve(manifest_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, object=object, timestamp=timestamp)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>Retrieve firmware manifest</p>

### Example 
```python
import time
import firmware_catalog
from firmware_catalog.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
firmware_catalog.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# firmware_catalog.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = firmware_catalog.DefaultApi()
manifest_id = 56 # int | The ID of the firmware manifest
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
object = 'object_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_manifest_retrieve(manifest_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, name=name, description=description, created_at=created_at, updated_at=updated_at, datafile_checksum=datafile_checksum, device_class=device_class, etag=etag, object=object, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->firmware_manifest_retrieve: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **int**| The ID of the firmware manifest | 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 

### Return type

[**FirmwareManifestSerializer**](FirmwareManifestSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

