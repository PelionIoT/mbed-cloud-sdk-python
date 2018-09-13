# TrustedCertificateUpdateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | A chain of X509.v3 trusted certificates in PEM format. The chain must contain all certificates from root to leaf. Otherwise, the signature parameter is required. | [optional] 
**description** | **str** | Human readable description of this certificate, not longer than 500 characters. | [optional] 
**enrollment_mode** | **bool** | Certificate is used in enrollment mode. Default value is false. | [optional] 
**name** | **str** | Certificate name, not longer than 100 characters. | [optional] 
**service** | **str** | Service name where the certificate must be used. | [optional] 
**signature** | **str** | DEPRECATED: Base64 encoded signature of the account ID signed by the certificate to be uploaded. The signature must be hashed with SHA256. | [optional] 
**status** | **str** | Status of the certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


