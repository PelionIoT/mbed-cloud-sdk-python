"""
.. warning::
    Device should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: Device
=========================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`Device.create`
- :meth:`Device.delete`
- :meth:`Device.list`
- :meth:`Device.read`
- :meth:`Device.renew_certificate`
- :meth:`Device.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    devices = pelion_dm_sdk.foundation.device()

How to import Device directly:

.. code-block:: python
    
    from mbed_cloud.foundation import Device

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class Device(Entity):
    """Represents the `Device` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "account_id",
        "auto_update",
        "bootstrap_expiration_date",
        "bootstrapped_timestamp",
        "ca_id",
        "connector_expiration_date",
        "created_at",
        "custom_attributes",
        "deployed_state",
        "deployment",
        "description",
        "device_class",
        "device_execution_mode",
        "device_key",
        "endpoint_name",
        "endpoint_type",
        "enrolment_list_timestamp",
        "firmware_checksum",
        "host_gateway",
        "id",
        "issuer_fingerprint",
        "manifest",
        "manifest_timestamp",
        "mechanism",
        "mechanism_url",
        "name",
        "serial_number",
        "state",
        "updated_at",
        "vendor_id",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        auto_update=None,
        bootstrap_expiration_date=None,
        bootstrapped_timestamp=None,
        ca_id=None,
        connector_expiration_date=None,
        created_at=None,
        custom_attributes=None,
        deployed_state=None,
        deployment=None,
        description=None,
        device_class=None,
        device_execution_mode=None,
        device_key=None,
        endpoint_name=None,
        endpoint_type=None,
        enrolment_list_timestamp=None,
        firmware_checksum=None,
        host_gateway=None,
        id=None,
        issuer_fingerprint=None,
        manifest=None,
        manifest_timestamp=None,
        mechanism=None,
        mechanism_url=None,
        name=None,
        serial_number=None,
        state=None,
        updated_at=None,
        vendor_id=None,
    ):
        """Creates a local `Device` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: The ID of the associated account.
        :type account_id: str
        :param auto_update: DEPRECATED: Mark this device for automatic firmware update.
        :type auto_update: bool
        :param bootstrap_expiration_date: The expiration date of the certificate used to connect to
            bootstrap server.
        :type bootstrap_expiration_date: date
        :param bootstrapped_timestamp: The timestamp of the device's most recent bootstrap process.
        :type bootstrapped_timestamp: datetime
        :param ca_id: The certificate issuer's ID.
        :type ca_id: str
        :param connector_expiration_date: The expiration date of the certificate used to connect to LwM2M
            server.
        :type connector_expiration_date: date
        :param created_at: The timestamp of when the device was created in the device
            directory.
        :type created_at: datetime
        :param custom_attributes: Up to five custom key-value attributes. Note that keys cannot
            begin with a number. Both keys and values are limited to 128
            characters. Updating this field replaces existing contents.
        :type custom_attributes: dict
        :param deployed_state: DEPRECATED: The state of the device's deployment.
        :type deployed_state: str
        :param deployment: DEPRECATED: The last deployment used on the device.
        :type deployment: str
        :param description: The description of the device.
        :type description: str
        :param device_class: An ID representing the model and hardware revision of the device.
        :type device_class: str
        :param device_execution_mode: The execution mode from the certificate of the device. Defaults to
            inheriting from host_gateway device.
            Permitted values:
              - 0 -
            unspecified execution mode (default if host_gateway invalid or not
            set)
              - 1 - development devices
              - 5 - production devices
        :type device_execution_mode: int
        :param device_key: The fingerprint of the device certificate.
        :type device_key: str
        :param endpoint_name: The endpoint name given to the device.
        :type endpoint_name: str
        :param endpoint_type: The endpoint type of the device. For example, the device is a
            gateway.
        :type endpoint_type: str
        :param enrolment_list_timestamp: The claim date/time.
        :type enrolment_list_timestamp: datetime
        :param firmware_checksum: The SHA256 checksum of the current firmware image.
        :type firmware_checksum: str
        :param host_gateway: The ID of the host gateway, if appropriate.
        :type host_gateway: str
        :param id: (Required) The ID of the device. The device ID is used across all Device
            Management APIs.
        :type id: str
        :param issuer_fingerprint: SHA256 fingerprint of the certificate used to validate the
            signature of the device certificate.
        :type issuer_fingerprint: str
        :param manifest: DEPRECATED: The URL for the current device manifest.
        :type manifest: str
        :param manifest_timestamp: The timestamp of the current manifest version.
        :type manifest_timestamp: datetime
        :param mechanism: The ID of the channel used to communicate with the device.
        :type mechanism: str
        :param mechanism_url: The address of the connector to use.
        :type mechanism_url: str
        :param name: The name of the device.
        :type name: str
        :param serial_number: The serial number of the device.
        :type serial_number: str
        :param state: The current state of the device.
        :type state: str
        :param updated_at: The time the object was updated.
        :type updated_at: datetime
        :param vendor_id: The device vendor ID.
        :type vendor_id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._auto_update = fields.BooleanField(value=auto_update)
        self._bootstrap_expiration_date = fields.DateField(value=bootstrap_expiration_date)
        self._bootstrapped_timestamp = fields.DateTimeField(value=bootstrapped_timestamp)
        self._ca_id = fields.StringField(value=ca_id)
        self._connector_expiration_date = fields.DateField(value=connector_expiration_date)
        self._created_at = fields.DateTimeField(value=created_at)
        self._custom_attributes = fields.DictField(value=custom_attributes)
        self._deployed_state = fields.StringField(value=deployed_state, enum=enums.DeviceDeployedStateEnum)
        self._deployment = fields.StringField(value=deployment)
        self._description = fields.StringField(value=description)
        self._device_class = fields.StringField(value=device_class)
        self._device_execution_mode = fields.IntegerField(value=device_execution_mode)
        self._device_key = fields.StringField(value=device_key)
        self._endpoint_name = fields.StringField(value=endpoint_name)
        self._endpoint_type = fields.StringField(value=endpoint_type)
        self._enrolment_list_timestamp = fields.DateTimeField(value=enrolment_list_timestamp)
        self._firmware_checksum = fields.StringField(value=firmware_checksum)
        self._host_gateway = fields.StringField(value=host_gateway)
        self._id = fields.StringField(value=id)
        self._issuer_fingerprint = fields.StringField(value=issuer_fingerprint)
        self._manifest = fields.StringField(value=manifest)
        self._manifest_timestamp = fields.DateTimeField(value=manifest_timestamp)
        self._mechanism = fields.StringField(value=mechanism, enum=enums.DeviceMechanismEnum)
        self._mechanism_url = fields.StringField(value=mechanism_url)
        self._name = fields.StringField(value=name)
        self._serial_number = fields.StringField(value=serial_number)
        self._state = fields.StringField(value=state, enum=enums.DeviceStateEnum)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._vendor_id = fields.StringField(value=vendor_id)

    @property
    def account_id(self):
        """The ID of the associated account.
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._account_id.value

    @property
    def auto_update(self):
        """DEPRECATED: Mark this device for automatic firmware update.
        
        :rtype: bool
        """

        return self._auto_update.value

    @auto_update.setter
    def auto_update(self, value):
        """Set value of `auto_update`

        :param value: value to set
        :type value: bool
        """

        self._auto_update.set(value)

    @property
    def bootstrap_expiration_date(self):
        """The expiration date of the certificate used to connect to bootstrap server.
        
        :rtype: date
        """

        return self._bootstrap_expiration_date.value

    @bootstrap_expiration_date.setter
    def bootstrap_expiration_date(self, value):
        """Set value of `bootstrap_expiration_date`

        :param value: value to set
        :type value: date
        """

        self._bootstrap_expiration_date.set(value)

    @property
    def bootstrapped_timestamp(self):
        """The timestamp of the device's most recent bootstrap process.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._bootstrapped_timestamp.value

    @property
    def ca_id(self):
        """The certificate issuer's ID.
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._ca_id.value

    @ca_id.setter
    def ca_id(self, value):
        """Set value of `ca_id`

        :param value: value to set
        :type value: str
        """

        self._ca_id.set(value)

    @property
    def connector_expiration_date(self):
        """The expiration date of the certificate used to connect to LwM2M server.
        
        :rtype: date
        """

        return self._connector_expiration_date.value

    @connector_expiration_date.setter
    def connector_expiration_date(self, value):
        """Set value of `connector_expiration_date`

        :param value: value to set
        :type value: date
        """

        self._connector_expiration_date.set(value)

    @property
    def created_at(self):
        """The timestamp of when the device was created in the device directory.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def custom_attributes(self):
        """Up to five custom key-value attributes. Note that keys cannot begin with a
        number. Both keys and values are limited to 128 characters. Updating this
        field replaces existing contents.
        
        api example: {'key': 'value'}
        
        :rtype: dict
        """

        return self._custom_attributes.value

    @custom_attributes.setter
    def custom_attributes(self, value):
        """Set value of `custom_attributes`

        :param value: value to set
        :type value: dict
        """

        self._custom_attributes.set(value)

    @property
    def deployed_state(self):
        """DEPRECATED: The state of the device's deployment.
        
        :rtype: str
        """

        return self._deployed_state.value

    @property
    def deployment(self):
        """DEPRECATED: The last deployment used on the device.
        
        :rtype: str
        """

        return self._deployment.value

    @deployment.setter
    def deployment(self, value):
        """Set value of `deployment`

        :param value: value to set
        :type value: str
        """

        self._deployment.set(value)

    @property
    def description(self):
        """The description of the device.
        
        api example: 'description'
        
        :rtype: str
        """

        return self._description.value

    @description.setter
    def description(self, value):
        """Set value of `description`

        :param value: value to set
        :type value: str
        """

        self._description.set(value)

    @property
    def device_class(self):
        """An ID representing the model and hardware revision of the device.
        
        :rtype: str
        """

        return self._device_class.value

    @device_class.setter
    def device_class(self, value):
        """Set value of `device_class`

        :param value: value to set
        :type value: str
        """

        self._device_class.set(value)

    @property
    def device_execution_mode(self):
        """The execution mode from the certificate of the device. Defaults to inheriting
        from host_gateway device.
        Permitted values:
          - 0 - unspecified execution mode
        (default if host_gateway invalid or not set)
          - 1 - development devices
          - 5
        - production devices
        
        :rtype: int
        """

        return self._device_execution_mode.value

    @device_execution_mode.setter
    def device_execution_mode(self, value):
        """Set value of `device_execution_mode`

        :param value: value to set
        :type value: int
        """

        self._device_execution_mode.set(value)

    @property
    def device_key(self):
        """The fingerprint of the device certificate.
        
        api example: '00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
            :00:00:00:00:00:00'
        
        :rtype: str
        """

        return self._device_key.value

    @device_key.setter
    def device_key(self, value):
        """Set value of `device_key`

        :param value: value to set
        :type value: str
        """

        self._device_key.set(value)

    @property
    def endpoint_name(self):
        """The endpoint name given to the device.
        
        api example: '00000000-0000-0000-0000-000000000000'
        
        :rtype: str
        """

        return self._endpoint_name.value

    @property
    def endpoint_type(self):
        """The endpoint type of the device. For example, the device is a gateway.
        
        :rtype: str
        """

        return self._endpoint_type.value

    @endpoint_type.setter
    def endpoint_type(self, value):
        """Set value of `endpoint_type`

        :param value: value to set
        :type value: str
        """

        self._endpoint_type.set(value)

    @property
    def enrolment_list_timestamp(self):
        """The claim date/time.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._enrolment_list_timestamp.value

    @property
    def firmware_checksum(self):
        """The SHA256 checksum of the current firmware image.
        
        api example: '0000000000000000000000000000000000000000000000000000000000000000'
        
        :rtype: str
        """

        return self._firmware_checksum.value

    @property
    def host_gateway(self):
        """The ID of the host gateway, if appropriate.
        
        :rtype: str
        """

        return self._host_gateway.value

    @host_gateway.setter
    def host_gateway(self, value):
        """Set value of `host_gateway`

        :param value: value to set
        :type value: str
        """

        self._host_gateway.set(value)

    @property
    def id(self):
        """The ID of the device. The device ID is used across all Device Management APIs.

        This field must be set when updating or deleting an existing Device Entity.
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        self._id.set(value)

    @property
    def issuer_fingerprint(self):
        """SHA256 fingerprint of the certificate used to validate the signature of the
        device certificate.
        
        api example: 'C42EDEFC75871E4CE2146FCDA67D03DDA05CC26FDF93B17B55F42C1EADFDC322'
        
        :rtype: str
        """

        return self._issuer_fingerprint.value

    @issuer_fingerprint.setter
    def issuer_fingerprint(self, value):
        """Set value of `issuer_fingerprint`

        :param value: value to set
        :type value: str
        """

        self._issuer_fingerprint.set(value)

    @property
    def manifest(self):
        """DEPRECATED: The URL for the current device manifest.
        
        :rtype: str
        """

        return self._manifest.value

    @manifest.setter
    def manifest(self, value):
        """Set value of `manifest`

        :param value: value to set
        :type value: str
        """

        self._manifest.set(value)

    @property
    def manifest_timestamp(self):
        """The timestamp of the current manifest version.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._manifest_timestamp.value

    @property
    def mechanism(self):
        """The ID of the channel used to communicate with the device.
        
        :rtype: str
        """

        return self._mechanism.value

    @mechanism.setter
    def mechanism(self, value):
        """Set value of `mechanism`

        :param value: value to set
        :type value: str
        """

        self._mechanism.set(value)

    @property
    def mechanism_url(self):
        """The address of the connector to use.
        
        :rtype: str
        """

        return self._mechanism_url.value

    @mechanism_url.setter
    def mechanism_url(self, value):
        """Set value of `mechanism_url`

        :param value: value to set
        :type value: str
        """

        self._mechanism_url.set(value)

    @property
    def name(self):
        """The name of the device.
        
        api example: '00000000-0000-0000-0000-000000000000'
        
        :rtype: str
        """

        return self._name.value

    @name.setter
    def name(self, value):
        """Set value of `name`

        :param value: value to set
        :type value: str
        """

        self._name.set(value)

    @property
    def serial_number(self):
        """The serial number of the device.
        
        api example: '00000000-0000-0000-0000-000000000000'
        
        :rtype: str
        """

        return self._serial_number.value

    @serial_number.setter
    def serial_number(self, value):
        """Set value of `serial_number`

        :param value: value to set
        :type value: str
        """

        self._serial_number.set(value)

    @property
    def state(self):
        """The current state of the device.
        
        :rtype: str
        """

        return self._state.value

    @state.setter
    def state(self, value):
        """Set value of `state`

        :param value: value to set
        :type value: str
        """

        self._state.set(value)

    @property
    def updated_at(self):
        """The time the object was updated.
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @property
    def vendor_id(self):
        """The device vendor ID.
        
        api example: '00000000-0000-0000-0000-000000000000'
        
        :rtype: str
        """

        return self._vendor_id.value

    @vendor_id.setter
    def vendor_id(self, value):
        """Set value of `vendor_id`

        :param value: value to set
        :type value: str
        """

        self._vendor_id.set(value)

    def create(self):
        """Create a device

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/devices/>`_.
        
        :rtype: Device
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._auto_update.value_set:
            body_params["auto_update"] = self._auto_update.to_api()
        if self._bootstrap_expiration_date.value_set:
            body_params["bootstrap_expiration_date"] = self._bootstrap_expiration_date.to_api()
        if self._ca_id.value_set:
            body_params["ca_id"] = self._ca_id.to_api()
        if self._connector_expiration_date.value_set:
            body_params["connector_expiration_date"] = self._connector_expiration_date.to_api()
        if self._custom_attributes.value_set:
            body_params["custom_attributes"] = self._custom_attributes.to_api()
        if self._deployment.value_set:
            body_params["deployment"] = self._deployment.to_api()
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._device_class.value_set:
            body_params["device_class"] = self._device_class.to_api()
        if self._device_execution_mode.value_set:
            body_params["device_execution_mode"] = self._device_execution_mode.to_api()
        if self._device_key.value_set:
            body_params["device_key"] = self._device_key.to_api()
        if self._endpoint_name.value_set:
            body_params["endpoint_name"] = self._endpoint_name.to_api()
        if self._endpoint_type.value_set:
            body_params["endpoint_type"] = self._endpoint_type.to_api()
        if self._host_gateway.value_set:
            body_params["host_gateway"] = self._host_gateway.to_api()
        if self._issuer_fingerprint.value_set:
            body_params["issuer_fingerprint"] = self._issuer_fingerprint.to_api()
        if self._manifest.value_set:
            body_params["manifest"] = self._manifest.to_api()
        if self._mechanism.value_set:
            body_params["mechanism"] = self._mechanism.to_api()
        if self._mechanism_url.value_set:
            body_params["mechanism_url"] = self._mechanism_url.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()
        if self._serial_number.value_set:
            body_params["serial_number"] = self._serial_number.to_api()
        if self._state.value_set:
            body_params["state"] = self._state.to_api()
        if self._vendor_id.value_set:
            body_params["vendor_id"] = self._vendor_id.to_api()

        return self._client.call_api(
            method="post", path="/v3/devices/", content_type="application/json", body_params=body_params, unpack=self
        )

    def delete(self):
        """Delete a device.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/devices/{id}/>`_.
        
        :rtype: Device
        """

        return self._client.call_api(
            method="delete",
            path="/v3/devices/{id}/",
            content_type="application/json",
            path_params={"id": self._id.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """List all devices.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/devices/>`_.

        **API Filters**

        The following filters are supported by the API when listing Device entities:

        +---------------------------+------+------+------+------+------+------+------+
        | Field                     | eq   | neq  | gte  | lte  | in   | nin  | like |
        +===========================+======+======+======+======+======+======+======+
        | account_id                | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | auto_update               | Y    | Y    |      |      |      |      |      |
        +---------------------------+------+------+------+------+------+------+------+
        | bootstrap_expiration_date |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | bootstrapped_timestamp    |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | ca_id                     | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | connector_expiration_date |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | created_at                |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | deployed_state            | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | deployment                | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | description               | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | device_class              | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | device_execution_mode     | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | device_key                | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | endpoint_name             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | endpoint_type             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | enrolment_list_timestamp  |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | firmware_checksum         | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | host_gateway              | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | id                        | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | manifest                  | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | manifest_timestamp        |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | mechanism                 | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | mechanism_url             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | name                      | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | serial_number             | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | state                     | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | updated_at                |      |      | Y    | Y    | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+
        | vendor_id                 | Y    | Y    |      |      | Y    | Y    |      |
        +---------------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import Device
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("account_id", "eq", <filter value>)
            for device in Device().list(filter=api_filter):
                print(device.account_id)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(Device)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import Device
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=Device._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = Device._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=Device,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """List all devices.
        
        :param after: The ID of The item after which to retrieve the next page.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, `ASC` or `DESC`; by
            default `ASC`.
        :type order: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param include: Comma-separated list of data fields to return. Currently supported:
            `total_count`.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get", path="/v3/devices/", content_type="application/json", query_params=query_params, unpack=False
        )

    def read(self):
        """Get a device

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/devices/{id}/>`_.
        
        :rtype: Device
        """

        return self._client.call_api(
            method="get",
            path="/v3/devices/{id}/",
            content_type="application/json",
            path_params={"id": self._id.to_api()},
            unpack=self,
        )

    def renew_certificate(self, certificate_name):
        """Request certificate renewal.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/devices/{device-id}/certificates/{certificate-name}/renew>`_.
        
        :param certificate_name: The certificate name.
        :type certificate_name: str
        
        :rtype: CertificateEnrollment
        """

        from mbed_cloud.foundation import CertificateEnrollment

        return self._client.call_api(
            method="post",
            path="/v3/devices/{device-id}/certificates/{certificate-name}/renew",
            content_type="application/json",
            path_params={
                "certificate-name": fields.StringField(certificate_name).to_api(),
                "device-id": self._id.to_api(),
            },
            unpack=CertificateEnrollment,
        )

    def update(self):
        """Update a device

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/devices/{id}/>`_.
        
        :rtype: Device
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._auto_update.value_set:
            body_params["auto_update"] = self._auto_update.to_api()
        if self._ca_id.value_set:
            body_params["ca_id"] = self._ca_id.to_api()
        if self._custom_attributes.value_set:
            body_params["custom_attributes"] = self._custom_attributes.to_api()
        if self._description.value_set:
            body_params["description"] = self._description.to_api()
        if self._device_key.value_set:
            body_params["device_key"] = self._device_key.to_api()
        if self._endpoint_name.value_set:
            body_params["endpoint_name"] = self._endpoint_name.to_api()
        if self._endpoint_type.value_set:
            body_params["endpoint_type"] = self._endpoint_type.to_api()
        if self._host_gateway.value_set:
            body_params["host_gateway"] = self._host_gateway.to_api()
        if self._name.value_set:
            body_params["name"] = self._name.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/devices/{id}/",
            content_type="application/json",
            body_params=body_params,
            path_params={"id": self._id.to_api()},
            unpack=self,
        )
