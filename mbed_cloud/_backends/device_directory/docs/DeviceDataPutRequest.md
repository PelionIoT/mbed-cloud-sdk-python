# DeviceDataPutRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the device. | [optional] 
**endpoint_name** | **str** | The endpoint name given to the device. | [optional] 
**auto_update** | **bool** | DEPRECATED Mark this device for auto firmware update. | [optional] 
**host_gateway** | **str** | The endpoint_name of the host gateway, if appropriate. | [optional] 
**object** | **str** | The API resource entity. | [optional] 
**custom_attributes** | **dict(str, str)** | Custom attributes(key/value). Up to 5 attributes | [optional] 
**device_key** | **str** | Fingerprint of the device certificate. | 
**endpoint_type** | **str** | The endpoint type of the device - e.g. if the device is a gateway. | [optional] 
**ca_id** | **str** | ID of the issuer of the certificate. | 
**name** | **str** | The name of the device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


