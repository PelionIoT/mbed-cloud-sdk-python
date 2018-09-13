# UploadChunkInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time the entity was created | [optional] 
**etag** | **str** | API resource entity version | [optional] 
**hash** | **str** | The hash of the chunk. The default hash is MD5. If no Content-MD5 header is supplied as part of uploading the chunk then this will be empty. | [optional] 
**id** | **int** | The chunk number | [optional] 
**length** | **int** | The length of the chunk | [optional] 
**object** | **str** | Entity name: always &#39;upload-info&#39; | [optional] 
**status** | **str** | The upload status of this chunk | [optional] 
**updated_at** | **datetime** | The time the entity was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


