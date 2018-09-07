# update_service.DefaultApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firmware_image_create**](DefaultApi.md#firmware_image_create) | **POST** /v3/firmware-images/ | Create an image
[**firmware_image_destroy**](DefaultApi.md#firmware_image_destroy) | **DELETE** /v3/firmware-images/{image_id}/ | Delete an image
[**firmware_image_list**](DefaultApi.md#firmware_image_list) | **GET** /v3/firmware-images/ | List all images
[**firmware_image_retrieve**](DefaultApi.md#firmware_image_retrieve) | **GET** /v3/firmware-images/{image_id}/ | Get an image
[**firmware_manifest_create**](DefaultApi.md#firmware_manifest_create) | **POST** /v3/firmware-manifests/ | Create a manifest
[**firmware_manifest_destroy**](DefaultApi.md#firmware_manifest_destroy) | **DELETE** /v3/firmware-manifests/{manifest_id}/ | Delete a manifest
[**firmware_manifest_list**](DefaultApi.md#firmware_manifest_list) | **GET** /v3/firmware-manifests/ | List manifests
[**firmware_manifest_retrieve**](DefaultApi.md#firmware_manifest_retrieve) | **GET** /v3/firmware-manifests/{manifest_id}/ | Get a manifest
[**update_campaign_archive**](DefaultApi.md#update_campaign_archive) | **POST** /v3/update-campaigns/{campaign_id}/archive | Archive a campaign.
[**update_campaign_create**](DefaultApi.md#update_campaign_create) | **POST** /v3/update-campaigns/ | Create a campaign
[**update_campaign_destroy**](DefaultApi.md#update_campaign_destroy) | **DELETE** /v3/update-campaigns/{campaign_id}/ | Delete a campaign
[**update_campaign_list**](DefaultApi.md#update_campaign_list) | **GET** /v3/update-campaigns/ | List all campaigns
[**update_campaign_metadata_list**](DefaultApi.md#update_campaign_metadata_list) | **GET** /v3/update-campaigns/{campaign_id}/campaign-device-metadata/ | List all campaign device metadata
[**update_campaign_metadata_retrieve**](DefaultApi.md#update_campaign_metadata_retrieve) | **GET** /v3/update-campaigns/{campaign_id}/campaign-device-metadata/{campaign_device_metadata_id}/ | Get a campaign device metadata
[**update_campaign_metrics**](DefaultApi.md#update_campaign_metrics) | **GET** /v3/update-campaigns/{campaign_id}/metrics | Get campaign metrics
[**update_campaign_retrieve**](DefaultApi.md#update_campaign_retrieve) | **GET** /v3/update-campaigns/{campaign_id}/ | Get a campaign.
[**update_campaign_start**](DefaultApi.md#update_campaign_start) | **POST** /v3/update-campaigns/{campaign_id}/start | Start a campaign.
[**update_campaign_stop**](DefaultApi.md#update_campaign_stop) | **POST** /v3/update-campaigns/{campaign_id}/stop | Stop a campaign.
[**update_campaign_update**](DefaultApi.md#update_campaign_update) | **PUT** /v3/update-campaigns/{campaign_id}/ | Modify a campaign
[**upload_job_chunk_create**](DefaultApi.md#upload_job_chunk_create) | **POST** /v3/firmware-images/upload-jobs/{upload_job_id}/chunks | Append a chunks to an upload job
[**upload_job_chunk_list**](DefaultApi.md#upload_job_chunk_list) | **GET** /v3/firmware-images/upload-jobs/{upload_job_id}/chunks | List all metadata for uploaded chunks
[**upload_job_chunk_retreive**](DefaultApi.md#upload_job_chunk_retreive) | **GET** /v3/firmware-images/upload-jobs/{upload_job_id}/chunks/{chunk_id} | Get metadata about a chunk
[**upload_job_create**](DefaultApi.md#upload_job_create) | **POST** /v3/firmware-images/upload-jobs | Create a new upload job
[**upload_job_delete**](DefaultApi.md#upload_job_delete) | **DELETE** /v3/firmware-images/upload-jobs/{upload_job_id} | Delete an upload job
[**upload_job_list**](DefaultApi.md#upload_job_list) | **GET** /v3/firmware-images/upload-jobs | Get all upload jobs
[**upload_job_retrieve**](DefaultApi.md#upload_job_retrieve) | **GET** /v3/firmware-images/upload-jobs/{upload_job_id} | Get an upload job
[**upload_job_update**](DefaultApi.md#upload_job_update) | **PUT** /v3/firmware-images/upload-jobs/{upload_job_id} | Update an upload job


# **firmware_image_create**
> FirmwareImage firmware_image_create(datafile, name, description=description)

Create an image

Create a firmware image.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
datafile = '/path/to/file.txt' # file | The firmware image file to upload
name = 'name_example' # str | The name of the firmware image
description = 'description_example' # str | The description of the firmware image (optional)

try: 
    # Create an image
    api_response = api_instance.firmware_image_create(datafile, name, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **file**| The firmware image file to upload | 
 **name** | **str**| The name of the firmware image | 
 **description** | **str**| The description of the firmware image | [optional] 

### Return type

[**FirmwareImage**](FirmwareImage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_destroy**
> firmware_image_destroy(image_id)

Delete an image

Delete a firmware image.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
image_id = 'image_id_example' # str | The firmware image ID

try: 
    # Delete an image
    api_instance.firmware_image_destroy(image_id)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The firmware image ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_list**
> FirmwareImagePage firmware_image_list(limit=limit, order=order, after=after, include=include, filter=filter)

List all images

List all firmware images.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
limit = 56 # int | How many firmware images to retrieve (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
include = 'include_example' # str | A comma-separated list of data fields to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data  `?filter={URL-encoded query string}`  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  <table>   <thead>     <tr>       <th>Field</th>       <th>= / __eq / __neq</th>       <th>__in /  __nin</th>       <th>__lte / __gte</th>     <tr>   <thead>   <tbody>     <tr>       <td>created_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>datafile</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>datafile_checksum</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>datafile_size</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>description</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>etag</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>id</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>name</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>timestamp</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>updated_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>   </tbody> </table> &nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: `key1=value1&key2=value2&key3=value3`  would be URL-encoded as: `?filter=key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3`   **Filtering by properties** `name__eq=myimage`  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality by appending `__eq` to the field name * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  `{field name}[|__eq|__lte|__gte]={UTC RFC3339 date-time}`  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  `created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering on multiple fields**  `name__eq=myimage&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `name__in=fw-image1,fw-image2` (optional)

try: 
    # List all images
    api_response = api_instance.firmware_image_list(limit=limit, order=order, after=after, include=include, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many firmware images to retrieve | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page | [optional] 
 **include** | **str**| A comma-separated list of data fields to return. Currently supported: total_count | [optional] 
 **filter** | **str**| URL-encoded query string parameter to filter returned data  &#x60;?filter&#x3D;{URL-encoded query string}&#x60;  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;Field&lt;/th&gt;       &lt;th&gt;&#x3D; / __eq / __neq&lt;/th&gt;       &lt;th&gt;__in /  __nin&lt;/th&gt;       &lt;th&gt;__lte / __gte&lt;/th&gt;     &lt;tr&gt;   &lt;thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;created_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;datafile&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;datafile_checksum&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;datafile_size&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;description&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;etag&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;id&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;name&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;timestamp&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;updated_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; &amp;nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: &#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;  would be URL-encoded as: &#x60;?filter&#x3D;key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3&#x60;   **Filtering by properties** &#x60;name__eq&#x3D;myimage&#x60;  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality by appending &#x60;__eq&#x60; to the field name * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  &#x60;{field name}[|__eq|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  &#x60;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering on multiple fields**  &#x60;name__eq&#x3D;myimage&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;name__in&#x3D;fw-image1,fw-image2&#x60; | [optional] 

### Return type

[**FirmwareImagePage**](FirmwareImagePage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_retrieve**
> FirmwareImage firmware_image_retrieve(image_id)

Get an image

Retrieve a firmware image.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
image_id = 'image_id_example' # str | The firmware image ID

try: 
    # Get an image
    api_response = api_instance.firmware_image_retrieve(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The firmware image ID | 

### Return type

[**FirmwareImage**](FirmwareImage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_create**
> FirmwareManifest firmware_manifest_create(datafile, name, description=description, key_table=key_table)

Create a manifest

Create a firmware manifest.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
datafile = '/path/to/file.txt' # file | The manifest file to create. The API gateway enforces the account-specific file size.
name = 'name_example' # str | The name of the firmware manifest
description = 'description_example' # str | The description of the firmware manifest (optional)
key_table = '/path/to/file.txt' # file | The key table of pre-shared keys for devices (optional)

try: 
    # Create a manifest
    api_response = api_instance.firmware_manifest_create(datafile, name, description=description, key_table=key_table)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **file**| The manifest file to create. The API gateway enforces the account-specific file size. | 
 **name** | **str**| The name of the firmware manifest | 
 **description** | **str**| The description of the firmware manifest | [optional] 
 **key_table** | **file**| The key table of pre-shared keys for devices | [optional] 

### Return type

[**FirmwareManifest**](FirmwareManifest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_destroy**
> firmware_manifest_destroy(manifest_id)

Delete a manifest

Delete a firmware manifest.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
manifest_id = 'manifest_id_example' # str | The firmware manifest ID

try: 
    # Delete a manifest
    api_instance.firmware_manifest_destroy(manifest_id)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **str**| The firmware manifest ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_list**
> FirmwareManifestPage firmware_manifest_list(limit=limit, order=order, after=after, include=include, filter=filter)

List manifests

List firmware manifests.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
limit = 56 # int | How many firmware manifests to retrieve (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
include = 'include_example' # str | A comma-separated list of data fields to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data  `?filter={URL-encoded query string}`  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  <table>   <thead>     <tr>       <th>Field</th>       <th>= / __eq / __neq</th>       <th>__in /  __nin</th>       <th>__lte / __gte</th>     <tr>   <thead>   <tbody>     <tr>       <td>created_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>datafile</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>datafile_size</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>description</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>device_class</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>etag</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>id</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>name</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>timestamp</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>updated_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>   </tbody> </table> &nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: `key1__eq=value1&key2__eq=value2&key3__eq=value3`  would be URL-encoded as: `?filter=key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3`   **Filtering by properties** `name__eq=mymanifest`  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality by appending `__eq` to the field name * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  `{field name}[|__eq|__lte|__gte]={UTC RFC3339 date-time}`  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  `created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering on multiple fields**  `name__eq=mymanifest&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `name__in=fw-manifest1,fw-manifest2` (optional)

try: 
    # List manifests
    api_response = api_instance.firmware_manifest_list(limit=limit, order=order, after=after, include=include, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many firmware manifests to retrieve | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page | [optional] 
 **include** | **str**| A comma-separated list of data fields to return. Currently supported: total_count | [optional] 
 **filter** | **str**| URL-encoded query string parameter to filter returned data  &#x60;?filter&#x3D;{URL-encoded query string}&#x60;  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;Field&lt;/th&gt;       &lt;th&gt;&#x3D; / __eq / __neq&lt;/th&gt;       &lt;th&gt;__in /  __nin&lt;/th&gt;       &lt;th&gt;__lte / __gte&lt;/th&gt;     &lt;tr&gt;   &lt;thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;created_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;datafile&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;datafile_size&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;description&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;device_class&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;etag&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;id&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;name&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;timestamp&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;updated_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; &amp;nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: &#x60;key1__eq&#x3D;value1&amp;key2__eq&#x3D;value2&amp;key3__eq&#x3D;value3&#x60;  would be URL-encoded as: &#x60;?filter&#x3D;key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3&#x60;   **Filtering by properties** &#x60;name__eq&#x3D;mymanifest&#x60;  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality by appending &#x60;__eq&#x60; to the field name * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  &#x60;{field name}[|__eq|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  &#x60;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering on multiple fields**  &#x60;name__eq&#x3D;mymanifest&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;name__in&#x3D;fw-manifest1,fw-manifest2&#x60; | [optional] 

### Return type

[**FirmwareManifestPage**](FirmwareManifestPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_retrieve**
> FirmwareManifest firmware_manifest_retrieve(manifest_id)

Get a manifest

Retrieve a firmware manifest.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
manifest_id = 'manifest_id_example' # str | The firmware manifest ID

try: 
    # Get a manifest
    api_response = api_instance.firmware_manifest_retrieve(manifest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **str**| The firmware manifest ID | 

### Return type

[**FirmwareManifest**](FirmwareManifest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_archive**
> update_campaign_archive(campaign_id)

Archive a campaign.

This command will archive a campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The campaign ID

try: 
    # Archive a campaign.
    api_instance.update_campaign_archive(campaign_id)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_create**
> UpdateCampaign update_campaign_create(campaign)

Create a campaign

Create an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign = update_service.UpdateCampaignPostRequest() # UpdateCampaignPostRequest | Update campaign

try: 
    # Create a campaign
    api_response = api_instance.update_campaign_create(campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**UpdateCampaignPostRequest**](UpdateCampaignPostRequest.md)| Update campaign | 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_destroy**
> update_campaign_destroy(campaign_id)

Delete a campaign

Delete an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The ID of the update campaign

try: 
    # Delete a campaign
    api_instance.update_campaign_destroy(campaign_id)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the update campaign | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_list**
> UpdateCampaignPage update_campaign_list(limit=limit, order=order, after=after, include=include, filter=filter)

List all campaigns

Get update campaigns for devices specified by a filter.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
limit = 56 # int | How many update campaigns to retrieve (optional)
order = 'order_example' # str | The order of the records. Acceptable values: ASC, DESC. Default: ASC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
include = 'include_example' # str | A comma-separated list of data fields to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data  `?filter={URL-encoded query string}`   ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  <table>   <thead>     <tr>       <th>Field</th>       <th>= / __eq / __neq</th>       <th>__in /  __nin</th>       <th>__lte / __gte</th>     <tr>   <thead>   <tbody>     <tr>       <td>created_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>description</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>device_filter</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>etag</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>finished</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>id</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>name</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>root_manifest_id</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>started_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>state</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>updated_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>when</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>   </tbody> </table> &nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: `key1__eq=value1&key2__eq=value2&key3__eq=value3`  would be URL-encoded as: `?filter=key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3`   **Filtering by campaign properties** `state__eq=[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]`  `root_manifest_id__eq=43217771234242e594ddb433816c498a`  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality by appending `__eq` to the field name * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  `{field name}[|__eq|__lte|__gte]={UTC RFC3339 date-time}`  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  `created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering on multiple fields**  `state__eq=deployed&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `name__in=fw-image1,fw-image2` (optional)

try: 
    # List all campaigns
    api_response = api_instance.update_campaign_list(limit=limit, order=order, after=after, include=include, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many update campaigns to retrieve | [optional] 
 **order** | **str**| The order of the records. Acceptable values: ASC, DESC. Default: ASC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page | [optional] 
 **include** | **str**| A comma-separated list of data fields to return. Currently supported: total_count | [optional] 
 **filter** | **str**| URL-encoded query string parameter to filter returned data  &#x60;?filter&#x3D;{URL-encoded query string}&#x60;   ###### Filterable fields:  The below table lists all the fields that can be filtered on with certain filters:  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;Field&lt;/th&gt;       &lt;th&gt;&#x3D; / __eq / __neq&lt;/th&gt;       &lt;th&gt;__in /  __nin&lt;/th&gt;       &lt;th&gt;__lte / __gte&lt;/th&gt;     &lt;tr&gt;   &lt;thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;created_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;description&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;device_filter&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;etag&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;finished&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;id&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;name&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;root_manifest_id&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;started_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;state&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;updated_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;when&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; &amp;nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: &#x60;key1__eq&#x3D;value1&amp;key2__eq&#x3D;value2&amp;key3__eq&#x3D;value3&#x60;  would be URL-encoded as: &#x60;?filter&#x3D;key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3&#x60;   **Filtering by campaign properties** &#x60;state__eq&#x3D;[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]&#x60;  &#x60;root_manifest_id__eq&#x3D;43217771234242e594ddb433816c498a&#x60;  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality by appending &#x60;__eq&#x60; to the field name * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  &#x60;{field name}[|__eq|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  &#x60;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering on multiple fields**  &#x60;state__eq&#x3D;deployed&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;name__in&#x3D;fw-image1,fw-image2&#x60; | [optional] 

### Return type

[**UpdateCampaignPage**](UpdateCampaignPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_metadata_list**
> CampaignDeviceMetadataPage update_campaign_metadata_list(campaign_id, limit=limit, order=order, after=after, include=include)

List all campaign device metadata

Get campaign device metadata.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The update campaign ID
limit = 56 # int | How many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
include = 'include_example' # str | A comma-separated list of data fields to return. Currently supported: total_count (optional)

try: 
    # List all campaign device metadata
    api_response = api_instance.update_campaign_metadata_list(campaign_id, limit=limit, order=order, after=after, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_metadata_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The update campaign ID | 
 **limit** | **int**| How many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page | [optional] 
 **include** | **str**| A comma-separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**CampaignDeviceMetadataPage**](CampaignDeviceMetadataPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_metadata_retrieve**
> CampaignDeviceMetadata update_campaign_metadata_retrieve(campaign_id, campaign_device_metadata_id)

Get a campaign device metadata

Get update campaign metadata.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The update campaign ID
campaign_device_metadata_id = 'campaign_device_metadata_id_example' # str | The campaign device metadata ID

try: 
    # Get a campaign device metadata
    api_response = api_instance.update_campaign_metadata_retrieve(campaign_id, campaign_device_metadata_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_metadata_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The update campaign ID | 
 **campaign_device_metadata_id** | **str**| The campaign device metadata ID | 

### Return type

[**CampaignDeviceMetadata**](CampaignDeviceMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_metrics**
> CampaignMetrics update_campaign_metrics(campaign_id)

Get campaign metrics

Get detailed statistics of a campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The campaign ID

try: 
    # Get campaign metrics
    api_response = api_instance.update_campaign_metrics(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID | 

### Return type

[**CampaignMetrics**](CampaignMetrics.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_retrieve**
> UpdateCampaign update_campaign_retrieve(campaign_id)

Get a campaign.

Get an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The campaign ID

try: 
    # Get a campaign.
    api_response = api_instance.update_campaign_retrieve(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID | 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_start**
> update_campaign_start(campaign_id)

Start a campaign.

This command will begin the process of starting a campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The campaign ID

try: 
    # Start a campaign.
    api_instance.update_campaign_start(campaign_id)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_stop**
> update_campaign_stop(campaign_id)

Stop a campaign.

This command will begin the process of stopping a campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | The campaign ID

try: 
    # Stop a campaign.
    api_instance.update_campaign_stop(campaign_id)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_update**
> UpdateCampaign update_campaign_update(campaign_id, campaign)

Modify a campaign

Modify an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | 
campaign = update_service.UpdateCampaignPutRequest() # UpdateCampaignPutRequest | Update campaign

try: 
    # Modify a campaign
    api_response = api_instance.update_campaign_update(campaign_id, campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**|  | 
 **campaign** | [**UpdateCampaignPutRequest**](UpdateCampaignPutRequest.md)| Update campaign | 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_chunk_create**
> UploadChunkInfo upload_job_chunk_create(content_length, upload_job_id, content_md5=content_md5, chunk=chunk)

Append a chunks to an upload job

Append a chunks to an upload job

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
content_length = 56 # int | 
upload_job_id = 'upload_job_id_example' # str | Upload job ID
content_md5 = 'content_md5_example' # str |  (optional)
chunk = 'chunk_example' # str | Chunk (optional)

try: 
    # Append a chunks to an upload job
    api_response = api_instance.upload_job_chunk_create(content_length, upload_job_id, content_md5=content_md5, chunk=chunk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_chunk_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_length** | **int**|  | 
 **upload_job_id** | **str**| Upload job ID | 
 **content_md5** | **str**|  | [optional] 
 **chunk** | **str**| Chunk | [optional] 

### Return type

[**UploadChunkInfo**](UploadChunkInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: binary/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_chunk_list**
> UploadChunkInfoPage upload_job_chunk_list(upload_job_id, limit=limit, order=order, after=after, include=include, filter=filter)

List all metadata for uploaded chunks

List all metadata for uploaded chunks

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
upload_job_id = 'upload_job_id_example' # str | Upload job
limit = 56 # int | How many metadata items for uploaded chunks to retrieve (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
include = 'include_example' # str | A comma-separated list of data fields to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data  `?filter={URL-encoded query string}`  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  <table>   <thead>     <tr>       <th>Field</th>       <th>= / __eq / __neq</th>       <th>__in /  __nin</th>       <th>__lte / __gte</th>     <tr>   <thead>   <tbody>     <tr>       <td>created_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>etag</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>id</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>updated_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>status</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>hash</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>length</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>   </tbody> </table> &nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: `key1=value1&key2=value2&key3=value3`  would be URL-encoded as: `?filter=key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3`   **Filtering by properties** `status__eq=in_progress`  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality by appending `__eq` to the field name * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  `{field name}[|__eq|__lte|__gte]={UTC RFC3339 date-time}`  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  `created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering on multiple fields**  `status__eq=in_progress&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `status__in=in_progress,success` (optional)

try: 
    # List all metadata for uploaded chunks
    api_response = api_instance.upload_job_chunk_list(upload_job_id, limit=limit, order=order, after=after, include=include, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_chunk_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_job_id** | **str**| Upload job | 
 **limit** | **int**| How many metadata items for uploaded chunks to retrieve | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page | [optional] 
 **include** | **str**| A comma-separated list of data fields to return. Currently supported: total_count | [optional] 
 **filter** | **str**| URL-encoded query string parameter to filter returned data  &#x60;?filter&#x3D;{URL-encoded query string}&#x60;  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;Field&lt;/th&gt;       &lt;th&gt;&#x3D; / __eq / __neq&lt;/th&gt;       &lt;th&gt;__in /  __nin&lt;/th&gt;       &lt;th&gt;__lte / __gte&lt;/th&gt;     &lt;tr&gt;   &lt;thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;created_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;etag&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;id&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;updated_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;status&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;hash&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;length&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; &amp;nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: &#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;  would be URL-encoded as: &#x60;?filter&#x3D;key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3&#x60;   **Filtering by properties** &#x60;status__eq&#x3D;in_progress&#x60;  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality by appending &#x60;__eq&#x60; to the field name * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  &#x60;{field name}[|__eq|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  &#x60;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering on multiple fields**  &#x60;status__eq&#x3D;in_progress&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;status__in&#x3D;in_progress,success&#x60; | [optional] 

### Return type

[**UploadChunkInfoPage**](UploadChunkInfoPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_chunk_retreive**
> UploadChunkInfo upload_job_chunk_retreive(upload_job_id, chunk_id)

Get metadata about a chunk

Get metadata about a chunk

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
upload_job_id = 'upload_job_id_example' # str | Upload job
chunk_id = 'chunk_id_example' # str | Chunk

try: 
    # Get metadata about a chunk
    api_response = api_instance.upload_job_chunk_retreive(upload_job_id, chunk_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_chunk_retreive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_job_id** | **str**| Upload job | 
 **chunk_id** | **str**| Chunk | 

### Return type

[**UploadChunkInfo**](UploadChunkInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_create**
> UploadJob upload_job_create(upload_job)

Create a new upload job

Create a new upload job

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
upload_job = update_service.UploadJob() # UploadJob | Upload job

try: 
    # Create a new upload job
    api_response = api_instance.upload_job_create(upload_job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_job** | [**UploadJob**](UploadJob.md)| Upload job | 

### Return type

[**UploadJob**](UploadJob.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_delete**
> upload_job_delete(upload_job_id)

Delete an upload job

Delete an upload job

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
upload_job_id = 'upload_job_id_example' # str | Upload job

try: 
    # Delete an upload job
    api_instance.upload_job_delete(upload_job_id)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_job_id** | **str**| Upload job | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_list**
> UploadJobPage upload_job_list(limit=limit, order=order, after=after, include=include, filter=filter)

Get all upload jobs

Get all upload jobs

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
limit = 56 # int | How many upload jobs to retrieve (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
include = 'include_example' # str | A comma-separated list of data fields to return. Currently supported: total_count (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data  `?filter={URL-encoded query string}`  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  <table>   <thead>     <tr>       <th>Field</th>       <th>= / __eq / __neq</th>       <th>__in /  __nin</th>       <th>__lte / __gte</th>     <tr>   <thead>   <tbody>     <tr>       <td>name</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>description</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>complete</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>id</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>firmware_image_id</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>status</td>       <td>✓</td>       <td>✓</td>       <td>&nbsp;</td>     </tr>     <tr>       <td>created_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>etag</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>     <tr>       <td>updated_at</td>       <td>✓</td>       <td>✓</td>       <td>✓</td>     </tr>   </tbody> </table> &nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: `key1=value1&key2=value2&key3=value3`  would be URL-encoded as: `?filter=key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3`   **Filtering by properties** `name__eq=myimage`  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality by appending `__eq` to the field name * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  `{field name}[|__eq|__lte|__gte]={UTC RFC3339 date-time}`  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  `created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering on multiple fields**  `name__eq=myimage&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z`  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: `__eq` * non-equality: `__neq` * in : `__in` * not in: `__nin`  For `__in` and `__nin` filters list of parameters must be comma-separated:  `name__in=fw-image1,fw-image2` (optional)

try: 
    # Get all upload jobs
    api_response = api_instance.upload_job_list(limit=limit, order=order, after=after, include=include, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many upload jobs to retrieve | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page | [optional] 
 **include** | **str**| A comma-separated list of data fields to return. Currently supported: total_count | [optional] 
 **filter** | **str**| URL-encoded query string parameter to filter returned data  &#x60;?filter&#x3D;{URL-encoded query string}&#x60;  ###### Filterable fields:  The table lists all the fields that can be filtered on with certain filters:  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;Field&lt;/th&gt;       &lt;th&gt;&#x3D; / __eq / __neq&lt;/th&gt;       &lt;th&gt;__in /  __nin&lt;/th&gt;       &lt;th&gt;__lte / __gte&lt;/th&gt;     &lt;tr&gt;   &lt;thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;name&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;description&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;complete&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;id&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;firmware_image_id&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;status&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&amp;nbsp;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;created_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;etag&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;updated_at&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; &amp;nbsp;  The query string is made up of key-value pairs separated by ampersands. For example, this query: &#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;  would be URL-encoded as: &#x60;?filter&#x3D;key1__eq%3Dvalue1%26key2__eq%3Dvalue2%26key3__eq%3Dvalue3&#x60;   **Filtering by properties** &#x60;name__eq&#x3D;myimage&#x60;  **Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality by appending &#x60;__eq&#x60; to the field name * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  &#x60;{field name}[|__eq|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  &#x60;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering on multiple fields**  &#x60;name__eq&#x3D;myimage&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;  **Filtering with filter operators**  String field filtering supports the following operators:  * equality: &#x60;__eq&#x60; * non-equality: &#x60;__neq&#x60; * in : &#x60;__in&#x60; * not in: &#x60;__nin&#x60;  For &#x60;__in&#x60; and &#x60;__nin&#x60; filters list of parameters must be comma-separated:  &#x60;name__in&#x3D;fw-image1,fw-image2&#x60; | [optional] 

### Return type

[**UploadJobPage**](UploadJobPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_retrieve**
> UploadJob upload_job_retrieve(upload_job_id)

Get an upload job

Get an upload job

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
upload_job_id = 'upload_job_id_example' # str | Upload job

try: 
    # Get an upload job
    api_response = api_instance.upload_job_retrieve(upload_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_job_id** | **str**| Upload job | 

### Return type

[**UploadJob**](UploadJob.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_update**
> UploadJob upload_job_update(upload_job_id, upload_job)

Update an upload job

Update an upload job

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = update_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi(update_service.ApiClient(configuration))
upload_job_id = 'upload_job_id_example' # str | Upload job id
upload_job = update_service.UploadJob1() # UploadJob1 | Upload job

try: 
    # Update an upload job
    api_response = api_instance.upload_job_update(upload_job_id, upload_job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_job_id** | **str**| Upload job id | 
 **upload_job** | [**UploadJob1**](UploadJob1.md)| Upload job | 

### Return type

[**UploadJob**](UploadJob.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

