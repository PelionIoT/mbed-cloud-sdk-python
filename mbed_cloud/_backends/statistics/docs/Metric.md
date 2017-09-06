# Metric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_server_rest_api_error** | **int** | The number of failed [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed. | [optional] 
**registration_updates** | **int** | The number of registration updates linked to the account. Registration update is the process of updating the registration status with the Mbed Cloud Connect to update or extend the lifetime of the device. | [optional] 
**full_registrations** | **int** | The number of full registrations linked to the account. Full registration is the process of registering a device with the Mbed Cloud Connect by providing its lifetime and capabilities such as the resource structure.The registered status of the device does not guarantee that the device is active and accessible from Mebd Cloud Connect at any point of time. | [optional] 
**bootstraps_failed** | **int** | The number of failed bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server. | [optional] 
**transactions** | **int** | The number of transaction events from or to devices linked to the account. A transaction is a 512-byte block of data processed by mbed Cloud. It can be either sent by the device (device --&gt; mbed cloud) or received by the device (mbed cloud --&gt; device). A transaction does not include IP, TCP or UDP, TLS or DTLS packet overhead. It only contains the packet payload (full CoAP packet including CoAP headers). | [optional] 
**timestamp** | **datetime** | UTC time in RFC3339 format. The timestamp is the starting point of the interval for which the data is aggregated. Each interval includes data for the time greater than or equal to the timestamp and less than the next interval&#39;s starting point. | [optional] 
**device_server_rest_api_success** | **int** | The number of successful [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed. | [optional] 
**bootstraps_pending** | **int** | The number of pending bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server. | [optional] 
**expired_registrations** | **int** | The number of expired registrations linked to the account. Mbed Cloud Connect removes the device registrations when the devices cannot update their registration before the expiry of the lifetime. Mbed Cloud Connect no longer handles requests for a device whose registration has expired already. | [optional] 
**handshakes_successful** | **int** | The number of successful TLS handshakes the account has performed. The SSL or TLS handshake enables the SSL or TLS client and server to establish the secret keys with which they communicate. A successful TLS handshake is required for establishing a connection with Mbed Cloud Connect for any operaton such as registration, registration update and deregistration. | [optional] 
**bootstraps_successful** | **int** | The number of successful bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server. | [optional] 
**deleted_registrations** | **int** | The number of deleted registrations (deregistrations) linked to the account. Deregistration is the process of removing the device registration from the Mbed Cloud Connect registry. The deregistration is usually initiated by the device. Mbed Cloud Connect no longer handles requests for a deregistered device. | [optional] 
**id** | **str** | A unique metric ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


