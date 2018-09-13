# ReportResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ReportAccountContactInfo**](ReportAccountContactInfo.md) | Account contact information. | 
**aggregated** | [**ReportBillingData**](ReportBillingData.md) | Aggregated report billing data including all subtenant accounts if any. | 
**billing_data** | [**ReportBillingData**](ReportBillingData.md) | Report billing data. | 
**id** | **str** | Billing report ID. | 
**month** | **str** | Month of requested billing report | 
**object** | **str** | Billing report response object. Always set to &#39;billing-report&#39;. | 
**service_package** | [**ServicePackageReport**](ServicePackageReport.md) | Report service package. | [optional] 
**subtenants** | [**list[SubtenantAccountReport]**](SubtenantAccountReport.md) | List of billing reports for subtenant accounts. Empty list if account does not have any subtenant account. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


