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


# **firmware_image_create**
> FirmwareImage firmware_image_create(datafile, name, description=description)



Create firmware image.

### Example 
```python
from __future__ import print_statement
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
datafile = '/path/to/file.txt' # file | The firmware image file to upload.
name = 'name_example' # str | The name of the object.
description = 'description_example' # str | The description of the object. (optional)

try: 
    api_response = api_instance.firmware_image_create(datafile, name, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **file**| The firmware image file to upload. | 
 **name** | **str**| The name of the object. | 
 **description** | **str**| The description of the object. | [optional] 

### Return type

[**FirmwareImage**](FirmwareImage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_destroy**
> firmware_image_destroy(image_id)



Delete firmware image.

### Example 
```python
from __future__ import print_statement
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
image_id = 'image_id_example' # str | The ID of the firmware image.

try: 
    api_instance.firmware_image_destroy(image_id)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The ID of the firmware image. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_image_list**
> FirmwareImagePage firmware_image_list(limit=limit, order=order, after=after, filter=filter, include=include)



List all firmware images

### Example 
```python
from __future__ import print_statement
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
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data. The result will be paged into pages of 50.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ###### By firmware image properties (all properties are filterable): For example: ```name={value}``` ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example ```name=MyName&bootstrapped&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded: ```?filter=name%3DMyName%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z``` (optional)
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
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data. The result will be paged into pages of 50.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60; The examples below show the queries in *unencoded* form.  ###### By firmware image properties (all properties are filterable): For example: &#x60;&#x60;&#x60;name&#x3D;{value}&#x60;&#x60;&#x60; ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example &#x60;&#x60;&#x60;name&#x3D;MyName&amp;bootstrapped&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;&#x60;&#x60;  Encoded: &#x60;&#x60;&#x60;?filter&#x3D;name%3DMyName%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&#x60;&#x60;&#x60; | [optional] 
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
> FirmwareImage firmware_image_retrieve(image_id)



Retrieve firmware image.

### Example 
```python
from __future__ import print_statement
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
image_id = 'image_id_example' # str | The ID of the firmware image.

try: 
    api_response = api_instance.firmware_image_retrieve(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_image_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The ID of the firmware image. | 

### Return type

[**FirmwareImage**](FirmwareImage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_create**
> FirmwareManifest firmware_manifest_create(datafile, name, description=description)



Create firmware manifest.

### Example 
```python
from __future__ import print_statement
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
datafile = '/path/to/file.txt' # file | The manifest file to create. The size of the file is account specific and enforced by the api gateway.
name = 'name_example' # str | The name of the object.
description = 'description_example' # str | The description of the object. (optional)

try: 
    api_response = api_instance.firmware_manifest_create(datafile, name, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datafile** | **file**| The manifest file to create. The size of the file is account specific and enforced by the api gateway. | 
 **name** | **str**| The name of the object. | 
 **description** | **str**| The description of the object. | [optional] 

### Return type

[**FirmwareManifest**](FirmwareManifest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_destroy**
> firmware_manifest_destroy(manifest_id)



Delete firmware manifest.

### Example 
```python
from __future__ import print_statement
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
manifest_id = 'manifest_id_example' # str | The ID of the firmware manifest.

try: 
    api_instance.firmware_manifest_destroy(manifest_id)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **str**| The ID of the firmware manifest. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_manifest_list**
> FirmwareManifestPage firmware_manifest_list(limit=limit, order=order, after=after, filter=filter, include=include)



List all firmware manifests.

### Example 
```python
from __future__ import print_statement
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
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL-encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL-encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ##### By manifest ID: ```manifest_id={id}```  ##### By firmware manifest properties (all properties are filterable):  ```device_class={value}```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example ```device_class=1234&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z```  Encoded: ```?filter=device_class%3D1234%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z``` (optional)
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
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL-encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL-encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60; The examples below show the queries in *unencoded* form.  ##### By manifest ID: &#x60;&#x60;&#x60;manifest_id&#x3D;{id}&#x60;&#x60;&#x60;  ##### By firmware manifest properties (all properties are filterable):  &#x60;&#x60;&#x60;device_class&#x3D;{value}&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example &#x60;&#x60;&#x60;device_class&#x3D;1234&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;&#x60;&#x60;  Encoded: &#x60;&#x60;&#x60;?filter&#x3D;device_class%3D1234%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&#x60;&#x60;&#x60; | [optional] 
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
> FirmwareManifest firmware_manifest_retrieve(manifest_id)



Retrieve firmware manifest.

### Example 
```python
from __future__ import print_statement
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
manifest_id = 'manifest_id_example' # str | The ID of the firmware manifest.

try: 
    api_response = api_instance.firmware_manifest_retrieve(manifest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_manifest_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **str**| The ID of the firmware manifest. | 

### Return type

[**FirmwareManifest**](FirmwareManifest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_create**
> UpdateCampaign update_campaign_create(campaign)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Create update campaign</p>

### Example 
```python
from __future__ import print_statement
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_destroy**
> update_campaign_destroy(campaign_id)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Delete update campaign</p>

### Example 
```python
from __future__ import print_statement
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_list**
> UpdateCampaignPage update_campaign_list(limit=limit, order=order, after=after, filter=filter, include=include)



The APIs for creating and manipulating update campaigns.

### Example 
```python
from __future__ import print_statement
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
limit = 56 # int | How many objects to retrieve in the page. (optional)
order = 'order_example' # str | ASC or DESC (optional)
after = 'after_example' # str | The ID of the the item after which to retrieve the next page. (optional)
filter = 'filter_example' # str | URL encoded query string parameter to filter returned data.  ##### Filtering ```?filter={URL encoded query string}```  The query string is made up of key/value pairs separated by ampersands. So for a query of ```key1=value1&key2=value2&key3=value3``` this would be encoded as follows: ```?filter=key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3``` The examples below show the queries in *unencoded* form.  ###### By campaign properties (all properties are filterable): For example: ```state=[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]```  ```root_manifest_id=43217771234242e594ddb433816c498a```  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format ```YYYY-MM-DDThh:mm:ss.msZ```. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &ndash; field name suffixed with ```__gte``` * less than or equal to &ndash; field name suffixed with ```__lte```  Lower and upper limits to a date-time range may be specified by including both the ```__gte``` and ```__lte``` forms in the filter.  ```{field name}[|__lte|__gte]={UTC RFC3339 date-time}```  ##### Multi-field example ```state=deployed&created_at__gte=2016-11-30T16:25:12.1234Z&created_at__lte=2016-12-30T00:00:00Z``` Encoded: ```?filter=state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z``` (optional)
include = 'include_example' # str | Comma separated list of data fields to return. Currently supported: total_count (optional)

try: 
    api_response = api_instance.update_campaign_list(limit=limit, order=order, after=after, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many objects to retrieve in the page. | [optional] 
 **order** | **str**| ASC or DESC | [optional] 
 **after** | **str**| The ID of the the item after which to retrieve the next page. | [optional] 
 **filter** | **str**| URL encoded query string parameter to filter returned data.  ##### Filtering &#x60;&#x60;&#x60;?filter&#x3D;{URL encoded query string}&#x60;&#x60;&#x60;  The query string is made up of key/value pairs separated by ampersands. So for a query of &#x60;&#x60;&#x60;key1&#x3D;value1&amp;key2&#x3D;value2&amp;key3&#x3D;value3&#x60;&#x60;&#x60; this would be encoded as follows: &#x60;&#x60;&#x60;?filter&#x3D;key1%3Dvalue1%26key2%3Dvalue2%26key3%3Dvalue3&#x60;&#x60;&#x60; The examples below show the queries in *unencoded* form.  ###### By campaign properties (all properties are filterable): For example: &#x60;&#x60;&#x60;state&#x3D;[draft|scheduled|devicefectch|devicecopy|publishing|deploying|deployed|manifestremoved|expired]&#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;root_manifest_id&#x3D;43217771234242e594ddb433816c498a&#x60;&#x60;&#x60;  ###### On date-time fields: Date-time fields should be specified in UTC RFC3339 format &#x60;&#x60;&#x60;YYYY-MM-DDThh:mm:ss.msZ&#x60;&#x60;&#x60;. There are three permitted variations:  * UTC RFC3339 with milliseconds e.g. 2016-11-30T16:25:12.1234Z * UTC RFC3339 without milliseconds e.g. 2016-11-30T16:25:12Z * UTC RFC3339 shortened - without milliseconds and punctuation e.g. 20161130T162512Z  Date-time filtering supports three operators:  * equality * greater than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; * less than or equal to &amp;ndash; field name suffixed with &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60;  Lower and upper limits to a date-time range may be specified by including both the &#x60;&#x60;&#x60;__gte&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;__lte&#x60;&#x60;&#x60; forms in the filter.  &#x60;&#x60;&#x60;{field name}[|__lte|__gte]&#x3D;{UTC RFC3339 date-time}&#x60;&#x60;&#x60;  ##### Multi-field example &#x60;&#x60;&#x60;state&#x3D;deployed&amp;created_at__gte&#x3D;2016-11-30T16:25:12.1234Z&amp;created_at__lte&#x3D;2016-12-30T00:00:00Z&#x60;&#x60;&#x60; Encoded: &#x60;&#x60;&#x60;?filter&#x3D;state%3Ddeployed%26created_at__gte%3D2016-11-30T16%3A25%3A12.1234Z%26created_at__lte%3D2016-11-30T00%3A00%3A00Z&#x60;&#x60;&#x60; | [optional] 
 **include** | **str**| Comma separated list of data fields to return. Currently supported: total_count | [optional] 

### Return type

[**UpdateCampaignPage**](UpdateCampaignPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_partial_update**
> UpdateCampaign update_campaign_partial_update(campaign_id, campaign)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign fields</p>

### Example 
```python
from __future__ import print_statement
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_retrieve**
> UpdateCampaign update_campaign_retrieve(campaign_id)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Retrieve campaign</p>

### Example 
```python
from __future__ import print_statement
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
campaign_id = 'campaign_id_example' # str | The ID of the campaign

try: 
    api_response = api_instance.update_campaign_retrieve(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign | 

### Return type

[**UpdateCampaign**](UpdateCampaign.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_update**
> UpdateCampaign update_campaign_update(campaign_id, campaign)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign</p>

### Example 
```python
from __future__ import print_statement
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

