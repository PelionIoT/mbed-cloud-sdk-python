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
from six.moves import queue
import threading
import time
import urllib

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.exceptions import AsyncError
from mbed_cloud.exceptions import TimeoutError
from mbed_cloud.exceptions import UnhandledError
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.device_catalog as dc
from mbed_cloud._backends.device_catalog.models import \
    DeviceDetail as DeviceDetailBackend
from mbed_cloud._backends.device_catalog.rest import \
    ApiException as DeviceCatalogApiException
import mbed_cloud._backends.device_query_service as dc_queries
from mbed_cloud._backends.device_query_service.models import \
    DeviceQueryDetail
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
        - Create and manage device filters
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

    def start_long_polling(self):
        """Start the long-polling thread.

        If not an external callback is setup (using `add_webhook`) then
        calling this function is mandatory.

        .. code-block:: python

            >>> api.start_long_polling()
            >>> print(api.get_resource_value(endpoint, path))
            Some value
            >>> api.stop_long_polling()

        :returns: void
        """
        self._long_polling_thread.start()
        self._long_polling_is_active = True

    def stop_long_polling(self):
        """Stop the long-polling thread.

        :returns: void
        """
        self._long_polling_thread.stop()
        self._long_polling_is_active = False

    @catch_exceptions(MdsApiException)
    def list_connected_devices(self, **kwargs):
        """List all endpoints.

        :returns: a list of currently *connected* `DeviceDetail` objects
        :rtype: PaginatedResponse
        """
        api = self.mds.EndpointsApi()

        # We wrap each object into a Device catalog object. Doing so we rename
        # some keys and throw away some information.
        endpoints = api.v2_endpoints_get()
        devices = [DeviceDetail({'id': d.name}) for d in endpoints]

        # As this doesn't actually return a paginated response - we mock it.
        return PaginatedResponse(lambda: None, init_data=devices)

    @catch_exceptions(MdsApiException)
    def list_resources(self, device_id):
        """List all resources registered to a connected endpoint/device.

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
        return [Resource(r) for r in api.v2_endpoints_endpoint_name_get(device_id)]

    @catch_exceptions(MdsApiException)
    def get_resource_value(self, device_id, resource_path, fix_path=True, timeout=None):
        """Get a resource value for a given endpoint and resource path by blocking thread.

        Example usage:

        .. code-block:: python

            try:
                v = api.get_resource_value(device_id, path)
                print("Current value", v)
            except AsyncError, e:
                print("Error", e)

        :param str endpoint_name: The name/id of the endpoint
        :param str resource_path: The resource path to get
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :param timeout: Seconds to request value for before timeout. If not provided, the
            program might hang indefinitly.
        :raises: AsyncError, TimeoutError
        :returns: The resource value for the requested resource path
        :rtype: str
        """
        # Ensure we're long polling first
        if not self._long_polling_is_active:
            raise UnhandledError(
                "Long polling needs to be enabled before getting resource value synchronously.")

        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_get(device_id, resource_path)

        # The async consumer, which will read data from long-polling thread
        consumer = AsyncConsumer(resp.async_response_id, self._db)

        # We block the thread and get the value for the user.
        return self._get_value_synchronized(consumer, timeout)

    @catch_exceptions(MdsApiException)
    def get_resource_value_async(self, endpoint_name, resource_path, fix_path=True):
        """Get a resource value for a given endpoint and resource path.

        Will not block, but instead return an AsyncConsumer. Example usage:

        .. code-block:: python

            a = api.get_resource_value_async(endpoint, path)
            while not a.is_done:
                time.sleep(0.1)
            if a.error:
                print("Error", a.error)
            print("Current value", a.value)

        :param str endpoint_name: The name/id of the endpoint
        :param str resource_path: The resource path to get
        :param bool fix_path: strip leading / of path if present
        :returns: Consumer object to control asynchronous request
        :rtype: AsyncConsumer
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_get(endpoint_name, resource_path)

        # The async consumer, which will read data from long-polling thread
        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def set_resource_value(self, endpoint_name, resource_path,
                           resource_value=None, fix_path=True):
        """Set resource value for given resource path, on endpoint.

        Will block and wait for response to come through. Usage:

        .. code-block:: python

            try:
                v = api.set_resource_value(endpoint, path, value)
                print("Success, new value:", v)
            except AsyncError, e:
                print("Error", e)

        :param str endpoint_name: The name/id of the endpoint
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
            resp = api.v2_endpoints_endpoint_name_resource_path_put(endpoint_name,
                                                                    resource_path,
                                                                    resource_value)
        else:
            resp = api.v2_endpoints_endpoint_name_resource_path_post(endpoint_name,
                                                                     resource_path)
        consumer = AsyncConsumer(resp.async_response_id, self._db)
        return self._get_value_synchronized(consumer)

    @catch_exceptions(MdsApiException)
    def set_resource_value_async(self, endpoint_name, resource_path,
                                 resource_value=None, fix_path=True):
        """Set resource value for given resource path, on endpoint.

        Will not block. Returns immediatly. Usage:

        .. code-block:: python

            a = api.set_resource_value_async(endpoint, path, value)
            while not a.is_done:
                time.sleep(0.1)
            if a.error:
                print("Error", a.error)
            print("Success, new value:", a.value)

        :param str endpoint_name: The name/id of the endpoint
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
            resp = api.v2_endpoints_endpoint_name_resource_path_put(endpoint_name,
                                                                    resource_path,
                                                                    resource_value)
        else:
            resp = api.v2_endpoints_endpoint_name_resource_path_post(endpoint_name,
                                                                     resource_path)

        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def add_subscription(self, endpoint_name, resource_path, fix_path=True, queue_size=5):
        """Subscribe to resource updates.

        When called on valid endpoint and resource path a subscription is setup so that
        any update on the resource path value triggers a new element on the FIFO queue.
        The returned object is a native Python Queue object.

        :param endpoint_name: Name of endpoint to subscribe on
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
        self._queues[endpoint_name][resource_path] = q

        # Send subscription request
        api = self.mds.SubscriptionsApi()
        api.v2_subscriptions_endpoint_name_resource_path_put(endpoint_name, fixed_path)

        # Return the Queue object to the user
        return q

    @catch_exceptions(MdsApiException)
    def add_subscription_with_callback(self, endpoint_name, resource_path, callback_fn,
                                       fix_path=True, queue_size=5):
        """Subscribe to resource updates with callback function.

        When called on valid endpoint and resource path a subscription is setup so that
        any update on the resource path value triggers an update on the callback function.

        :param endpoint_name: Name of endpoint to subscribe on
        :param resource_path: The resource path on device to observe
        :param callback_fn: Callback function to be executed on update to subscribed resource
        :param fix_path: Removes leading / on resource_path if found
        :param queue_size: set the Queue size. If set to 0, no queue object will be created
        :returns: void
        """
        queue = self.add_subscription(endpoint_name, resource_path, fix_path, queue_size)

        # Setup daemon thread for callback function
        t = threading.Thread(target=self._subscription_handler, args=[queue, callback_fn])
        t.daemon = True
        t.start()

    @catch_exceptions(MdsApiException)
    def add_pre_subscription(self, endpoint_name, resource_path, endpoint_type=""):
        """Create pre-subscription for endpoint and resource path.

        :returns: void
        """
        api = self.mds.SubscriptionsApi()

        presubscription = self.mds.Presubscription(
            endpoint_name=endpoint_name,
            endpoint_type=endpoint_type,
            _resource_path=[resource_path]
        )
        api.v2_subscriptions_put([presubscription])

        # Returns void
        return

    @catch_exceptions(MdsApiException)
    def delete_subscription(self, endpoint_name=None, resource_path=None, fix_path=True):
        """Unsubscribe from endpoint and/or resource_path updates.

        If endpoint_name or resource_path is None, we remove every subscripton
        for them. I.e. calling this method without arguments removes all subscriptions,
        but calling it with only endpoint_name removes subscriptions for all resources
        on the given endpoint.

        :param endpoint_name: endpoint to unsubscribe events from. If not
            provided, all registered endpoints will be unsubscribed.
        :param resource_path: resource_path to unsubscribe events from. If not
            provided, all resource paths will be unsubscribed.
        :param fix_path: remove trailing / in resouce path to ensure API works.
        :return: void
        """
        endpoints = filter(None, [endpoint_name])
        if not endpoint_name:
            endpoints = self._queues.keys()
        resource_paths = [resource_path]
        if not resource_path:
            resource_paths = []
            for e in endpoints:
                resource_paths.extend(self._queues[e].keys())

        # Delete the subscriptions
        api = self.mds.SubscriptionsApi()
        for e in endpoints:
            for r in resource_paths:
                # Fix the path, if required.
                fixed_path = r
                if fix_path and r.startswith("/"):
                    fixed_path = r[1:]

                # Make request to API, ignoring result
                api.v2_subscriptions_endpoint_name_resource_path_delete(endpoint_name, fixed_path)

                # Remove Queue from dictionary
                del self._queues[e][r]
        return

    @catch_exceptions(MdsApiException)
    def add_webhook(self, url, headers={}):
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
        :returns: a list of :py:class:`DeviceDetail` objects registered in the catalog.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        api = self.dc.DefaultApi()
        return PaginatedResponse(api.device_list, lwrap_type=DeviceDetail, **kwargs)

    @catch_exceptions(DeviceCatalogApiException)
    def get_device(self, device_id):
        """Get device details from catalog.

        :param device_id: the ID of the device to retrieve (str)
        :returns: device object matching the `device_id`.
        :rtype: DeviceDetail
        """
        api = self.dc.DefaultApi()
        return DeviceDetail(api.device_retrieve(device_id))

    @catch_exceptions(DeviceCatalogApiException)
    def update_device(self, device_id, **kwargs):
        """Update existing device in catalog.

        .. code-block:: python

            existing_device = api.get_device(...)
            updated_device = api.update_device(
                existing_device.id,
                provision_key = "something new"
            )

        :param str mechanism: The ID of the channel used to communicate with the device (str)
        :param str provision_key: The key used to provision the device (str)
        :param str account_id: Owning IAM account ID
        :param bool auto_update: Mark this device for auto firmware update
        :param str custom_attributes: Up to 5 JSON attributes (json encoded)
        :param str description: Description of the device
        :param str device_class: Class of the device
        :param str manifest: URL for the current device manifest
        :param str mechanism_url: Address of the connector to use
        :param str name: Name of the device
        :param int trust_class: Trust class of device
        :param int trust_level: Trust level of device
        :param int vendor_id: Device vendor ID
        :returns: the updated device object
        :rtype: DeviceDetail
        """
        api = self.dc.DefaultApi()
        body = self.dc.DeviceUpdateDetail(**kwargs)
        return DeviceDetail(api.device_update(device_id, body))

    @catch_exceptions(DeviceCatalogApiException)
    def add_device(self, mechanism, provision_key, **kwargs):
        """Add a new device to catalog.

        .. code-block:: python

            device = {
                "mechanism": "connector",
                "provision_key": "unique key",
                "name": "New device name",
                "auto_update": True,
                "vendor_id": "<id>"
            }
            resp = api.add_device(**device)
            print(resp.created_at)

        :param str mechanism: The ID of the channel used to communicate with the device
        :param str provision_key: The key used to provision the device
        :param str account_id: Owning IAM account ID
        :param bool auto_update: Mark this device for auto firmware update
        :param str created_at: When the device was created (ISO-8601)
        :param str custom_attributes: Up to 5 JSON attributes (json encoded)
        :param str deployed_state: State of the device's deployment
        :param str deployment: Last deployment used on the device
        :param str description: Description of the device
        :param str device_class: Class of the device
        :param str id: ID of the device
        :param str manifest: URL for the current device manifest
        :param str mechanism_url: Address of the connector to use
        :param str name: Name of the device
        :param str serial_number: Serial number of device
        :param str state: Current state of device
        :param int trust_class: Trust class of device
        :param int trust_level: Trust level of device
        :param int updated_at: Time the device was updated
        :param int vendor_id: Device vendor ID
        :return: the newly created device object.
        :rtype: DeviceDetail
        """
        api = self.dc.DefaultApi()
        return DeviceDetail(
            api.device_create(mechanism=mechanism, provision_key=provision_key, **kwargs)
        )

    @catch_exceptions(DeviceCatalogApiException)
    def delete_device(self, device_id):
        """Delete device from catalog.

        :param str device_id: ID of device in catalog to delete
        :return: void
        """
        api = self.dc.DefaultApi()
        return api.device_destroy(device_id)

    @catch_exceptions(DeviceQueryServiceApiException)
    def list_filters(self, **kwargs):
        """List filters in device query service.

        :param int limit: (Optional) The number of devices to retrieve.
        :param str order: (Optional) The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: (Optional) Get devices after/starting at given `device_id`
        :returns: a list of :py:class:`Filter` objects.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.dc_queries.DefaultApi()

        return PaginatedResponse(api.device_query_list, lwrap_type=Filter, **kwargs)

    @catch_exceptions(DeviceQueryServiceApiException)
    def add_filter(self, name, query, custom_attributes=None, **kwargs):
        """Add a new filter to device query service.

        .. code-block:: python

            f = api.add_filter(
                name = "Filter name",
                query = {},
                custom_attributes = {
                    "foo": "bar"
                }
            )
            print(f.created_at)

        :param str name: Name of filter
        :param dict query: Filter properties to apply
        :param dict custom_attributes: Extra filter attributes
        :param return: the newly created filter object.
        :return: the newly created filter object
        :rtype: Filter
        """
        api = self.dc_queries.DefaultApi()

        # Ensure we have the correct types and get the new query object based on
        # passed in query object and custom attributes.
        query = self._get_filter_attributes(query, custom_attributes)

        return Filter(api.device_query_create(name=name, query=query, **kwargs))

    @catch_exceptions(DeviceQueryServiceApiException)
    def update_filter(self, filter_id, name, query, custom_attributes=None, **kwargs):
        """Update existing filter in device query service.

        .. code-block:: python

            f = api.get_filter(...)
            new_custom_attributes = {
                "foo": "bar"
            }
            new_f = api.update_filter(
                filter_id = f.id,
                name = "new name",
                query = f.query,
                custom_attributes = new_custom_attributes
            )

        :param str filter_id: Existing filter ID to update
        :param str name: (New) name of filter
        :param dict query: (New) filter properties to apply
        :param dict custom_attributes: (New) extra filter attributes
        :param return: the newly updated filter object.
        :rtype: Filter
        """
        api = self.dc_queries.DefaultApi()

        # Get urlencoded query attribute
        query = self._get_filter_attributes(query, custom_attributes)

        body = self.dc_queries.Body(
            name=name,
            query=query,
            **kwargs
        )

        return Filter(api.device_query_update(filter_id, body))

    @catch_exceptions(DeviceQueryServiceApiException)
    def delete_filter(self, filter_id):
        """Delete filter in device query service.

        :param int filter_id: id of the filter to delete
        :param return: void
        """
        api = self.dc_queries.DefaultApi()
        api.device_query_destroy(filter_id)
        return

    @catch_exceptions(DeviceQueryServiceApiException)
    def get_filter(self, filter_id):
        """Get filter in device query service.

        :param int filter_id: id of the filter to get
        :returns: device filter object
        :rtype: Filter
        """
        api = self.dc_queries.DefaultApi()
        return Filter(api.device_query_retrieve(filter_id))

    def _subscription_handler(self, queue, callback_fn):
        while True:
            value = queue.get()
            callback_fn(value)

    def _get_filter_attributes(self, query, custom_attributes):
        # Ensure the query is of dict type
        if query and not isinstance(query, dict):
            raise ValueError("'query' parameter needs to be of type dict")

        # Add custom attributes, if provided
        if custom_attributes:
            if not isinstance(custom_attributes, dict):
                raise ValueError("Custom attributes when creating filter needs to be dict object")
            for k, v in custom_attributes.iteritems():
                if not k:
                    LOG.warning("Ignoring custom attribute with value %r as key is empty" % (v,))
                    continue
                query['custom_attributes__' + k] = v

        # Ensure query is valid
        if not query.keys():
            raise ValueError("'query' parameter not valid, needs to contain query keys")

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
                raise TimeoutError("Timeout getting async value. Timeout: %d seconds" % (timeout,))
            time.sleep(0.1)

        # If we get an error we throw an exception to the user, which can then be handled
        # accordingly.
        if consumer.error:
            raise AsyncError(consumer.error)

        return consumer.value


class AsyncConsumer(object):
    """Consumer object for reading values from a long-polling thread.

    Example usage:

    .. code-block:: python

        async_resp = api.get_resource_value(endpoint, resource)
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

        :raises UnhandledError: When not checking `is_done` first
        :return: the error value/payload, if found.
        :rtype: str
        """
        if not self.is_done:
            raise UnhandledError("Need to check if request is done, before checking for error")
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

        :raises UnhandledError: When not checking value of `error` or `is_done` first
        :return: the payload value
        :rtype: str
        """
        if not self.is_done:
            raise UnhandledError("Need to check if request is done, before getting value")
        if self.error:
            raise UnhandledError("Async request returned an error. Need to check for errors,"
                                 "before getting value.\nError: %s" % self.error)

        # Return the payload
        return self.db[self.async_id]["payload"]


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


class DeviceDetail(DeviceDetailBackend):
    """Describes device object from the catalog."""

    def __init__(self, device_obj):
        """Override __init__ and allow passing in backend object."""
        # Check type of device_obj to find params. If dict we use that, if class we ensure it has
        # the required `to_dict` function - and use that to get a dict.
        params = device_obj
        if not isinstance(device_obj, dict) and callable(getattr(device_obj, "to_dict", None)):
            params = device_obj.to_dict()
        super(DeviceDetail, self).__init__(**params)


class Filter(DeviceQueryDetail):
    """Describes device query object / filter."""

    def __init__(self, device_query_obj):
        """Override __init__ and allow passing in backend object."""
        super(Filter, self).__init__(**device_query_obj.to_dict())


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
        self._uri = resource_obj.uri
        self._name = resource_obj.rt

    @property
    def observable(self):
        """Get the observability of this Resource.

        Whether the resource is observable or not (true/false)

        :return: The observability of this ResourcesData.
        :rtype: bool
        """
        return self._observable

    @property
    def uri(self):
        """Get the URI of this Resource.

        :return: The URI of this Resource.
        :rtype: str
        """
        return self._uri

    @property
    def name(self):
        """Get the friendly name of this Resource, if set.

        :return: The name of the Resource.
        :rtype: str
        """
        return self._name

    def to_dict(self):
        """Return dictionary of object."""
        return {
            'observable': self.observable,
            'uri': self.uri,
            'name': self.name
        }

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())
