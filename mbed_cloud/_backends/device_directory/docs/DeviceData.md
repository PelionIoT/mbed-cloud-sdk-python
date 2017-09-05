# DeviceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootstrap_expiration_date** | **datetime** | Expiration date of the certificate used to connect to bootstrap server. | [optional] 
**bootstrapped_timestamp** | **datetime** | Timestamp of when the device last went through the bootstrap process. | [optional] 
**connector_expiration_date** | **datetime** | Expiration date of the certificate used to connect to the lwm2m server. | [optional] 
**updated_at** | **datetime** | The time the object was updated. | [optional] 
**ca_id** | **str** | ID of the issuer of the certificate. | [optional] 
**device_class** | **str** | An id representing the model and hardware revision of the device. | [optional] 
**id** | **str** | The id of the device. The device id is used to manage a device across all mbed cloud apis. | [optional] 
**account_id** | **str** | The ID of the associated account. | [optional] 
**endpoint_name** | **str** | The endpoint name given to the device. | [optional] 
**auto_update** | **bool** | DEPRECATED Mark this device for auto firmware update. | [optional] 
**host_gateway** | **str** | The endpoint_name of the host gateway, if appropriate. | [optional] 
**device_execution_mode** | **int** | Defines the type of certificate used. | [optional] 
**mechanism** | **str** | The ID of the channel used to communicate with the device. | [optional] 
**state** | **str** | The current state of the device. | [optional] 
**etag** | **datetime** | The entity instance signature. | [optional] 
**serial_number** | **str** | The serial number of the device. | [optional] 
**firmware_checksum** | **str** | The SHA256 checksum of the current firmware image. | [optional] 
**manifest_timestamp** | **datetime** | The timestamp of the current manifest version. | [optional] 
**vendor_id** | **str** | The device vendor ID. | [optional] 
**description** | **str** | The description of the device. | [optional] 
**deployed_state** | **str** | DEPRECATED The state of the device&#39;s deployment. | [optional] 
**object** | **str** | The API resource entity. | [optional] 
**endpoint_type** | **str** | The endpoint type of the device - e.g. if the device is a gateway. | [optional] 
**deployment** | **str** | DEPRECATED The last deployment used on the device. | [optional] 
**mechanism_url** | **str** | The address of the connector to use. | [optional] 
**trust_level** | **int** | The device trust level. | [optional] 
**name** | **str** | The name of the device. | [optional] 
**device_key** | **str** | Fingerprint of the device certificate. | [optional] 
**created_at** | **datetime** | Timestamp of when the device was created in the device directory. | [optional] 
**manifest** | **str** | DEPRECATED The URL for the current device manifest. | [optional] 
**custom_attributes** | **dict(str, str)** | Custom attributes(key/value). Up to 5 attributes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


