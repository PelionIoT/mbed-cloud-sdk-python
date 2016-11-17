# ApiKeyInfoResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the API key. | [optional] 
**apikey** | **str** | API key. | 
**name** | **str** | The display name for the API key. | 
**created_at** | **str** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | entity name: always &#39;apikey&#39; | 
**creation_time** | **int** | The timestamp of the API key creation in the storage, in milliseconds. | [optional] 
**etag** | **str** | API resource entity version. | 
**groups** | **list[str]** | A list of group IDs this API key belongs to. | [optional] 
**owner** | **str** | The owner of this API key, who is the creator by default. | [optional] 
**secret_key** | **str** | API key secret. | [optional] 
**id** | **str** | UUID of the API key. | 
**last_login_time** | **int** | The timestamp of the latest API key usage, in milliseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


