# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Custom decorators used in mbed_cloud."""
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
                e = CloudApiException(str(value), value.reason, value.status)
                raise_(CloudApiException, e, traceback)
        return wrapped_f
    return wrap
