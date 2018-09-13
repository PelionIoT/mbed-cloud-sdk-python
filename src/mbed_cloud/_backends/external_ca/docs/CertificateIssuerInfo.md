# CertificateIssuerInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**description** | **str** | General description for the certificate issuer. | [optional] 
**etag** | **str** | Entity instance signature. | [optional] 
**id** | **str** | The ID of the certificate issuer. | [optional] 
**issuer_attributes** | **dict(str, str)** | General attributes for connecting the certificate issuer. When the issuer_type is GLOBAL_SIGN, the value shall be empty. When the issuer_type is CFSSL_AUTH, see definition of CfsslAttributes.  | [optional] 
**issuer_type** | **str** | The type of the certificate issuer. - GLOBAL_SIGN:   Certificates are issued by GlobalSign service. The users must provide their own GlobalSign account credentials. - CFSSL_AUTH:   Certificates are issued by CFSSL authenticated signing service.   The users must provide their own CFSSL host_url and credentials.  | 
**name** | **str** | Certificate issuer name, unique per account. | [optional] 
**object** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


