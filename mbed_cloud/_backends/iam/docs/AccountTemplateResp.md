# AccountTemplateResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **dict(str, str)** | List of limits as name-value pairs. | [optional] 
**name** | **str** | Account template name. | 
**parent** | **str** | ID of the parent template, can be null. | [optional] 
**created_at** | **str** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;account-template&#39; | 
**etag** | **str** | API resource entity version. | 
**creation_time_millis** | **int** |  | [optional] 
**id** | **str** | Entity ID. | 
**resources** | [**list[Policy]**](Policy.md) | List of resource-action-allow triplets, policies. | [optional] 
**description** | **str** | Account template description. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


