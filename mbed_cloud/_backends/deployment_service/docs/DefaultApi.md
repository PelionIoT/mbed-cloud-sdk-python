# deployment_service.DefaultApi

All URIs are relative to *http://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_info_get**](DefaultApi.md#deploy_info_get) | **GET** /v3/ds_deploy_info | 
[**update_campaign_create**](DefaultApi.md#update_campaign_create) | **POST** /v3/update-campaigns/ | 
[**update_campaign_destroy**](DefaultApi.md#update_campaign_destroy) | **DELETE** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_list**](DefaultApi.md#update_campaign_list) | **GET** /v3/update-campaigns/ | 
[**update_campaign_partial_update**](DefaultApi.md#update_campaign_partial_update) | **PATCH** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_retrieve**](DefaultApi.md#update_campaign_retrieve) | **GET** /v3/update-campaigns/{campaign_id}/ | 
[**update_campaign_status**](DefaultApi.md#update_campaign_status) | **GET** /v3/update-campaigns/{campaign_id}/status/ | 
[**update_campaign_update**](DefaultApi.md#update_campaign_update) | **PUT** /v3/update-campaigns/{campaign_id}/ | 


# **deploy_info_get**
> object deploy_info_get()



<p>Reads the deploy_info.json file and returns the Build and Git ID to the caller.</p> <p>Will return a 500 error if the file is missing, cannot be parsed or the keys are missing.</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()

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

# **update_campaign_create**
> UpdateCampaignSerializer update_campaign_create(body)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Create update campaign</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
body = deployment_service.WriteUpdateCampaignSerializer() # WriteUpdateCampaignSerializer | Update campaign object to create

try: 
    api_response = api_instance.update_campaign_create(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_campaign_create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteUpdateCampaignSerializer**](WriteUpdateCampaignSerializer.md)| Update campaign object to create | 

### Return type

[**UpdateCampaignSerializer**](UpdateCampaignSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_destroy**
> UpdateCampaignSerializer update_campaign_destroy(campaign_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Delete update campaign</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The ID of the update campaign
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
attempts = 'attempts_example' # str |  (optional)
description = 'description_example' # str |  (optional)
device_filter = 'device_filter_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
finished = 'finished_example' # str |  (optional)
name = 'name_example' # str |  (optional)
object = 'object_example' # str |  (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str |  (optional)
when = 'when_example' # str |  (optional)

try: 
    api_response = api_instance.update_campaign_destroy(campaign_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_campaign_destroy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the update campaign | 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **attempts** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **device_filter** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **finished** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **when** | **str**|  | [optional] 

### Return type

[**UpdateCampaignSerializer**](UpdateCampaignSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_list**
> list[UpdateCampaignSerializer] update_campaign_list(updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, campaign_id=campaign_id, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when, page=page, root_manifest_url=root_manifest_url)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>List all update campaigns</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
attempts = 'attempts_example' # str |  (optional)
campaign_id = 'campaign_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
device_filter = 'device_filter_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
finished = 'finished_example' # str |  (optional)
name = 'name_example' # str |  (optional)
object = 'object_example' # str |  (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str |  (optional)
when = 'when_example' # str |  (optional)
page = 56 # int | The page number to retrieve. If not given, then defaults to first page. (optional)
root_manifest_url = 'root_manifest_url_example' # str | The firmware catalog URL for the manifest that will be sent to the device as part of the campaign (optional)

try: 
    api_response = api_instance.update_campaign_list(updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, campaign_id=campaign_id, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when, page=page, root_manifest_url=root_manifest_url)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_campaign_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **attempts** | **str**|  | [optional] 
 **campaign_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **device_filter** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **finished** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **when** | **str**|  | [optional] 
 **page** | **int**| The page number to retrieve. If not given, then defaults to first page. | [optional] 
 **root_manifest_url** | **str**| The firmware catalog URL for the manifest that will be sent to the device as part of the campaign | [optional] 

### Return type

[**list[UpdateCampaignSerializer]**](UpdateCampaignSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_partial_update**
> UpdateCampaignSerializer update_campaign_partial_update(campaign_id=campaign_id, description=description, device_filter=device_filter, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign fields</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | DEPRECATED: The ID of the campaign (optional)
description = 'description_example' # str | An optional description of the campaign (optional)
device_filter = 'device_filter_example' # str | The filter for the devices the campaign will target (optional)
finished = '2013-10-20T19:20:30+01:00' # datetime | The timestamp when the update campaign finished (optional)
name = 'name_example' # str | A name for this campaign (optional)
object = 'object_example' # str | The API resource entity (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str | The state of the campaign (optional)
when = '2013-10-20T19:20:30+01:00' # datetime | The timestamp at which update campaign scheduled to start (optional)

try: 
    api_response = api_instance.update_campaign_partial_update(campaign_id=campaign_id, description=description, device_filter=device_filter, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_campaign_partial_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| DEPRECATED: The ID of the campaign | [optional] 
 **description** | **str**| An optional description of the campaign | [optional] 
 **device_filter** | **str**| The filter for the devices the campaign will target | [optional] 
 **finished** | **datetime**| The timestamp when the update campaign finished | [optional] 
 **name** | **str**| A name for this campaign | [optional] 
 **object** | **str**| The API resource entity | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**| The state of the campaign | [optional] 
 **when** | **datetime**| The timestamp at which update campaign scheduled to start | [optional] 

### Return type

[**UpdateCampaignSerializer**](UpdateCampaignSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_retrieve**
> UpdateCampaignSerializer update_campaign_retrieve(campaign_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when, root_manifest_url=root_manifest_url)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Retrieve campaign</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The ID of the campaign
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
attempts = 'attempts_example' # str |  (optional)
description = 'description_example' # str |  (optional)
device_filter = 'device_filter_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
finished = 'finished_example' # str |  (optional)
name = 'name_example' # str |  (optional)
object = 'object_example' # str |  (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str |  (optional)
when = 'when_example' # str |  (optional)
root_manifest_url = 'root_manifest_url_example' # str | The firmware catalog URL for the manifest that will be sent to the device as part of the campaign (optional)

try: 
    api_response = api_instance.update_campaign_retrieve(campaign_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when, root_manifest_url=root_manifest_url)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_campaign_retrieve: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign | 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **attempts** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **device_filter** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **finished** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **when** | **str**|  | [optional] 
 **root_manifest_url** | **str**| The firmware catalog URL for the manifest that will be sent to the device as part of the campaign | [optional] 

### Return type

[**UpdateCampaignSerializer**](UpdateCampaignSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_status**
> UpdateCampaignStatusSerializer update_campaign_status(campaign_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Show the status of an update campaign</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
campaign_id = 'campaign_id_example' # str | The ID of the update campaign
updating_request_id = 'updating_request_id_example' # str |  (optional)
updating_ip_address = 'updating_ip_address_example' # str |  (optional)
created_at = 'created_at_example' # str |  (optional)
updated_at = 'updated_at_example' # str |  (optional)
attempts = 'attempts_example' # str |  (optional)
description = 'description_example' # str |  (optional)
device_filter = 'device_filter_example' # str |  (optional)
etag = 'etag_example' # str |  (optional)
finished = 'finished_example' # str |  (optional)
name = 'name_example' # str |  (optional)
object = 'object_example' # str |  (optional)
root_manifest_id = 'root_manifest_id_example' # str |  (optional)
state = 'state_example' # str |  (optional)
when = 'when_example' # str |  (optional)

try: 
    api_response = api_instance.update_campaign_status(campaign_id, updating_request_id=updating_request_id, updating_ip_address=updating_ip_address, created_at=created_at, updated_at=updated_at, attempts=attempts, description=description, device_filter=device_filter, etag=etag, finished=finished, name=name, object=object, root_manifest_id=root_manifest_id, state=state, when=when)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_campaign_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the update campaign | 
 **updating_request_id** | **str**|  | [optional] 
 **updating_ip_address** | **str**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **updated_at** | **str**|  | [optional] 
 **attempts** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **device_filter** | **str**|  | [optional] 
 **etag** | **str**|  | [optional] 
 **finished** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object** | **str**|  | [optional] 
 **root_manifest_id** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **when** | **str**|  | [optional] 

### Return type

[**UpdateCampaignStatusSerializer**](UpdateCampaignStatusSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_update**
> UpdateCampaignSerializer update_campaign_update(body)



<p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign</p>

### Example 
```python
import time
import deployment_service
from deployment_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
deployment_service.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# deployment_service.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deployment_service.DefaultApi()
body = deployment_service.WriteUpdateCampaignSerializer() # WriteUpdateCampaignSerializer | Update campaign object to create

try: 
    api_response = api_instance.update_campaign_update(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_campaign_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteUpdateCampaignSerializer**](WriteUpdateCampaignSerializer.md)| Update campaign object to create | 

### Return type

[**UpdateCampaignSerializer**](UpdateCampaignSerializer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

