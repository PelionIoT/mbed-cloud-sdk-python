# GlobalSignCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Unique ID for API client (provided by GlobalSign).  | 
**api_secret** | **str** | API Secret matching the API key (provided by GlobalSign).  | 
**client_certificate** | **str** | The client certificate provided by GlobalSign to allow HTTPS connection over TLS/SSL. The certificate wraps a public key that matches a private key provided by the customer. The certificate must be in PEM format.  | 
**passphrase** | **str** | The passphrase to decrypt the private key in case it is encrypted. Empty if the private key is not encrypted.  | [optional] 
**private_key** | **str** | The private key that matches the client certificate to allow HTTPS connection over TLS/SSL. The private key may be encrypted using a symmetric encryption key derived from a passphrase. The private key must be in PEM format.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


