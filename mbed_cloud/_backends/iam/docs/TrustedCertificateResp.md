# TrustedCertificateResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Human readable description of this certificate. | [optional] 
**service** | **str** | Service name where the certificate is to be used. | 
**device_execution_mode** | **int** | Device execution mode where 1 means a developer certificate. | [optional] 
**created_at** | **str** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;trusted-cert&#39; | 
**subject** | **str** | Subject of the certificate. | 
**account_id** | **str** | The UUID of the account. | 
**etag** | **str** | API resource entity version. | 
**validity** | **str** | Expiration time in UTC formatted as RFC3339. | 
**creation_time_millis** | **int** |  | [optional] 
**issuer** | **str** | Issuer of the certificate. | 
**cert_data** | **str** | X509.v3 trusted certificate in PEM or base64 encoded DER format. | 
**id** | **str** | Entity ID. | 
**name** | **str** | Certificate name. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


