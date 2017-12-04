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

import datetime
import logging
import re
import threading
from collections import defaultdict

# Import backend API
import mbed_cloud._backends.device_directory as device_directory
import mbed_cloud._backends.mds as mds
import mbed_cloud._backends.statistics as statistics
# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud import PaginatedResponse
from mbed_cloud._backends.device_directory.rest import ApiException as DeviceDirectoryApiException
from mbed_cloud._backends.mds.models.presubscription import Presubscription as PresubscriptionData
from mbed_cloud._backends.mds.models.webhook import Webhook as WebhookData
from mbed_cloud._backends.mds.rest import ApiException as MdsApiException
from mbed_cloud._backends.statistics.rest import ApiException as StatisticsApiException
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.device_directory import Device
from mbed_cloud.exceptions import CloudApiException
from mbed_cloud.exceptions import CloudUnhandledError
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud.metric import Metric
from mbed_cloud.notifications import _NotificationsThread
from mbed_cloud.notifications import AsyncConsumer
from mbed_cloud.notifications import handle_channel_message
from mbed_cloud.presubscription import Presubscription
from mbed_cloud.resource import Resource
from mbed_cloud.webhooks import Webhook
from six.moves import queue

LOG = logging.getLogger(__name__)


class ConnectAPI(BaseAPI):
    """API reference for the Connect API.

    Exposing functionality for doing a range of device related actions:
        - Listing connected devices
        - Exploring and managing resources and resource values on said devices
        - Setup resource subscriptions and webhooks for resource monitoring
    """

    api_structure = {
        mds: [
            mds.DefaultApi,
            mds.EndpointsApi,
            mds.NotificationsApi,
            mds.ResourcesApi,
            mds.SubscriptionsApi
        ],
        statistics: [statistics.AccountApi, statistics.StatisticsApi],
        device_directory: [device_directory.DefaultApi],
    }

    def __init__(self, params=None):
        """Setup the backend APIs with provided config."""
        super(ConnectAPI, self).__init__(params)

        self._db = {}
        self._queues = defaultdict(lambda: defaultdict(queue.Queue))

        self.b64decode = True
        self._notifications_are_active = False
        self._notifications_thread = None

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
        api = self._get_api(mds.NotificationsApi)
        if self._notifications_are_active:
            return
        self._notifications_thread = _NotificationsThread(
            self._db,
            self._queues,
            b64decode=self.b64decode,
            notifications_api=api
        )
        self._notifications_thread.daemon = True
        self._notifications_thread.start()
        self._notifications_are_active = True

    def stop_notifications(self):
        """Stop the notifications thread.

        :returns: void
        """
        if not self._notifications_are_active:
            return
        self._notifications_thread.stop()
        self._notifications_thread = None
        self._notifications_are_active = False

    @catch_exceptions(DeviceDirectoryApiException)
    def list_connected_devices(self, **kwargs):
        """List connected devices.

        Example usage, listing all registered devices in the catalog:

        .. code-block:: python

            filters = {
                'created_at': {'$gte': datetime.datetime(2017,01,01),
                               '$lte': datetime.datetime(2017,12,31)
                              }
            }
            devices = api.list_connected_devices(order='asc', filters=filters)
            for idx, device in enumerate(devices):
                print(device)

            ## Other example filters

            # Directly connected devices (not via gateways):
            filters = {
                'host_gateway': {'$eq': ''},
                'device_type': {'$eq': ''}
            }

            # Devices connected via gateways:
            filters = {
                'host_gateway': {'$neq': ''}
            }

            # Gateway devices:
            filters = {
                'device_type': {'$eq': 'MBED_GW'}
            }


        :param int limit: The number of devices to retrieve.
        :param str order: The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: Get devices after/starting at given `device_id`
        :param filters: Dictionary of filters to apply.
        :returns: a list of connected :py:class:`Device` objects.
        :rtype: PaginatedResponse
        """
        filters = kwargs.get("filters", {})
        filters.update({'state': {'$eq': 'registered'}})
        kwargs.update({'filters': filters})
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, Device, True)
        api = self._get_api(device_directory.DefaultApi)
        return PaginatedResponse(api.device_list, lwrap_type=Device, **kwargs)

    @catch_exceptions(MdsApiException)
    def list_resources(self, device_id):
        """List all resources registered to a connected device.

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
        api = self._get_api(mds.EndpointsApi)
        return [Resource(r) for r in api.v2_endpoints_device_id_get(device_id)]

    @catch_exceptions(MdsApiException)
    def get_resource(self, device_id, resource_path):
        """Get a resource.

        :param str device_id: ID of the device (Required)
        :param str path: Path of the resource to get (Required)
        :returns: Device resource
        :rtype Resource
        """
        resources = self.list_resources(device_id)
        for r in resources:
            if r.path == resource_path:
                return r
        raise CloudApiException("Resource not found")

    @catch_exceptions(MdsApiException)
    def delete_resource(self, device_id, resource_path, fix_path=False):
        """Deletes a resource.

        :param str device_id: The ID of the device (Required)
        :param str resource_path: Path of the resource to delete
        :param fix_path: Removes leading / on resource_path if found
        :returns: Async ID
        :rtype: str
        """
        api = self._get_api(mds.ResourcesApi)
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

        consumer = self.get_resource_value_async(device_id, resource_path, fix_path)

        # We block the thread and get the value for the user.
        return consumer.wait(timeout)

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
        if fix_path:
            resource_path = resource_path.lstrip('/')

        api = self._get_api(mds.ResourcesApi)
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

        api = self._get_api(mds.ResourcesApi)

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

        api = self._get_api(mds.ResourcesApi)

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

        api = self._get_api(mds.ResourcesApi)
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

        api = self._get_api(mds.ResourcesApi)

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
        api = self._get_api(mds.SubscriptionsApi)
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

        api = self._get_api(mds.SubscriptionsApi)
        return api.v2_subscriptions_device_id_resource_path_get(device_id, fixed_path)

    @catch_exceptions(MdsApiException)
    def update_presubscriptions(self, presubscriptions):
        """Update pre-subscription data. Pre-subscription data will be removed for empty list.

        :param presubscriptions: list of `Presubscription` objects (Required)
        :returns: None
        """
        api = self._get_api(mds.SubscriptionsApi)
        presubscriptions_list = []
        for presubscription in presubscriptions:
            if not isinstance(presubscription, dict):
                presubscription = presubscription.to_dict()
            presubscription = {
                "endpoint_name": presubscription.get("device_id", None),
                "endpoint_type": presubscription.get("device_type", None),
                "_resource_path": presubscription.get("resource_paths", None)
            }
            presubscriptions_list.append(PresubscriptionData(**presubscription))
        return api.v2_subscriptions_put(presubscriptions_list)

    @catch_exceptions(MdsApiException)
    def delete_presubscriptions(self):
        """Deletes pre-subscription data.

        :returns: None
        """
        api = self._get_api(mds.SubscriptionsApi)
        return api.v2_subscriptions_put([])

    @catch_exceptions(MdsApiException)
    def delete_subscriptions(self):
        """Remove all subscriptions.

        :returns: None
        """
        api = self._get_api(mds.SubscriptionsApi)
        return api.v2_subscriptions_delete()

    @catch_exceptions(MdsApiException)
    def list_presubscriptions(self, **kwargs):
        """Get a list of pre-subscription data

        :returns: a list of `Presubscription` objects
        :rtype: list of mbed_cloud.presubscription.Presubscription
        """
        api = self._get_api(mds.SubscriptionsApi)
        resp = api.v2_subscriptions_get(**kwargs)
        return [Presubscription(p) for p in resp]

    @catch_exceptions(MdsApiException)
    def list_device_subscriptions(self, device_id, **kwargs):
        """Lists all subscribed resources from a single device

        :param device_id: Id of the device
        :returns: a list of subscribed resources
        :rtype: list of str
        """
        api = self._get_api(mds.SubscriptionsApi)
        resp = api.v2_subscriptions_device_id_get(device_id, **kwargs)
        return resp.split("\n")

    @catch_exceptions(MdsApiException)
    def delete_device_subscriptions(self, device_id):
        """Removes a device's subscriptions

        :param device_id: Id of the device
        :returns: None
        """
        api = self._get_api(mds.SubscriptionsApi)
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
        api = self._get_api(mds.SubscriptionsApi)
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

    def notify_webhook_received(self, ep, path, payload):
        """Callback function for triggering notification channel handlers.

        Use this in conjunction with a webserver to complete the loop when using
        webhooks as the notification channel.

        :param str ep: the Device ID
        :param str path: the resource path
        :param str payload: the encoded payload
        """
        notification = self._get_api(mds.DefaultApi).api_client.deserialise(
            payload, mds.NotificationMessage.__name__
        )
        handle_channel_message(
            db=self._db,
            queues=self._queues,
            b64decode=self.b64decode,
            notification_object=notification
        )

    @catch_exceptions(MdsApiException)
    def get_webhook(self):
        """Get the current callback URL if it exists.

        :return: The currently set webhook
        """
        api = self._get_api(mds.DefaultApi)
        return Webhook(api.v2_notification_callback_get())

    @catch_exceptions(MdsApiException)
    def update_webhook(self, url, headers=None):
        """Register new webhook for incoming subscriptions.

        If a webhook is already set, this will do an overwrite.

        :param str url: the URL with listening webhook (Required)
        :param dict headers: K/V dict with additional headers to send with request
        :return: void
        """
        headers = headers or {}
        api = self._get_api(mds.NotificationsApi)

        # Delete notifications channel
        api.v2_notification_pull_delete()

        # Send the request to register the webhook
        webhook_obj = WebhookData(url=url, headers=headers)
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
        api = self._get_api(mds.DefaultApi)
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
        kwargs = self._verify_filters(kwargs, Metric)
        api = self._get_api(statistics.StatisticsApi)
        include = Metric._map_includes(include)
        kwargs.update({"include": include})
        kwargs.update({"interval": interval})
        return PaginatedResponse(api.v3_metrics_get, lwrap_type=Metric, **kwargs)

    def _subscription_handler(self, queue, device_id, path, callback_fn):
        while True:
            value = queue.get()
            callback_fn(device_id, path, value)

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
