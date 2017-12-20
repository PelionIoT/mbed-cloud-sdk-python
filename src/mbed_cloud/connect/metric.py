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
"""Metrics"""
from mbed_cloud.core import BaseObject
from six import iteritems


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
        """The number of observations received by Mbed Cloud Connect from the devices.

        The observations are pushed from the devices linked to the account to Mbed Cloud Connect
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
        """The number of successful proxy requests from Mbed Cloud Connect to devices.

        The proxy requests are made from Mbed Cloud Connect to devices linked to
        the account when you try to read or write values to device resources
        using Connect API endpoints.

        :rtype: int
        """
        return self._successful_proxy_requests

    @property
    def failed_proxy_requests(self):
        """The number of failed proxy requests from Mbed Cloud Connect to devices.

        The proxy requests are made from Mbed Cloud Connect to devices linked to
        the account when you try to read or write values to device resources
        using Connect API endpoints.

        :rtype: int
        """
        return self._failed_proxy_requests

    @property
    def successful_subscription_requests(self):
        """The number of successful subscription requests from Mbed Cloud Connect to devices.

        The subscription requests are made from Mbed Cloud Connect to devices linked to
        the account when you try to subscribe to a resource path using Connect API endpoints.

        :rtype: int
        """
        return self._successful_subscription_requests

    @property
    def failed_subscription_requests(self):
        """The number of failed subscription requests from Mbed Cloud Connect to devices.

        The subscription requests are made from Mbed Cloud Connect to devices linked to
        the account when you try to subscribe to a resource path using Connect API endpoints.

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
