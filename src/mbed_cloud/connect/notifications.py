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
"""Notifications"""
import functools
import logging
import threading
import time
import random

import six

from mbed_cloud import tlv

from mbed_cloud._backends import mds

from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.exceptions import CloudAsyncError
from mbed_cloud.exceptions import CloudTimeoutError
from mbed_cloud.exceptions import CloudUnhandledError

LOG = logging.getLogger(__name__)


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

    def wait(self, timeout=0):
        """Blocks until timeout (seconds) or forever

        :param timeout: time to wait, in seconds
        :return:
        """
        start_time = time.time()

        # We return synchronously, so we block in a busy loop waiting for the
        # request to be done.
        while not self.is_done:
            duration = time.time() - start_time
            if timeout and duration > timeout:
                raise CloudTimeoutError(
                    "Timeout getting async value. Timeout: %d seconds" % timeout
                )
            time.sleep(0.1)

        # If we get an any status code other than a 2xx we raise an exception to the user, which can then be handled
        # accordingly.
        status_code, error_msg, payload = self.check_error()
        if not self._status_ok(status_code):
            raise CloudAsyncError("Async response for '%s' returned an error." % self.async_id,
                                  reason=error_msg,
                                  status=status_code)

        value = self.value
        if isinstance(value, six.binary_type):
            value = value.decode('utf-8')
        return value

    @staticmethod
    def _status_ok(status_code):
        """Check the status code is in the 2xx range"""
        return 200 <= status_code <= 299

    @property
    def is_done(self):
        """Check if the DB has received an event with the specified async ID.

        :return: Whether the async request has finished or not
        :rtype: bool
        """
        return self.async_id in self.db

    def check_error(self):
        """Check if the async response is an error.

        Take care to call `is_done` before calling `error`. Note that the error
        messages are always encoded as strings.

        :raises CloudUnhandledError: When not checking `is_done` first
        :return: status_code, error_msg, payload
        :rtype: tuple
        """
        if not self.is_done:
            raise CloudUnhandledError("Need to check if request is done, before checking for error")
        response = self.db[self.async_id]
        error_msg = response["error"]
        status_code = int(response["status_code"])
        payload = response["payload"]
        return status_code, error_msg, payload

    @property
    def error(self):
        """Check if the async response is an error.

        Take care to call `is_done` before calling `error`. Note that the error
        messages are always encoded as strings.

        :raises CloudUnhandledError: When not checking `is_done` first
        :return: the error value/payload, if found.
        :rtype: str
        """
        status_code, error_msg, payload = self.check_error()

        if status_code != 200 and not error_msg and not payload:
            return "Async error (%s). Status code: %r" % (self.async_id, status_code)
        return error_msg

    @property
    def value(self):
        """Get the value of the finished async request, if it is available.

        :raises CloudUnhandledError: When not checking value of `error` or `is_done` first
        :return: the payload value
        :rtype: str
        """
        status_code, error_msg, payload = self.check_error()

        if not self._status_ok(status_code) and not payload:
            raise CloudUnhandledError("Attempted to decode async request which returned an error.",
                                      reason=error_msg,
                                      status=status_code)
        return self.db[self.async_id]["payload"]

    def to_dict(self):
        """JSON serializable representation of the consumer."""
        return str(self)

    def __repr__(self):
        """String representation of this AsyncConsumer."""
        return self.async_id


def handle_channel_message(db, queues, b64decode, notification_object):
    """Handler for notification channels

    Given a NotificationMessage object, update internal state, notify
    any subscribers and resolve async deferred tasks.

    :param db:
    :param queues:
    :param b64decode:
    :param notification_object:
    :return:
    """
    for notification in getattr(notification_object, 'notifications') or []:
        # Ensure we have subscribed for the path we received a notification for
        subscriber_queue = queues[notification.ep].get(notification.path)
        if subscriber_queue is None:
            LOG.debug(
                "Ignoring notification on %s (%s) as no subscription is registered",
                notification.ep,
                notification.path
            )
            break

        payload = tlv.decode(
            payload=notification.payload,
            content_type=notification.ct,
            decode_b64=b64decode
        )
        subscriber_queue.put(payload)

    for response in getattr(notification_object, 'async_responses') or []:
        payload = tlv.decode(
            payload=response.payload,
            content_type=response.ct,
            decode_b64=b64decode
        )
        db.update({response.id: dict(
            payload=payload,
            error=response.error,
            status_code=response.status
        )})


class NotificationsThread(threading.Thread):
    """A thread object"""

    def __init__(self, db, queues, b64decode=True, notifications_api=None,
                 subscription_manager=None):
        """Stoppable thread"""
        super(NotificationsThread, self).__init__()

        self.db = db
        self.queues = queues
        self.notifications_api = notifications_api
        self.subscription_manager = subscription_manager

        self._b64decode = b64decode

        self._stopping = False
        self._stopped = threading.Event()

    @catch_exceptions(mds.rest.ApiException)
    @functools.wraps(threading.Thread.run)
    def run(self):
        """Thread main loop"""
        retries = 0
        try:
            while not self._stopping:
                try:
                    data = self.notifications_api.long_poll_notifications()
                except mds.rest.ApiException as e:
                    # An HTTP 410 can be raised when stopping so don't log anything
                    if not self._stopping:
                        backoff = 2 ** retries - random.randint(int(retries / 2), retries)
                        LOG.error('Notification long poll failed with exception (retry in %d seconds):\n%s', backoff, e)
                        retries += 1
                        # Backoff for an increasing amount of time until we have tried 10 times, then reset the backoff.
                        if retries >= 10:
                            retries = 0
                        time.sleep(backoff)
                else:
                    handle_channel_message(
                        db=self.db,
                        queues=self.queues,
                        b64decode=self._b64decode,
                        notification_object=data
                    )
                    if self.subscription_manager:
                        self.subscription_manager.notify(data.to_dict())
        finally:
            self._stopped.set()

    def stop(self):
        """Request thread stop"""
        self._stopping = True
        return self._stopped
