# ManifestContents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | Hex representation of the 128-bit RFC4122 GUID that represents the device class that the update targets. | [optional] 
**vendor_id** | **str** | Hex representation of the 128-bit RFC4122 GUID that represents the vendor. | [optional] 
**manifest_version** | **int** | A short description of the update. | [optional] 
**description** | **str** | A short description of the update. | [optional] 
**nonce** | **str** | A 128-bit random field | [optional] 
**timestamp** | **int** | The time the manifest was created. The timestamp is stored as Unix time. | [optional] 
**encryption_mode** | [**ManifestContentsEncryptionMode**](ManifestContentsEncryptionMode.md) |  | [optional] 
**apply_immediately** | **bool** | A flag that indicates that the update described by the manifest should be applied as soon as possible. | [optional] 
**device_id** | **str** | Hex representation of the 128-bit RFC4122 GUID that uniquely identifies the device. Each device has a single, unique device ID. | [optional] 
**payload** | [**ManifestContentsPayload**](ManifestContentsPayload.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


