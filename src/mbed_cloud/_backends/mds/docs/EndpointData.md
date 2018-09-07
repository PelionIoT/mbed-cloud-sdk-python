# EndpointData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ep** | **str** | Unique Device Management device ID. | [optional] 
**ept** | **str** | Endpoint type. | [optional] 
**original_ep** | **str** | In case of a self-provided endpoint name that is used to initiate the device registration, Device Management provides a new device ID to be used from that point on. The new Pelion platform provided Device ID is forwarded as the &#39;ep&#39; property and the original self-provided one as the optional &#39;original-ep&#39; property in a registration notification. The name and ID can then be mapped accordingly. Device Management saves the original endpoint name in the Device Directory for future device registrations so that you don&#39;t need to do the mapping again.  | [optional] 
**q** | **bool** | Queue mode (default value is false). | [optional] 
**resources** | [**list[ResourcesData]**](ResourcesData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


