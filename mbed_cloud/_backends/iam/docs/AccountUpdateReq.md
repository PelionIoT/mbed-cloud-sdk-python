# AccountUpdateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line2** | **str** | Postal address line 2. | [optional] 
**city** | **str** | The city part of the postal address. | [optional] 
**address_line1** | **str** | Postal address line 1. | [optional] 
**display_name** | **str** | The display name for the account. | [optional] 
**country** | **str** | The country part of the postal address. | [optional] 
**company** | **str** | The name of the company. | [optional] 
**template_id** | **str** | Account template ID. Manageable by the root admin only. | [optional] 
**status** | **str** | The status of the account. Manageable by the root admin only. | [optional] 
**state** | **str** | The state part of the postal address. | [optional] 
**contact** | **str** | The name of the contact person for this account. | [optional] 
**postal_code** | **str** | The postal code part of the postal address. | [optional] 
**is_provisioning_allowed** | **bool** | Flag (true/false) indicating whether Factory Tool is allowed to download or not. Manageable by the root admin only. | [optional] [default to False]
**parent_id** | **str** | The ID of the parent account, if it has any. | [optional] 
**tier** | **str** | The tier level of the account; &#39;0&#39;: free tier, &#39;1&#39;: commercial account. Other values are reserved for the future. Manageable by the root admin only. | [optional] 
**phone_number** | **str** | The phone number of the company. | [optional] 
**email** | **str** | The company email address for this account. | [optional] 
**aliases** | **list[str]** | An array of aliases. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


