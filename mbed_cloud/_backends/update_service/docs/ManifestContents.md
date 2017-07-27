# ManifestContents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** | A 128-bit random field | [optional] 
**payload_info** | [**ManifestContentsPayloadInfo**](ManifestContentsPayloadInfo.md) |  | [optional] 
**manifest_version** | **str** | The version of the manifest format being used. | [optional] 
**digest_algorithm** | [**ManifestContentsDigestAlgorithm**](ManifestContentsDigestAlgorithm.md) |  | [optional] 
**text** | [**list[ManifestContentsText]**](ManifestContentsText.md) |  | [optional] 
**directives** | [**list[ManifestContentsDirectives]**](ManifestContentsDirectives.md) |  | [optional] 
**timestamp** | **int** | The time the manifest was created. The timestamp is stored as Unix time. | [optional] 
**dependenices** | [**list[ManifestContentsPayloadInfoPayloadReference]**](ManifestContentsPayloadInfoPayloadReference.md) |  | [optional] 
**conditions** | [**list[ManifestContentsConditions]**](ManifestContentsConditions.md) |  | [optional] 
**aliases** | [**list[ManifestContentsPayloadInfoPayloadReference]**](ManifestContentsPayloadInfoPayloadReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


