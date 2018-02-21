# TrustedCertificateInternalResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | Service name where the certificate is to be used. | 
**enrollment_mode** | **bool** | If true, signature is not required. Default value false. | [optional] 
**private_key** | **str** | Private key of the certificate in PEM or base64 encoded DER format. | 
**account_id** | **str** | The UUID of the account. | 
**certificate** | **str** | X509.v3 trusted certificate in PEM format. | 
**updated_at** | **datetime** | Last update UTC time RFC3339. | [optional] 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;trusted-cert&#39; | 
**device_execution_mode** | **int** | Device execution mode where 1 means a developer certificate. | [optional] 
**owner_id** | **str** | The UUID of the owner. | [optional] 
**subject** | **str** | Subject of the certificate. | 
**name** | **str** | Certificate name. | 
**etag** | **str** | API resource entity version. | 
**status** | **str** | Status of the certificate. | [optional] 
**validity** | **datetime** | Expiration time in UTC formatted as RFC3339. | 
**issuer** | **str** | Issuer of the certificate. | 
**id** | **str** | Entity ID. | 
**description** | **str** | Human readable description of this certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


