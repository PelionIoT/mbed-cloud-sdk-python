"""Custom decorators used in mbed_cloud."""
import functools
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
                raise(CloudApiException, value, traceback)
        return wrapped_f
    return wrap
