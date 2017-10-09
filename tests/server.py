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
"""Test server for remote execution of test tasks.

Run by:

    $ FLASK_APP=server.py flask run
    * Serving Flask app "server"
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""
from __future__ import absolute_import
from __future__ import unicode_literals

from builtins import str
from flask import Flask
from flask import jsonify
from flask import request
from mbed_cloud.account_management import AccountManagementAPI
from mbed_cloud.certificates import CertificatesAPI
from mbed_cloud.connect import ConnectAPI
from mbed_cloud.device_directory import DeviceDirectoryAPI
from mbed_cloud.update import UpdateAPI
from six.moves import urllib

import json
import queue
import sys
import traceback


app = Flask(__name__)

# Empty on purpose. Initialized later.
MODULES = {}


def _call_api(module, method, args):
    if module not in MODULES:
        raise ApiCallException("Invalid module: %r" % (module), status_code=400)

    # Get API object
    api = MODULES.get(module)

    # Get function contained in API object
    api_functions = list([f for f in dir(api) if not f.startswith("_")])
    if method not in api_functions:
        raise ApiCallException(
            "%r not found in %r" % (method, ", ".join(api_functions)),
            status_code=400)

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
            self.status = status_code
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
        'account_management': AccountManagementAPI(params=params),
        'certificates': CertificatesAPI(params=params),
        'connect': ConnectAPI(params=params),
        'device_directory': DeviceDirectoryAPI(params=params),
        'update': UpdateAPI(params=params)
    }

    # Return empty JSON for now. Might change in the future.
    return jsonify({})


@app.route("/<module>/<method>/")
def main(module, method, methods=["GET"]):
    """Main runner, responding to remote test calls - mapping module and method to SDK"""
    # Check if we've added arguments to function. Unquote and parse the query string,
    # preparing it for argument to function.
    qs = urllib.parse.unquote_plus(request.args.get("args", ""))
    # quote + char to prevent parse_qs from replacing '+' with space.
    qs = qs.replace('+', "%2B")
    args_struct = urllib.parse.parse_qs(qs)
    args = dict(((k, _get_type(",".join(v))) for k, v in list(args_struct.items())))
    # We call the SDK module and function, with provided arguments.
    try:
        return_obj = _call_api(module, method, args)

        # Handle functions which returns void
        if not return_obj:
            return jsonify({})

        # Check if we can concert to dict for inner objects in a list
        if isinstance(return_obj, list):
            return_obj = [_get_dict(o) for o in return_obj]

        # Check if we can convert to dict before returning (we can for most models)
        if not isinstance(return_obj, dict):
            return_obj = _get_dict(return_obj)

        # Check if type is Queue (device subscriptions), in which case we just return empty
        if isinstance(return_obj, queue.Queue):
            return_obj = {}

        return jsonify(return_obj)
    except Exception as e:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        message = str(e)
        if hasattr(e, "message"):
            message = e.message

        error_msg = "{}: An error occurred on line {} in statement '{}': {}".format(
            filename,
            line,
            text,
            message
        )

        # Set default status_code as 500
        status_code = 500
        # Check if error contains code status, return it if it does
        if hasattr(e, 'status'):
            status_code = e.status

        raise ApiCallException(str(error_msg), status_code=status_code)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
