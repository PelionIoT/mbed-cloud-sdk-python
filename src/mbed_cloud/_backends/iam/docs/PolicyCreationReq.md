# PolicyCreationReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of this policy. | [optional] 
**valid_until** | **datetime** | Specifies the date and time until the policy is valid in UTC time RFC3339. E.g. &#39;2018-02-05T09:43:44Z&#39; | [optional] 
**grant_expires_in** | **int** | Specifies the value in seconds for how long an authorization result is valid. | [optional] 
**name** | **str** | The name of this policy, must be unique and not longer than 100 character. | 
**error_message** | **str** | Custom error message returned when this policy matches with not allowed result. | [optional] 
**not_resources** | **list[str]** | List of not_resources in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. | [optional] 
**actions** | **dict(str, bool)** | List of actions as key-pairs of &#39;{action}&#39;: &#39;true&#39; or &#39;false&#39;, not more than 100. For enabling all actions use { &#39;*&#39;: true }. | [optional] 
**not_conditions** | **list[str]** | List of not_conditions in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. | [optional] 
**valid_from** | **datetime** | Specifies the date and time when the policy will become valid in UTC time RFC3339. E.g. &#39;2018-02-05T09:43:44Z&#39; | [optional] 
**users** | **list[str]** | List of user IDs this policy is attached to, not more than 100. | [optional] 
**groups** | **list[str]** | List of group IDs this policy is attached to, not more than 100. | [optional] 
**tag** | **str** | Policy tag that can be used for various purposes to be able to distinguish between policies. Not longer than 100 characters. | [optional] 
**not_actions** | **list[str]** | List of not_actions, not more than 100. | [optional] 
**apikeys** | **list[str]** | List of API key IDs this policy is attached to, not more than 100. | [optional] 
**conditions** | **list[str]** | List of conditions in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. | [optional] 
**resources** | **list[str]** | List of resources in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. | [optional] 
**description** | **str** | The description of this policy, not longer than 500 character. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


