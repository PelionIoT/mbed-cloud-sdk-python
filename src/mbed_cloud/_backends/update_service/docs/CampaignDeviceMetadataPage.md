# CampaignDeviceMetadataPage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | The entity ID to fetch after the given one | [optional] 
**has_more** | **bool** | Flag indicating whether there are more results | [optional] 
**total_count** | **int** | The total number or records, if requested. It might be returned also for small lists. | [optional] 
**object** | **str** | Entity name: always &#39;list&#39; | [optional] 
**limit** | **int** | The number of results to return, (range: 2-1000), or equals to total_count | [optional] 
**data** | [**list[CampaignDeviceMetadata]**](CampaignDeviceMetadata.md) | A list of entities | [optional] 
**order** | **str** | The order of the records to return. Acceptable values: ASC, DESC. Default: ASC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


