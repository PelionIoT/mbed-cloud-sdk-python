# coding: utf-8

"""
    Device Directory API

    This is the API Documentation for the Mbed Device Directory service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bootstrap_expiration_date': 'datetime',
        'bootstrapped_timestamp': 'datetime',
        'connector_expiration_date': 'datetime',
        'updated_at': 'datetime',
        'ca_id': 'str',
        'device_class': 'str',
        'id': 'str',
        'account_id': 'str',
        'endpoint_name': 'str',
        'auto_update': 'bool',
        'host_gateway': 'str',
        'device_execution_mode': 'int',
        'mechanism': 'str',
        'state': 'str',
        'etag': 'datetime',
        'serial_number': 'str',
        'firmware_checksum': 'str',
        'manifest_timestamp': 'datetime',
        'vendor_id': 'str',
        'description': 'str',
        'deployed_state': 'str',
        'object': 'str',
        'endpoint_type': 'str',
        'deployment': 'str',
        'mechanism_url': 'str',
        'name': 'str',
        'device_key': 'str',
        'created_at': 'datetime',
        'manifest': 'str',
        'custom_attributes': 'dict(str, str)'
    }

    attribute_map = {
        'bootstrap_expiration_date': 'bootstrap_expiration_date',
        'bootstrapped_timestamp': 'bootstrapped_timestamp',
        'connector_expiration_date': 'connector_expiration_date',
        'updated_at': 'updated_at',
        'ca_id': 'ca_id',
        'device_class': 'device_class',
        'id': 'id',
        'account_id': 'account_id',
        'endpoint_name': 'endpoint_name',
        'auto_update': 'auto_update',
        'host_gateway': 'host_gateway',
        'device_execution_mode': 'device_execution_mode',
        'mechanism': 'mechanism',
        'state': 'state',
        'etag': 'etag',
        'serial_number': 'serial_number',
        'firmware_checksum': 'firmware_checksum',
        'manifest_timestamp': 'manifest_timestamp',
        'vendor_id': 'vendor_id',
        'description': 'description',
        'deployed_state': 'deployed_state',
        'object': 'object',
        'endpoint_type': 'endpoint_type',
        'deployment': 'deployment',
        'mechanism_url': 'mechanism_url',
        'name': 'name',
        'device_key': 'device_key',
        'created_at': 'created_at',
        'manifest': 'manifest',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, bootstrap_expiration_date=None, bootstrapped_timestamp=None, connector_expiration_date=None, updated_at=None, ca_id=None, device_class=None, id=None, account_id=None, endpoint_name=None, auto_update=None, host_gateway=None, device_execution_mode=None, mechanism=None, state=None, etag=None, serial_number=None, firmware_checksum=None, manifest_timestamp=None, vendor_id=None, description=None, deployed_state=None, object=None, endpoint_type=None, deployment=None, mechanism_url=None, name=None, device_key=None, created_at=None, manifest=None, custom_attributes=None):
        """
        DeviceData - a model defined in Swagger
        """

        self._bootstrap_expiration_date = bootstrap_expiration_date
        self._bootstrapped_timestamp = bootstrapped_timestamp
        self._connector_expiration_date = connector_expiration_date
        self._updated_at = updated_at
        self._ca_id = ca_id
        self._device_class = device_class
        self._id = id
        self._account_id = account_id
        self._endpoint_name = endpoint_name
        self._auto_update = auto_update
        self._host_gateway = host_gateway
        self._device_execution_mode = device_execution_mode
        self._mechanism = mechanism
        self._state = state
        self._etag = etag
        self._serial_number = serial_number
        self._firmware_checksum = firmware_checksum
        self._manifest_timestamp = manifest_timestamp
        self._vendor_id = vendor_id
        self._description = description
        self._deployed_state = deployed_state
        self._object = object
        self._endpoint_type = endpoint_type
        self._deployment = deployment
        self._mechanism_url = mechanism_url
        self._name = name
        self._device_key = device_key
        self._created_at = created_at
        self._manifest = manifest
        self._custom_attributes = custom_attributes
        self.discriminator = None

    @property
    def bootstrap_expiration_date(self):
        """
        Gets the bootstrap_expiration_date of this DeviceData.
        The expiration date of the certificate used to connect to bootstrap server.

        :return: The bootstrap_expiration_date of this DeviceData.
        :rtype: datetime
        """
        return self._bootstrap_expiration_date

    @bootstrap_expiration_date.setter
    def bootstrap_expiration_date(self, bootstrap_expiration_date):
        """
        Sets the bootstrap_expiration_date of this DeviceData.
        The expiration date of the certificate used to connect to bootstrap server.

        :param bootstrap_expiration_date: The bootstrap_expiration_date of this DeviceData.
        :type: datetime
        """

        self._bootstrap_expiration_date = bootstrap_expiration_date

    @property
    def bootstrapped_timestamp(self):
        """
        Gets the bootstrapped_timestamp of this DeviceData.
        The timestamp of the device's most recent bootstrap process.

        :return: The bootstrapped_timestamp of this DeviceData.
        :rtype: datetime
        """
        return self._bootstrapped_timestamp

    @bootstrapped_timestamp.setter
    def bootstrapped_timestamp(self, bootstrapped_timestamp):
        """
        Sets the bootstrapped_timestamp of this DeviceData.
        The timestamp of the device's most recent bootstrap process.

        :param bootstrapped_timestamp: The bootstrapped_timestamp of this DeviceData.
        :type: datetime
        """

        self._bootstrapped_timestamp = bootstrapped_timestamp

    @property
    def connector_expiration_date(self):
        """
        Gets the connector_expiration_date of this DeviceData.
        The expiration date of the certificate used to connect to LWM2M server.

        :return: The connector_expiration_date of this DeviceData.
        :rtype: datetime
        """
        return self._connector_expiration_date

    @connector_expiration_date.setter
    def connector_expiration_date(self, connector_expiration_date):
        """
        Sets the connector_expiration_date of this DeviceData.
        The expiration date of the certificate used to connect to LWM2M server.

        :param connector_expiration_date: The connector_expiration_date of this DeviceData.
        :type: datetime
        """

        self._connector_expiration_date = connector_expiration_date

    @property
    def updated_at(self):
        """
        Gets the updated_at of this DeviceData.
        The time the object was updated.

        :return: The updated_at of this DeviceData.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this DeviceData.
        The time the object was updated.

        :param updated_at: The updated_at of this DeviceData.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def ca_id(self):
        """
        Gets the ca_id of this DeviceData.
        The certificate issuer's ID.

        :return: The ca_id of this DeviceData.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """
        Sets the ca_id of this DeviceData.
        The certificate issuer's ID.

        :param ca_id: The ca_id of this DeviceData.
        :type: str
        """
        if ca_id is not None and len(ca_id) > 500:
            raise ValueError("Invalid value for `ca_id`, length must be less than or equal to `500`")

        self._ca_id = ca_id

    @property
    def device_class(self):
        """
        Gets the device_class of this DeviceData.
        An ID representing the model and hardware revision of the device.

        :return: The device_class of this DeviceData.
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """
        Sets the device_class of this DeviceData.
        An ID representing the model and hardware revision of the device.

        :param device_class: The device_class of this DeviceData.
        :type: str
        """
        if device_class is not None and len(device_class) > 32:
            raise ValueError("Invalid value for `device_class`, length must be less than or equal to `32`")

        self._device_class = device_class

    @property
    def id(self):
        """
        Gets the id of this DeviceData.
        The ID of the device. The device ID is used to manage a device across all Mbed Cloud APIs.

        :return: The id of this DeviceData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceData.
        The ID of the device. The device ID is used to manage a device across all Mbed Cloud APIs.

        :param id: The id of this DeviceData.
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """
        Gets the account_id of this DeviceData.
        The ID of the associated account.

        :return: The account_id of this DeviceData.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this DeviceData.
        The ID of the associated account.

        :param account_id: The account_id of this DeviceData.
        :type: str
        """

        self._account_id = account_id

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this DeviceData.
        The endpoint name given to the device.

        :return: The endpoint_name of this DeviceData.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this DeviceData.
        The endpoint name given to the device.

        :param endpoint_name: The endpoint_name of this DeviceData.
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceData.
        DEPRECATED: Mark this device for automatic firmware update.

        :return: The auto_update of this DeviceData.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceData.
        DEPRECATED: Mark this device for automatic firmware update.

        :param auto_update: The auto_update of this DeviceData.
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def host_gateway(self):
        """
        Gets the host_gateway of this DeviceData.
        The `endpoint_name` of the host gateway, if appropriate.

        :return: The host_gateway of this DeviceData.
        :rtype: str
        """
        return self._host_gateway

    @host_gateway.setter
    def host_gateway(self, host_gateway):
        """
        Sets the host_gateway of this DeviceData.
        The `endpoint_name` of the host gateway, if appropriate.

        :param host_gateway: The host_gateway of this DeviceData.
        :type: str
        """

        self._host_gateway = host_gateway

    @property
    def device_execution_mode(self):
        """
        Gets the device_execution_mode of this DeviceData.
        The execution mode from the certificate of the device. Defaults to inheriting from host_gateway device. Permitted values:   - 0 - unspecified execution mode (default if host_gateway invalid or not set)   - 1 - development devices   - 5 - production devices

        :return: The device_execution_mode of this DeviceData.
        :rtype: int
        """
        return self._device_execution_mode

    @device_execution_mode.setter
    def device_execution_mode(self, device_execution_mode):
        """
        Sets the device_execution_mode of this DeviceData.
        The execution mode from the certificate of the device. Defaults to inheriting from host_gateway device. Permitted values:   - 0 - unspecified execution mode (default if host_gateway invalid or not set)   - 1 - development devices   - 5 - production devices

        :param device_execution_mode: The device_execution_mode of this DeviceData.
        :type: int
        """

        self._device_execution_mode = device_execution_mode

    @property
    def mechanism(self):
        """
        Gets the mechanism of this DeviceData.
        The ID of the channel used to communicate with the device.

        :return: The mechanism of this DeviceData.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this DeviceData.
        The ID of the channel used to communicate with the device.

        :param mechanism: The mechanism of this DeviceData.
        :type: str
        """
        allowed_values = ["connector", "direct"]
        if mechanism not in allowed_values:
            raise ValueError(
                "Invalid value for `mechanism` ({0}), must be one of {1}"
                .format(mechanism, allowed_values)
            )

        self._mechanism = mechanism

    @property
    def state(self):
        """
        Gets the state of this DeviceData.
        The current state of the device.

        :return: The state of this DeviceData.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DeviceData.
        The current state of the device.

        :param state: The state of this DeviceData.
        :type: str
        """
        allowed_values = ["unenrolled", "cloud_enrolling", "bootstrapped", "registered", "deregistered"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def etag(self):
        """
        Gets the etag of this DeviceData.
        The entity instance signature.

        :return: The etag of this DeviceData.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this DeviceData.
        The entity instance signature.

        :param etag: The etag of this DeviceData.
        :type: datetime
        """

        self._etag = etag

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DeviceData.
        The serial number of the device.

        :return: The serial_number of this DeviceData.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DeviceData.
        The serial number of the device.

        :param serial_number: The serial_number of this DeviceData.
        :type: str
        """

        self._serial_number = serial_number

    @property
    def firmware_checksum(self):
        """
        Gets the firmware_checksum of this DeviceData.
        The SHA256 checksum of the current firmware image.

        :return: The firmware_checksum of this DeviceData.
        :rtype: str
        """
        return self._firmware_checksum

    @firmware_checksum.setter
    def firmware_checksum(self, firmware_checksum):
        """
        Sets the firmware_checksum of this DeviceData.
        The SHA256 checksum of the current firmware image.

        :param firmware_checksum: The firmware_checksum of this DeviceData.
        :type: str
        """

        self._firmware_checksum = firmware_checksum

    @property
    def manifest_timestamp(self):
        """
        Gets the manifest_timestamp of this DeviceData.
        The timestamp of the current manifest version.

        :return: The manifest_timestamp of this DeviceData.
        :rtype: datetime
        """
        return self._manifest_timestamp

    @manifest_timestamp.setter
    def manifest_timestamp(self, manifest_timestamp):
        """
        Sets the manifest_timestamp of this DeviceData.
        The timestamp of the current manifest version.

        :param manifest_timestamp: The manifest_timestamp of this DeviceData.
        :type: datetime
        """

        self._manifest_timestamp = manifest_timestamp

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this DeviceData.
        The device vendor ID.

        :return: The vendor_id of this DeviceData.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this DeviceData.
        The device vendor ID.

        :param vendor_id: The vendor_id of this DeviceData.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def description(self):
        """
        Gets the description of this DeviceData.
        The description of the device.

        :return: The description of this DeviceData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceData.
        The description of the device.

        :param description: The description of this DeviceData.
        :type: str
        """
        if description is not None and len(description) > 2000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2000`")

        self._description = description

    @property
    def deployed_state(self):
        """
        Gets the deployed_state of this DeviceData.
        DEPRECATED: The state of the device's deployment.

        :return: The deployed_state of this DeviceData.
        :rtype: str
        """
        return self._deployed_state

    @deployed_state.setter
    def deployed_state(self, deployed_state):
        """
        Sets the deployed_state of this DeviceData.
        DEPRECATED: The state of the device's deployment.

        :param deployed_state: The deployed_state of this DeviceData.
        :type: str
        """
        allowed_values = ["development", "production"]
        if deployed_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployed_state` ({0}), must be one of {1}"
                .format(deployed_state, allowed_values)
            )

        self._deployed_state = deployed_state

    @property
    def object(self):
        """
        Gets the object of this DeviceData.
        The API resource entity.

        :return: The object of this DeviceData.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceData.
        The API resource entity.

        :param object: The object of this DeviceData.
        :type: str
        """

        self._object = object

    @property
    def endpoint_type(self):
        """
        Gets the endpoint_type of this DeviceData.
        The endpoint type of the device. For example, the device is a gateway.

        :return: The endpoint_type of this DeviceData.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this DeviceData.
        The endpoint type of the device. For example, the device is a gateway.

        :param endpoint_type: The endpoint_type of this DeviceData.
        :type: str
        """
        if endpoint_type is not None and len(endpoint_type) > 64:
            raise ValueError("Invalid value for `endpoint_type`, length must be less than or equal to `64`")

        self._endpoint_type = endpoint_type

    @property
    def deployment(self):
        """
        Gets the deployment of this DeviceData.
        DEPRECATED: The last deployment used on the device.

        :return: The deployment of this DeviceData.
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this DeviceData.
        DEPRECATED: The last deployment used on the device.

        :param deployment: The deployment of this DeviceData.
        :type: str
        """

        self._deployment = deployment

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this DeviceData.
        The address of the connector to use.

        :return: The mechanism_url of this DeviceData.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this DeviceData.
        The address of the connector to use.

        :param mechanism_url: The mechanism_url of this DeviceData.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def name(self):
        """
        Gets the name of this DeviceData.
        The name of the device.

        :return: The name of this DeviceData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceData.
        The name of the device.

        :param name: The name of this DeviceData.
        :type: str
        """
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")

        self._name = name

    @property
    def device_key(self):
        """
        Gets the device_key of this DeviceData.
        The fingerprint of the device certificate.

        :return: The device_key of this DeviceData.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """
        Sets the device_key of this DeviceData.
        The fingerprint of the device certificate.

        :param device_key: The device_key of this DeviceData.
        :type: str
        """
        if device_key is not None and len(device_key) > 512:
            raise ValueError("Invalid value for `device_key`, length must be less than or equal to `512`")

        self._device_key = device_key

    @property
    def created_at(self):
        """
        Gets the created_at of this DeviceData.
        The timestamp of when the device was created in the device directory.

        :return: The created_at of this DeviceData.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DeviceData.
        The timestamp of when the device was created in the device directory.

        :param created_at: The created_at of this DeviceData.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def manifest(self):
        """
        Gets the manifest of this DeviceData.
        DEPRECATED: The URL for the current device manifest.

        :return: The manifest of this DeviceData.
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this DeviceData.
        DEPRECATED: The URL for the current device manifest.

        :param manifest: The manifest of this DeviceData.
        :type: str
        """

        self._manifest = manifest

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceData.
        Up to five custom key-value attributes.

        :return: The custom_attributes of this DeviceData.
        :rtype: dict(str, str)
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceData.
        Up to five custom key-value attributes.

        :param custom_attributes: The custom_attributes of this DeviceData.
        :type: dict(str, str)
        """

        self._custom_attributes = custom_attributes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DeviceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
