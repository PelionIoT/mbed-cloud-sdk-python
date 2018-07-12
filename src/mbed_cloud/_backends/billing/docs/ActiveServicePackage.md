# ActiveServicePackage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Service package creation time in RFC3339 date-time with millisecond accuracy and UTC time zone. | 
**expires** | **datetime** | Service package expiration time in RFC3339 date-time with millisecond accuracy and UTC time zone. | 
**firmware_update_count** | **int** | Size of firmware update quota of this service package. | 
**grace_period** | **bool** | Is this service package on grace period or not? | 
**id** | **str** | ID of this service package. | 
**modified** | **datetime** | Service package latest modified time in RFC3339 date-time with millisecond accuracy and UTC time zone. | 
**next_id** | **str** | Next service package ID if this service package has a pending renewal or null. | [optional] 
**previous_id** | **str** | Previous service package ID or null. | [optional] 
**start_time** | **datetime** | Service package start time in RFC3339 date-time with millisecond accuracy and UTC time zone. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


