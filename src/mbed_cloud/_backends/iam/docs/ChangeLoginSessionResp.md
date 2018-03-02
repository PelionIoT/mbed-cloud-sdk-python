# ChangeLoginSessionResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the logged in user. &#39;Reset&#39; means that the password must be changed immediately. | 
**user_id** | **str** | User ID. | 
**account_id** | **str** | The UUID of the account where the user login session is changed to. | 
**roles** | **list[str]** | The roles of the logged in user. | 
**token** | **str** | Reference token. | 
**parent_account_id** | **str** | The UUID of the parent account. | 
**mfa_status** | **str** | The enforcement status of setting up the multi-factor authentication. &#39;Enabled&#39; means that the MFA has been enabled despite the enforcement. &#39;Enforced&#39; means that setting up the MFA is required after login. &#39;Optional&#39; means that the MFA is not required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


