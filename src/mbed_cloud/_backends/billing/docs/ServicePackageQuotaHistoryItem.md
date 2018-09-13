# ServicePackageQuotaHistoryItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | **datetime** | Added time of quota history entry in RFC3339 date-time with millisecond accuracy and UTC time zone. | 
**amount** | **int** | the amount of quota usage, negative or positive | 
**id** | **str** | Service package quota history ID. | 
**reason** | **str** | Type of quota usage entry. | 
**reservation** | [**ServicePackageQuotaHistoryReservation**](ServicePackageQuotaHistoryReservation.md) | Reservation details if reason is reservation, reservation_release or reservation_termination. | [optional] 
**service_package** | [**ServicePackageQuotaHistoryServicePackage**](ServicePackageQuotaHistoryServicePackage.md) | Service package details if reason is package_creation, package_renewal or package_termination | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


