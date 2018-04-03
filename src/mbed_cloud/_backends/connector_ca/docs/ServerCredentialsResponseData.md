# ServerCredentialsResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**etag** | **str** | API resource entity version. | [optional] 
**id** | **str** | mUUID that uniquely identifies the entity. | [optional] 
**object** | **str** | Entity name, always &#39;server-credentials&#39; | [optional] 
**server_certificate** | **str** | PEM format X.509 server certificate that will be used to validate the server certificate that will be received during the TLS/DTLS handshake. | [optional] 
**server_uri** | **str** | Server URI to which the client needs to connect to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


