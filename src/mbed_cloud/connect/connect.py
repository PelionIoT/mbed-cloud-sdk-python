# --------------------------------------------------------------------------
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
import logging
import re
import threading
import warnings

from collections import defaultdict

from mbed_cloud._backends import device_directory
from mbed_cloud._backends import mds
from mbed_cloud._backends.mds.models.presubscription import Presubscription as PresubscriptionData
from mbed_cloud._backends.mds.models.webhook import Webhook as WebhookData
from mbed_cloud._backends import statistics

from mbed_cloud.connect.metric import Metric
from mbed_cloud.connect.notifications import AsyncConsumer
from mbed_cloud.connect.notifications import handle_channel_message
from mbed_cloud.connect.notifications import NotificationsThread
from mbed_cloud.connect.presubscription import Presubscription
from mbed_cloud.connect.resource import Resource
from mbed_cloud.connect.webhooks import Webhook

from mbed_cloud.core import BaseAPI
from mbed_cloud.pagination import PaginatedResponse

from mbed_cloud.decorators import catch_exceptions

from mbed_cloud.device_directory import Device

from mbed_cloud.exceptions import CloudApiException
from mbed_cloud.exceptions import CloudValueError
from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud import utils

from six.moves import queue

LOG = logging.getLogger(__name__)


class ConnectAPI(BaseAPI):
    """API reference for the Connect API.

    Exposing functionality for doing a range of device related actions:
        - Listing connected devices
        - Exploring and managing resources and resource values on connected devices
        - Setup resource subscriptions and webhooks for resource monitoring
    """

    api_structure = {
        mds: [
            mds.EndpointsApi,
            mds.NotificationsApi,
            mds.DeviceRequestsApi,
            mds.ResourcesApi,
            mds.SubscriptionsApi
        ],
        statistics: [statistics.AccountApi, statistics.StatisticsApi],
        device_directory: [device_directory.DefaultApi],
    }

    def __init__(self, params=None):
        """A module to access this section of the Mbed Cloud API.

        :param params: Dictionary to override configuration values
                     : autostart_notification_thread : Automatically starts a thread
                     if needed for Async APIs (e.g. get_resource_value).
                     This should be set to False when using webhooks for notifications.
        """
        super(ConnectAPI, self).__init__(params)

        self._db = {}
        self._queues = defaultdict(dict)

        self.b64decode = True
        self._notifications_thread = None
        self._notifications_lock = threading.RLock()
        self.subscribe = SubscriptionsManager(self)

    @property
    def has_active_notification_thread(self):
        """Has active notification thread"""
        with self._notifications_lock:
            return bool(self._notifications_thread)

    def ensure_notifications_thread(self):
        """Ensure notification thread is running"""
        if self.config.get('autostart_notification_thread'):
            if not self.has_active_notification_thread:
                self.start_notifications()

    def start_notifications(self):
        """Start the notifications thread.

        If an external callback is not set up (using `update_webhook`) then
        calling this function is mandatory to get or set resource.

        .. code-block:: python

            >>> api.start_notifications()
            >>> print(api.get_resource_value(device, path))
            Some value
            >>> api.stop_notifications()

        :returns: void
        """
        with self._notifications_lock:
            if self.has_active_notification_thread:
                return
            api = self._get_api(mds.NotificationsApi)
            self._notifications_thread = NotificationsThread(
                self._db,
                self._queues,
                b64decode=self.b64decode,
                notifications_api=api,
                subscription_manager=self.subscribe,
            )
            self._notifications_thread.daemon = True
            self._notifications_thread.start()

    def stop_notifications(self):
        """Stop the notifications thread.

        :returns:
        """
        with self._notifications_lock:
            if not self.has_active_notification_thread:
                return
            thread = self._notifications_thread
            self._notifications_thread = None
            stopping = thread.stop()
            api = self._get_api(mds.NotificationsApi)
            api.delete_long_poll_channel()
            return stopping.wait()

    @catch_exceptions(device_directory.rest.ApiException)
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
        # TODO(pick one of these)
        filter_or_filters = 'filter' if 'filter' in kwargs else 'filters'
        kwargs.setdefault(filter_or_filters, {}).setdefault('state', {'$eq': 'registered'})
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs, Device, True)
        api = self._get_api(device_directory.DefaultApi)
        return PaginatedResponse(api.device_list, lwrap_type=Device, **kwargs)

    @catch_exceptions(mds.rest.ApiException)
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
        return [Resource(r) for r in api.get_endpoint_resources(device_id)]

    @catch_exceptions(mds.rest.ApiException)
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

    def _mds_rpc_post(self, device_id, _wrap_with_consumer=True, async_id=None, **params):
        """Helper for using RPC endpoint"""
        self.ensure_notifications_thread()
        api = self._get_api(mds.DeviceRequestsApi)
        async_id = async_id or utils.new_async_id()
        device_request = mds.DeviceRequest(**params)
        api.create_async_request(
            device_id,
            async_id=async_id,
            body=device_request,
        )
        return AsyncConsumer(async_id, self._db) if _wrap_with_consumer else async_id

    @catch_exceptions(mds.rest.ApiException)
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
        return self._mds_rpc_post(device_id=device_id, method='GET', uri=resource_path)

    @catch_exceptions(mds.rest.ApiException)
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
            program might hang indefinitely.
        :raises: CloudAsyncError, CloudTimeoutError
        :returns: The resource value for the requested resource path
        :rtype: str
        """
        return self.get_resource_value_async(device_id, resource_path, fix_path).wait(timeout)

    @catch_exceptions(mds.rest.ApiException)
    def set_resource_value(self, device_id, resource_path, resource_value,
                           fix_path=True, timeout=None):
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
        :param str resource_value: The new value to set for given path
        :param fix_path: Unused
        :param timeout: Timeout in seconds
        :raises: AsyncError
        :returns: The value of the new resource
        :rtype: str
        """
        self.ensure_notifications_thread()
        return self.set_resource_value_async(
            device_id, resource_path, resource_value
        ).wait(timeout)

    @staticmethod
    def _base64_encode(resource_value):
        """Base64 encode the value in a Python version agnostic way.

        Use encode and decode to covert to and from a bytes object which b64encode will encode.
        """
        if resource_value is None:
            return ""
        else:
            return base64.b64encode(str(resource_value).encode("utf-8")).decode("utf-8")

    @catch_exceptions(mds.rest.ApiException)
    def set_resource_value_async(self, device_id, resource_path,
                                 resource_value=None, fix_path=True):
        """Set resource value for given resource path, on device.

        Will not block. Returns immediately. Usage:

        .. code-block:: python

            a = api.set_resource_value_async(device, path, value)
            while not a.is_done:
                time.sleep(0.1)
            if a.error:
                print("Error", a.error)
            print("Success, new value:", a.value)

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to update (Required)
        :param str resource_value: The new value to set for given path
        :param fix_path: Unused
        :returns: An async consumer object holding reference to request
        :rtype: AsyncConsumer
        """
        payload_b64 = self._base64_encode(resource_value)

        if not resource_path.startswith("/"):
            resource_path = "/" + resource_path

        return self._mds_rpc_post(
            device_id,
            method='PUT',
            uri=resource_path,
            content_type="text/plain",
            payload_b64=payload_b64
        )

    @catch_exceptions(mds.rest.ApiException)
    def execute_resource(self, device_id, resource_path, fix_path=True, timeout=None):
        """Execute a function on a resource.

        Will block and wait for response to come through. Usage:

        .. code-block:: python

            try:
                v = api.execute_resource(device, path)
                print("Success, returned value:", v)
            except AsyncError, e:
                print("Error", e)

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to update (Required)
        :param str resource_function: Unused
        :param fix_path: Unused
        :param timeout: Timeout in seconds
        :raises: AsyncError
        :returns: The value returned from the function executed on the resource
        :rtype: str
        """
        self.ensure_notifications_thread()
        return self.execute_resource_async(device_id, resource_path).wait(timeout)

    @catch_exceptions(mds.rest.ApiException)
    def execute_resource_async(self, device_id, resource_path, fix_path=True):
        """Execute a function on a resource.

        Will not block. Returns immediately. Usage:

        .. code-block:: python

            a = api.execute_resource_async(device, path)
            while not a.is_done:
                time.sleep(0.1)
            if a.error:
                print("Error", a.error)
            print("Success, returned value:", a.value)

        :param str device_id: The name/id of the device (Required)
        :param str resource_path: The resource path to update (Required)
        :param fix_path: Unused
        :returns: An async consumer object holding reference to request
        :rtype: AsyncConsumer
        """
        if not resource_path.startswith("/"):
            resource_path = "/" + resource_path

        return self._mds_rpc_post(device_id=device_id, method='POST', uri=resource_path)

    @catch_exceptions(mds.rest.ApiException)
    def _add_subscription(self, device_id, resource_path):
        api = self._get_api(mds.SubscriptionsApi)
        return api.add_resource_subscription(device_id, resource_path)

    @catch_exceptions(mds.rest.ApiException)
    def add_resource_subscription(self, device_id, resource_path, fix_path=True, queue_size=5):
        """Subscribe to resource updates.

        When called on a valid device and resource path a subscription is setup so that
        any update on the resource path value triggers a new element on the FIFO queue.
        The returned object is a native Python Queue object.

        :param device_id: Name of device to subscribe on (Required)
        :param resource_path: The resource path on device to observe (Required)
        :param fix_path: Removes leading / on resource_path if found
        :param queue_size: Sets the Queue size. If set to 0, no queue object will be created
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

        # FIXME: explicit behaviour on replacing an existing queue
        self._queues[device_id][resource_path] = q

        # Send subscription request
        self._add_subscription(device_id, fixed_path)

        # Return the Queue object to the user
        return q

    @catch_exceptions(mds.rest.ApiException)
    def add_resource_subscription_async(self, device_id, resource_path, callback_fn,
                                        fix_path=True, queue_size=5):
        """Subscribe to resource updates with callback function.

        When called on a valid device and resource path a subscription is setup so that
        any update on the resource path value triggers an update on the callback function.

        :param device_id: Name of device to set the subscription on (Required)
        :param resource_path: The resource path on device to observe (Required)
        :param callback_fn: Callback function to be executed on update to subscribed resource
        :param fix_path: Removes leading / on resource_path if found
        :param queue_size: Sets the Queue size. If set to 0, no queue object will be created
        :returns: void
        """
        queue = self.add_resource_subscription(device_id, resource_path, fix_path, queue_size)

        # Setup daemon thread for callback function
        t = threading.Thread(target=self._subscription_handler,
                             args=[queue, device_id, resource_path, callback_fn])
        t.daemon = True
        t.start()

    @catch_exceptions(mds.rest.ApiException)
    def get_resource_subscription(self, device_id, resource_path, fix_path=True):
        """Read subscription status.

        :param device_id: Name of device to set the subscription on (Required)
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
        try:
            api.check_resource_subscription(device_id, fixed_path)
        except Exception as e:
            if e.status == 404:
                return False
            raise
        return True

    @catch_exceptions(mds.rest.ApiException)
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
        return api.update_pre_subscriptions(presubscriptions_list)

    @catch_exceptions(mds.rest.ApiException)
    def delete_presubscriptions(self):
        """Deletes pre-subscription data.

        :returns: None
        """
        api = self._get_api(mds.SubscriptionsApi)
        return api.update_pre_subscriptions([])

    @catch_exceptions(mds.rest.ApiException)
    def delete_subscriptions(self):
        """Remove all subscriptions.

        Warning: This could be slow for large numbers of connected devices.
        If possible, explicitly delete subscriptions known to have been created.

        :returns: None
        """
        warnings.warn('This could be slow for large numbers of connected devices.'
                      'If possible, explicitly delete subscriptions known to have been created.')
        for device in self.list_connected_devices():
            try:
                self.delete_device_subscriptions(device_id=device.id)
            except CloudApiException as e:
                LOG.warning('failed to remove subscription for %s: %s', device.id, e)
                continue

    @catch_exceptions(mds.rest.ApiException)
    def list_presubscriptions(self, **kwargs):
        """Get a list of pre-subscription data

        :returns: a list of `Presubscription` objects
        :rtype: list of mbed_cloud.presubscription.Presubscription
        """
        api = self._get_api(mds.SubscriptionsApi)
        resp = api.get_pre_subscriptions(**kwargs)
        return [Presubscription(p) for p in resp]

    @catch_exceptions(mds.rest.ApiException)
    def list_device_subscriptions(self, device_id, **kwargs):
        """Lists all subscribed resources from a single device

        :param device_id: ID of the device (Required)
        :returns: a list of subscribed resources
        :rtype: list of str
        """
        api = self._get_api(mds.SubscriptionsApi)
        resp = api.get_endpoint_subscriptions(device_id, **kwargs)
        return resp.split("\n")

    @catch_exceptions(mds.rest.ApiException)
    def delete_device_subscriptions(self, device_id):
        """Removes a device's subscriptions

        :param device_id: ID of the device (Required)
        :returns: None
        """
        api = self._get_api(mds.SubscriptionsApi)
        return api.delete_endpoint_subscriptions(device_id)

    @catch_exceptions(mds.rest.ApiException)
    def _delete_subscription(self, device_id, resource_path):
        api = self._get_api(mds.SubscriptionsApi)
        return api.delete_resource_subscription(device_id, resource_path)

    @catch_exceptions(mds.rest.ApiException)
    def delete_resource_subscription(self, device_id=None, resource_path=None, fix_path=True):
        """Unsubscribe from device and/or resource_path updates.

        If device_id or resource_path is None, or this method is called without arguments,
        all subscriptions are removed.
        Calling it with only device_id removes subscriptions for all resources
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
        for e in devices:
            for r in resource_paths:
                # Fix the path, if required.
                fixed_path = r
                if fix_path and r.startswith("/"):
                    fixed_path = r[1:]

                # Make request to API, ignoring result
                self._delete_subscription(device_id, fixed_path)

                # Remove Queue from dictionary
                del self._queues[e][r]
        return

    def notify_webhook_received(self, payload):
        """Callback function for triggering notification channel handlers.

        Use this in conjunction with a webserver to complete the loop when using
        webhooks as the notification channel.

        :param str payload: the encoded payload, as sent by the notification channel
        """
        class PayloadContainer:  # noqa
            # bodge to give attribute lookup
            data = payload

        notification = self._get_api(mds.NotificationsApi).api_client.deserialize(
            PayloadContainer, mds.NotificationMessage.__name__
        )
        handle_channel_message(
            db=self._db,
            queues=self._queues,
            b64decode=self.b64decode,
            notification_object=notification
        )

    @catch_exceptions(mds.rest.ApiException)
    def get_webhook(self):
        """Get the current callback URL if it exists.

        :return: The currently set webhook
        """
        api = self._get_api(mds.NotificationsApi)
        return Webhook(api.get_webhook())

    @catch_exceptions(mds.rest.ApiException)
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
        api.delete_long_poll_channel()

        # Send the request to register the webhook
        webhook_obj = WebhookData(url=url, headers=headers)
        api.register_webhook(webhook_obj)
        return

    @catch_exceptions(mds.rest.ApiException)
    def delete_webhook(self):
        """Delete/remove registered webhook.

        If no webhook is registered, an exception (404) will be raised.

        Note that every registered subscription will be deleted as part of
        deregistering a webhook.

        :return: void
        """
        api = self._get_api(mds.NotificationsApi)
        api.deregister_webhook()

        # Every subscription will be deleted, so we can clear the queues too.
        self._queues.clear()
        return

    @catch_exceptions(statistics.rest.ApiException)
    def list_metrics(self, include=None, interval="1d", **kwargs):
        """Get statistics.

        :param list[str] include: List of fields included in response.
            None, or an empty list will return all fields.
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
        include = Metric._map_includes(include)
        kwargs.update(dict(include=include, interval=interval))
        api = self._get_api(statistics.StatisticsApi)
        return PaginatedResponse(api.get_metrics, lwrap_type=Metric, **kwargs)

    def _subscription_handler(self, queue, device_id, path, callback_fn):
        while True:
            value = queue.get()
            callback_fn(device_id, path, value)

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
            kwargs['start'] = utils.force_utc(start, 'start', precision=3)
        # convert end into UTC RFC3339 format
        if end:
            kwargs['end'] = utils.force_utc(end, 'end', precision=3)
