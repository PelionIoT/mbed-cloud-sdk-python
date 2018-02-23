# AdminUserUpdateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number, not longer than 100 characters. | [optional] 
**username** | **str** | A username containing alphanumerical letters and -,._@+&#x3D; characters. It must be at least 4 but not more than 30 character long. | [optional] 
**groups** | **list[str]** | A list of group IDs this user belongs to. | [optional] 
**is_marketing_accepted** | **bool** | A flag indicating that receiving marketing information has been accepted. | [optional] 
**user_properties** | [**dict(str, dict(str, str))**](dict.md) | User&#39;s account specific custom properties. | [optional] 
**is_gtc_accepted** | **bool** | A flag indicating that the General Terms and Conditions has been accepted. | [optional] 
**is_totp_enabled** | **bool** | A flag indicating whether 2-factor authentication (TOTP) has to be enabled or disabled. | [optional] 
**notification_properties** | **dict(str, str)** | Users notification properties for root admins. Currently supported; &#39;agreement_acceptance_notification&#39;, which controls whether notification should be sent upon accepting an agreement in an account. Possible values are: &#39;always_notify&#39;, &#39;only_first&#39; and &#39;not_interested&#39;. | [optional] 
**status** | **str** | The status of the user. | [optional] 
**full_name** | **str** | The full name of the user, not longer than 100 characters. | [optional] 
**address** | **str** | Address, not longer than 100 characters. | [optional] 
**password** | **str** | The password when creating a new user. It will be generated when not present in the request. | [optional] 
**email** | **str** | The email address, not longer than 254 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


