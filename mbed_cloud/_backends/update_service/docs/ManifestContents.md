# ManifestContents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The device class&#39;s 128-bit RFC4122 GUID as a hexidecimal digit string | [optional] 
**vendor_id** | **str** | The vendor&#39;s 128-bit RFC4122 GUID as a hexidecimal digit string | [optional] 
**manifest_version** | **int** | The manifest format version | [optional] 
**description** | **str** | A short description of the update | [optional] 
**nonce** | **str** | A 128-bit random field. This is provided by the manifest tool to ensure that the signing algorithm is safe from timing side-channel attacks. | [optional] 
**timestamp** | **int** | The time the manifest was created. The timestamp is stored as Unix time. | [optional] 
**encryption_mode** | [**ManifestContentsEncryptionMode**](ManifestContentsEncryptionMode.md) |  | [optional] 
**apply_immediately** | **bool** | A flag that indicates whether the update described by the manifest should be applied as soon as possible | [optional] 
**device_id** | **str** | The device&#39;s 128-bit RFC4122 GUID as a hexidecimal digit string. Each device has a single, unique device ID. | [optional] 
**payload** | [**ManifestContentsPayload**](ManifestContentsPayload.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


