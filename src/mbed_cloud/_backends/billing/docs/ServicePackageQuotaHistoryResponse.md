# ServicePackageQuotaHistoryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | After which quota history ID this paged response is fetched. | [optional] 
**data** | [**list[ServicePackageQuotaHistoryItem]**](ServicePackageQuotaHistoryItem.md) | List of history items, empty list if no entries are available. | 
**has_more** | **bool** | If there is next available quota history paged response to be fetched. | 
**limit** | **int** | Maximum amount of quota history entries contained in one paged response. | 
**object** | **str** | Always set to &#39;service-package-quota-history&#39;. | 
**total_count** | **int** | Sum of all quota history entries that should be returned | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


