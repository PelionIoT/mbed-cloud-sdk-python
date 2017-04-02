# EndpointData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q** | **bool** | Queue mode (default value is false). | [optional] 
**ept** | **str** | Endpoint type. | [optional] 
**original_ep** | **str** | In case of a self-provided endpoint name that is used to initiate the device registration, mbed Cloud provides a new device name to be used from that point on. The new mbed-Cloud-provided name is forwarded as the &#39;ep&#39; property and the original self-provided one as the optional &#39;original-ep&#39; property in a registration notification. The names can then be mapped accordingly. mbed Cloud saves the original endpoint name for future device registrations so there is no need to do the mapping again.  | [optional] 
**resources** | [**list[ResourcesData]**](ResourcesData.md) |  | [optional] 
**ep** | **str** | Endpoint name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


