# TrustedCertificateUpdateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the certificate. | [optional] 
**certificate** | **str** | X509.v3 trusted certificate in PEM format. | [optional] 
**name** | **str** | Certificate name, not longer than 100 characters. | [optional] 
**service** | **str** | Service name where the certificate must be used. | [optional] 
**signature** | **str** | Base64 encoded signature of the account ID signed by the certificate whose data to be updated. Signature must be hashed with SHA256. | [optional] 
**description** | **str** | Human readable description of this certificate, not longer than 500 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


