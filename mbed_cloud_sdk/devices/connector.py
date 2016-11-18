import threading, Queue, time, base64, logging
from collections import defaultdict

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI, config
from mbed_cloud_sdk.exceptions import AsyncError, UnhandledError, CloudApiException
from mbed_cloud_sdk.decorators import catch_exceptions

# Import backend API
import mbed_cloud_sdk.devices.mds as mds
from mbed_cloud_sdk.devices.mds.rest import ApiException

logger = logging.getLogger(__name__)

class ConnectorAPI(BaseAPI):
    def __init__(self, b64decode = True):
        # Set the api_key for the requests
        mds.configuration.api_key['Authorization'] = config.get("api_key")
        mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

        self._db = {}
        self._queues = defaultdict(lambda: defaultdict(Queue.Queue))

        self._long_polling_thread = _LongPollingThread(self._db, self._queues, b64decode = b64decode)
        self._long_polling_thread.daemon = True

    def start_long_polling(self):
        self._long_polling_thread.start()

    def stop_long_polling(self):
        self._long_polling_thread.start()

    @catch_exceptions(ApiException)
    def list_endpoints(self):
        api = mds.EndpointsApi()
        return api.v2_endpoints_get()

    @catch_exceptions(ApiException)
    def list_resources(self, endpoint_name):
        api = mds.EndpointsApi()
        return api.v2_endpoints_endpoint_name_get(endpoint_name)

    @catch_exceptions(ApiException)
    def get_resource_value(self, endpoint_name, resource_path, fix_path = True, sync = False):
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
    def set_resource_value(self, endpoint_name, resource_path, resource_value, fix_path = True, sync = True):
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_put(endpoint_name, resource_path, resource_value)

        consumer = _AsyncConsumer(resp.async_response_id, self._db)
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    @catch_exceptions(ApiException)
    def subscribe(self, endpoint_name, resource_path, fix_path = True, queue_size = 5):
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
    def pre_subscribe(self, endpoint_name, resource_path, endpoint_type = ""):
        api = mds.SubscriptionsApi()

        presubscription = mds.Presubscription(
            endpoint_name = endpoint_name,
            endpoint_type = endpoint_type,
            _resource_path = [resource_path]
        )
        api.v2_subscriptions_put([presubscription])

        # Returns void
        return

    @catch_exceptions(ApiException)
    def unsubscribe(self, endpoint_name = None, resource_path = None, fix_path = True):
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
    def register_webhook(url, headers = {}):
        api = mds.NotificationsApi()

        webhook_obj = mds.Webhook()
        webhook_obj.url = url
        webhook_obj.headers = headers

        # Send the request to register the webhook
        api.v2_notification_callback_put(webhook_obj)

        # Returns void
        return

    @catch_exceptions(ApiException)
    def execute(self, endpoint_name, resource_path, fix_path = True, sync = True, **kwargs):
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

    def get_value(self, b64_decode = True):
        if not self.is_done():
            raise UnhandledError("Need to check if request is done, before getting value")
        if self.error():
            raise UnhandledError("Async request returned an error. Need to check for errors,"
                                 "before getting value.\nError: %s" % self.error())

        # Return the payload
        return self.db[self.async_id]["payload"]

class _LongPollingThread(threading.Thread):
    def __init__(self, db, queues, b64decode = True):
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
                        logger.warning("Ignoring notification on %s (%s) as no subscription is registered" % (n.ep, n.path))

                    # Decode b64 encoded data
                    payload = base64.b64decode(n.payload) if self._b64decode else payload
                    self.queues[n.ep][n.path].put(payload)

            if resp.async_responses:
                for r in resp.async_responses:
                    # Check if we have a payload, and decode it if required
                    payload = r.payload if r.payload else None
                    payload = base64.b64decode(payload) if (self._b64decode and payload) else payload

                    self.db[r.id] = {
                        "payload": payload,
                        "error": r.error,
                        "status_code": r.status
                    }

    def stop(self):
        self._stopped = True
