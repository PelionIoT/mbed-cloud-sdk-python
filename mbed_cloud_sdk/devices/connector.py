import threading, Queue, time, base64, logging
from collections import defaultdict

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI, config
from mbed_cloud_sdk.exceptions import AsyncError, UnhandledError, CloudApiException

# Import backend API
import mbed_cloud_sdk.devices.mds
from mbed_cloud_sdk.devices.mds.rest import ApiException

logger = logging.getLogger(__name__)

class ConnectorAPI(BaseAPI):
    def __init__(self):
        # Set the api_key for the requests
        mds.configuration.api_key['Authorization'] = config.get("api_key")
        mds.configuration.api_key_prefix['Authorization'] = 'Bearer'

        self._db = {}
        self._queues = defaultdict(lambda: defaultdict(Queue.Queue))

        self._long_polling_thread = _LongPollingThread(self._db)
        self._long_polling_thread.daemon = True

    def start_long_polling(self):
        self._long_polling_thread.start()

    def stop_long_polling(self):
        self._long_polling_thread.start()

    @error_handler(exceptions = [ApiException])
    def get_endpoints(self):
        api = mds.EndpointsApi()
        return api.v2_endpoints_get()

    @error_handler(exceptions = [ApiException])
    def get_endpoint(self, endpoint_name):
        api = mds.EndpointsApi()
        return api.v2_endpoints_endpoint_name_get(endpoint_name)

    @error_handler(exceptions = [ApiException])
    def get_resource(self, endpoint_name, resource_path, fix_path = True, sync = False):
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            path = path[1:]

        # The async consumer, which will read data from long-polling thread
        consumer = _AsyncConsumer(async_id, self._db)

        # If, by default, the user has not requested a synchronized request we return
        # the async object - which allows the user to control how and when to read the
        # value. If not we block the thread and get the value for the user.
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    @error_handler(exceptions = [ApiException])
    def subscribe(self, endpoint_name, resource_path, fix_path = True, queue_size = 5):
        # When path starts with / we remove the slash, as the API can't handle //.
        # Keep the original path around however, as we use that for queue registration.
        fixed_path = path
        if fix_path and resource_path.startswith("/"):
            fixed_path = path[1:]

        # Create the queue and register it with the dict holding all queues
        q = Queue.Queue(queue_size)
        self.queues[endpoint_name][resource_path] = q

        # Send subscription request
        api = mds.SubscriptionsApi()
        api.v2_subscriptions_endpoint_name_resource_path_put(endpoint_name, fixed_path)

        # Return the Queue object to the user
        return q

    def _get_value_synchronized(consumer):
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
        return self.db[async_id].error

    def get_value(self, b64_decode = True):
        if not self.is_done():
            raise UnhandledError("Need to check if request is done, before getting value")
        if self.error():
            raise UnhandledError("Async request returned an error. Need to check for errors,"
                                 "before getting value.\nError: %s" % self.error())

        # Return the payload
        payload = self.db[async_id].payload
        if not b64_decode:
            return payload
        return base64.b64decode(payload)

class _LongPollingThread(threading.Thread):
    def __init__(self, db, queues):
        super(_LongPollingThread, self).__init__()

        self.db = db
        self.queues = queues
        self._stopped = False

    @error_handler(exceptions = [ApiException])
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
                    payload = base64.b64decode(n.payload)
                    self.queues[n.ep][n.path].put(payload)

            if resp.async_responses:
                for r in resp.async_responses:
                    payload = base64.b64decode(r.payload) if r.payload else None
                    self.db[r.id] = {
                        "payload": payload,
                        "error": r.error,
                        "status_code": r.status
                    }

    def stop(self):
        self._stopped = True
