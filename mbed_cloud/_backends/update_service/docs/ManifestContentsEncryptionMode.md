# ManifestContentsEncryptionMode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enum** | **int** | The kind of hashing, signing, and encryption to use. These modes are available: 1: none-ecc-secp256r1-sha256: SHA-256 hashing, ECDSA signatures, using the secp256r1 curve. No payload encryption is used. 2: aes-128-ctr-ecc-secp256r1-sha256: SHA-256 hashing, ECDSA signatures, using the secp256r1 curve. The payload is encrypted with AES-128 in CTR-mode. 3: none-none-sha256: SHA-256 hashing. No signature is used. No payload encryption is used. This mode is not recommended except over existing, trusted connections.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


