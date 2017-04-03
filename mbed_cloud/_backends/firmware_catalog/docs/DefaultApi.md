# firmware_catalog.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firmware_image_create**](DefaultApi.md#firmware_image_create) | **POST** /v3/firmware-images/ | 
[**firmware_image_destroy**](DefaultApi.md#firmware_image_destroy) | **DELETE** /v3/firmware-images/{image_id}/ | 
[**firmware_image_list**](DefaultApi.md#firmware_image_list) | **GET** /v3/firmware-images/ | 
[**firmware_image_retrieve**](DefaultApi.md#firmware_image_retrieve) | **GET** /v3/firmware-images/{image_id}/ | 
[**firmware_manifest_create**](DefaultApi.md#firmware_manifest_create) | **POST** /v3/firmware-manifests/ | 
[**firmware_manifest_destroy**](DefaultApi.md#firmware_manifest_destroy) | **DELETE** /v3/firmware-manifests/{manifest_id}/ | 
[**firmware_manifest_list**](DefaultApi.md#firmware_manifest_list) | **GET** /v3/firmware-manifests/ | 
[**firmware_manifest_retrieve**](DefaultApi.md#firmware_manifest_retrieve) | **GET** /v3/firmware-manifests/{manifest_id}/ | 


# **firmware_image_create**
> FirmwareImage firmware_image_create(datafile, name, description=description, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_request_id=updating_request_id, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, description2=description2, object=object, image_id=image_id, datafile_checksum=datafile_checksum, name2=name2)



<p>The APIs for creating and manipulating firmware images.  </p> <p>Create firmware image</p>

### Example 
```python
from __future__ import print_statement
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
datafile = 'B' # str | The firmware image file to upload
name = 'name_example' # str | The name of the object
description = 'description_example' # str | The description of the object (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
description2 = 'description_example' # str |  (optional)
object = 'object_example' # str |  (optional)
image_id = 'image_id_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
name2 = 'name_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_image_create(datafile, name, description=description, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_request_id=updating_request_id, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, description2=description2, object=object, image_id=image_id, datafile_checksum=datafile_checksum, name2=name2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **str**| The firmware image file to upload | 
 **name** | **str**| The name of the object | 
 **description** | **str**| The description of the object | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **description2** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **image_id** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **name2** | **str**|  | [optional] 

### Return type

[**FirmwareImage**](FirmwareImage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_destroy**
> FirmwareImage firmware_image_destroy(image_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_request_id=updating_request_id, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, description=description, object=object, datafile_checksum=datafile_checksum, name=name)



<p>The APIs for creating and manipulating firmware images.  </p> <p>Delete firmware image</p>

### Example 
```python
from __future__ import print_statement
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
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
description = 'description_example' # str |  (optional)
object = 'object_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_image_destroy(image_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_request_id=updating_request_id, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, description=description, object=object, datafile_checksum=datafile_checksum, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **int**| The ID of the firmware image | 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**FirmwareImage**](FirmwareImage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_list**
> FirmwareImagePage firmware_image_list(limit=limit, order=order, after=after, filter=filter, include=include)



<p>The APIs for creating and manipulating firmware images.  </p> <p>List all firmware images. The result will be paged into pages of 50.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <p>`</p> <h5 id=\"by-firmware-image-properties-all-properties-are-filterable\">By firmware image properties (all properties are filterable):</h5> <p>For example:</p> <p><code>name={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>name=MyName&amp;bootstrapped&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=name%3DMyName%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>

### Example 
```python
from __future__ import print_statement
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
limit = 56 # int | how many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | the ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data (optional)
include = 'include_example' # str | Comma separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.firmware_image_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| how many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| the ID of the the item after which to retrieve the next page | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data | [optional] 
 **include** | **str**| Comma separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**FirmwareImagePage**](FirmwareImagePage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_retrieve**
> FirmwareImage firmware_image_retrieve(image_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_request_id=updating_request_id, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, description=description, object=object, datafile_checksum=datafile_checksum, name=name)



<p>The APIs for creating and manipulating firmware images.  </p> <p>Retrieve firmware image</p>

### Example 
```python
from __future__ import print_statement
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
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
description = 'description_example' # str |  (optional)
object = 'object_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_image_retrieve(image_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, updating_ip_address=updating_ip_address, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_request_id=updating_request_id, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, description=description, object=object, datafile_checksum=datafile_checksum, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **int**| The ID of the firmware image | 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**FirmwareImage**](FirmwareImage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_create**
> FirmwareManifest firmware_manifest_create(datafile, name, description=description, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_ip_address=updating_ip_address, manifest_id=manifest_id, updating_request_id=updating_request_id, description2=description2, timestamp=timestamp, timestamp__gte=timestamp__gte, timestamp__lte=timestamp__lte, object=object, device_class=device_class, datafile_checksum=datafile_checksum, name2=name2)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>Create firmware manifest</p>

### Example 
```python
from __future__ import print_statement
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
datafile = 'B' # str | The manifest file to create
name = 'name_example' # str | The name of the object
description = 'description_example' # str | The description of the object (optional)
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
manifest_id = 'manifest_id_example' # str |  (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
description2 = 'description_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)
timestamp__gte = 'timestamp__gte_example' # str |  (optional)
timestamp__lte = 'timestamp__lte_example' # str |  (optional)
object = 'object_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
name2 = 'name_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_manifest_create(datafile, name, description=description, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_ip_address=updating_ip_address, manifest_id=manifest_id, updating_request_id=updating_request_id, description2=description2, timestamp=timestamp, timestamp__gte=timestamp__gte, timestamp__lte=timestamp__lte, object=object, device_class=device_class, datafile_checksum=datafile_checksum, name2=name2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **str**| The manifest file to create | 
 **name** | **str**| The name of the object | 
 **description** | **str**| The description of the object | [optional] 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **manifest_id** | **str**|  | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **description2** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **timestamp__gte** | **str**|  | [optional] 
 **timestamp__lte** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **name2** | **str**|  | [optional] 

### Return type

[**FirmwareManifest**](FirmwareManifest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_destroy**
> FirmwareManifest firmware_manifest_destroy(manifest_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_ip_address=updating_ip_address, updating_request_id=updating_request_id, description=description, timestamp=timestamp, timestamp__gte=timestamp__gte, timestamp__lte=timestamp__lte, object=object, device_class=device_class, datafile_checksum=datafile_checksum, name=name)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>Delete firmware manifest</p>

### Example 
```python
from __future__ import print_statement
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
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)
timestamp__gte = 'timestamp__gte_example' # str |  (optional)
timestamp__lte = 'timestamp__lte_example' # str |  (optional)
object = 'object_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_manifest_destroy(manifest_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_ip_address=updating_ip_address, updating_request_id=updating_request_id, description=description, timestamp=timestamp, timestamp__gte=timestamp__gte, timestamp__lte=timestamp__lte, object=object, device_class=device_class, datafile_checksum=datafile_checksum, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **int**| The ID of the firmware manifest | 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **timestamp__gte** | **str**|  | [optional] 
 **timestamp__lte** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**FirmwareManifest**](FirmwareManifest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_list**
> FirmwareManifestPage firmware_manifest_list(limit=limit, order=order, after=after, filter=filter, include=include)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>List all firmware manifests.</p> <h4 id=\"filtering\">Filtering:</h4> <p><code>?filter={URL encoded query string}</code></p> <p>The query string is made up of key/value pairs separated by ampersands. So for a query of <code>key1=value1&amp;key2=value2&amp;key3=value3</code> this would be encoded as follows:</p> <p><code>?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3</code></p> <p>The examples below show the queries in <em>unencoded</em> form.</p> <h5 id=\"by-manifest-id\">By manifest ID:</h5> <p>` manifest_id={id} '</p> <h5 id=\"by-firmware-manifest-properties-all-properties-are-filterable\">By firmware manifest properties (all properties are filterable):</h5> <p><code>device_class={value}</code></p> <h5 id=\"on-date-time-fields\">On date-time fields:</h5> <p>Date-time fields should be specified in UTC RFC3339 format <code>YYYY-MM-DDThh:mm:ss.msZ</code>. There are three permitted variations:</p> <ul> <li>UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z</li> <li>UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z</li> <li>UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z</li> </ul> <p>Date-time filtering supports three operators:</p> <ul> <li>equality</li> <li>greater than or equal to &ndash; field name suffixed with <code>__gte</code></li> <li>less than or equal to &ndash; field name suffixed with <code>__lte</code></li> </ul> <p>Lower and upper limits to a date-time range may be specified by including both the <code>__gte</code> and <code>__lte</code> forms in the filter.</p> <p><code>{field name}[|__lte|__gte]={UTC RFC3339 date-time}</code></p> <h4 id=\"multi-field-example\">Multi-field example</h4> <p><code>device_class=1234&amp;d&amp;created_at__gte=2016-11-30T16:25:12.1234Z&amp;created_at__lte=2016-12-30T00:00:00Z</code></p> <p>Encoded: <code>?filter=device_class%3D1234%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z</code></p>

### Example 
```python
from __future__ import print_statement
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
limit = 56 # int | how many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | the ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data (optional)
include = 'include_example' # str | Comma separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.firmware_manifest_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| how many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| the ID of the the item after which to retrieve the next page | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data | [optional] 
 **include** | **str**| Comma separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**FirmwareManifestPage**](FirmwareManifestPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_retrieve**
> FirmwareManifest firmware_manifest_retrieve(manifest_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_ip_address=updating_ip_address, updating_request_id=updating_request_id, description=description, timestamp=timestamp, timestamp__gte=timestamp__gte, timestamp__lte=timestamp__lte, object=object, device_class=device_class, datafile_checksum=datafile_checksum, name=name)



<p>The APIs for creating and manipulating firmware manifests.  </p> <p>Retrieve firmware manifest</p>

### Example 
```python
from __future__ import print_statement
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
updated_at = 'updated_at_example' # str |  (optional)
updated_at__gte = 'updated_at__gte_example' # str |  (optional)
updated_at__lte = 'updated_at__lte_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
created_at__gte = 'created_at__gte_example' # str |  (optional)
created_at__lte = 'created_at__lte_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
etag__gte = 'etag__gte_example' # str |  (optional)
etag__lte = 'etag__lte_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
updating_request_id = 'updating_request_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)
timestamp__gte = 'timestamp__gte_example' # str |  (optional)
timestamp__lte = 'timestamp__lte_example' # str |  (optional)
object = 'object_example' # str |  (optional)
device_class = 'device_class_example' # str |  (optional)
datafile_checksum = 'datafile_checksum_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try: 
    api_response = api_instance.firmware_manifest_retrieve(manifest_id, updated_at=updated_at, updated_at__gte=updated_at__gte, updated_at__lte=updated_at__lte, created_at=created_at, created_at__gte=created_at__gte, created_at__lte=created_at__lte, etag=etag, etag__gte=etag__gte, etag__lte=etag__lte, updating_ip_address=updating_ip_address, updating_request_id=updating_request_id, description=description, timestamp=timestamp, timestamp__gte=timestamp__gte, timestamp__lte=timestamp__lte, object=object, device_class=device_class, datafile_checksum=datafile_checksum, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **int**| The ID of the firmware manifest | 
 **updated_at** | **str**|  | [optional] 
 **updated_at__gte** | **str**|  | [optional] 
 **updated_at__lte** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **created_at__gte** | **str**|  | [optional] 
 **created_at__lte** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **etag__gte** | **str**|  | [optional] 
 **etag__lte** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **updating_request_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **timestamp__gte** | **str**|  | [optional] 
 **timestamp__lte** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **device_class** | **str**|  | [optional] 
 **datafile_checksum** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**FirmwareManifest**](FirmwareManifest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

