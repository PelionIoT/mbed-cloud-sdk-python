# Metric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_server_rest_api_error** | **int** | The number of failed [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed. | [optional] 
**bootstraps_failed** | **int** | The number of failed bootstraps the account has performed. | [optional] 
**transactions** | **int** | The number of transaction events from or to devices linked to the account. A transaction is a 512-byte block of data processed by mbed Cloud. It can be either sent by the device (device --&gt; mbed cloud) or received by the device (mbed cloud --&gt; device). A transaction does not include IP, TCP or UDP, TLS or DTLS packet overhead. It only contains the packet payload (full CoAP packet including CoAP headers). | [optional] 
**timestamp** | **str** | UTC time in RFC3339 format. The timestamp is the starting point of the interval for which the data is aggregated. Each interval includes data for the time greater than or equal to the timestamp and less than the next interval&#39;s starting point. | [optional] 
**registered_devices** | **int** | The maximum number of registered devices linked to the account. The registered devices count is calculated based on unique registrations plus registration updates over a period of 5 minutes. | [optional] 
**bootstraps_pending** | **int** | The number of pending bootstraps the account has performed. | [optional] 
**device_server_rest_api_success** | **int** | The number of successful [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed. | [optional] 
**handshakes_successful** | **int** | The number of successful handshakes the account has performed. | [optional] 
**bootstraps_successful** | **int** | The number of successful bootstraps the account has performed. | [optional] 
**id** | **str** | A unique metric ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


