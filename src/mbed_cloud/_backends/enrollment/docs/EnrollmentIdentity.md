# EnrollmentIdentity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_identity** | **str** | Enrollment identity. | [optional] 
**object** | **str** |  | [optional] 
**account_id** | **str** | muuid | 
**created_at** | **datetime** | The time of the enrollment identity creation. | 
**claimed_at** | **datetime** | The time of claiming the device to be assigned to the account. | [optional] 
**expires_at** | **datetime** | The enrollment claim expiration time. If the device does not connect to Mbed Cloud before the expiration, the claim is removed without a separate notice | 
**enrolled_device_id** | **str** | Enrolled device internal ID | [optional] 
**etag** | **str** |  | 
**id** | **str** | Enrollment identity internal id | 
**device_id** | **str** | The ID of the device in the Device Directory once it has been registered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


