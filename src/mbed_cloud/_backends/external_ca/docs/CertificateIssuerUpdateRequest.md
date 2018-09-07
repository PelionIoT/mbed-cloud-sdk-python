# CertificateIssuerUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | General description for the certificate issuer. | [optional] 
**issuer_attributes** | **dict(str, str)** | General attributes for connecting the certificate issuer. When the issuer_type is GLOBAL_SIGN, the value shall be empty. When the issuer_type is CFSSL_AUTH, see definition of CfsslAttributes.  | [optional] 
**issuer_credentials** | **dict(str, str)** | The credentials required for connecting to the certificate issuer. When the issuer_type is GLOBAL_SIGN, see definition of GlobalSignCredentials. When the issuer_type is CFSSL_AUTH, see definition of CfsslAuthCredentials.  | [optional] 
**name** | **str** | Certificate issuer name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


