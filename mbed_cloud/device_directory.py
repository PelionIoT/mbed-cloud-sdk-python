# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Public API for Device API."""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import BaseObject
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.device_directory as device_directory
from mbed_cloud._backends.device_directory.models import DeviceData
from mbed_cloud._backends.device_directory.models import DeviceEventData
from mbed_cloud._backends.device_directory.rest import \
    ApiException as DeviceDirectoryApiException

LOG = logging.getLogger(__name__)


class DeviceDirectoryAPI(BaseAPI):
    """API reference for the Device API.

    Exposing functionality for doing a range of device related actions:
        - Listing registered devices
        - Create and manage device queries
    """

    def __init__(self, params={}, b64decode=True):
        """Setup the backend APIs with provided config."""
        super(DeviceDirectoryAPI, self).__init__(params)

        # Initialize the wrapped APIs
        self.device_directory = self._init_api(device_directory)

    @catch_exceptions(DeviceDirectoryApiException)
    def list_devices(self, **kwargs):
        """List devices in the device catalog.

        Example usage, listing all registered devices in the catalog:

        .. code-block:: python

            filters = { 'state': {'$eq': 'registered' } }
            devices = api.list_devices(order='asc', filters=filters)
            for idx, d in enumerate(devices):
                print(idx, d.id)

        :param int limit: The number of devices to retrieve.
        :param str order: The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: Get devices after/starting at given `device_id`
        :param filters: Dictionary of filters to apply.
        :returns: a list of :py:class:`Device` objects registered in the catalog.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, True)

        api = self.device_directory.DefaultApi()
        return PaginatedResponse(api.device_list, lwrap_type=Device, **kwargs)

    @catch_exceptions(DeviceDirectoryApiException)
    def get_device(self, device_id):
        """Get device details from catalog.

        :param str device_id: the ID of the device to retrieve (Required)
        :returns: device object matching the `device_id`.
        :rtype: Device
        """
        api = self.device_directory.DefaultApi()
        return Device(api.device_retrieve(device_id))

    @catch_exceptions(DeviceDirectoryApiException)
    def update_device(self, device_id, **kwargs):
        """Update existing device in catalog.

        .. code-block:: python

            existing_device = api.get_device(...)
            updated_device = api.update_device(
                existing_device.id,
                certificate_fingerprint = "something new"
            )

        :param str device_id: The ID of the device to update (Required)
        :param obj custom_attributes: Up to 5 custom JSON attributes
        :param str description: The description of the device
        :param str name: The name of the device
        :param str alias: The alias of the device
        :parama str endpoint_type: The endpoint type of the device - e.g. if the device is a gateway
        :param str host_gateway: The endpoint_name of the host gateway, if appropriate
        :param str certificate_fingerprint: Fingerprint of the device certificate
        :param str certificate_issuer_id: ID of the issuer of the certificate
        :returns: the updated device object
        :rtype: Device
        """
        api = self.device_directory.DefaultApi()
        device = Device.create_request_map(kwargs)
        body = self.device_directory.DeviceDataPostRequest(**device)
        return Device(api.device_update(device_id, body))

    @catch_exceptions(DeviceDirectoryApiException)
    def add_device(self, **kwargs):
        """Add a new device to catalog.

        .. code-block:: python

            device = {
                "mechanism": "connector",
                "certificate_fingerprint": "<certificate>",
                "name": "New device name",
                "certificate_issuer_id": "<id>"
            }
            resp = api.add_device(**device)
            print(resp.created_at)

        :param str certificate_fingerprint: Fingerprint of the device certificate (Required)
        :param str certificate_issuer_id: ID of the issuer of the certificate (Required)
        :param str name: The name of the device
        :param str account_id: The owning IAM account ID
        :param obj custom_attributes: Up to 5 custom JSON attributes
        :param str deployed_state: State of the device's deployment
        :param str description: The description of the device
        :param str device_class: Class of the device
        :param str id: The ID of the device
        :param str manifest_url: URL for the current device manifest
        :param str mechanism: The ID of the channel used to communicate with the device
        :param str mechanism_url: The address of the connector to use
        :param str serial_number: The serial number of the device
        :param str state: The current state of the device
        :param int trust_class: The device trust class
        :param int trust_level: The device trust level
        :param str vendor_id: The device vendor ID
        :param str alias: The alias of the device
        :parama str endpoint_type: The endpoint type of the device - e.g. if the device is a gateway
        :param str host_gateway: The endpoint_name of the host gateway, if appropriate
        :param datetime bootstrap_certificate_expiration:
        :param datetime connector_certificate_expiration: Expiration date of the certificate
            used to connect to connector server
        :param int device_execution_mode: The device class
        :param str firmware_checksum: The SHA256 checksum of the current firmware image
        :param datetime manifest_timestamp: The timestamp of the current manifest version
        :return: the newly created device object.
        :rtype: Device
        """
        api = self.device_directory.DefaultApi()
        device = Device.create_request_map(kwargs)
        device = DeviceData(**device)
        return Device(api.device_create(device))

    @catch_exceptions(DeviceDirectoryApiException)
    def delete_device(self, device_id):
        """Delete device from catalog.

        :param str device_id: ID of device in catalog to delete (Required)
        :return: void
        """
        api = self.device_directory.DefaultApi()
        return api.device_destroy(id=device_id)

    @catch_exceptions(DeviceDirectoryApiException)
    def list_queries(self, **kwargs):
        """List queries in device query service.

        :param int limit: The number of devices to retrieve.
        :param str order: The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: Get devices after/starting at given `device_id`
        :param filters: Dictionary of filters to apply.
        :returns: a list of :py:class:`Query` objects.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, True)
        api = self.device_directory.DefaultApi()

        return PaginatedResponse(api.device_query_list, lwrap_type=Query, **kwargs)

    @catch_exceptions(DeviceDirectoryApiException)
    def add_query(self, name, filter, **kwargs):
        """Add a new query to device query service.

        .. code-block:: python

            f = api.add_query(
                name = "Query name",
                filter = {
                    "device_id": {"$eq": "01234"},
                    custom_attributes = {
                        "foo": {"$eq": "bar"}
                    }
                }
            )
            print(f.created_at)

        :param str name: Name of query (Required)
        :param dict filter: Filter properties to apply (Required)
        :param return: the newly created query object.
        :return: the newly created query object
        :rtype: Query
        """
        api = self.device_directory.DefaultApi()

        # Ensure we have the correct types and get the new query object
        query = self._encode_query(filter)
        query_map = Query.create_request_map(kwargs)
        # Create the query object
        f = self.device_directory.DeviceQuery(name=name, query=query, **query_map)

        return Query(api.device_query_create(f))

    @catch_exceptions(DeviceDirectoryApiException)
    def update_query(self, query_id, name=None, filter=None, **kwargs):
        """Update existing query in device query service.

        .. code-block:: python

            q = api.get_query(...)
            q.filter["custom_attributes"]["foo"] = {
                "$eq": "bar"
            }
            new_q = api.update_query(
                query_id = q.id,
                name = "new name",
                filter = q.filter
            )

        :param str query_id: Existing query ID to update (Required)
        :param str name: name of query
        :param dict filter: query properties to apply
        :return: the newly updated query object.
        :rtype: Query
        """
        api = self.device_directory.DefaultApi()

        # Get urlencoded query attribute
        if filter is not None:
            query = self._encode_query(filter)
        else:
            query = filter

        query_map = Query.create_request_map(kwargs)
        body = self.device_directory.DeviceQueryPatchRequest(
            name=name,
            query=query,
            **query_map
        )

        return Query(api.device_query_partial_update(query_id, body))

    @catch_exceptions(DeviceDirectoryApiException)
    def delete_query(self, query_id):
        """Delete query in device query service.

        :param int query_id: id of the query to delete (Required)
        :return: void
        """
        api = self.device_directory.DefaultApi()
        api.device_query_destroy(query_id)
        return

    @catch_exceptions(DeviceDirectoryApiException)
    def get_query(self, query_id):
        """Get query in device query service.

        :param int query_id: id of the query to get (Required)
        :returns: device query object
        :rtype: Query
        """
        api = self.device_directory.DefaultApi()
        return Query(api.device_query_retrieve(query_id))

    @catch_exceptions(DeviceDirectoryApiException)
    def list_device_events(self, **kwargs):
        """List all device logs.

        :param int limit: The number of logs to retrieve.
        :param str order: The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: Get logs after/starting at given `device_event_id`
        :param dict filters: Dictionary of filters to apply.
        :return: list of :py:class:`DeviceEvent` objects
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, True)

        api = self.device_directory.DefaultApi()
        return PaginatedResponse(api.device_log_list, lwrap_type=DeviceEvent, **kwargs)

    @catch_exceptions(DeviceDirectoryApiException)
    def get_device_event(self, device_event_id):
        """Get device event with provided ID.

        :param int device_event_id: id of the event to get (Required)
        :rtype: DeviceEvent
        """
        api = self.device_directory.DefaultApi()
        return DeviceEvent(api.device_log_retrieve(device_event_id))


class Device(BaseObject):
    """Describes device object from the catalog."""

    @staticmethod
    def _get_attributes_map():
        return {
            "account_id": "account_id",
            "bootstrapped_timestamp": "bootstrapped_timestamp",
            "created_at": "created_at",
            "custom_attributes": "custom_attributes",
            "deployed_state": "deployed_state",
            "last_deployment": "deployment",
            "description": "description",
            "device_class": "device_class",
            "id": "id",
            "manifest_url": "manifest",
            "mechanism": "mechanism",
            "mechanism_url": "mechanism_url",
            "name": "name",
            "host_gateway": "host_gateway",
            "endpoint_type": "endpoint_type",
            "serial_number": "serial_number",
            "state": "state",
            "trust_class": "trust_class",
            "trust_level": "trust_level",
            "updated_at": "updated_at",
            "vendor_id": "vendor_id",
            "alias": "endpoint_name",
            "bootstrap_certificate_expiration": "bootstrap_expiration_date",
            "certificate_fingerprint": "device_key",
            "certificate_issuer_id": "ca_id",
            "connector_certificate_expiration": "connector_expiration_date",
            "device_execution_mode": "device_execution_mode",
            "firmware_checksum": "firmware_checksum",
            "manifest_timestamp": "manifest_timestamp"
        }

    @property
    def account_id(self):
        """The owning IAM account ID.

        :rtype: str
        """
        return self._account_id

    @property
    def bootstrapped_timestamp(self):
        """The time device was created..

        :rtype: datetime
        """
        return self._bootstrapped_timestamp

    @property
    def created_at(self):
        """The time the device was created.

        :rtype: datetime
        """
        return self._created_at

    @property
    def custom_attributes(self):
        """Up to 5 custom JSON attributes.

        :rtype: object
        """
        return self._custom_attributes

    @property
    def deployed_state(self):
        """State of the device's deployment.

        :rtype: str
        """
        return self._deployed_state

    @property
    def last_deployment(self):
        """The last deployment used on the device.

        :rtype: datetime
        """
        return self._last_deployment

    @property
    def description(self):
        """The description of the device.

        :rtype: str
        """
        return self._description

    @property
    def device_class(self):
        """Class of the device.

        :rtype: str
        """
        return self._device_class

    @property
    def id(self):
        """The ID of the device.

        :rtype: str
        """
        return self._id

    @property
    def manifest_url(self):
        """URL for the current device manifest.

        :rtype: str
        """
        return self._manifest_url

    @property
    def mechanism(self):
        """The ID of the channel used to communicate with the device.

        :rtype: str
        """
        return self._mechanism

    @property
    def mechanism_url(self):
        """The address of the connector to use.

        :rtype: str
        """
        return self._mechanism_url

    @property
    def name(self):
        """The name of the device.

        :rtype: str
        """
        return self._name

    @property
    def serial_number(self):
        """The serial number of the device.

        :rtype: str
        """
        return self._serial_number

    @property
    def state(self):
        """The current state of the device.

        :rtype: str
        """
        return self._state

    @property
    def trust_class(self):
        """The device trust class.

        The time the object was created

        :return: The created_at of this Query.
        :rtype: int
        """
        return self._trust_class

    @property
    def trust_level(self):
        """The device trust level.

        The time the object was created

        :return: The created_at of this Query.
        :rtype: int
        """
        return self._trust_level

    @property
    def updated_at(self):
        """The time the device was updated.

        The time the object was created

        :return: The created_at of this Query.
        :rtype: datetime
        """
        return self._updated_at

    @property
    def vendor_id(self):
        """The device vendor ID.

        The time the object was created

        :return: The created_at of this Query.
        :rtype: str
        """
        return self._vendor_id

    @property
    def alias(self):
        """The alias of the device.

        :rtype: str
        """
        return self._alias

    @property
    def bootstrap_certificate_expiration(self):
        """Expiration date of certificate.

        :rtype: datetime
        """
        return self._bootstrap_certificate_expiration

    @property
    def certificate_fingerprint(self):
        """Fingerprint of the device certificate.

        :rtype: str
        """
        return self._certificate_fingerprint

    @property
    def certificate_issuer_id(self):
        """ID of the issuer of the certificate.

        :rtype: str
        """
        return self._certificate_issuer_id

    @property
    def connector_certificate_expiration(self):
        """Expiration date of the certificate used to connect to connector server.

        :rtype: datetime
        """
        return self._connector_certificate_expiration

    @property
    def device_execution_mode(self):
        """The device class.

        :rtype: int
        """
        return self._device_execution_mode

    @property
    def firmware_checksum(self):
        """The SHA256 checksum of the current firmware image.

        :rtype: str
        """
        return self._firmware_checksum

    @property
    def manifest_timestamp(self):
        """The timestamp of the current manifest version.

        :rtype: datetime
        """
        return self._manifest_timestamp


class Query(BaseObject):
    """Describes device query object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "created_at": "created_at",
            "description": "description",
            "id": "id",
            "name": "name",
            "updated_at": "updated_at",
            "filter": "query"
        }

    @property
    def created_at(self):
        """Get the created_at of this Query.

        The time the object was created

        :return: The created_at of this Query.
        :rtype: datetime
        """
        return self._created_at

    @property
    def description(self):
        """Get the description of this Query.

        The description of the object

        :return: The description of this Query.
        :rtype: str
        """
        return self._description

    @property
    def id(self):
        """Get the id of this Query.

        The ID of the query

        :return: The id of this Query.
        :rtype: str
        """
        return self._id

    @property
    def name(self):
        """Get the name of this Query.

        The name of the query

        :return: The name of this Query.
        :rtype: str
        """
        return self._name

    @property
    def updated_at(self):
        """Get the updated_at of this Query.

        The time the object was updated

        :return: The updated_at of this Query.
        :rtype: datetime
        """
        return self._updated_at

    @property
    def filter(self):
        """Get the query of this Query.

        The device query

        :return: The query of this Query.
        :rtype: dict
        """
        if isinstance(self._filter, str):
            return self._decode_query(self._filter)
        return self._filter

    @filter.setter
    def filter(self, value):
        self._filter = value


class DeviceEvent(DeviceEventData):
    """Describes device event object."""

    def __init__(self, device_event_obj):
        """Override __init__ and allow passing in backend object."""
        super(DeviceEvent, self).__init__(**device_event_obj.to_dict())
