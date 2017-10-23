# UserUpdateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number, not longer than 100 characters. | [optional] 
**username** | **str** | A username containing alphanumerical letters and -,._@+&#x3D; characters. It must be at least 4 but not more than 30 character long. | [optional] 
**is_marketing_accepted** | **bool** | A flag indicating that receiving marketing information has been accepted. | [optional] 
**is_gtc_accepted** | **bool** | A flag indicating that the General Terms and Conditions has been accepted. | [optional] 
**is_totp_enabled** | **bool** | A flag indicating whether 2-factor authentication (TOTP) has to be enabled or disabled. | [optional] 
**status** | **str** | The status of the user. | [optional] 
**full_name** | **str** | The full name of the user, not longer than 100 characters. | [optional] 
**address** | **str** | Address, not longer than 100 characters. | [optional] 
**password** | **str** | The password when creating a new user. It will be generated when not present in the request. | [optional] 
**email** | **str** | The email address, not longer than 254 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


