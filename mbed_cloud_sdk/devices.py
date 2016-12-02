"""Public API for Device API."""
from __future__ import absolute_import
import base64
from collections import defaultdict
import logging
import Queue
import threading
import time

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI
from mbed_cloud_sdk import config
from mbed_cloud_sdk.decorators import catch_exceptions
from mbed_cloud_sdk.exceptions import AsyncError
from mbed_cloud_sdk.exceptions import UnhandledError

# Import backend API
import mbed_cloud_sdk._backends.device_catalog as dc
from mbed_cloud_sdk._backends.device_catalog.rest import ApiException as DeviceCatalogApiException
import mbed_cloud_sdk._backends.mds as mds
from mbed_cloud_sdk._backends.mds.rest import ApiException as MdsApiException

LOG = logging.getLogger(__name__)


class DeviceAPI(BaseAPI):
    """Describing the public device API.

    Exposing functionality from the following underlying services:
        - Connector / mDS
        - Device query service
        - Device catlog
    """

    def __init__(self, params={}, b64decode=True):
        """Setup the backend APIs with provided config.

        In addition we need to setup some special handling of background
        threads for the mDS functionality - as it relies on background polling.
        """
        super(DeviceAPI, self).__init__(params)

        # Set the api_key for the requests
        mds.configuration.api_key['Authorization'] = config.get("api_key")
        dc.configuration.api_key['Authorization'] = config.get("api_key")
        mds.configuration.api_key_prefix['Authorization'] = 'Bearer'
        dc.configuration.api_key_prefix['Authorization'] = 'Bearer'

        # Override host, if defined
        if config.get("host"):
            mds.configuration.host = config.get("host")
            dc.configuration.host = config.get("host")

        self._db = {}
        self._queues = defaultdict(lambda: defaultdict(Queue.Queue))

        self._long_polling_thread = _LongPollingThread(self._db, self._queues, b64decode=b64decode)
        self._long_polling_thread.daemon = True

    def start_long_polling(self):
        """Start the long-polling thread.

        If not an external callback is setup (using `register_webhook`) then
        calling this function is mandatory.
        """
        self._long_polling_thread.start()

    def stop_long_polling(self):
        """Stop the long-polling thread."""
        self._long_polling_thread.start()

    @catch_exceptions(MdsApiException)
    def list_endpoints(self, start=0, sort_by=None, sort_direction="asc"):
        """List all endpoints.

        :param start: Not yet implemented.
        :param sort_by: Not yet implemented.
        :param sort_direction: Not yet implemented.
        :returns: a list of device objects registered in the catalog.
        """
        if start != 0 or sort_by is not None or sort_direction != "asc":
            raise NotImplementedError("Sorting and pagination is not yet implemented")

        api = mds.EndpointsApi()
        return api.v2_endpoints_get()

    @catch_exceptions(MdsApiException)
    def list_resources(self, endpoint_name):
        """List all resources registered to a connected endpoint/device."""
        api = mds.EndpointsApi()
        return api.v2_endpoints_endpoint_name_get(endpoint_name)

    @catch_exceptions(MdsApiException)
    def get_resource_value(self, endpoint_name, resource_path, fix_path=True, sync=False):
        """Get a resource value for a given endpoint and resource path.

        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :param sync: if True then the function will not return an async consumer, but instead
            block the thread until the async request is done.
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_get(endpoint_name, resource_path)

        # The async consumer, which will read data from long-polling thread
        consumer = AsyncConsumer(resp.async_response_id, self._db)

        # If, by default, the user has not requested a synchronized request we return
        # the async object - which allows the user to control how and when to read the
        # value. If not we block the thread and get the value for the user.
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    @catch_exceptions(MdsApiException)
    def set_resource_value(self, endpoint_name, resource_path,
                           resource_value, fix_path=True, sync=True):
        """Set resource value for given resource path, on endpoint."""
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_put(endpoint_name,
                                                                resource_path,
                                                                resource_value)

        consumer = AsyncConsumer(resp.async_response_id, self._db)
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    @catch_exceptions(MdsApiException)
    def subscribe(self, endpoint_name, resource_path, fix_path=True, queue_size=5):
        """Subscribe to resource updates.

        When called on valid endpoint and resource path a subscription is setup so that
        any update on the resource path value triggers a new element on the FIFO queue.
        The returned object is a native Python Queue object.

        :param fix_path: Removes leading / on resource_path if found.
        :param queue_size: set the Queue size. If set to 0, no queue object will be created.
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        # Keep the original path around however, as we use that for queue registration.
        fixed_path = resource_path
        if fix_path and resource_path.startswith("/"):
            fixed_path = resource_path[1:]

        # Create the queue and register it with the dict holding all queues
        q = Queue.Queue(queue_size) if queue_size > 0 else None
        self._queues[endpoint_name][resource_path] = q

        # Send subscription request
        api = mds.SubscriptionsApi()
        api.v2_subscriptions_endpoint_name_resource_path_put(endpoint_name, fixed_path)

        # Return the Queue object to the user
        return q

    @catch_exceptions(MdsApiException)
    def pre_subscribe(self, endpoint_name, resource_path, endpoint_type=""):
        """Create pre-subscription for endpoint and resource path."""
        api = mds.SubscriptionsApi()

        presubscription = mds.Presubscription(
            endpoint_name=endpoint_name,
            endpoint_type=endpoint_type,
            _resource_path=[resource_path]
        )
        api.v2_subscriptions_put([presubscription])

        # Returns void
        return

    @catch_exceptions(MdsApiException)
    def unsubscribe(self, endpoint_name=None, resource_path=None, fix_path=True):
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
        self._clear_subscriptions()

        api = mds.SubscriptionsApi()
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
    def register_webhook(self, url, headers={}):
        """Register new webhook for incoming subscriptions.

        If a webhook is already set, this will do an overwrite.

        :param url: the URL with listening webhook (str)
        :return: void
        """
        api = mds.NotificationsApi()

        # Send the request to register the webhook
        webhook_obj = mds.Webhook(url=url, headers=headers)
        api.v2_notification_callback_put(webhook_obj)
        return

    @catch_exceptions(MdsApiException)
    def deregister_webhook(self):
        """Delete/remove registered webhook.

        If no webhook is registered, an exception (404) will be raised.

        Note that every registered subscription will be deleted as part of
        deregistering a webhook.

        :return: void
        """
        api = mds.DefaultApi()
        api.v2_notification_callback_delete()

        # Every subscription will be deleted, so we can clear the queues too.
        self._queues.clear()

        return

    @catch_exceptions(MdsApiException)
    def execute(self, endpoint_name, resource_path, fix_path=True, sync=True, **kwargs):
        """Execute the callback function associated with a resource.

        :param endpoint_name: the endpoint/device to execute on.
        :param resource_path: resource URL on endpoint.
        :param fix_path: ensure leading / is stripped from path to comply with backend API.
        :param sync: run in (blocking) synchronized mode. If false,
            it returns a ::class:`AsyncConsumer`
        :param resource_function: (Optional) Most of the time resources do not
            accept a function but they have their own functions predefined. You can
            use this to trigger them.

        :return: an ::class:`AsyncConsumer` if not `sync` is set to True, in
            which case it returns the value as a string.
        """
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_post(
            endpoint_name,
            resource_path,
            **kwargs
        )

        consumer = AsyncConsumer(resp.async_response_id, self._db)
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    def is_active(self, endpoint_name):
        """Check if endpoint/device has active status."""
        endpoints = self.list_endpoints()
        # Create map by endpoint name, and check if requested endpoint is in it and status is ACTIVE
        active_endpoints = dict((e.name, True) for e in endpoints if e.status == "ACTIVE")
        return active_endpoints.get(endpoint_name, False)

    @catch_exceptions(DeviceCatalogApiException)
    def list_devices(self, **kwargs):
        """List devices in the device catalog.

        :param limit: (Optional) The number of devices to retrieve. (int)
        :param order: (Optional) The ordering direction, ascending (asc) or
            descending (desc) (str)
        :param after: (Optional) Get devices after/starting at given `device_id` (str)
        :param filters: (Optional) Dictionary of filters to apply.
        :returns: a list of device objects registered in the catalog.
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        api = dc.DefaultApi()
        return api.device_list(**kwargs).data

    @catch_exceptions(DeviceCatalogApiException)
    def get_device(self, device_id):
        """Get device details from catalog.

        :param device_id: the ID of the device to retrieve (str)
        :returns: device object matching the `device_id`.
        """
        api = dc.DefaultApi()
        return api.device_retrieve(device_id)

    @catch_exceptions(DeviceCatalogApiException)
    def create_device(self, mechanism, provision_key, **kwargs):
        """Create new device in catalog.

        :param mechanism: The ID of the channel used to communicate with the device (str)
        :param provision_key: The key used to provision the device (str)

        :param account_id: Owning IAM account ID (str)
        :param auto_update: Mark this device for auto firmware update (bool)
        :param created_at: When the device was created (str, ISO-8601)
        :param custom_attributes: Up to 5 JSON attributes (str, json encoded)
        :param deployed_state: State of the device's deployment (str)
        :param deployment: Last deployment used on the device (str)
        :param description: Description of the device (str)
        :param device_class: Class of the device (str)
        :param etag: Entity instance signature (str)
        :param id: ID of the device (str)
        :param manifest: URL for the current device manifest (str)
        :param mechanism_url: Address of the connector to use (str)
        :param name: Name of the device (str)
        :param object: API resource entity (str)
        :param serial_number: Serial number of device (str)
        :param state: Current state of device (str)
        :param trust_class: Trust class of device (int)
        :param trust_level: Trust level of device (int)
        :param updated_at: Time the device was updated (int)
        :param vendor_id: Device vendor ID (int)

        :return: the newly created device object.
        """
        api = dc.DefaultApi()
        return api.device_create(mechanism=mechanism, provision_key=provision_key, **kwargs)

    @catch_exceptions(DeviceCatalogApiException)
    def delete_device(self, device_id):
        """Delete device from catalog.

        :param device_id: ID of device in catalog to delete (str)
        :return: void
        """
        api = dc.DefaultApi()
        return api.device_destroy(device_id)

    def _get_value_synchronized(self, consumer):
        # We return synchronously, so we block in a busy loop waiting for the
        # request to be done.
        while not consumer.is_done():
            time.sleep(0.1)

        # If we get an error we throw an exception to the user, which can then be handled
        # accordingly.
        if consumer.error():
            raise AsyncError(consumer.error())

        return consumer.get_value()


class AsyncConsumer(object):
    """Consumer object for reading values from a long-polling thread."""

    def __init__(self, async_id, db):
        """Setup the consumer, listening for a specific async ID to appear in external DB.

        The DB is populated from the long polling thread.
        """
        self.async_id = async_id
        self.db = db

    def is_done(self):
        """Check if the DB has received an event with the specified async ID."""
        return self.async_id in self.db

    def error(self):
        """Check if the async response is an error.

        Take care to call `is_done()` before calling `error()`. Note that the error
        messages are always encoded as strings.

        :return: the error string.
        """
        if not self.is_done():
            raise UnhandledError("Need to check if request is done, before checking for error")
        return self.db[self.async_id]["error"]

    def get_value(self):
        """Get the value of the finished async request.

        Take care to ensure the async request is indeed done, by checking both `is_done()`
        and `error()` before calling `get_value()`.

        :return: the payload string.
        """
        if not self.is_done():
            raise UnhandledError("Need to check if request is done, before getting value")
        if self.error():
            raise UnhandledError("Async request returned an error. Need to check for errors,"
                                 "before getting value.\nError: %s" % self.error())

        # Return the payload
        return self.db[self.async_id]["payload"]


class _LongPollingThread(threading.Thread):
    def __init__(self, db, queues, b64decode=True):
        super(_LongPollingThread, self).__init__()

        self.db = db
        self.queues = queues

        self._b64decode = b64decode
        self._stopped = False

    @catch_exceptions(MdsApiException)
    def run(self):
        while not self._stopped:
            api = mds.NotificationsApi()
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
