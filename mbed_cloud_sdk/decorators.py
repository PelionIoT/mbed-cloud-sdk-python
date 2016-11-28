import sys
import functools

from mbed_cloud_sdk.exceptions import CloudApiException


def catch_exceptions(*exceptions):
    def wrap(fn):
        @functools.wraps(fn)
        def wrapped_f(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except exceptions:
                t, value, traceback = sys.exc_info()
                raise CloudApiException, value, traceback
        return wrapped_f
    return wrap
