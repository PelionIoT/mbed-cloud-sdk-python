# UpdateCampaignStatusSerializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_devices** | **str** |  | 
**connector_devices** | **str** |  | 
**description** | **str** | An optional description of the campaign | 
**state** | **str** | The state of the campaign | 
**updating_user_id** | **str** | The updating IAM user ID | 
**created_at** | **datetime** | The time the object was created | 
**total_devices** | **str** |  | 
**campaigndevicemetadata_set** | [**list[CampaignDeviceMetadataSerializer]**](CampaignDeviceMetadataSerializer.md) |  | 
**campaign_id** | **str** | DEPRECATED: The ID of the campaign | 
**deployed_devices** | **str** |  | 
**updated_at** | **datetime** | The time the object was updated | 
**when** | **datetime** | The timestamp at which campaign is scheduled to start | 
**finished** | **datetime** | The timestamp when the update campaign finished | 
**root_manifest_url** | **str** |  | 
**updating_api_key** | **str** | The gateway client API key | 
**updating_account_id** | **str** | The updating account ID | 
**device_filter** | **str** | The filter for the devices the campaign will target | 
**name** | **str** | A name for this campaign | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


