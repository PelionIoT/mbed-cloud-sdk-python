# BulkResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID | 
**completed_at** | **datetime** | The time of completing the bulk creation task.  | [optional] 
**created_at** | **datetime** | The time of receiving the bulk creation task.  | 
**errors_count** | **int** | The number of enrollment identities with failed processing.  | 
**errors_report_file** | **str** |  | [optional] 
**etag** | **str** | etag | 
**full_report_file** | **str** |  | [optional] 
**id** | **str** | Bulk ID | 
**object** | **str** |  | 
**processed_count** | **int** | The number of enrollment identities processed until now.  | 
**status** | **str** | The state of the process is &#39;new&#39; at the time of creation. If the creation is still in progress, the state is shown as &#39;processing&#39;. When the request has been fully processed, the state changes to &#39;completed&#39;.  | [default to 'new']
**total_count** | **int** | Total number of enrollment identities found in the input CSV.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


