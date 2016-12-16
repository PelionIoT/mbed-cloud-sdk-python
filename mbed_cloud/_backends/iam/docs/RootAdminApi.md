# iam.RootAdminApi

All URIs are relative to *https://api.mbedcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_template**](RootAdminApi.md#create_account_template) | **POST** /admin/v3/account-templates | Create a new account template.
[**delete_account_template**](RootAdminApi.md#delete_account_template) | **DELETE** /admin/v3/account-templates/{template-id} | Delete account template by ID.
[**get_account_template**](RootAdminApi.md#get_account_template) | **GET** /admin/v3/account-templates/{template-id} | Get account template by ID.
[**get_all_account_templates**](RootAdminApi.md#get_all_account_templates) | **GET** /admin/v3/account-templates | Get all account templates.
[**update_account_template**](RootAdminApi.md#update_account_template) | **PUT** /admin/v3/account-templates/{template-id} | Update an existing account template.


# **create_account_template**
> AccountTemplateResp create_account_template(body)

Create a new account template.

Endpoint for creating a new account template.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.RootAdminApi()
body = iam.AccountTemplateReq() # AccountTemplateReq | Details of the account template to be created.

try: 
    # Create a new account template.
    api_response = api_instance.create_account_template(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RootAdminApi->create_account_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountTemplateReq**](AccountTemplateReq.md)| Details of the account template to be created. | 

### Return type

[**AccountTemplateResp**](AccountTemplateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_template**
> delete_account_template(template_id)

Delete account template by ID.

Endpoint for deleting a account template by ID.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.RootAdminApi()
template_id = 'template_id_example' # str | The ID of the account template to be deleted.

try: 
    # Delete account template by ID.
    api_instance.delete_account_template(template_id)
except ApiException as e:
    print "Exception when calling RootAdminApi->delete_account_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the account template to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_template**
> AccountTemplateResp get_account_template(template_id)

Get account template by ID.

Endpoint for retrieving a account template by ID.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.RootAdminApi()
template_id = 'template_id_example' # str | The ID of the account template to be retrieved.

try: 
    # Get account template by ID.
    api_response = api_instance.get_account_template(template_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RootAdminApi->get_account_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the account template to be retrieved. | 

### Return type

[**AccountTemplateResp**](AccountTemplateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_account_templates**
> AccountTemplateRespList get_all_account_templates(limit=limit, after=after, order=order, include=include)

Get all account templates.

Endpoint for retrieving account templates in an array.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.RootAdminApi()
limit = 50 # int | The number of results to return (2-1000), default is 50. (optional) (default to 50)
after = 'after_example' # str | The entity id to fetch after it (optional)
order = 'ASC' # str | The order of the records, ASC or DESC. Default value is ASC (optional) (default to ASC)
include = 'include_example' # str | Comma separate additional data to return. Currently supported: total_count (optional)

try: 
    # Get all account templates.
    api_response = api_instance.get_all_account_templates(limit=limit, after=after, order=order, include=include)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RootAdminApi->get_all_account_templates: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results to return (2-1000), default is 50. | [optional] [default to 50]
 **after** | **str**| The entity id to fetch after it | [optional] 
 **order** | **str**| The order of the records, ASC or DESC. Default value is ASC | [optional] [default to ASC]
 **include** | **str**| Comma separate additional data to return. Currently supported: total_count | [optional] 

### Return type

[**AccountTemplateRespList**](AccountTemplateRespList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_template**
> AccountTemplateResp update_account_template(template_id, body)

Update an existing account template.

Endpoint for updating an existing account template.

### Example 
```python
import time
import iam
from iam.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
iam.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# iam.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iam.RootAdminApi()
template_id = 'template_id_example' # str | The ID of the account template to be updated.
body = iam.AccountTemplateReq() # AccountTemplateReq | Details of the account template to be updated.

try: 
    # Update an existing account template.
    api_response = api_instance.update_account_template(template_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RootAdminApi->update_account_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the account template to be updated. | 
 **body** | [**AccountTemplateReq**](AccountTemplateReq.md)| Details of the account template to be updated. | 

### Return type

[**AccountTemplateResp**](AccountTemplateResp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

