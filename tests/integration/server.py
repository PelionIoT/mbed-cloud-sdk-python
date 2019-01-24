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
"""This test server is executed by CI test runs with a common"""

import logging
import queue
from collections import namedtuple
import datetime
import traceback
import threading
import uuid
import re
import json

from dateutil import parser as du_parser
from dateutil import tz as du_tz
from builtins import str

import flask
from flask import request
from flask import jsonify
from werkzeug.exceptions import HTTPException, NotFound, MethodNotAllowed

from mbed_cloud.core import BaseAPI
from mbed_cloud import __version__
from mbed_cloud import pagination
from mbed_cloud.core import BaseObject

from mbed_cloud.sdk.entities import __all__ as entity_list
from mbed_cloud.sdk import SDK


LOG = logging.getLogger(__name__)

app = flask.Flask(__name__)
STORE = {}
MODULE_REMAP = dict(  # to avoid writing these as attributes in the SDK, we map them here
    AccountManagementAPI='account_management',
    BillingAPI='billing',
    BootstrapAPI='bootstrap',
    CertificatesAPI='certificates',
    ConnectAPI='connect',
    DeviceDirectoryAPI='device_directory',
    EnrollmentAPI='enrollment',
    StubAPI='test_stub',
    UpdateAPI='update',
)
MODULES = {MODULE_REMAP[kls.__name__]: kls for kls in BaseAPI.__subclasses__()}
LockedInstance = namedtuple('LockedInstance', ['lock', 'instance', 'module', 'entity', 'uuid', 'created_at'])

SDK_ENTITY_NAME = "Sdk"

_BANNER = """
______    _ _              _________  ___
| ___ \  | (_)             |  _  \  \/  |
| |_/ /__| |_  ___  _ __   | | | | .  . |
|  __/ _ \ | |/ _ \| '_ \  | | | | |\/| |
| | |  __/ | | (_) | | | | | |/ /| |  | |
\_|  \___|_|_|\___/|_| |_| |___/ \_|  |_/
______      _   _                   ___________ _   __
| ___ \    | | | |                 /  ___|  _  \ | / /
| |_/ /   _| |_| |__   ___  _ __   \ `--.| | | | |/ / 
|  __/ | | | __| '_ \ / _ \| '_ \   `--. \ | | |    \ 
| |  | |_| | |_| | | | (_) | | | | /\__/ / |/ /| |\  \ 
\_|   \__, |\__|_| |_|\___/|_| |_| \____/|___/ \_| \_/
       __/ |                                          
      |___/                                           
 _____         _     _____ 
|_   _|       | |   /  ___|
  | | ___  ___| |_  \ `--.  ___ _ ____   _____ _ __   
  | |/ _ \/ __| __|  `--. \/ _ \ '__\ \ / / _ \ '__|
  | |  __/\__ \ |_  /\__/ /  __/ |   \ V /  __/ |
  \_/\___||___/\__| \____/ \___|_|    \_/ \___|_|

"""


def serialise(obj):
    """Serialises custom datatypes used in the SDK"""
    if isinstance(obj, datetime.datetime):
        # maybe assume UTC (as deserialise does the reverse)
        return obj.replace(tzinfo=du_tz.tzutc()).isoformat()

    if isinstance(obj, queue.Queue):
        return {}

    if isinstance(obj, (pagination.PaginatedResponse, BaseObject)):
        return obj.to_dict()

    try:
        return obj.to_dict()
    except AttributeError:
        pass

    raise TypeError("Object of type '%s' is not JSON serializable" %
                    obj.__class__.__name__)


def deserialise(obj):
    """Converts objects from custom json-rpc to Python"""
    if isinstance(obj, str) and 12 < len(obj) < 40:
        try:
            # some tests try tricking us with timezones - but we assume naive datetime objects in utc
            # 1970-01-21T21:14:37+12:45 -> 1970-01-21 08:29:37 (1970-01-21T08:29:37)
            x = obj
            obj = du_parser.parse(obj).astimezone(tz=du_tz.tzutc()).replace(tzinfo=None)
            LOG.info('datetime rehydrated: %s -> %s (%s)' % (x, obj, obj.isoformat()))
        except Exception as e:
            LOG.debug('not a date: %s (%s)' % (obj, e))
    return obj


def run_module(method, kwargs):
    """Runs the requested method and returns result as json string"""
    for k, v in kwargs.items():
        kwargs[k] = deserialise(v)

    result = dict(payload=method(**kwargs))

    return json.dumps(result, default=serialise)


def serialise_instance(instance):
    if instance.module:
        return dict(created_at=instance.created_at.isoformat(), id=instance.uuid, module=instance.module)
    else:
        return dict(created_at=instance.created_at.isoformat(), id=instance.uuid, entity=instance.entity)


@app.before_first_request
def startup():
    print('{banner}{line}\n\n\tcRPC server\tSDK version: {version}\n'.format(
        banner=_BANNER,
        line=30*' =',
        version=__version__
    ))


def get_instance_or_404(uuid):
    instance = STORE.get(uuid)
    if not instance:
        raise NotFound('404 Not Found: SDK server has no such instance %r' % (uuid,))
    return instance


@app.errorhandler(HTTPException)
def handle_missing_objects(exc):
    """Let through all raised HTTP errors with formatting."""
    return jsonify(dict(
        message=str(exc)
    )), exc.code


@app.errorhandler(Exception)
def handle_unknown_errors(exc):
    """All not HTTP errors should result in a formatted server error."""
    return jsonify(dict(
        traceback=traceback.format_exc(),
        message=str(exc),
    )), 500


@app.route('/modules')
def modules_all():
    return jsonify(list(MODULES.keys()))


@app.route('/modules/<module>/instances')
def modules_all_instances(module):
    return jsonify([serialise_instance(i) for i in STORE.values() if i.module == module])


@app.route('/modules/<module>/instances', methods=['POST'])
def modules_new_instance(module):
    try:
        module_class = MODULES[module]
    except KeyError:
        raise NotFound("Module '%s' cannot be found." % module)

    instance = LockedInstance(
        lock=threading.Lock(),
        instance=module_class(params=request.get_json()),
        module=module,
        entity=None,
        uuid=str(uuid.uuid4().hex),
        created_at=datetime.datetime.utcnow(),
    )
    STORE[instance.uuid] = instance
    response = app.response_class(
        response=json.dumps(serialise_instance(instance)),
        status=201,
        mimetype='application/json'
    )
    return response


@app.route('/instances')
def instances_all():
    return jsonify([serialise_instance(i) for i in STORE.values() if i.module is not None])


@app.route('/instances/<uuid>')
@app.route('/foundation/instances/<uuid>')
def instances_detail(uuid):
    return jsonify(serialise_instance(get_instance_or_404(uuid)))


@app.route('/instances/<uuid>', methods=['DELETE'])
def instances_delete(uuid):
    locked_instance = get_instance_or_404(uuid)
    with locked_instance.lock:
        try:
            locked_instance.instance.stop_notifications()
        except AttributeError:
            pass
        STORE.pop(uuid)
    return jsonify(True)


@app.route('/instances/<uuid>/methods')
@app.route('/foundation/instances/<uuid>/methods')
def instances_methods(uuid):
    locked_instance = get_instance_or_404(uuid)
    return jsonify([
        dict(name=k, signature=str(v))
        for k, v in vars(locked_instance.instance.__class__).items()
        if not k.startswith('_')
    ])


@app.route('/instances/<uuid>/methods/<method>', methods=['POST'])
@app.route('/foundation/instances/<uuid>/methods/<method>', methods=['POST'])
def instances_call_rpc(uuid, method):
    locked_instance = get_instance_or_404(uuid)
    with locked_instance.lock:
        method = getattr(locked_instance.instance, method, None)
        if method is None:
            raise NotFound('SDK server: no such method on %s' % (uuid,))
        if not callable(method):
            raise MethodNotAllowed("Method '%s' is not callable" % method)
        return app.response_class(
            response=run_module(method, request.get_json() or {}),
            status=200,
            mimetype='application/json'
        )


@app.route('/foundation/sdk/instances')
def list_foundation_sdk_instances():
    """List all top level SDK instances"""
    return jsonify([serialise_instance(instance) for instance in STORE.values() if instance.entity == SDK_ENTITY_NAME])


@app.route('/foundation/sdk/instances', methods=['POST'])
def create_foundation_sdk_instance():
    """Create an instance of a Foundation SDK Entity"""
    instance = LockedInstance(
        lock=threading.Lock(),
        instance=SDK(**(request.get_json() or {})),
        module=None,
        entity=SDK_ENTITY_NAME,
        uuid=str(uuid.uuid4().hex),
        created_at=datetime.datetime.utcnow(),
    )
    STORE[instance.uuid] = instance
    response = app.response_class(
        response=json.dumps(serialise_instance(instance)),
        status=201,
        mimetype='application/json'
    )
    return response


@app.route('/foundation/entities')
def list_foundation_entities():
    """List all entities."""
    # Use the __all__ list created during code generation.
    return jsonify(entity_list)


@app.route('/foundation/entities/<entity>/instances')
def list_foundation_entity_instances(entity):
    """List all entity instances"""
    return jsonify([serialise_instance(instance) for instance in STORE.values() if instance.entity == entity])


@app.route('/foundation/entities/<entity>/instances', methods=['POST'])
def create_foundation_entity_instance(entity):
    """Create an instance of a Foundation SDK Entity"""
    # Get an SDK class and use the configuration generation behaviour to pass in parameters
    sdk_instance = SDK(**(request.get_json() or {}))

    try:
        # Entity names are PascalCase, SDK entity methods are snake case.
        method_name = re.sub('(?<!^)(?=[A-Z])', '_', entity).lower()
        entity_class = getattr(sdk_instance.entities, method_name)
    except AttributeError:
        raise NotFound("Entity '%s' which was reformatted to '%s' cannot be found." % (entity, method_name))

    instance = LockedInstance(
        lock=threading.Lock(),
        instance=entity_class(),
        module=None,
        entity=entity,
        uuid=str(uuid.uuid4().hex),
        created_at=datetime.datetime.utcnow(),
    )
    STORE[instance.uuid] = instance
    response = app.response_class(
        response=json.dumps(serialise_instance(instance)),
        status=201,
        mimetype='application/json'
    )
    return response

@app.route('/foundation/instances')
def list_foundation_instances():
    return jsonify([serialise_instance(instance) for instance in STORE.values() if instance.entity is not None])


@app.route('/foundation/instances/<instance_id>', methods=['DELETE'])
def delete_foundation_instance(instance_id):
    """Delete a Foundation SDK Entity instance."""
    locked_instance = get_instance_or_404(instance_id)
    with locked_instance.lock:
        try:
            locked_instance.instance.stop_notifications()
        except AttributeError:
            pass
        STORE.pop(instance_id)
    return '', 204


@app.route('/ping')
def server_ping():
    return jsonify('pong')


@app.route('/reset', methods=['POST'])
def server_reset():
    for uuid in list(STORE):
        instances_delete(uuid)
    return app.response_class(
        response=None,
        status=205,
    )


@app.route('/shutdown', methods=['POST'])
def server_shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down', 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
