# UserInvitationResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The UUID of the account the user is invited to. | 
**created_at** | **datetime** | Creation UTC time RFC3339. | 
**email** | **str** | Email address of the invited user. | 
**etag** | **str** | API resource entity version. | 
**expiration** | **datetime** | Invitation expiration as UTC time RFC3339. | [optional] 
**groups** | **list[str]** | A list of IDs of the groups the user is invited to. | [optional] 
**id** | **str** | The UUID of the invitation. | 
**object** | **str** | Entity name: always &#39;user-invitation&#39; | 
**updated_at** | **datetime** | Last update UTC time RFC3339. | [optional] 
**user_id** | **str** | The UUID of the invited user. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


