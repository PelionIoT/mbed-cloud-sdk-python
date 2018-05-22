# TrustedCertificateResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The UUID of the account. | 
**certificate** | **str** | X509.v3 trusted certificate in PEM format. | 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**description** | **str** | Human readable description of this certificate. | [optional] 
**device_execution_mode** | **int** | Device execution mode where 1 means a developer certificate. | [optional] 
**enrollment_mode** | **bool** | If true, signature is not required. Default value false. | [optional] 
**etag** | **str** | API resource entity version. | 
**id** | **str** | Entity ID. | 
**issuer** | **str** | Issuer of the certificate. | 
**name** | **str** | Certificate name. | 
**object** | **str** | Entity name: always &#39;trusted-cert&#39; | 
**owner_id** | **str** | The UUID of the owner. | [optional] 
**service** | **str** | Service name where the certificate is to be used. | 
**status** | **str** | Status of the certificate. | [optional] 
**subject** | **str** | Subject of the certificate. | 
**updated_at** | **datetime** | Last update UTC time RFC3339. | [optional] 
**validity** | **datetime** | Expiration time in UTC formatted as RFC3339. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


