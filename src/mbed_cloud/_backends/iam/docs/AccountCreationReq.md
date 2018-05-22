# AccountCreationReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Postal address line 1, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**address_line2** | **str** | Postal address line 2, not longer than 100 characters. | [optional] 
**admin_email** | **str** | The email address of the account admin, not longer than 254 characters. | [optional] 
**admin_full_name** | **str** | The full name of the admin user to be created. | [optional] 
**admin_name** | **str** | The username of the admin user to be created, containing alphanumerical letters and -,._@+&#x3D; characters. It must be at least 4 but not more than 30 character long. | [optional] 
**admin_password** | **str** | The password when creating a new user. It will be generated when not present in the request. | [optional] 
**aliases** | **list[str]** | An array of aliases, not more than 10. An alias is not shorter than 8 and not longer than 100 characters. | [optional] 
**city** | **str** | The city part of the postal address, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**company** | **str** | The name of the company, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**contact** | **str** | The name of the contact person for this account, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**contract_number** | **str** | Contract number of the customer. | [optional] 
**country** | **str** | The country part of the postal address, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**customer_number** | **str** | Customer number of the customer. | [optional] 
**display_name** | **str** | The display name for the account, not longer than 100 characters. | [optional] 
**email** | **str** | The company email address for this account, not longer than 254 characters. Required for commercial accounts only. | [optional] 
**end_market** | **str** | The end market of the account to be created. | 
**phone_number** | **str** | The phone number of a representative of the company, not longer than 100 characters. | [optional] 
**postal_code** | **str** | The postal code part of the postal address, not longer than 100 characters. | [optional] 
**state** | **str** | The state part of the postal address, not longer than 100 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


