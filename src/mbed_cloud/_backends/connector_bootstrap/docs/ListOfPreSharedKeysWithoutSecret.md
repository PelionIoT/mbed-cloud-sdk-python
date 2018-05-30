# ListOfPreSharedKeysWithoutSecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | An offset token for current page. | [optional] 
**continuation_marker** | **str** | An offset token for fetching the next page. Note that exactly the same limit needs to be used on the request for fetching the subsequent pages. | [optional] 
**data** | [**list[PreSharedKeyWithoutSecret]**](PreSharedKeyWithoutSecret.md) | Array of the pre-shared key entries. The array is empty if there are no pre-shared keys. | 
**has_more** | **bool** | Are there more results available. | 
**limit** | **int** | The value of limit query parameter from the request, or default if not specified. | 
**object** | **str** | The type of this API object is a \&quot;list\&quot;. | 
**order** | **str** | The creation time based order of the entries. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


