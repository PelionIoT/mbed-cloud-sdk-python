# WebsocketChannel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | Unique identifier of the channel | [optional] 
**queue_size** | **int** | Number of events in the channel&#39;s event queue waiting to be delivered. | [optional] 
**status** | **str** | Channel status will be &#39;connected&#39; when the channel has an active WebSocket bound to it. The state will be &#39;disconnected&#39; when either the channel or the WebSocket bound to it is closed.  | [optional] [default to 'disconnected']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


