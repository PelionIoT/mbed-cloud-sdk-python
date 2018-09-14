"""Logging control"""
import logging
import contextlib

LOGGER = logging.getLogger(__file__)

# TODO: how to restrict capture to a single session / SDK Client


def set_http_level(level):
    # adjusts the http logging level
    # inspired by:
    # https://stackoverflow.com/a/24588289/4628768

    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(level)

    try:
        from http.client import HTTPConnection  # py3
    except ImportError:
        from httplib import HTTPConnection  # py2

    HTTPConnection.debuglevel = 1 if level == logging.DEBUG else 0


@contextlib.contextmanager
def http_logging_enabled():
    # if the user has no logging set at all ...
    logging.basicConfig(level=logging.DEBUG)

    set_http_level(logging.DEBUG)
    try:
        yield
    finally:
        set_http_level(logging.WARNING)
