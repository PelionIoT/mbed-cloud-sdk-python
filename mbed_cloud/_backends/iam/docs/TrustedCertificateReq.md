# TrustedCertificateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | Base64 encoded signature of the account ID signed by the certificate to be uploaded. Signature must be hashed with SHA256. | 
**cert_data** | **str** | X509.v3 trusted certificate in PEM or base64 encoded DER format. | 
**name** | **str** | Certificate name. | 
**service** | **str** | Service name where the certificate must be used. | 
**description** | **str** | Human readable description of this certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


