# update_service.DefaultApi

All URIs are relative to *https://api.us-east-1.mbedcloud.com*

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
[**update_campaign_create**](DefaultApi.md#update_campaign_create) | **POST** /v3/update-campaigns/ | 
[**update_campaign_destroy**](DefaultApi.md#update_campaign_destroy) | **DELETE** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_list**](DefaultApi.md#update_campaign_list) | **GET** /v3/update-campaigns/ | 
[**update_campaign_partial_update**](DefaultApi.md#update_campaign_partial_update) | **PATCH** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_retrieve**](DefaultApi.md#update_campaign_retrieve) | **GET** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_update**](DefaultApi.md#update_campaign_update) | **PUT** /v3/update-campaigns/{campaign_id}/ | 
[**v3_update_campaigns_campaign_id_campaign_device_metadata_campaign_device_metadata_id_get**](DefaultApi.md#v3_update_campaigns_campaign_id_campaign_device_metadata_campaign_device_metadata_id_get) | **GET** /v3/update-campaigns/{campaign_id}/campaign-device-metadata/{campaign_device_metadata_id}/ | 
[**v3_update_campaigns_campaign_id_campaign_device_metadata_get**](DefaultApi.md#v3_update_campaigns_campaign_id_campaign_device_metadata_get) | **GET** /v3/update-campaigns/{campaign_id}/campaign-device-metadata/ | 


# **firmware_image_create**
> FirmwareImage firmware_image_create(datafile, name, description=description)



Create firmware image.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
datafile = '/path/to/file.txt' # file | The firmware image file to upload
name = 'name_example' # str | The name of the firmware image
description = 'description_example' # str | The description of the firmware image (optional)

try: 
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



Delete firmware image.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
image_id = 'image_id_example' # str | The firmware image ID

try: 
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
> FirmwareImagePage firmware_image_list(limit=limit, order=order, after=after, filter=filter, include=include)



List all firmware images.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
limit = 56 # int | How many firmware images to retrieve (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data. The results are paginated into groups of 50.  <br/> ?filter={URL-encoded query string} <br/>  The query string is made up of key-value pairs separated by ampersands. For example, this query: key1=value1&key2=value2&key3=value3  would be URL-encoded as: ?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3 <br/>  The examples below show the queries in *unencoded* form.<br/>  <br/>**Filtering by campaign properties** state=[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]  <br/> root_manifest_id=43217771234242e594ddb433816c498a  <br/>**Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  {field name}[|__lte|__gte]={UTC RFC3339 date-time} <br/>  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z  <br/>**Filtering on multiple fields**  Example: state=deployed&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z  The example after URL encoding: ?filter=state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.firmware_image_list(limit=limit, order=order, after=after, filter=filter, include=include)
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
 **filter** | **str**| URL-encoded query string parameter to filter returned data. The results are paginated into groups of 50.  &lt;br/&gt; ?filter&#x3D;{URL-encoded query string} &lt;br/&gt;  The query string is made up of key-value pairs separated by ampersands. For example, this query: key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3  would be URL-encoded as: ?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3 &lt;br/&gt;  The examples below show the queries in *unencoded* form.&lt;br/&gt;  &lt;br/&gt;**Filtering by campaign properties** state&#x3D;[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]  &lt;br/&gt; root_manifest_id&#x3D;43217771234242e594ddb433816c498a  &lt;br/&gt;**Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  {field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time} &lt;br/&gt;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z  &lt;br/&gt;**Filtering on multiple fields**  Example: state&#x3D;deployed&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z  The example after URL encoding: ?filter&#x3D;state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: total_count | [optional] 

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



Retrieve firmware image.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
image_id = 'image_id_example' # str | The firmware image ID

try: 
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
> FirmwareManifest firmware_manifest_create(datafile, name, description=description)



Create firmware manifest.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
datafile = '/path/to/file.txt' # file | The manifest file to create. The API gateway enforces the account-specific file size.
name = 'name_example' # str | The name of the firmware manifest
description = 'description_example' # str | The description of the firmware manifest (optional)

try: 
    api_response = api_instance.firmware_manifest_create(datafile, name, description=description)
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



Delete firmware manifest.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
manifest_id = 'manifest_id_example' # str | The firmware manifest ID

try: 
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
> FirmwareManifestPage firmware_manifest_list(limit=limit, order=order, after=after, filter=filter, include=include)



List firmware manifests.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
limit = 56 # int | How many firmware manifests to retrieve (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data  <br/> ?filter={URL-encoded query string} <br/>  The query string is made up of key-value pairs separated by ampersands. For example, this query: key1=value1&key2=value2&key3=value3  would be URL-encoded as: ?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3 <br/>  The examples below show the queries in *unencoded* form.<br/>  <br/>**Filtering by campaign properties** state=[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]  <br/> root_manifest_id=43217771234242e594ddb433816c498a  <br/>**Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  {field name}[|__lte|__gte]={UTC RFC3339 date-time} <br/>  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z  <br/>**Filtering on multiple fields**  Example: state=deployed&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z  The example after URL encoding: ?filter=state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.firmware_manifest_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many firmware manifests to retrieve | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL-encoded query string parameter to filter returned data  &lt;br/&gt; ?filter&#x3D;{URL-encoded query string} &lt;br/&gt;  The query string is made up of key-value pairs separated by ampersands. For example, this query: key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3  would be URL-encoded as: ?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3 &lt;br/&gt;  The examples below show the queries in *unencoded* form.&lt;br/&gt;  &lt;br/&gt;**Filtering by campaign properties** state&#x3D;[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]  &lt;br/&gt; root_manifest_id&#x3D;43217771234242e594ddb433816c498a  &lt;br/&gt;**Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  {field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time} &lt;br/&gt;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z  &lt;br/&gt;**Filtering on multiple fields**  Example: state&#x3D;deployed&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z  The example after URL encoding: ?filter&#x3D;state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: total_count | [optional] 

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



Retrieve firmware manifest.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
manifest_id = 'manifest_id_example' # str | The firmware manifest ID

try: 
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

# **update_campaign_create**
> UpdateCampaign update_campaign_create(campaign)



Create an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
campaign = update_service.UpdateCampaignPostRequest() # UpdateCampaignPostRequest | Update campaign

try: 
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



Delete an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The ID of the update campaign

try: 
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
> UpdateCampaignPage update_campaign_list(limit=limit, order=order, after=after, filter=filter, include=include)



Get update campaigns for devices specified by a filter.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
limit = 56 # int | How many update campaigns to retrieve (optional)
order = 'order_example' # str | The order of the records. Acceptable values: ASC, DESC. Default: ASC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data  <br/>             ?filter={URL-encoded query string} <br/>  The query string is made up of key-value pairs separated by ampersands. For example, this query: key1=value1&key2=value2&key3=value3  would be URL-encoded as: ?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3 <br/>  The examples below show the queries in *unencoded* form.<br/>  <br/>**Filtering by campaign properties** state=[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]  <br/> root_manifest_id=43217771234242e594ddb433816c498a  <br/>**Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, `YYYY-MM-DDThh:mm:ss.msZ`. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: `2016-11-30T16:25:12.1234Z` * UTC RFC3339 without milliseconds. Example: `2016-11-30T16:25:12Z` * UTC RFC3339 shortened without milliseconds and punctuation. Example: `20161130T162512Z`  Date-time filtering supports three operators:  * equality * greater than or equal to by appending `__gte` to the field name * less than or equal to by appending `__lte` to the field name  {field name}[|__lte|__gte]={UTC RFC3339 date-time} <br/>  Time ranges may be specified by including both the `__gte` and `__lte` forms in the filter. For example:  created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z  <br/>**Filtering on multiple fields**  Example: state=deployed&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z  The example after URL encoding: ?filter=state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.update_campaign_list(limit=limit, order=order, after=after, filter=filter, include=include)
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
 **filter** | **str**| URL-encoded query string parameter to filter returned data  &lt;br/&gt;             ?filter&#x3D;{URL-encoded query string} &lt;br/&gt;  The query string is made up of key-value pairs separated by ampersands. For example, this query: key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3  would be URL-encoded as: ?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3 &lt;br/&gt;  The examples below show the queries in *unencoded* form.&lt;br/&gt;  &lt;br/&gt;**Filtering by campaign properties** state&#x3D;[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]  &lt;br/&gt; root_manifest_id&#x3D;43217771234242e594ddb433816c498a  &lt;br/&gt;**Filtering on date-time fields**  Date-time fields should be specified in UTC RFC3339 format, &#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds. Example: &#x60;2016-11-30T16:25:12.1234Z&#x60; * UTC RFC3339 without milliseconds. Example: &#x60;2016-11-30T16:25:12Z&#x60; * UTC RFC3339 shortened without milliseconds and punctuation. Example: &#x60;20161130T162512Z&#x60;  Date-time filtering supports three operators:  * equality * greater than or equal to by appending &#x60;__gte&#x60; to the field name * less than or equal to by appending &#x60;__lte&#x60; to the field name  {field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time} &lt;br/&gt;  Time ranges may be specified by including both the &#x60;__gte&#x60; and &#x60;__lte&#x60; forms in the filter. For example:  created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z  &lt;br/&gt;**Filtering on multiple fields**  Example: state&#x3D;deployed&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z  The example after URL encoding: ?filter&#x3D;state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**UpdateCampaignPage**](UpdateCampaignPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_partial_update**
> UpdateCampaign update_campaign_partial_update(campaign_id, campaign)



Modify a subset of an update campaign's fields.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | 
campaign = update_service.UpdateCampaignPatchRequest() # UpdateCampaignPatchRequest | Update campaign

try: 
    api_response = api_instance.update_campaign_partial_update(campaign_id, campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**|  | 
 **campaign** | [**UpdateCampaignPatchRequest**](UpdateCampaignPatchRequest.md)| Update campaign | 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_retrieve**
> UpdateCampaign update_campaign_retrieve(campaign_id)



Get an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The campaign ID

try: 
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

# **update_campaign_update**
> UpdateCampaign update_campaign_update(campaign_id, campaign)



Modify an update campaign.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | 
campaign = update_service.UpdateCampaignPutRequest() # UpdateCampaignPutRequest | Update campaign

try: 
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

# **v3_update_campaigns_campaign_id_campaign_device_metadata_campaign_device_metadata_id_get**
> CampaignDeviceMetadata v3_update_campaigns_campaign_id_campaign_device_metadata_campaign_device_metadata_id_get(campaign_id, campaign_device_metadata_id)



Get update campaign metadata.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The update campaign ID
campaign_device_metadata_id = 'campaign_device_metadata_id_example' # str | The campaign device metadata ID

try: 
    api_response = api_instance.v3_update_campaigns_campaign_id_campaign_device_metadata_campaign_device_metadata_id_get(campaign_id, campaign_device_metadata_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v3_update_campaigns_campaign_id_campaign_device_metadata_campaign_device_metadata_id_get: %s\n" % e)
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

# **v3_update_campaigns_campaign_id_campaign_device_metadata_get**
> CampaignDeviceMetadataPage v3_update_campaigns_campaign_id_campaign_device_metadata_get(campaign_id, limit=limit, order=order, after=after, include=include)



Get campaign device metadata.

### Example 
```python
from __future__ import print_function
import time
import update_service
from update_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
update_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# update_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = update_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The update campaign ID
limit = 56 # int | How many objects to retrieve in the page (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page (optional)
include = 'include_example' # str | Comma-separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.v3_update_campaigns_campaign_id_campaign_device_metadata_get(campaign_id, limit=limit, order=order, after=after, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v3_update_campaigns_campaign_id_campaign_device_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The update campaign ID | 
 **limit** | **int**| How many objects to retrieve in the page | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page | [optional] 
 **include** | **str**| Comma-separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**CampaignDeviceMetadataPage**](CampaignDeviceMetadataPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

