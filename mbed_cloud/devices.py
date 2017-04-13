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
import base64
from collections import defaultdict
import logging
from six import iteritems
from six.moves import queue
import threading
import time
import urllib

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import ClassAPI
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.exceptions import CloudAsyncError
from mbed_cloud.exceptions import CloudTimeoutError
from mbed_cloud.exceptions import CloudUnhandledError
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.device_catalog as dc
from mbed_cloud._backends.device_catalog.models import DeviceData
from mbed_cloud._backends.device_catalog.rest import \
    ApiException as DeviceCatalogApiException
import mbed_cloud._backends.device_query_service as dc_queries
from mbed_cloud._backends.device_query_service.rest import \
    ApiException as DeviceQueryServiceApiException
import mbed_cloud._backends.mds as mds
from mbed_cloud._backends.mds.rest import ApiException as MdsApiException

LOG = logging.getLogger(__name__)


class DeviceAPI(BaseAPI):
    """API reference for the Device API.

    Exposing functionality for doing a range of device related actions:
        - Listing registered and connected devices
        - Exploring and managing resources and resource values on said devices
        - Setup resource subscriptions and webhooks for resource monitoring
        - Create and manage device queries
    """

    def __init__(self, params={}, b64decode=True):
        """Setup the backend APIs with provided config.

        In addition we need to setup some special handling of background
        threads for the mDS functionality - as it relies on background polling.
        """
        super(DeviceAPI, self).__init__(params)

        # Initialize the wrapped APIs
        self.mds = self._init_api(mds)
        self.dc = self._init_api(dc)
        self.dc_queries = self._init_api(dc_queries)

        self._db = {}
        self._queues = defaultdict(lambda: defaultdict(queue.Queue))

        self._long_polling_thread = _LongPollingThread(self._db,
                                                       self._queues,
                                                       b64decode=b64decode,
                                                       mds=self.mds)
        self._long_polling_is_active = False
        self._long_polling_thread.daemon = True

    def start_notifications(self):
        """Start the long-polling thread.

        If not an external callback is setup (using `update_webhook`) then
        calling this function is mandatory.

        .. code-block:: python

            >>> api.start_notifications()
            >>> print(api.get_resource_value(device, path))
            Some value
            >>> api.stop_notifications()

        :returns: void
        """
        self._long_polling_thread.start()
        self._long_polling_is_active = True

    def stop_notifications(self):
        """Stop the long-polling thread.

        :returns: void
        """
        self._long_polling_thread.stop()
        self._long_polling_is_active = False

    @catch_exceptions(MdsApiException)
    def list_connected_devices(self, **kwargs):
        """List connected devices.

        :returns: a list of currently *connected* `ConnectedDevice` objects
        :rtype: list of ConnectedDevice
        """
        api = self.mds.EndpointsApi()

        resp = api.v2_endpoints_get()
        return [ConnectedDevice(e) for e in resp]

    @catch_exceptions(MdsApiException)
    def list_resources(self, device_id):
        """List all resources registered to a connected device/device.

        .. code-block:: python

            >>> for r in api.list_resources(device_id):
                    print(r.name, r.observable, r.uri)
            None,True,/3/0/1
            Update,False,/5/0/3
            ...

        :returns: A list of :py:class:`Resource` objects for the device
        :rtype: list
        """
        api = self.mds.EndpointsApi()
        return [Resource(r) for r in api.v2_endpoints_id_get(device_id)]

    @catch_exceptions(MdsApiException)
    def get_resource_value(self, device_id, resource_path, fix_path=True, timeout=None):
        """Get a resource value for a given device and resource path by blocking thread.

        Example usage:

        .. code-block:: python

            try:
                v = api.get_resource_value(device_id, path)
                print("Current value", v)
            except CloudAsyncError, e:
                print("Error", e)

        :param str device_id: The name/id of the device
        :param str resource_path: The resource path to get
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :param timeout: Seconds to request value for before timeout. If not provided, the
            program might hang indefinitly.
        :raises: CloudAsyncError, CloudTimeoutError
        :returns: The resource value for the requested resource path
        :rtype: str
        """
        # Ensure we're long polling first
        if not self._long_polling_is_active:
            raise CloudUnhandledError(
                "Long polling needs to be enabled before getting resource value synchronously.")

        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]
        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_id_resource_path_get(device_id, resource_path)

        # The async consumer, which will read data from long-polling thread
        consumer = AsyncConsumer(resp.async_response_id, self._db)

        # We block the thread and get the value for the user.
        return self._get_value_synchronized(consumer, timeout)

    @catch_exceptions(MdsApiException)
    def get_resource_value_async(self, device_id, resource_path, fix_path=True):
        """Get a resource value for a given device and resource path.

        Will not block, but instead return an AsyncConsumer. Example usage:

        .. code-block:: python

            a = api.get_resource_value_async(device, path)
            while not a.is_done:
                time.sleep(0.1)
            if a.error:
                print("Error", a.error)
            print("Current value", a.value)

        :param str device_id: The name/id of the device
        :param str resource_path: The resource path to get
        :param bool fix_path: strip leading / of path if present
        :returns: Consumer object to control asynchronous request
        :rtype: AsyncConsumer
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_id_resource_path_get(device_id, resource_path)

        # The async consumer, which will read data from long-polling thread
        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def set_resource_value(self, device_id, resource_path,
                           resource_value=None, fix_path=True):
        """Set resource value for given resource path, on device.

        Will block and wait for response to come through. Usage:

        .. code-block:: python

            try:
                v = api.set_resource_value(device, path, value)
                print("Success, new value:", v)
            except AsyncError, e:
                print("Error", e)

        :param str device_id: The name/id of the device
        :param str resource_path: The resource path to update
        :param str resource_value: The new value to set for given path (if None
            the resource function will be executed)
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :raises: AsyncError
        :returns: The value of the new resource
        :rtype: str
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()

        if resource_value:
            resp = api.v2_endpoints_id_resource_path_put(device_id, resource_path, resource_value)
        else:
            resp = api.v2_endpoints_id_resource_path_post(device_id, resource_path)
        consumer = AsyncConsumer(resp.async_response_id, self._db)
        return self._get_value_synchronized(consumer)

    @catch_exceptions(MdsApiException)
    def set_resource_value_async(self, device_id, resource_path,
                                 resource_value=None, fix_path=True):
        """Set resource value for given resource path, on device.

        Will not block. Returns immediatly. Usage:

        .. code-block:: python

            a = api.set_resource_value_async(device, path, value)
            while not a.is_done:
                time.sleep(0.1)
            if a.error:
                print("Error", a.error)
            print("Success, new value:", a.value)

        :param str device_id: The name/id of the device
        :param str resource_path: The resource path to update
        :param str resource_value: The new value to set for given path (if
            None, the resource function will be executed)
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :returns: An async consumer object holding reference to request
        :rtype: AsyncConsumer
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()

        if resource_value:
            resp = api.v2_endpoints_id_resource_path_put(device_id, resource_path, resource_value)
        else:
            resp = api.v2_endpoints_id_resource_path_post(device_id, resource_path)

        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def add_subscription(self, device_id, resource_path, fix_path=True, queue_size=5):
        """Subscribe to resource updates.

        When called on valid device and resource path a subscription is setup so that
        any update on the resource path value triggers a new element on the FIFO queue.
        The returned object is a native Python Queue object.

        :param device_id: Name of device to subscribe on
        :param resource_path: The resource path on device to observe
        :param fix_path: Removes leading / on resource_path if found
        :param queue_size: set the Queue size. If set to 0, no queue object will be created
        :returns: a queue of resource updates
        :rtype: Queue
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        # Keep the original path around however, as we use that for queue registration.
        fixed_path = resource_path
        if fix_path and resource_path.startswith("/"):
            fixed_path = resource_path[1:]

        # Create the queue and register it with the dict holding all queues
        q = queue.Queue(queue_size) if queue_size > 0 else None
        self._queues[device_id][resource_path] = q

        # Send subscription request
        api = self.mds.SubscriptionsApi()
        api.v2_subscriptions_id_resource_path_put(device_id, fixed_path)

        # Return the Queue object to the user
        return q

    @catch_exceptions(MdsApiException)
    def add_subscription_async(self, device_id, resource_path, callback_fn,
                               fix_path=True, queue_size=5):
        """Subscribe to resource updates with callback function.

        When called on valid device and resource path a subscription is setup so that
        any update on the resource path value triggers an update on the callback function.

        :param device_id: Name of device to subscribe on
        :param resource_path: The resource path on device to observe
        :param callback_fn: Callback function to be executed on update to subscribed resource
        :param fix_path: Removes leading / on resource_path if found
        :param queue_size: set the Queue size. If set to 0, no queue object will be created
        :returns: void
        """
        queue = self.add_subscription(device_id, resource_path, fix_path, queue_size)

        # Setup daemon thread for callback function
        t = threading.Thread(target=self._subscription_handler, args=[queue, callback_fn])
        t.daemon = True
        t.start()

    @catch_exceptions(MdsApiException)
    def update_presubscription(self, device_id, resource_path, device_type=""):
        """Create pre-subscription for device and resource path.

        :returns: void
        """
        api = self.mds.SubscriptionsApi()

        presubscription = self.mds.Presubscription(
            endpoint_name=device_id,
            endpoint_type=device_type,
            _resource_path=[resource_path]
        )
        api.v2_subscriptions_put([presubscription])

        # Returns void
        return

    @catch_exceptions(MdsApiException)
    def delete_subscription(self, device_id=None, resource_path=None, fix_path=True):
        """Unsubscribe from device and/or resource_path updates.

        If device_id or resource_path is None, we remove every subscripton
        for them. I.e. calling this method without arguments removes all subscriptions,
        but calling it with only device_id removes subscriptions for all resources
        on the given device.

        :param device_id: device to unsubscribe events from. If not
            provided, all registered devices will be unsubscribed.
        :param resource_path: resource_path to unsubscribe events from. If not
            provided, all resource paths will be unsubscribed.
        :param fix_path: remove trailing / in resouce path to ensure API works.
        :return: void
        """
        devices = filter(None, [device_id])
        if not device_id:
            devices = self._queues.keys()
        resource_paths = [resource_path]
        if not resource_path:
            resource_paths = []
            for e in devices:
                resource_paths.extend(self._queues[e].keys())

        # Delete the subscriptions
        api = self.mds.SubscriptionsApi()
        for e in devices:
            for r in resource_paths:
                # Fix the path, if required.
                fixed_path = r
                if fix_path and r.startswith("/"):
                    fixed_path = r[1:]

                # Make request to API, ignoring result
                api.v2_subscriptions_endpoint_name_resource_path_delete(device_id, fixed_path)

                # Remove Queue from dictionary
                del self._queues[e][r]
        return

    @catch_exceptions(MdsApiException)
    def get_webhook(self):
        """Get the current callback URL if it exists.

        return: void
        """
        api = self.mds.DefaultApi()
        return Webhook(api.v2_notification_callback_get())

    @catch_exceptions(MdsApiException)
    def update_webhook(self, url, headers={}):
        """Register new webhook for incoming subscriptions.

        If a webhook is already set, this will do an overwrite.

        :param str url: the URL with listening webhook
        :param dict headers: K/V dict with additional headers to send with request
        :return: void
        """
        api = self.mds.NotificationsApi()

        # Send the request to register the webhook
        webhook_obj = self.mds.Webhook(url=url, headers=headers)
        api.v2_notification_callback_put(webhook_obj)
        return

    @catch_exceptions(MdsApiException)
    def delete_webhook(self):
        """Delete/remove registered webhook.

        If no webhook is registered, an exception (404) will be raised.

        Note that every registered subscription will be deleted as part of
        deregistering a webhook.

        :return: void
        """
        api = self.mds.DefaultApi()
        api.v2_notification_callback_delete()

        # Every subscription will be deleted, so we can clear the queues too.
        self._queues.clear()
        return

    @catch_exceptions(DeviceCatalogApiException)
    def list_devices(self, **kwargs):
        """List devices in the device catalog.

        Example usage, listing all registered devices in the catalog:

        .. code-block:: python

            filters = { 'state': 'registered' }
            devices = api.list_devices(order='asc', filters=filters)
            for d, idx in devices.iteritems():
                print(idx, d.id)

        :param int limit: (Optional) The number of devices to retrieve.
        :param str order: (Optional) The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: (Optional) Get devices after/starting at given `device_id`
        :param filters: (Optional) Dictionary of filters to apply.
        :returns: a list of :py:class:`Device` objects registered in the catalog.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        api = self.dc.DefaultApi()
        return PaginatedResponse(api.device_list, lwrap_type=Device, **kwargs)

    @catch_exceptions(DeviceCatalogApiException)
    def get_device(self, device_id):
        """Get device details from catalog.

        :param device_id: the ID of the device to retrieve (str)
        :returns: device object matching the `device_id`.
        :rtype: Device
        """
        api = self.dc.DefaultApi()
        return Device(api.device_retrieve(device_id))

    @catch_exceptions(DeviceCatalogApiException)
    def update_device(self, device_id, **kwargs):
        """Update existing device in catalog.

        .. code-block:: python

            existing_device = api.get_device(...)
            updated_device = api.update_device(
                existing_device.id,
                certificate_fingerprint = "something new"
            )

        :param bool auto_update: Mark this device for auto firmware update
        :param obj custom_attributes: Up to 5 custom JSON attributes
        :param str description: The description of the device
        :param str name: The name of the device
        :param str alias: The alias of the device
        :param str certificate_fingerprint: Fingerprint of the device certificate
        :param str certificate_issuer_id: ID of the issuer of the certificate
        :returns: the updated device object
        :rtype: Device
        """
        kwargs = Device()._verify_args(kwargs)
        api = self.dc.DefaultApi()
        body = self.dc.DeviceDataPostRequest(**kwargs)
        return Device(api.device_update(device_id, body))

    @catch_exceptions(DeviceCatalogApiException)
    def add_device(self, **kwargs):
        """Add a new device to catalog.

        .. code-block:: python

            device = {
                "mechanism": "connector",
                "certificateFingerprint": "<certificate>",
                "name": "New device name",
                "auto_update": True,
                "certificateIssuerId": "<id>"
            }
            resp = api.add_device(**device)
            print(resp.created_at)

        :param str account_id: The owning IAM account ID
        :param bool auto_update: Mark this device for auto firmware update
        :param obj custom_attributes: Up to 5 custom JSON attributes
        :param str deployed_state: State of the device's deployment
        :param str description: The description of the device
        :param str device_class: Class of the device
        :param str id: The ID of the device
        :param str manifest_url: URL for the current device manifest
        :param str mechanism: The ID of the channel used to communicate with the device
        :param str mechanism_url: The address of the connector to use
        :param str name: The name of the device
        :param str serial_number: The serial number of the device
        :param str state: The current state of the device
        :param int trust_class: The device trust class
        :param int trust_level: The device trust level
        :param str vendor_id: The device vendor ID
        :param str alias: The alias of the device
        :param datetime bootstrap_certificate_expiration:
        :param str certificate_fingerprint: Fingerprint of the device certificate
        :param str certificate_issuer_id: ID of the issuer of the certificate
        :param datetime connector_certificate_expiration: Expiration date of the certificate
        used to connect to connector server
        :param int device_execution_mode: The device class
        :param str firmware_checksum: The SHA256 checksum of the current firmware image
        :param datetime manifest_timestamp: The timestamp of the current manifest version
        :return: the newly created device object.
        :rtype: Device
        """
        kwargs = Device()._verify_args(kwargs)
        api = self.dc.DefaultApi()
        device = DeviceData(**kwargs)
        return Device(api.device_create(device))

    @catch_exceptions(DeviceCatalogApiException)
    def delete_device(self, id):
        """Delete device from catalog.

        :param str id: ID of device in catalog to delete
        :return: void
        """
        api = self.dc.DefaultApi()
        return api.device_destroy(id=id)

    @catch_exceptions(DeviceQueryServiceApiException)
    def list_queries(self, **kwargs):
        """List queries in device query service.

        :param int limit: (Optional) The number of devices to retrieve.
        :param str order: (Optional) The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: (Optional) Get devices after/starting at given `device_id`
        :returns: a list of :py:class:`Query` objects.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.dc_queries.DefaultApi()

        return PaginatedResponse(api.device_query_list, lwrap_type=Query, **kwargs)

    @catch_exceptions(DeviceQueryServiceApiException)
    def add_query(self, name, filter, custom_attributes=None, **kwargs):
        """Add a new query to device query service.

        .. code-block:: python

            f = api.add_query(
                name = "Query name",
                query = {},
                custom_attributes = {
                    "foo": "bar"
                }
            )
            print(f.created_at)

        :param str name: Name of query
        :param dict filter: Filter properties to apply
        :param dict custom_attributes: Extra query attributes
        :param return: the newly created query object.
        :return: the newly created query object
        :rtype: Query
        """
        api = self.dc_queries.DefaultApi()

        # Ensure we have the correct types and get the new query object based on
        # passed in query object and custom attributes.
        query = self._get_query_attributes(filter, custom_attributes)

        # Create the query object
        f = self.dc_queries.DeviceQuery(name=name, query=query, **kwargs)

        return Query(api.device_query_create(f))

    @catch_exceptions(DeviceQueryServiceApiException)
    def update_query(self, query_id, name, filter, custom_attributes=None, **kwargs):
        """Update existing query in device query service.

        .. code-block:: python

            q = api.get_query(...)
            new_custom_attributes = {
                "foo": "bar"
            }
            new_q = api.update_query(
                query_id = q.id,
                name = "new name",
                filter = q.filter,
                custom_attributes = new_custom_attributes
            )

        :param str query_id: Existing query ID to update
        :param str name: (New) name of query
        :param dict query: (New) query properties to apply
        :param dict custom_attributes: (New) extra query attributes
        :param return: the newly updated query object.
        :rtype: Query
        """
        api = self.dc_queries.DefaultApi()

        # Get urlencoded query attribute
        query = self._get_query_attributes(filter, custom_attributes)

        body = self.dc_queries.DeviceQueryPostPutRequest(
            name=name,
            query=query,
            **kwargs
        )

        return Query(api.device_query_update(query_id, body))

    @catch_exceptions(DeviceQueryServiceApiException)
    def delete_query(self, query_id):
        """Delete query in device query service.

        :param int query_id: id of the query to delete
        :param return: void
        """
        api = self.dc_queries.DefaultApi()
        api.device_query_destroy(query_id)
        return

    @catch_exceptions(DeviceQueryServiceApiException)
    def get_query(self, query_id):
        """Get query in device query service.

        :param int query_id: id of the query to get
        :returns: device query object
        :rtype: Query
        """
        api = self.dc_queries.DefaultApi()
        return Query(api.device_query_retrieve(query_id))

    def _subscription_handler(self, queue, callback_fn):
        while True:
            value = queue.get()
            callback_fn(value)

    def _get_query_attributes(self, query, custom_attributes):
        # Ensure the query is of dict type
        if query and not isinstance(query, dict):
            raise CloudValueError("'query' parameter needs to be of type dict")

        # Add custom attributes, if provided
        if custom_attributes:
            if not isinstance(custom_attributes, dict):
                raise CloudValueError("Custom attributes when creating query"
                                      "needs to be dict object")
            for k, v in custom_attributes.iteritems():
                if not k:
                    LOG.warning("Ignoring custom attribute with value %r as key is empty" % (v,))
                    continue
                query['custom_attributes__' + k] = v

        # Ensure query is valid
        if not query.keys():
            raise CloudValueError("'query' parameter not valid, needs to contain query keys")

        return self._urlify_query(query)

    def _urlify_query(self, query):
        # Quote strings using %20, not '+' which is default when urlencoding dicts
        for k, v in query.iteritems():
            if type(v) is str:
                query[k] = urllib.quote(v)

        # Encode the query string
        return urllib.urlencode(query)

    def _get_value_synchronized(self, consumer, timeout=None):
        start_time = int(time.time())

        # We return synchronously, so we block in a busy loop waiting for the
        # request to be done.
        while not consumer.is_done:
            duration = int(time.time()) - start_time
            if timeout and duration > timeout:
                raise CloudTimeoutError("Timeout getting async value. Timeout: %d seconds"
                                        % (timeout,)
                                        )
            time.sleep(0.1)

        # If we get an error we throw an exception to the user, which can then be handled
        # accordingly.
        if consumer.error:
            raise CloudAsyncError(consumer.error)

        return consumer.value


class AsyncConsumer(object):
    """Consumer object for reading values from a long-polling thread.

    Example usage:

    .. code-block:: python

        async_resp = api.get_resource_value(device, resource)
        while not async_resp.is_done:
            time.sleep(0.1)
        if async_resp.error:
            raise Exception("Async error: %r" % async_resp.error)
        print("Got value: %r" % (async_resp.value,))

    """

    def __init__(self, async_id, db):
        """Setup the consumer, listening for a specific async ID to appear in external DB.

        The DB is populated from the long polling thread.
        """
        self.async_id = async_id
        self.db = db

    @property
    def is_done(self):
        """Check if the DB has received an event with the specified async ID.

        :return: Whether the async request has finished or not
        :rtype: bool
        """
        return self.async_id in self.db

    @property
    def error(self):
        """Check if the async response is an error.

        Take care to call `is_done` before calling `error`. Note that the error
        messages are always encoded as strings.

        :raises CloudUnhandledError: When not checking `is_done` first
        :return: the error value/payload, if found.
        :rtype: str
        """
        if not self.is_done:
            raise CloudUnhandledError("Need to check if request is done, before checking for error")
        error_msg = self.db[self.async_id]["error"]
        resp_code = int(self.db[self.async_id]["status_code"])
        payload = self.db[self.async_id]["payload"]
        if resp_code != 200 and not error_msg and not payload:
            return "Async error (%s). Status code: %r" % (self.async_id, resp_code)
        return error_msg

    @property
    def value(self):
        """Get the value of the finished async request.

        Take care to ensure the async request is indeed done, by checking both `is_done`
        and `error` before calling `value`.

        :raises CloudUnhandledError: When not checking value of `error` or `is_done` first
        :return: the payload value
        :rtype: str
        """
        if not self.is_done:
            raise CloudUnhandledError("Need to check if request is done, before getting value")
        if self.error:
            raise CloudUnhandledError("Async request returned an error. Need to check for errors,"
                                      "before getting value.\nError: %s" % self.error)

        # Return the payload
        return self.db[self.async_id]["payload"]

    def to_dict(self):
        """JSON serializable representation of the consumer."""
        return str(self)

    def __repr__(self):
        """String representation of this AsyncConsumer."""
        return self.async_id


class _LongPollingThread(threading.Thread):
    def __init__(self, db, queues, b64decode=True, mds=None):
        super(_LongPollingThread, self).__init__()

        self.db = db
        self.queues = queues
        self.mds = mds

        self._b64decode = b64decode
        self._stopped = False

    @catch_exceptions(MdsApiException)
    def run(self):
        while not self._stopped:
            api = self.mds.NotificationsApi()
            resp = api.v2_notification_pull_get()

            if resp.notifications:
                for n in resp.notifications:
                    # Ensure we have subscribed for the path we received a notification for
                    if n.ep not in self.queues and n.path not in self.queues[n.ep]:
                        LOG.warning(
                            "Ignoring notification on %s (%s) as no subscription is registered" %
                            (n.ep, n.path))

                    # Decode b64 encoded data
                    payload = base64.b64decode(n.payload) if self._b64decode else n.payload
                    self.queues[n.ep][n.path].put(payload)

            if resp.async_responses:
                for r in resp.async_responses:
                    # Check if we have a payload, and decode it if required
                    payload = r.payload if r.payload else None
                    should_b64 = self._b64decode and payload
                    payload = base64.b64decode(payload) if should_b64 else payload

                    self.db[r.id] = {
                        "payload": payload,
                        "error": r.error,
                        "status_code": r.status
                    }

    def stop(self):
        self._stopped = True


class ConnectedDevice(object):
    """Describes device object from the mDS."""

    def __init__(self, connected_device_obj):
        """Override __init__ and allow passing in backend object."""
        if not isinstance(connected_device_obj, dict):
            connected_device_obj = connected_device_obj.to_dict()
        for key, value in iteritems(ConnectedDevice._get_map_attributes()):
            setattr(self, "_%s" % key, connected_device_obj.get(value, None))

    @staticmethod
    def _get_map_attributes():
        return {
            'state': 'status',
            'queue_mode': 'q',
            'type': 'type',
            'id': 'name'
        }

    @property
    def state(self):
        """Get the state of this Endpoint.

        Possible values ACTIVE, STALE.

        :return: The state of this Endpoint.
        :rtype: str
        """
        return self._state

    @property
    def queue_mode(self):
        """Get the queue mode of this Endpoint.

        Determines whether the device is in queue mode.
        When an endpoint is in Queue mode,
        messages sent to the endpoint do not wake up the physical device.
        The messages are queued and delivered when the device
        wakes up and connects to mbed Cloud Connect itself.
        You can also use the Queue mode when the device
        is behind a NAT and cannot be reached directly by mbed Cloud Connect.

        :return: The queue_mode of this Endpoint.
        :rtype: bool
        """
        return self._queue_mode

    @property
    def type(self):
        """Get the type of this Endpoint.

        Type of endpoint. (Free text)

        :return: The type of this Endpoint.
        :rtype: str
        """
        return self._type

    @property
    def id(self):
        """Get the id of this Endpoint.

        Unique mbed Cloud Device ID representing the endpoint.

        :return: The id of this Endpoint.
        :rtype: str
        """
        return self._id

    def to_dict(self):
        """Return dictionary of object."""
        return {
            'id': self.id,
            'state': self.state,
            'queue_mode': self.queue_mode,
            'type': self.type
        }

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())


class Device(ClassAPI):
    """Describes device object from the catalog.

    :ivar account_id: The owning IAM account ID
    :vartype account_id: str
    :ivar auto_update: Mark this device for auto firmware update
    :vartype auto_update: bool
    :ivar bootstrapped_timestamp:
    :vartype bootstrapped_timestamp: datetime
    :ivar created_at: The time the device was created
    :vartype created_at: datetime
    :ivar custom_attributes: Up to 5 custom JSON attributes
    :vartype custom_attributes: object
    :ivar deployed_state: State of the device's deployment
    :vartype deployed_state: str
    :ivar last_deployment: The last deployment used on the device
    :vartype last_deployment: datetime
    :ivar description: The description of the device
    :vartype description: str
    :ivar device_class: Class of the device
    :vartype device_class: str
    :ivar id: The ID of the device
    :vartype id: str
    :ivar manifest_url: URL for the current device manifest
    :vartype manifest_url: str
    :ivar mechanism: The ID of the channel used to communicate with the device
    :vartype mechanism: str
    :ivar mechanism_url: The address of the connector to use
    :vartype mechanism_url: str
    :ivar name: The name of the device
    :vartype name: str
    :ivar serial_number: The serial number of the device
    :vartype serial_number: str
    :ivar state: The current state of the device
    :vartype state: str
    :ivar trust_class: The device trust class
    :vartype trust_class: int
    :ivar trust_level: The device trust level
    :vartype trust_level: int
    :ivar updated_at: The time the device was updated
    :vartype updated_at: datetime
    :ivar vendor_id: The device vendor ID
    :vartype vendor_id: str
    :ivar alias: The alias of the device
    :vartype alias: str
    :ivar bootstrap_certificate_expiration:
    :vartype bootstrap_certificate_expiration: datetime
    :ivar certificate_fingerprint: Fingerprint of the device certificate
    :vartype certificate_fingerprint: str
    :ivar certificate_issuer_id: ID of the issuer of the certificate
    :vartype certificate_issuer_id: str
    :ivar connector_certificate_expiration: Expiration date of the certificate
    used to connect to connector server
    :vartype connector_certificate_expiration: datetime
    :ivar device_execution_mode: The device class
    :vartype device_execution_mode: int
    :ivar firmware_checksum: The SHA256 checksum of the current firmware image
    :vartype firmware_checksum: str
    :ivar manifest_timestamp: The timestamp of the current manifest version
    :vartype manifest_timestamp: datetime
    """

    def __init__(self, obj=None):
        """Override __init__ and allow passing in backend object."""
        if obj is not None:
            if isinstance(obj, dict):
                for key, value in iteritems(self._get_map_attributes()):
                    setattr(self, key, obj.get(value, None))
            else:
                for key, value in iteritems(self._get_map_attributes()):
                    setattr(self, key, getattr(obj, value, None))

    def _get_map_attributes(self):
        return {
            "account_id": "account_id",
            "auto_update": "auto_update",
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


class Query(object):
    """Describes device query object."""

    def __init__(self, query_obj):
        """Override __init__ and allow passing in backend object."""
        if not isinstance(query_obj, dict):
            query_obj = query_obj.to_dict()
        for key, value in iteritems(Query._get_map_attributes()):
            setattr(self, "_%s" % key, query_obj.get(value, None))

    @staticmethod
    def _get_map_attributes():
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
        :rtype: str
        """
        return self._filter

    def to_dict(self):
        """Return dictionary of object."""
        return {
            "created_at": self.created_at,
            "description": self.description,
            "id": self.id,
            "name": self.name,
            "updated_at": self.updated_at,
            "filter": self.filter
        }

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())


class Webhook(object):
    """Describes webhook object."""

    def __init__(self, webhook_obj):
        """Override __init__ and allow passing in backend object."""
        if not isinstance(webhook_obj, dict):
            webhook_obj = webhook_obj.to_dict()
        for key, value in iteritems(Webhook._get_map_attributes()):
            setattr(self, "_%s" % key, webhook_obj.get(value, None))

    @staticmethod
    def _get_map_attributes():
        return {
            "url": "url",
            "headers": "headers",
        }

    @property
    def url(self):
        """Get the url of this Webhook.

        The URL to which the notifications are sent.
        We recommend that you serve this URL over HTTPS.

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._url

    @property
    def headers(self):
        """Get the headers of this Webhook.

        Headers (key/value) that are sent with the notification. Optional.

        :return: The headers of this Webhook.
        :rtype: object
        """
        return self._headers

    def to_dict(self):
        """Return dictionary of object."""
        return {
            'url': self.url,
            'headers': self.headers
        }

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())


class Resource(object):
    """Describes resource type from device.

    Example usage:

    .. code-block:: python

        >>> resources = api.list_resources(device_id)
        >>> for r in resources:
                print(r.uri, r.name, r.observable)
        /3/0/1,None,True
        /5/0/2,Update,False
        ...
    """

    def __init__(self, resource_obj):
        """Override __init__ and allow passing in backend object."""
        self._observable = resource_obj.obs
        self._path = resource_obj.uri
        self._type = resource_obj.rt
        self._content_type = resource_obj.type

    @property
    def observable(self):
        """Get the observability of this Resource.

        Whether the resource is observable or not (true/false)

        :return: The observability of this ResourcesData.
        :rtype: bool
        """
        return self._observable

    @property
    def path(self):
        """Get the URI of this Resource.

        :return: The URI of this Resource.
        :rtype: str
        """
        return self._path

    @property
    def type(self):
        """Get the type of this Resource, if set.

        :return: The type of the Resource.
        :rtype: str
        """
        return self._type

    @property
    def content_type(self):
        """The content type of this Resource, if set.

        :return: The content type of the Resource.
        :rtype: str
        """
        return self._content_type

    def to_dict(self):
        """Return dictionary of object."""
        return {
            'observable': self.observable,
            'path': self.path,
            'type': self.type,
            'content_type': self.content_type
        }

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())
