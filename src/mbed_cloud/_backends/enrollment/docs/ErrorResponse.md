# ErrorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Response code. | [optional] 
**fields** | [**list[Field]**](Field.md) | Failed input fields during request object validation. | [optional] 
**message** | **str** | A human readable message with detailed info. | [optional] 
**object** | **str** | Entity name, always &#39;error&#39;. | [optional] [default to 'error']
**request_id** | **str** | Request ID. | [optional] 
**type** | **str** | Error type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


