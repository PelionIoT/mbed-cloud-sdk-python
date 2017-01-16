# CACertificateResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The UUID of the account. | 
**service** | **str** | Service name where the certificate is to be used. | 
**created_at** | **str** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;ca-cert&#39; | 
**subject** | **str** | Subject of the certificate. | 
**validity** | **str** | Expiration time in UTC formatted as RFC3339. | 
**etag** | **str** | API resource entity version. | 
**creation_time_millis** | **int** |  | [optional] 
**issuer** | **str** | Issuer of the certificate. | 
**cert_data** | **str** | X509.v3 CA certificate in PEM or base64 encoded DER format. | 
**id** | **str** | Entity ID. | 
**name** | **str** | Certificate name. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


