# Endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Deprecated and the value is always ACTIVE. Only used for API backwards compatibility reasons. | [optional] 
**q** | **bool** | Determines whether the device is in queue mode.  &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Queue mode&lt;/b&gt;&lt;br/&gt; When an endpoint is in Queue mode, messages sent to the endpoint do not wake up the physical device. The messages are queued  and delivered when the device wakes up and connects to mbed Cloud Connect itself. You can also use the Queue mode when  the device is behind a NAT and cannot be reached directly by mbed Cloud Connect.  | [optional] 
**type** | **str** | Type of endpoint. (Free text) | [optional] 
**name** | **str** | Unique mbed Cloud Device ID representing the endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


