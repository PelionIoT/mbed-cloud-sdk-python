# AccountInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the account. | 
**postal_code** | **str** | The postal code part of the postal address. | [optional] 
**parent_id** | **str** | The ID of the parent account, if it has any. | [optional] 
**id** | **str** | Account ID. | 
**aliases** | **list[str]** | An array of aliases. | 
**address_line2** | **str** | Postal address line 2. | [optional] 
**city** | **str** | The city part of the postal address. | [optional] 
**address_line1** | **str** | Postal address line 1. | [optional] 
**display_name** | **str** | The display name for the account. | [optional] 
**state** | **str** | The state part of the postal address. | [optional] 
**etag** | **str** | API resource entity version. | 
**is_provisioning_allowed** | **bool** | Flag (true/false) indicating whether Factory Tool is allowed to download or not. | [default to False]
**creation_time_millis** | **int** |  | [optional] 
**email** | **str** | The company email address for this account. | [optional] 
**phone_number** | **str** | The phone number of the company. | [optional] 
**company** | **str** | The name of the company. | [optional] 
**object** | **str** | Entity name: always &#39;account&#39; | 
**upgraded_at** | **str** | Time when upgraded to commercial account in UTC format RFC3339. | [optional] 
**sub_accounts** | [**list[AccountInfo]**](AccountInfo.md) | List of sub accounts. | [optional] 
**tier** | **str** | The tier level of the account; &#39;0&#39;: free tier, &#39;1&#39;: commercial account. Other values are reserved for the future. | 
**limits** | **dict(str, str)** | List of limits as key-value pairs if requested. | [optional] 
**country** | **str** | The country part of the postal address. | [optional] 
**created_at** | **str** | Creation UTC time RFC3339. | [optional] 
**contact** | **str** | The name of the contact person for this account. | [optional] 
**policies** | [**list[Policy]**](Policy.md) | List of policies if requested. | [optional] 
**template_id** | **str** | Account template ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


