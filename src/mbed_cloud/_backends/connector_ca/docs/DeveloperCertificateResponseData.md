# DeveloperCertificateResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_file_content** | **str** | The content of the &#x60;security.c&#x60; file that is flashed into the device to provide the security credentials | [optional] 
**description** | **str** | Description for the developer certificate. | [optional] 
**name** | **str** | The name of the developer certificate. | [optional] 
**developer_certificate** | **str** | The PEM format X.509 developer certificate. | [optional] 
**server_uri** | **str** | The URI to which the client needs to connect to. | [optional] 
**created_at** | **str** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name, always &#x60;trusted-cert&#x60;. | [optional] 
**developer_private_key** | **str** | The PEM format developer private key associated to the certificate. | [optional] 
**server_certificate** | **str** | The PEM format X.509 server certificate that is used to validate the server certificate that is received during the TLS/DTLS handshake. | [optional] 
**etag** | **str** | API resource entity version. | [optional] 
**id** | **str** | The mUUID that uniquely identifies the developer certificate. | [optional] 
**account_id** | **str** | The account to which the developer certificate belongs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


