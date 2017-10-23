# DeviceDataPatchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the device. | [optional] 
**endpoint_name** | **str** | The endpoint name given to the device. | [optional] 
**auto_update** | **bool** | DEPRECATED: Mark this device for automatic firmware update. | [optional] 
**host_gateway** | **str** | The &#x60;endpoint_name&#x60; of the host gateway, if appropriate. | [optional] 
**object** | **str** | The API resource entity. | [optional] 
**custom_attributes** | **dict(str, str)** | Up to five custom key-value attributes. Note that keys cannot start with a number. | [optional] 
**device_key** | **str** | The fingerprint of the device certificate. | [optional] 
**endpoint_type** | **str** | The endpoint type of the device. For example, the device is a gateway. | [optional] 
**ca_id** | **str** | The certificate issuer&#39;s ID. | [optional] 
**name** | **str** | The name of the device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


