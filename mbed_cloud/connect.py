# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Public API for mDS and Statistics APIs."""
from __future__ import absolute_import
from __future__ import unicode_literals
import base64
from builtins import object
from builtins import str
from collections import defaultdict
import datetime
import logging
import re
from six import iteritems
from six.moves import queue
import threading
import time

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import BaseObject
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.exceptions import CloudAsyncError
from mbed_cloud.exceptions import CloudTimeoutError
from mbed_cloud.exceptions import CloudUnhandledError
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.mds as mds
from mbed_cloud._backends.mds.rest import ApiException as MdsApiException
import mbed_cloud._backends.statistics as statistics
from mbed_cloud._backends.statistics.rest import ApiException as StatisticsApiException

LOG = logging.getLogger(__name__)


class ConnectAPI(BaseAPI):
    """API reference for the Connect API.

    Exposing functionality for doing a range of device related actions:
        - Listing connected devices
        - Exploring and managing resources and resource values on said devices
        - Setup resource subscriptions and webhooks for resource monitoring
    """

    def __init__(self, params={}, b64decode=True):
        """Setup the backend APIs with provided config."""
        super(ConnectAPI, self).__init__(params)

        # Initialize the wrapped APIs
        self.mds = self._init_api(mds)

        self._db = {}
        self._queues = defaultdict(lambda: defaultdict(queue.Queue))

        self._notifications_thread = _NotificationsThread(self._db,
                                                          self._queues,
                                                          b64decode=b64decode,
                                                          mds=self.mds)
        self._notifications_are_active = False
        self._notifications_thread.daemon = True

        self.statistics = self._init_api(statistics)

    def start_notifications(self):
        """Start the notifications thread.

        If not an external callback is setup (using `update_webhook`) then
        calling this function is mandatory to get or set resource.

        .. code-block:: python

            >>> api.start_notifications()
            >>> print(api.get_resource_value(device, path))
            Some value
            >>> api.stop_notifications()

        :returns: void
        """
        self._notifications_thread.start()
        self._notifications_are_active = True

    def stop_notifications(self):
        """Stop the notifications thread.

        :returns: void
        """
        self._notifications_thread.stop()
        self._notifications_are_active = False

    @catch_exceptions(MdsApiException)
    def list_connected_devices(self, **kwargs):
        """List connected devices.

        :param str type: Filter endpoints by endpoint-type.
        :returns: a list of currently *connected* `ConnectedDevice` objects
        :rtype: list of ConnectedDevice
        """
        api = self.mds.EndpointsApi()

        resp = api.v2_endpoints_get(**kwargs)
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

        :param str device_id: The ID of the device (Required)
        :returns: A list of :py:class:`Resource` objects for the device
        :rtype: list
        """
        api = self.mds.EndpointsApi()
        return [Resource(r) for r in api.v2_endpoints_device_id_get(device_id)]

    @catch_exceptions(MdsApiException)
    def delete_resource(self, device_id, resource_path, fix_path=False):
        """Deletes a resource.

        :param str device_id: The ID of the device (Required)
        :param str resource_path: Path of the resource to delete
        :param fix_path: Removes leading / on resource_path if found
        :returns: Async ID
        :rtype: str
        """
        api = self.mds.ResourcesApi()
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]
        api.v2_endpoints_device_id_resource_path_delete(device_id, resource_path)

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

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to get (Required)
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :param timeout: Seconds to request value for before timeout. If not provided, the
            program might hang indefinitly.
        :raises: CloudAsyncError, CloudTimeoutError
        :returns: The resource value for the requested resource path
        :rtype: str
        """
        # Ensure we're listening to notifications first
        if not self._notifications_are_active:
            raise CloudUnhandledError(
                "start_notifications needs to be called before getting resource value.")

        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]
        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_device_id_resource_path_get(device_id, resource_path)

        # The async consumer, which will read data from notifications thread
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

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to get (Required)
        :param bool fix_path: strip leading / of path if present
        :returns: Consumer object to control asynchronous request
        :rtype: AsyncConsumer
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_device_id_resource_path_get(device_id, resource_path)

        # The async consumer, which will read data from notifications thread
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

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to update (Required)
        :param str resource_value: The new value to set for given path (if None
            the resource function will be executed)
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :raises: AsyncError
        :returns: The value of the new resource
        :rtype: str
        """
        # Ensure we're listening to notifications first
        if not self._notifications_are_active:
            raise CloudUnhandledError(
                "start_notifications needs to be called before setting resource value.")

        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()

        if resource_value:
            resp = api.v2_endpoints_device_id_resource_path_put(device_id,
                                                                resource_path,
                                                                resource_value)
        else:
            resp = api.v2_endpoints_device_id_resource_path_post(device_id, resource_path)
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

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to update (Required)
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
            resp = api.v2_endpoints_device_id_resource_path_put(device_id,
                                                                resource_path,
                                                                resource_value)
        else:
            resp = api.v2_endpoints_device_id_resource_path_post(device_id, resource_path)

        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def execute_resource(self, device_id, resource_path, fix_path=True, **kwargs):
        """Execute a function on a resource.

        Will block and wait for response to come through. Usage:

        .. code-block:: python

            try:
                v = api.execute_resource(device, path, function_name)
                print("Success, returned value:", v)
            except AsyncError, e:
                print("Error", e)

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to update (Required)
        :param str resource_function: The function to trigger
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :raises: AsyncError
        :returns: The value returned from the function executed on the resource
        :rtype: str
        """
        # Ensure we're listening to notifications first
        if not self._notifications_are_active:
            raise CloudUnhandledError(
                "start_notifications needs to be called before setting resource value.")

        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_device_id_resource_path_post(device_id,
                                                             resource_path,
                                                             **kwargs)
        consumer = AsyncConsumer(resp.async_response_id, self._db)
        return self._get_value_synchronized(consumer)

    @catch_exceptions(MdsApiException)
    def execute_resource_async(self, device_id, resource_path, fix_path=True, **kwargs):
        """Execute a function on a resource.

        Will not block. Returns immediatly. Usage:

        .. code-block:: python

            a = api.execute_resource_async(device, path, function_name)
            while not a.is_done:
                time.sleep(0.1)
            if a.error:
                print("Error", a.error)
            print("Success, returned value:", a.value)

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to update (Required)
        :param str resource_function: The function to trigger
        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        :returns: An async consumer object holding reference to request
        :rtype: AsyncConsumer
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()

        resp = api.v2_endpoints_device_id_resource_path_post(device_id,
                                                             resource_path,
                                                             **kwargs)

        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def add_resource_subscription(self, device_id, resource_path, fix_path=True, queue_size=5):
        """Subscribe to resource updates.

        When called on valid device and resource path a subscription is setup so that
        any update on the resource path value triggers a new element on the FIFO queue.
        The returned object is a native Python Queue object.

        :param device_id: Name of device to subscribe on (Required)
        :param resource_path: The resource path on device to observe (Required)
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
        api.v2_subscriptions_device_id_resource_path_put(device_id, fixed_path)

        # Return the Queue object to the user
        return q

    @catch_exceptions(MdsApiException)
    def add_resource_subscription_async(self, device_id, resource_path, callback_fn,
                                        fix_path=True, queue_size=5):
        """Subscribe to resource updates with callback function.

        When called on valid device and resource path a subscription is setup so that
        any update on the resource path value triggers an update on the callback function.

        :param device_id: Name of device to subscribe on (Required)
        :param resource_path: The resource path on device to observe (Required)
        :param callback_fn: Callback function to be executed on update to subscribed resource
        :param fix_path: Removes leading / on resource_path if found
        :param queue_size: set the Queue size. If set to 0, no queue object will be created
        :returns: void
        """
        queue = self.add_resource_subscription(device_id, resource_path, fix_path, queue_size)

        # Setup daemon thread for callback function
        t = threading.Thread(target=self._subscription_handler,
                             args=[queue, device_id, resource_path, callback_fn])
        t.daemon = True
        t.start()

    @catch_exceptions(MdsApiException)
    def get_resource_subscription(self, device_id, resource_path, fix_path=True):
        """Read subscription status.

        :param device_id: Name of device to subscribe on (Required)
        :param resource_path: The resource path on device to observe (Required)
        :param fix_path: Removes leading / on resource_path if found
        :returns: status of subscription
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        # Keep the original path around however, as we use that for queue registration.
        fixed_path = resource_path
        if fix_path and resource_path.startswith("/"):
            fixed_path = resource_path[1:]

        api = self.mds.SubscriptionsApi()
        return api.v2_subscriptions_device_id_resource_path_get(device_id, fixed_path)

    @catch_exceptions(MdsApiException)
    def update_presubscriptions(self, presubscriptions):
        """Update pre-subscription data. Pre-subscription data will be removed for empty list.

        :param presubscriptions: list of `Presubscription` objects (Required)
        :returns: None
        """
        api = self.mds.SubscriptionsApi()
        presubscriptions_list = []
        for presubscription in presubscriptions:
            if not isinstance(presubscription, dict):
                presubscription = presubscription.to_dict()
            presubscription = {
                "endpoint_name": presubscription.get("device_id", None),
                "endpoint_type": presubscription.get("device_type", None),
                "_resource_path": presubscription.get("resource_paths", None)
            }
            presubscriptions_list.append(self.mds.Presubscription(**presubscription))
        return api.v2_subscriptions_put(presubscriptions_list)

    @catch_exceptions(MdsApiException)
    def delete_presubscriptions(self):
        """Deletes pre-subscription data.

        :returns: None
        """
        api = self.mds.SubscriptionsApi()
        return api.v2_subscriptions_put([])

    @catch_exceptions(MdsApiException)
    def delete_subscriptions(self):
        """Remove all subscriptions.

        :returns: None
        """
        api = self.mds.SubscriptionsApi()
        return api.v2_subscriptions_delete()

    @catch_exceptions(MdsApiException)
    def list_presubscriptions(self, **kwargs):
        """Get a list of pre-subscription data

        :returns: a list of `Presubscription` objects
        :rtype: list of Presubscription
        """
        api = self.mds.SubscriptionsApi()
        resp = api.v2_subscriptions_get(**kwargs)
        return [Presubscription(p) for p in resp]

    @catch_exceptions(MdsApiException)
    def list_device_subscriptions(self, device_id, **kwargs):
        """List a device's subscriptions

        :param device_id: Id of the device
        :returns: a list of `Presubscription` objects
        :rtype: list of Presubscription
        """
        api = self.mds.SubscriptionsApi()
        resp = api.v2_subscriptions_device_id_get(device_id, **kwargs)
        return [Presubscription(p) for p in resp]

    @catch_exceptions(MdsApiException)
    def delete_device_subscriptions(self, device_id):
        """Removes a device's subscriptions

        :param device_id: Id of the device
        :returns: None
        """
        api = self.mds.SubscriptionsApi()
        return api.v2_subscriptions_device_id_delete(device_id)

    @catch_exceptions(MdsApiException)
    def delete_resource_subscription(self, device_id=None, resource_path=None, fix_path=True):
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
        devices = [_f for _f in [device_id] if _f]
        if not device_id:
            devices = list(self._queues.keys())
        resource_paths = [resource_path]
        if not resource_path:
            resource_paths = []
            for e in devices:
                resource_paths.extend(list(self._queues[e].keys()))

        # Delete the subscriptions
        api = self.mds.SubscriptionsApi()
        for e in devices:
            for r in resource_paths:
                # Fix the path, if required.
                fixed_path = r
                if fix_path and r.startswith("/"):
                    fixed_path = r[1:]

                # Make request to API, ignoring result
                api.v2_subscriptions_device_id_resource_path_delete(device_id, fixed_path)

                # Remove Queue from dictionary
                del self._queues[e][r]
        return

    @catch_exceptions(MdsApiException)
    def get_webhook(self):
        """Get the current callback URL if it exists.

        :return: The currently set webhook
        """
        api = self.mds.DefaultApi()
        return Webhook(api.v2_notification_callback_get())

    @catch_exceptions(MdsApiException)
    def update_webhook(self, url, headers={}):
        """Register new webhook for incoming subscriptions.

        If a webhook is already set, this will do an overwrite.

        :param str url: the URL with listening webhook (Required)
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

    @catch_exceptions(StatisticsApiException)
    def list_metrics(self, include=None, interval="1d", **kwargs):
        """Get statistics.

        :param list[str] include: List of fields included in response.
        None or empty list will return all fields.
        Fields: transactions, successful_api_calls, failed_api_calls, successful_handshakes,
        pending_bootstraps, successful_bootstraps, failed_bootstraps, registrations,
        updated_registrations, expired_registrations, deleted_registrations
        :param str interval: Group data by this interval in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
        :param datetime start: Fetch the data with timestamp greater than or equal to this value.
            The parameter is not mandatory, if the period is specified.
        :param datetime end: Fetch the data with timestamp less than this value.
            The parameter is not mandatory, if the period is specified.
        :param str period: Period. Fetch the data for the period in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
            The parameter is not mandatory, if the start and end time are specified
        :param int limit: The number of devices to retrieve
        :param str order: The ordering direction, ascending (asc) or descending (desc)
        :param str after: Get metrics after/starting at given metric ID
        :returns: a list of :py:class:`Metric` objects
        :rtype: PaginatedResponse
        """
        self._verify_arguments(interval, kwargs)
        kwargs = self._verify_filters(kwargs)
        api = self.statistics.StatisticsApi()
        include = Metric._map_includes(include)
        kwargs.update({"include": include})
        kwargs.update({"interval": interval})
        return PaginatedResponse(api.v3_metrics_get, lwrap_type=Metric, **kwargs)

    def _subscription_handler(self, queue, device_id, path, callback_fn):
        while True:
            value = queue.get()
            callback_fn(device_id, path, value)

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
        value = consumer.value
        if value is not None:
            value = value.decode('utf-8')
        return value

    def _convert_to_UTC_RFC3339(self, time, name):
        if not isinstance(time, datetime.datetime):
            raise CloudValueError("%s should be of type datetime" % (name))
        return time.isoformat() + "Z"

    def _verify_arguments(self, interval, kwargs):
        start = kwargs.get("start", None)
        end = kwargs.get("end", None)
        period = kwargs.get("period", None)
        if not start and not end and not period:
            raise CloudValueError("start and end is mandatory if period is not specified.")
        if start and not end:
            raise CloudValueError("end is required if start is specified.")
        if end and not start:
            raise CloudValueError("start is required if end is specified.")
        pattern = re.compile("[0-9]+[h|d|w]$")
        if period and not pattern.match(period):
            raise CloudValueError("period is incorrect. Sample values: 2h, 3w, 4d.")
        if interval and not pattern.match(interval):
            raise CloudValueError("interval is incorrect. Sample values: 2h, 3w, 4d.")
        # convert start into UTC RFC3339 format
        if start:
            kwargs['start'] = self._convert_to_UTC_RFC3339(start, 'start')
        # convert end into UTC RFC3339 format
        if end:
            kwargs['end'] = self._convert_to_UTC_RFC3339(end, 'end')


class AsyncConsumer(object):
    """Consumer object for reading values from a notifications thread.

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

        The DB is populated from the notifications thread.
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


class _NotificationsThread(threading.Thread):
    def __init__(self, db, queues, b64decode=True, mds=None):
        super(_NotificationsThread, self).__init__()

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


class ConnectedDevice(BaseObject):
    """Describes device object from the mDS."""

    @staticmethod
    def _get_attributes_map():
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
        wakes up and connects to Mbed Cloud Connect itself.
        You can also use the Queue mode when the device
        is behind a NAT and cannot be reached directly by Mbed Cloud Connect.

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

        Unique Mbed Cloud Device ID representing the endpoint.

        :return: The id of this Endpoint.
        :rtype: str
        """
        return self._id


class Webhook(BaseObject):
    """Describes webhook object."""

    @staticmethod
    def _get_attributes_map():
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


class Metric(BaseObject):
    """Describes Metric object from statistics."""

    @staticmethod
    def _get_attributes_map():
        return {
            "id": "id",
            "timestamp": "timestamp",
            "handshakes": "handshakes_successful",
            "transactions": "transactions",
            "observations": "device_observations",
            "successful_api_calls": "connect_rest_api_success",
            "failed_api_calls": "connect_rest_api_error",
            "successful_proxy_requests": "device_proxy_request_success",
            "failed_proxy_requests": "device_proxy_request_error",
            "successful_subscription_requests": "device_subscription_request_success",
            "failed_subscription_requests": "device_subscription_request_error",
            "successful_bootstraps": "bootstraps_successful",
            "failed_bootstraps": "bootstraps_failed",
            "pending_bootstraps": "bootstraps_pending",
            "full_registrations": "full_registrations",
            "updated_registrations": "registration_updates",
            "expired_registrations": "expired_registrations",
            "deleted_registrations": "deleted_registrations"
        }

    @staticmethod
    def _map_includes(include):
        if include is None:
            include = []
        includes = []
        attributes_map = Metric._get_attributes_map()
        for key in include:
            val = attributes_map.get(key, None)
            if val is not None:
                includes.append(val)
        if len(includes) == 0:
            for key, value in iteritems(attributes_map):
                if key != "id" and key != "timestamp":
                    includes.append(value)
        s = ','
        return s.join(includes)

    @property
    def id(self):
        """The ID of the metric.

        :rtype: string
        """
        return self._id

    @property
    def timestamp(self):
        """UTC time in RFC3339 format.

        The timestamp is the starting point of the interval for which the data is aggregated.
        Each interval includes data for the time greater than or equal to the timestamp
        and less than the next interval's starting point.

        :return: The timestamp of this Metric.
        :rtype: datetime
        """
        return self._timestamp

    @property
    def handshakes(self):
        """The number of successful TLS handshakes the account has performed.

        The SSL or TLS handshake enables the SSL or TLS client and server to establish the
        secret keys with which they communicate. A successful TLS handshake is required
        for establishing a connection with Mbed Cloud Connect for any operaton such as registration,
        registration update and deregistration.
        :rtype: int
        """
        return self._handshakes

    @property
    def transactions(self):
        """The number of transaction events from or to devices linked to the account.

        A transaction is a 512-byte block of data processed by Mbed Cloud.
        It can be either sent by the device (device --> Mbed Cloud) or received by the device
        (Mbed Cloud --> device). A transaction does not include
        IP, TCP or UDP, TLS or DTLS packet overhead.
        It only contains the packet payload (full CoAP packet including CoAP headers).

        :rtype: int
        """
        return self._transactions

    @property
    def observations(self):
        """The number of observations received by Mbed Cloud Connect from the devices

        linked to the account. The observations are pushed from the device to Mbed Cloud Connect
        when you have successfully subscribed to the device resources using Connect API endpoints.
        :rtype: int
        """
        return self._observations

    @property
    def successful_api_calls(self):
        """The number of successful requests the account has performed.

        :rtype: int
        """
        return self._successful_api_calls

    @property
    def failed_api_calls(self):
        """The number of failed requests the account has performed.

        :rtype: int
        """
        return self._failed_api_calls

    @property
    def successful_proxy_requests(self):
        """The number of successful proxy requests from Mbed Cloud Connect to devices linked

        to the account. The proxy requests are made from Mbed Cloud Connect to devices
        when you try to read or write values to device resources using Connect API endpoints.

        :rtype: int
        """
        return self._successful_proxy_requests

    @property
    def failed_proxy_requests(self):
        """The number of failed proxy requests from Mbed Cloud Connect to devices linked to

        the account. The proxy requests are made from Mbed Cloud Connect to devices when you try
        to read or write values to device resources using Connect API endpoints.
        :rtype: int
        """
        return self._failed_proxy_requests

    @property
    def successful_subscription_requests(self):
        """The number of successful subscription requests from Mbed Cloud Connect to devices

        linked to the account. The subscription requests are made from Mbed Cloud Connect
        to devices when you try to subscribe to a resource path using Connect API endpoints.
        :rtype: int
        """
        return self._successful_subscription_requests

    @property
    def failed_subscription_requests(self):
        """The number of failed subscription requests from Mbed Cloud Connect to devices linked

        to the account. The subscription requests are made from Mbed Cloud Connect to devices
        when you try to subscribe to a resource path using Connect API endpoints.
        :rtype: int
        """
        return self._failed_subscription_requests

    @property
    def pending_bootstraps(self):
        """The number of pending bootstraps the account has performed.

        Bootstrap is the process of provisioning a Lightweight Machine to Machine Client
        to a state where it can initiate a management session to a new Lightweight Machine
        to Machine Server.

        :rtype: int
        """
        return self._pending_bootstraps

    @property
    def successful_bootstraps(self):
        """The number of successful bootstraps the account has performed.

        Bootstrap is the process of provisioning a Lightweight Machine to Machine Client
        to a state where it can initiate a management session to a new Lightweight Machine
        to Machine Server.

        :rtype: int
        """
        return self._successful_bootstraps

    @property
    def failed_bootstraps(self):
        """The number of failed bootstraps the account has performed.

        Bootstrap is the process of provisioning a Lightweight Machine to Machine Client
        to a state where it can initiate a management session to
        a new Lightweight Machine to Machine Server.

        :rtype: int
        """
        return self._failed_bootstraps

    @property
    def full_registrations(self):
        """The number of full registrations linked to the account.

        Full registration is the process of registering a device with the Mbed Cloud Connect
        by providing its lifetime and capabilities such as the resource structure.
        The registered status of the device does not guarantee that the device is active
        and accessible from Mebd Cloud Connect at any point of time.

        :rtype: int
        """
        return self._full_registrations

    @property
    def updated_registrations(self):
        """The number of registration updates linked to the account.

        Registration update is the process of updating the registration status with
        the Mbed Cloud Connect to update or extend the lifetime of the device.

        :rtype: int
        """
        return self._updated_registrations

    @property
    def expired_registrations(self):
        """The number of expired registrations linked to the account.

        Mbed Cloud Connect removes the device registrations when the devices cannot update
        their registration before the expiry of the lifetime. Mbed Cloud Connect
        no longer handles requests for a device whose registration has expired already.

        :rtype: int
        """
        return self._expired_registrations

    @property
    def deleted_registrations(self):
        """The number of deleted registrations (deregistrations) linked to the account.

        Deregistration is the process of removing the device registration from the
        Mbed Cloud Connect registry. The deregistration is usually initiated by the device.
        Mbed Cloud Connect no longer handles requests for a deregistered device.

        :rtype: int
        """
        return self._deleted_registrations


class Presubscription(BaseObject):
    """Presubscription data object"""

    @staticmethod
    def _get_attributes_map():
        return {
            'device_id': 'endpoint-name',
            'device_type': 'endpoint-type',
            'resource_paths': 'resource-path',
        }

    @property
    def device_id(self):
        """The Device ID

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._device_id

    @property
    def device_type(self):
        """Device type of this Presubscription.

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._device_type

    @property
    def resource_paths(self):
        """Resource paths of this Presubscription.

        :return: The url of this Webhook.
        :rtype: list[str]
        """
        return self._resource_paths
