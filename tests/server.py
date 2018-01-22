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

from collections import namedtuple
import datetime
import traceback
import threading
import uuid

import flask
from flask import request
from flask import jsonify

from module_runner import run_module

from mbed_cloud.core import BaseAPI
from mbed_cloud import __version__

app = flask.Flask(__name__)
STORE = {}
MODULE_REMAP = dict(  # to avoid writing these as attributes in the SDK, we map them here
    AccountManagementAPI='account_management',
    CertificatesAPI='certificates',
    ConnectAPI='connect',
    DeviceDirectoryAPI='device_directory',
    StubAPI='test_stub',
    UpdateAPI='update',
)
MODULES = {MODULE_REMAP[kls.__name__]: kls for kls in BaseAPI.__subclasses__()}
LockedInstance = namedtuple('LockedInstance', ['lock', 'instance', 'module', 'uuid', 'created_at'])

_BANNER = """
            _              _        _                 _     
           | |            | |      | |               | |    
  _ __ ___ | |__   ___  __| |   ___| | ___  _   _  __| |    
 | '_ ` _ \| '_ \ / _ \/ _` |  / __| |/ _ \| | | |/ _` |    
 | | | | | | |_) |  __/ (_| | | (__| | (_) | |_| | (_| |    
 |_| |_| |_|_.__/ \___|\__,_|  \___|_|\___/ \__,_|\__,_|    
                    | | |                                   
             ___  __| | | __   ___  ___ _ ____   _____ _ __ 
            / __|/ _` | |/ /  / __|/ _ \ '__\ \ / / _ \ '__|
            \__ \ (_| |   <   \__ \  __/ |   \ V /  __/ |   
            |___/\__,_|_|\_\  |___/\___|_|    \_/ \___|_|   

"""


def serialise_instance(instance):
    return dict(createdAt=instance.created_at.isoformat(), id=instance.uuid, module=instance.module)


class DoesNotExist(Exception):
    pass


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
        raise DoesNotExist('SDK server: no such instance %s' % (uuid,))
    return instance


@app.errorhandler(DoesNotExist)
def handle_missing_objects(exc):
    # missing objects are subtly different from missing API
    return jsonify(dict(
        message=str(exc)
    )), 404


@app.errorhandler(Exception)
def handle_unknown_errors(exc):
    return jsonify(dict(
        traceback=traceback.format_exc(),
        message=str(exc),
    )), 500


@app.route('/modules')
def modules_all():
    return jsonify(MODULES.keys())


@app.route('/modules/<module>/instances')
def modules_all_instances(module):
    return jsonify([serialise_instance(i) for i in STORE.values() if i.module == module])


@app.route('/modules/<module>/instances', methods=['POST'])
def modules_new_instance(module):
    instance = LockedInstance(
        lock=threading.Lock(),
        instance=MODULES.get(module)(**request.get_json()),
        module=module,
        uuid=str(uuid.uuid4().hex),
        created_at=datetime.datetime.utcnow(),
    )
    STORE[instance.uuid] = instance
    return jsonify(serialise_instance(instance))


@app.route('/instances')
def instances_all():
    return jsonify([serialise_instance(i) for i in STORE.values()])


@app.route('/instances/<uuid>')
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
def instances_methods(uuid):
    locked_instance = get_instance_or_404(uuid)
    return jsonify({k: str(v) for k, v in vars(locked_instance.instance.__class__).items() if not k.startswith('_')})


@app.route('/instances/<uuid>/methods/<method>', methods=['POST'])
def instances_call_rpc(uuid, method):
    locked_instance = get_instance_or_404(uuid)
    with locked_instance.lock:
        method = getattr(locked_instance.instance, method, None)
        if method is None:
            raise DoesNotExist('SDK server: no such method on %s' % (uuid,))
        return app.response_class(
            response=dict(payload=run_module(method, request.get_json() or {})),
            status=200,
            mimetype='application/json'
        )


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
    # do some clean shutdown logic for coverage
    request.environ.get('werkzeug.server.shutdown')()
    return app.response_class(
        response=None,
        status=202,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
