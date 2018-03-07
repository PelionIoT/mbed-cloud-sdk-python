# TrustedCertificateResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | Service name where the certificate is to be used. | 
**status** | **str** | Status of the certificate. | [optional] 
**name** | **str** | Certificate name. | 
**certificate** | **str** | X509.v3 trusted certificate in PEM format. | 
**enrollment_mode** | **bool** | If true, signature is not required. Default value false. | [optional] 
**issuer** | **str** | Issuer of the certificate. | 
**device_execution_mode** | **int** | Device execution mode where 1 means a developer certificate. | [optional] 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;trusted-cert&#39; | 
**subject** | **str** | Subject of the certificate. | 
**updated_at** | **datetime** | Last update UTC time RFC3339. | [optional] 
**account_id** | **str** | The UUID of the account. | 
**etag** | **str** | API resource entity version. | 
**validity** | **datetime** | Expiration time in UTC formatted as RFC3339. | 
**owner_id** | **str** | The UUID of the owner. | [optional] 
**id** | **str** | Entity ID. | 
**description** | **str** | Human readable description of this certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


