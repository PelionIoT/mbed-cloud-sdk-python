# ManifestContents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** | A 128-bit random field | [optional] 
**vendor_id** | **str** | Hex representation of the 128-bit RFC4122 GUID that represents the vendor. | [optional] 
**manifest_version** | **str** | The version of the manifest format being used. | [optional] 
**description** | **str** | A short description of the update. | [optional] 
**payload_info** | [**ManifestContentsPayloadInfo**](ManifestContentsPayloadInfo.md) |  | [optional] 
**digest_algorithm** | [**ManifestContentsDigestAlgorithm**](ManifestContentsDigestAlgorithm.md) |  | [optional] 
**text** | [**list[ManifestContentsText]**](ManifestContentsText.md) |  | [optional] 
**encryption_mode** | [**ManifestContentsEncryptionMode**](ManifestContentsEncryptionMode.md) |  | [optional] 
**apply_immediately** | **bool** | A flag that indicates that the update described by the manifest should be applied as soon as possible. | [optional] 
**directives** | [**list[ManifestContentsDirectives]**](ManifestContentsDirectives.md) |  | [optional] 
**device_id** | **str** | Hex representation of the 128-bit RFC4122 GUID that uniquely identifies the device. Each device has a single, unique device ID. | [optional] 
**timestamp** | **int** | The time the manifest was created. The timestamp is stored as Unix time. | [optional] 
**class_id** | **str** | Hex representation of the 128-bit RFC4122 GUID that represents the device class that the update targets. | [optional] 
**dependenices** | [**list[ManifestContentsPayloadInfoPayloadReference]**](ManifestContentsPayloadInfoPayloadReference.md) |  | [optional] 
**conditions** | [**list[ManifestContentsConditions]**](ManifestContentsConditions.md) |  | [optional] 
**payload** | [**ManifestContentsPayload**](ManifestContentsPayload.md) |  | [optional] 
**aliases** | [**list[ManifestContentsPayloadInfoPayloadReference]**](ManifestContentsPayloadInfoPayloadReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


