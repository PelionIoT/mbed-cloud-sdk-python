# ApiKeyInfoResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the API key. | [optional] 
**groups** | **list[str]** | A list of group IDs this API key belongs to. | [optional] 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;api-key&#39; | 
**creation_time** | **int** | The timestamp of the API key creation in the storage, in milliseconds. | [optional] 
**updated_at** | **datetime** | Last update UTC time RFC3339. | [optional] 
**name** | **str** | The display name for the API key. | 
**etag** | **str** | API resource entity version. | 
**key** | **str** | The API key. | 
**owner** | **str** | The owner of this API key, who is the creator by default. | [optional] 
**id** | **str** | The UUID of the API key. | 
**last_login_time** | **int** | The timestamp of the latest API key usage, in milliseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


