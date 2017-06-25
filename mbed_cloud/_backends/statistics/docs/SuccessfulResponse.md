# SuccessfulResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | continuation_token included in the request or null. | [optional] 
**has_more** | **bool** | true when there are more results to fetch using the included continuation_token. | [optional] 
**object** | **str** | API resource name. | [optional] 
**limit** | **int** | limit used in the request to retrieve the results. | [optional] 
**continuation_token** | **str** | token to use in after request parameter to fetch more results. | [optional] 
**data** | [**list[Metric]**](Metric.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


