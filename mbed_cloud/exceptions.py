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
"""All custom exceptions used in mbed_cloud."""
from __future__ import unicode_literals


class CloudApiException(Exception):
    """Exception thrown when an Exception is thrown is SDK"""

    def __init__(self, message, reason=None, status=400):
        """Initialize CloudApiException class"""
        super(CloudApiException, self).__init__(message)
        self.message = message
        self.status = status
        self.reason = reason


class CloudBackendError(CloudApiException):
    """Common exception thrown when ApiException is raised from backend API.

    CloudBackendError typically means that something went wrong in communicating
    with the cloud API. This can be authentication errors, connectivity issues
    or invalid usage of the API.
    """

    def __init__(self, e):
        """Init CloudBackendError class"""
        super(CloudBackendError, self).__init__(e.message, e.reason, e.status)


class CloudValueError(CloudApiException):
    """Common exception thrown when ApiException is raised from backend API.

    CloudApiException typically means that something went wrong in communicating
    with the cloud API. This can be authentication errors, connectivity issues
    or invalid usage of the API.
    """

    def __init__(self, message, reason=None, status=400):
        """Init CloudValueError class"""
        super(CloudValueError, self).__init__(message, reason, status)


class CloudUnhandledError(CloudApiException):
    """Thrown when function returns async consumer, but the error isn't handled.

    Only applicable when threads are setup and the user needs to call `is_done`
    and `error` before getting value.
    """

    def __init__(self, message, reason=None, status=400):
        """Init CloudUnhandledError class"""
        super(CloudUnhandledError, self).__init__(message, reason, status)


class CloudAsyncError(CloudApiException):
    """Thrown when running in synchronized/blocking mode, but an error is raised.

    Typically only found when an error is raised from the backend. Should be
    handled by the user.
    """

    def __init__(self, message, reason=None, status=400):
        """Init CloudAsyncError class"""
        super(CloudAsyncError, self).__init__(message, reason, status)


class CloudTimeoutError(CloudApiException):
    """Thrown when running in synchronized/blocking mode, and the request times out."""

    def __init__(self, message, reason=None, status=400):
        """Init CloudTimeoutError class"""
        super(CloudTimeoutError, self).__init__(message, reason, status)
