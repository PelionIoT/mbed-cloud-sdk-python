# DeveloperCertificateResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | account to which the developer certificate belongs | [optional] 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**description** | **str** | Description for the developer certificate. | [optional] 
**developer_certificate** | **str** | PEM format X.509 developer certificate. | [optional] 
**developer_private_key** | **str** | PEM format developer private key associated to the certificate. | [optional] 
**etag** | **str** | API resource entity version. | [optional] 
**id** | **str** | mUUID that uniquely identifies the developer certificate. | [optional] 
**name** | **str** | Name of the developer certificate. | [optional] 
**object** | **str** | Entity name, always &#39;trusted-cert&#39; | [optional] 
**security_file_content** | **str** | Content of the security.c file that will be flashed into the device to provide the security credentials | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


