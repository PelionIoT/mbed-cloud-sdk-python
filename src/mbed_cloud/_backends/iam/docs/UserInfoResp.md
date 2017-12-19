# UserInfoResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system. | 
**username** | **str** | A username containing alphanumerical letters and -,._@+&#x3D; characters. | [optional] 
**groups** | **list[str]** | A list of IDs of the groups this user belongs to. | [optional] 
**password_changed_time** | **int** | A timestamp of the latest change of the user password, in milliseconds. | [optional] 
**email_verified** | **bool** | A flag indicating whether the user&#39;s email address has been verified or not. | [optional] 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;user&#39; | 
**is_gtc_accepted** | **bool** | A flag indicating that the General Terms and Conditions has been accepted. | [optional] 
**account_id** | **str** | The UUID of the account. | 
**email** | **str** | The email address. | 
**login_history** | [**list[LoginHistory]**](LoginHistory.md) | Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format. | [optional] 
**is_totp_enabled** | **bool** | A flag indicating whether 2-factor authentication (TOTP) has been enabled. | [optional] 
**is_marketing_accepted** | **bool** | A flag indicating that receiving marketing information has been accepted. | [optional] 
**etag** | **str** | API resource entity version. | 
**full_name** | **str** | The full name of the user. | [optional] 
**address** | **str** | Address. | [optional] 
**creation_time** | **int** | A timestamp of the user creation in the storage, in milliseconds. | [optional] 
**password** | **str** | The password when creating a new user. It will be generated when not present in the request. | [optional] 
**phone_number** | **str** | Phone number. | [optional] 
**id** | **str** | The UUID of the user. | 
**last_login_time** | **int** | A timestamp of the latest login of the user, in milliseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


