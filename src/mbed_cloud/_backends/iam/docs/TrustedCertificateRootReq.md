# TrustedCertificateRootReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | X509.v3 trusted certificate in PEM format. Chaining multiple certificates after one another is supported. | 
**description** | **str** | Human readable description of this certificate, not longer than 500 characters. | [optional] 
**enrollment_mode** | **bool** | Certificate is used in enrollment mode. Default value is false. | [optional] 
**name** | **str** | Certificate name, not longer than 100 characters. | 
**service** | **str** | Service name where the certificate must be used. | 
**signature** | **str** | DEPRECATED: Base64 encoded signature of the account ID signed by the certificate to be uploaded. Signature must be hashed with SHA256. Optional if enrollment_mode is &#39;true&#39;. | [optional] 
**status** | **str** | Status of the certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


