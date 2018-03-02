# PolicyInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_until** | **datetime** | Specifies the date and time until the policy is valid. | [optional] 
**grant_expires_in** | **int** | Specifies the value in seconds for how long an authorization result is valid. | [optional] 
**updated_at** | **datetime** | Last update UTC time RFC3339. | 
**actions** | **dict(str, bool)** | List of actions. | 
**tag** | **str** | Policy tag that can be used for various purposes to be able to distinguish between policies. | [optional] 
**apikeys** | **list[str]** | List of API key IDs this policy is attached to. | [optional] 
**id** | **str** | Entity ID. | 
**users** | **list[str]** | List of user IDs this policy is attached to. | [optional] 
**valid_from** | **datetime** | Specifies the date and time when the policy will become valid. | [optional] 
**etag** | **str** | API resource entity version. | 
**account_id** | **str** | The UUID of the account. | 
**conditions** | **list[str]** | List of conditions. | 
**resources** | **list[str]** | List of resources. | 
**status** | **str** | The status of this policy. | 
**description** | **str** | The description of this policy. | [optional] 
**object** | **str** | Entity name: always &#39;policy&#39; | 
**groups** | **list[str]** | List of group IDs this policy is attached to. | [optional] 
**not_actions** | **list[str]** | List of not_actions. | 
**not_resources** | **list[str]** | List of not_resources. | 
**name** | **str** | The name of this policy. | 
**created_at** | **datetime** | Creation UTC time RFC3339. | [optional] 
**error_message** | **str** | Custom error message returned when this policy matches with not allowed result. | [optional] 
**not_conditions** | **list[str]** | List of not_conditions. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


