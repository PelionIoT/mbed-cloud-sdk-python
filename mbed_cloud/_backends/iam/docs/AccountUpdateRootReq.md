# AccountUpdateRootReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_market** | **str** | The end market for this account, not longer than 100 characters. | [optional] 
**phone_number** | **str** | The phone number of the company, not longer than 100 characters. | [optional] 
**password_policy** | [**PasswordPolicy**](PasswordPolicy.md) | Password policy for this account. | [optional] 
**postal_code** | **str** | The postal code part of the postal address, not longer than 100 characters. | [optional] 
**parent_id** | **str** | The ID of the parent account, if it has any. | [optional] 
**aliases** | **list[str]** | An array of aliases, not more than 10. An alias is not shorter than 8 and not longer than 100 characters. | [optional] 
**address_line2** | **str** | Postal address line 2, not longer than 100 characters. | [optional] 
**city** | **str** | The city part of the postal address, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**address_line1** | **str** | Postal address line 1, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**display_name** | **str** | The display name for the account, not longer than 100 characters. | [optional] 
**state** | **str** | The state part of the postal address, not longer than 100 characters. | [optional] 
**is_provisioning_allowed** | **bool** | Flag (true/false) indicating whether Factory Tool is allowed to download or not. Manageable by the root admin only. | [optional] 
**email** | **str** | The company email address for this account, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**status** | **str** | The status of the account. Manageable by the root admin only. | [optional] 
**company** | **str** | The name of the company, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**reason** | **str** | A reason note for changing account status. Manageable by the root admin only. | [optional] 
**tier** | **str** | The tier level of the account; &#39;0&#39;: free tier, &#39;1&#39;: commercial account, &#39;2&#39;: partner account, &#39;98&#39;: internal/demo account, &#39;99&#39;: root admin team. Other values are reserved for the future. Manageable by the root admin only. | [optional] 
**limits** | **dict(str, str)** | List of service limits. Manageable by the root admin only. | [optional] 
**country** | **str** | The country part of the postal address, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**idle_timeout** | **str** | The reference token expiration time in minutes for this account. Between 1 and 120 minutes. | [optional] 
**contact** | **str** | The name of the contact person for this account, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**policies** | [**list[FeaturePolicy]**](FeaturePolicy.md) | List of policies. Manageable by the root admin only. | [optional] 
**template_id** | **str** | Account template ID. Manageable by the root admin only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


