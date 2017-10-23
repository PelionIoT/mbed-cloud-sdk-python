# TrustedCertificateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the certificate. | [optional] 
**certificate** | **str** | X509.v3 trusted certificate in PEM format. | 
**name** | **str** | Certificate name, not longer than 100 characters. | 
**service** | **str** | Service name where the certificate must be used. | 
**signature** | **str** | Base64 encoded signature of the account ID signed by the certificate to be uploaded. Signature must be hashed with SHA256. | 
**description** | **str** | Human readable description of this certificate, not longer than 500 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


