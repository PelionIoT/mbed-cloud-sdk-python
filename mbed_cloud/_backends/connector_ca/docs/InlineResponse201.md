# InlineResponse201

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_file_content** | **str** | Content of the security.c file that will be flashed into the device to provide the security credentials | [optional] 
**description** | **str** | Description for the developer certificate. | [optional] 
**developer_certificate** | **str** | PEM format X.509 developer certificate. | [optional] 
**server_uri** | **str** | URI to which the client needs to connect to. | [optional] 
**account_id** | **str** | account to which the developer certificate belongs | [optional] 
**developer_private_key** | **str** | PEM format developer private key associated to the certificate. | [optional] 
**server_certificate** | **str** | PEM format X.509 server certificate that will be used to validate the server certificate that will be received during the TLS/DTLS handshake. | [optional] 
**id** | **str** | mUUID that uniquely identifies the developer certificate. | [optional] 
**name** | **str** | Name of the developer certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


