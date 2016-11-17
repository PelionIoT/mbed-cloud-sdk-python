# ApiKeyInfoRespList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | The entity id to fetch after it. | [optional] 
**object** | **str** | entity name: always &#39;list&#39; | 
**total_count** | **int** | The total number or records, if requested  | 
**limit** | **int** | The number of results to return, (range: 2-1000), or equals to total_count | 
**data** | [**list[ApiKeyInfoResp]**](ApiKeyInfoResp.md) | List of entities. | 
**order** | **str** | The order of the records to return. Available values: ASC, DESC. Default value is ASC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


