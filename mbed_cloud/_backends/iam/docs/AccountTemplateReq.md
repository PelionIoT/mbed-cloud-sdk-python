# AccountTemplateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **str** | ID of the parent template, can be null. | [optional] 
**name** | **str** | Account template name. | 
**limits** | **dict(str, str)** | List of limits as name-value pairs. | [optional] 
**template_type** | **str** | Account template type. | [optional] 
**reason** | **str** | Account template update reason. | [optional] 
**resources** | [**list[Policy]**](Policy.md) | List of resource-action-allow triplets, policies. | [optional] 
**description** | **str** | Account template description. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


