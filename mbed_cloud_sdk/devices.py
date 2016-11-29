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
import mbed_cloud_sdk._backends.mds as mds
from mbed_cloud_sdk._backends.mds.rest import ApiException

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

    @catch_exceptions(ApiException)
    def list_endpoints(self):
        """List all endpoints/devices."""
        api = mds.EndpointsApi()
        return api.v2_endpoints_get()

    @catch_exceptions(ApiException)
    def list_resources(self, endpoint_name):
        """List all resources registered to a connected endpoint/device."""
        api = mds.EndpointsApi()
        return api.v2_endpoints_endpoint_name_get(endpoint_name)

    @catch_exceptions(ApiException)
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
        consumer = _AsyncConsumer(resp.async_response_id, self._db)

        # If, by default, the user has not requested a synchronized request we return
        # the async object - which allows the user to control how and when to read the
        # value. If not we block the thread and get the value for the user.
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    @catch_exceptions(ApiException)
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

        consumer = _AsyncConsumer(resp.async_response_id, self._db)
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    @catch_exceptions(ApiException)
    def subscribe(self, endpoint_name, resource_path, fix_path=True, queue_size=5):
        """Subscribe to resource updates.

        When called on valid endpoint and resource path a subscription is setup so that
        any update on the resource path value triggers a new element on the FIFO queue.
        The returned object is a native Python Queue object.

        :param fix_path: Removes leading / on resource_path if found.
        :param queue_size: set the Queue size.
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        # Keep the original path around however, as we use that for queue registration.
        fixed_path = resource_path
        if fix_path and resource_path.startswith("/"):
            fixed_path = resource_path[1:]

        # Create the queue and register it with the dict holding all queues
        q = Queue.Queue(queue_size)
        self._queues[endpoint_name][resource_path] = q

        # Send subscription request
        api = mds.SubscriptionsApi()
        api.v2_subscriptions_endpoint_name_resource_path_put(endpoint_name, fixed_path)

        # Return the Queue object to the user
        return q

    @catch_exceptions(ApiException)
    def pre_subscribe(self, endpoint_name, resource_path, endpoint_type=""):
        """TODO: Write docstring."""
        api = mds.SubscriptionsApi()

        presubscription = mds.Presubscription(
            endpoint_name=endpoint_name,
            endpoint_type=endpoint_type,
            _resource_path=[resource_path]
        )
        api.v2_subscriptions_put([presubscription])

        # Returns void
        return

    @catch_exceptions(ApiException)
    def unsubscribe(self, endpoint_name=None, resource_path=None, fix_path=True):
        """TODO: Write docstring."""
        # If endpoint_name or resource_path is None, we remove every subscripton
        # for them. I.e. calling this method without arguments removes all subscriptions,
        # but calling it with only endpoint_name removes subscriptions for all resources
        # on the given endpoint.
        endpoints = filter(None, [endpoint_name])
        if not endpoint_name:
            endpoints = self._queues.keys()
        resource_paths = [resource_path]
        if not resource_path:
            resource_paths = []
            for e in endpoints:
                resource_paths.extend(self._queues[e].keys())

        # Delete the subscriptions
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

    @catch_exceptions(ApiException)
    def register_webhook(url, headers={}):
        """TODO: Write docstring."""
        api = mds.NotificationsApi()

        webhook_obj = mds.Webhook()
        webhook_obj.url = url
        webhook_obj.headers = headers

        # Send the request to register the webhook
        api.v2_notification_callback_put(webhook_obj)

        # Returns void
        return

    @catch_exceptions(ApiException)
    def execute(self, endpoint_name, resource_path, fix_path=True, sync=True, **kwargs):
        """TODO: Write docstring."""
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_post(
            endpoint_name,
            resource_path,
            **kwargs
        )

        consumer = _AsyncConsumer(resp.async_response_id, self._db)
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    def is_active(self, endpoint_name):
        """TODO: Write docstring."""
        endpoints = self.list_endpoints()
        # Create map by endpoint name, and check if requested endpoint is in it and status is ACTIVE
        active_endpoints = dict((e.name, True) for e in endpoints if e.status == "ACTIVE")
        return active_endpoints.get(endpoint_name, False)

    @catch_exceptions(ApiException)
    def list_devices(self):
        """TODO: Write docstring."""
        api = dc.DefaultApi()
        return api.device_list()

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


class _AsyncConsumer(object):
    def __init__(self, async_id, db):
        self.async_id = async_id
        self.db = db

    def is_done(self):
        return self.async_id in self.db

    def error(self):
        if not self.is_done():
            raise UnhandledError("Need to check if request is done, before checking for error")
        return self.db[self.async_id]["error"]

    def get_value(self, b64_decode=True):
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

    @catch_exceptions(ApiException)
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
