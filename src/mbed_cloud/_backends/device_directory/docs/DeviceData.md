# DeviceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the associated account. | [optional] 
**auto_update** | **bool** | DEPRECATED: Mark this device for automatic firmware update. | [optional] 
**bootstrap_expiration_date** | **date** | The expiration date of the certificate used to connect to bootstrap server. | [optional] 
**bootstrapped_timestamp** | **datetime** | The timestamp of the device&#39;s most recent bootstrap process. | [optional] 
**ca_id** | **str** | The certificate issuer&#39;s ID. | [optional] 
**connector_expiration_date** | **date** | The expiration date of the certificate used to connect to LwM2M server. | [optional] 
**created_at** | **datetime** | The timestamp of when the device was created in the device directory. | [optional] 
**custom_attributes** | **dict(str, str)** | Up to five custom key-value attributes. | [optional] 
**deployed_state** | **str** | DEPRECATED: The state of the device&#39;s deployment. | [optional] 
**deployment** | **str** | DEPRECATED: The last deployment used on the device. | [optional] 
**description** | **str** | The description of the device. | [optional] 
**device_class** | **str** | An ID representing the model and hardware revision of the device. | [optional] 
**device_execution_mode** | **int** | The execution mode from the certificate of the device. Defaults to inheriting from host_gateway device. Permitted values:   - 0 - unspecified execution mode (default if host_gateway invalid or not set)   - 1 - development devices   - 5 - production devices | [optional] 
**device_key** | **str** | The fingerprint of the device certificate. | [optional] 
**endpoint_name** | **str** | The endpoint name given to the device. | [optional] 
**endpoint_type** | **str** | The endpoint type of the device. For example, the device is a gateway. | [optional] 
**enrolment_list_timestamp** | **datetime** | The claim date/time. | [optional] 
**etag** | **datetime** | The entity instance signature. | [optional] 
**firmware_checksum** | **str** | The SHA256 checksum of the current firmware image. | [optional] 
**groups** | **list[str]** | An array containing an id of each group this device belongs to | [optional] 
**host_gateway** | **str** | The &#x60;endpoint_name&#x60; of the host gateway, if appropriate. | [optional] 
**id** | **str** | The ID of the device. The device ID is used across all Device Management APIs. | [optional] 
**manifest** | **str** | DEPRECATED: The URL for the current device manifest. | [optional] 
**manifest_timestamp** | **datetime** | The timestamp of the current manifest version. | [optional] 
**mechanism** | **str** | The ID of the channel used to communicate with the device. | [optional] 
**mechanism_url** | **str** | The address of the connector to use. | [optional] 
**name** | **str** | The name of the device. | [optional] 
**object** | **str** | The API resource entity. | [optional] 
**serial_number** | **str** | The serial number of the device. | [optional] 
**state** | **str** | The current state of the device. | [optional] 
**updated_at** | **datetime** | The time the object was updated. | [optional] 
**vendor_id** | **str** | The device vendor ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


