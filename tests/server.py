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
"""Test server for remote execution of test tasks.

Run by:

    $ FLASK_APP=server.py flask run
    * Serving Flask app "server"
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""
from __future__ import absolute_import
from flask import Flask
from flask import jsonify
from flask import request
from mbed_cloud.access import AccessAPI
from mbed_cloud.devices import DeviceAPI
from mbed_cloud.logging import LoggingAPI
from mbed_cloud import PaginatedResponse
from mbed_cloud.statistics import StatisticsAPI
from mbed_cloud.update import UpdateAPI
from urllib import unquote
from urlparse import parse_qs

import json
import Queue
import sys
import traceback


app = Flask(__name__)

# Empty on purpose. Initialized later.
MODULES = {}


def _call_api(module, method, args):
    if module not in MODULES:
        return "Invalid module: %r" % (module)

    # Get API object
    api = MODULES.get(module)

    # Get function contained in API object
    api_functions = list(filter(lambda f: not f.startswith("_"), dir(api)))
    if method not in api_functions:
        return "%r not found in %r" % (method, ", ".join(api_functions))

    # Call SDK function
    return getattr(api, method)(**args)


def _get_params(request_headers):
    params = {}
    api_key = request_headers.get('X-API-KEY', '')
    host = request_headers.get('X-API-HOST', '')
    if api_key:
        params["api_key"] = api_key
    if host:
        params["host"] = host
    return params


def _fix_paginated_response(resp):
    return_obj = list(resp)

    # Convert each inner object to Python dictionary.
    if return_obj and hasattr(return_obj[0], 'to_dict'):
        return_obj = [o.to_dict() for o in return_obj]

    return return_obj


def _get_type(v):
    """Try to get value as original type, if possible. If not, we just return original value."""
    # Check int
    try:
        return int(v)
    except ValueError:
        pass

    # Check float
    try:
        return float(v)
    except ValueError:
        pass

    # Check JSON
    try:
        return json.loads(v)
    except ValueError:
        pass

    # Return original value
    return v


class ApiCallException(Exception):
    """HTTP exception, accepting dynamic status code.

    http://flask.pocoo.org/docs/0.12/patterns/apierrors/
    """

    def __init__(self, message, status_code=None, payload=None):
        """Initialise the exception with custom message."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Convert to dict in prep for JSON output."""
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(ApiCallException)
def _handle_api_call_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def _get_dict(obj):
    if hasattr(obj, 'to_dict'):
        obj = obj.to_dict()
    return obj


@app.route("/_init")
def init(methods=["GET"]):
    """Initialse the APIs and pong the server to say it's up and ready."""
    # Check if api_key or host is provided through header
    params = _get_params(request.headers)

    # Initialise all the APIs with settings.
    global MODULES
    MODULES = {
        'access': AccessAPI(params=params),
        'devices': DeviceAPI(params=params),
        'logging': LoggingAPI(params=params),
        'statistics': StatisticsAPI(params=params),
        'update': UpdateAPI(params=params)
    }

    # Return empty JSON for now. Might change in the future.
    return jsonify({})


@app.route("/<module>/<method>/")
def main(module, method, methods=["GET"]):
    """Main runner, responding to remote test calls - mapping module and method to SDK"""
    # Check if we've added arguments to function. Unquote and parse the query string,
    # preparing it for argument to function.
    qs = unquote(request.args.get("args", ""))
    args_struct = parse_qs(qs)
    args = dict(((k, _get_type(",".join(v))) for k, v in args_struct.iteritems()))

    # We call the SDK module and function, with provided arguments.
    try:
        return_obj = _call_api(module, method, args)

        # Handle functions which returns void
        if not return_obj:
            return jsonify({})

        # Check if return object is of type PaginatedResponse, which we'll
        # handle specially by just returning the first page as an array.
        if isinstance(return_obj, PaginatedResponse):
            return_obj = _fix_paginated_response(return_obj)

        # Check if we can concert to dict for inner objects in a list
        if isinstance(return_obj, list):
            return_obj = map(lambda o: _get_dict(o), return_obj)

        # Check if we can convert to dict before returning (we can for most models)
        if not isinstance(return_obj, dict):
            return_obj = _get_dict(return_obj)

        # Check if type is Queue (device subscriptions), in which case we just return empty
        if isinstance(return_obj, Queue.Queue):
            return_obj = {}

        return jsonify(return_obj)
    except Exception as e:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        error_msg = "{}: An error occurred on line {} in statement '{}': {}".format(
            filename,
            line,
            text,
            str(e)
        )

        # Set defaul status_code as 500
        status_code = 500
        # Check if error contains code status, return it if it does
        if hasattr(e, 'status'):
            status_code = e.status

        raise ApiCallException(str(error_msg), status_code=status_code)


if __name__ == "__main__":
    app.run(port=5000)
