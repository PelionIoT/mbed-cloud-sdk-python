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
"""Custom decorators used in mbed_cloud."""
from __future__ import unicode_literals
from builtins import str
import functools
from six import reraise as raise_
import sys

from mbed_cloud.exceptions import CloudApiException


def catch_exceptions(*exceptions):
    """Catch all exceptions provided as arguments, and raise CloudApiException instead."""
    def wrap(fn):
        @functools.wraps(fn)
        def wrapped_f(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except exceptions:
                t, value, traceback = sys.exc_info()
                # If any resource does not exist, return None instead of raising
                if str(value.status) == '404':
                    return None
                e = CloudApiException(str(value), value.reason, value.status)
                raise_(CloudApiException, e, traceback)
        return wrapped_f
    return wrap
