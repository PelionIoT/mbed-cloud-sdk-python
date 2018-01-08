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

import datetime
import json
import logging
import os
import traceback

from dateutil import parser as du_parser
from dateutil import tz as du_tz

import queue

import mbed_cloud

from builtins import str
from flask import Flask
from flask import jsonify
from flask import request
from six.moves import urllib

app = Flask(__name__)

# Empty on purpose. Initialized later.
MODULES = {}


def _call_api(module, method, kwargs):
    api = MODULES[module]
    method = getattr(api, method)
    return method(**kwargs)


def _get_params(request_headers):
    params = {}
    api_key = request_headers.get('X-API-KEY', os.environ.get('MBED_CLOUD_API_KEY', ''))
    host = request_headers.get('X-API-HOST', os.environ.get('MBED_CLOUD_API_HOST', ''))
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


def _get_type(obj):
    """Try to get value as original type, if possible. If not, we just return original value."""
    try:
        obj = json.loads(obj)
    except ValueError:
        pass
    if isinstance(obj, str) and len(obj) < 30:
        try:
            # some tests try tricking us with timezones - but we assume naive datetime objects in utc
            x = obj
            obj = du_parser.parse(obj).astimezone(tz=du_tz.tzoffset(None, 0)).replace(tzinfo=None)
            logging.info('datetime rehydrated: %s -> %s (%s)' % (x, obj, obj.isoformat()))
        except (TypeError, ValueError):
            pass
    return obj


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


@app.route("/ping")
def ping(methods=["GET"]):
    return 'pong'


@app.route("/_bye")
def bye(methods=["GET"]):
    request.environ.get('werkzeug.server.shutdown')()
    print('shutting down server')
    return 'shutdown'


@app.route("/_init")
def init(methods=["GET"]):
    """Initialse the APIs and pong the server to say it's up and ready."""
    # Check if api_key or host is provided through header
    params = _get_params(request.headers)

    # Initialise all the APIs with settings.
    global MODULES
    MODULES = {
        'account_management': mbed_cloud.AccountManagementAPI(params=params),
        'certificates': mbed_cloud.CertificatesAPI(params=params),
        'connect': mbed_cloud.ConnectAPI(params=params),
        'device_directory': mbed_cloud.DeviceDirectoryAPI(params=params),
        'update': mbed_cloud.UpdateAPI(params=params)
    }

    # Return empty JSON for now. Might change in the future.
    return jsonify({})


def default_handler(obj):
    """Serialises custom datatypes used in the SDK"""
    try:
        return obj.to_dict()
    except AttributeError:
        pass

    if isinstance(obj, datetime.datetime):
        return obj.isoformat()

    if isinstance(obj, queue.Queue):
        return {}

    raise TypeError("Object of type '%s' is not JSON serializable" %
                    obj.__class__.__name__)


@app.route("/<module>/<method>/")
def main(module, method, methods=["GET"]):
    """Main runner, responding to remote test calls - mapping module and method to SDK"""
    # Check if we've added arguments to function. Unquote and parse the query string,
    # preparing it for argument to function.
    qs = urllib.parse.unquote_plus(request.args.get("args", ""))
    # quote + char to prevent parse_qs from replacing '+' with space.
    qs = qs.replace('+', "%2B")
    args_struct = urllib.parse.parse_qs(qs)
    kwargs = dict(((k, _get_type(",".join(v))) for k, v in list(args_struct.items())))
    # We call the SDK module and function, with provided arguments.
    try:
        obj = _call_api(module, method, kwargs)
        serialised = json.dumps(obj if obj is not None else {}, default=default_handler)  # FIXME: remove 'or {}'
        return app.response_class(response=serialised, status=200, mimetype='application/json')
    except Exception as exc:
        raise ApiCallException(traceback.format_exc(limit=5), status_code=getattr(exc, 'status', 500))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # nosec (only used in testing)
