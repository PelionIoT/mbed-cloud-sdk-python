# UserInfoReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **list[str]** | A list of IDs of the groups this user belongs to. | [optional] 
**username** | **str** | A username containing alphanumerical letters and -,._@+&#x3D; characters. | [optional] 
**is_marketing_accepted** | **bool** | A flag indicating that receiving marketing information has been accepted. | [optional] 
**is_gtc_accepted** | **bool** | A flag indicating that the General Terms and Conditions has been accepted. | [optional] 
**full_name** | **str** | The full name of the user, not longer than 100 characters. | [optional] 
**address** | **str** | Address, not longer than 100 characters. | [optional] 
**password** | **str** | The password when creating a new user. It will will generated when not present in the request. | [optional] 
**phone_number** | **str** | Phone number, not longer than 100 characters. | [optional] 
**email** | **str** | The email address, not longer than 100 characters. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


