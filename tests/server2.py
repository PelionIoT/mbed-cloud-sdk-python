from collections import namedtuple
import traceback
import threading
import uuid

import flask
from flask import request
from flask import jsonify
from werkzeug.exceptions import HTTPException

from tests.module_runner import run_module

from mbed_cloud.core import BaseAPI

app = flask.Flask(__name__)
STORE = {}
MODULES = {vars(kls).get('api_name', kls.__name__): kls for kls in BaseAPI.__subclasses__()}
LockedInstance = namedtuple('LockedInstance', ['lock', 'instance'])
Item = namedtuple('Item', ['module', 'instance'])


class DoesNotExist(Exception):
    pass


def get_instance_or_404(item):
    instance = STORE.get(item)
    if not instance:
        raise DoesNotExist('No such instance %s' % (item,))
    return instance


@app.errorhandler(DoesNotExist)
def handle_error(exc):
    return jsonify(dict(
        message=str(exc)
    )), 404


@app.errorhandler(Exception)
def handle_error(exc):
    return jsonify(dict(
        traceback=traceback.format_exc(),
        message=str(exc),
    )), 500


@app.route('/<module>', methods=['POST'])
def create_instance(module):
    idee = str(uuid.uuid4().hex)
    lock = threading.Lock()
    item = Item(module, idee)
    instance = MODULES.get(module)(**request.get_json())
    STORE[item] = LockedInstance(lock, instance)
    return jsonify(idee)


@app.route('/<module>/<instance>/<method>', methods=['POST'])
def rpc(module, instance, method):
    item = Item(module, instance)
    locked_instance = get_instance_or_404(item)
    with locked_instance.lock:
        method = getattr(locked_instance.instance, method, None)
        if method is None:
            return jsonify(dict(message='No such method on %s' % (item,))), 404
        return app.response_class(
            response=run_module(method, request.get_json() or {}),
            status=200,
            mimetype='application/json'
        )


@app.route('/')
def list_modules():
    return jsonify(MODULES.keys())


@app.route('/<module>')
def list_instances(module):
    return jsonify([i.instance for i in STORE if i.module == module])


@app.route('/<module>/<instance>')
def get_instance(module, instance):
    item = Item(module, instance)
    locked_instance = get_instance_or_404(item)
    return jsonify({k: str(v) for k, v in vars(locked_instance.instance.__class__).items() if not k.startswith('_')})


@app.route('/<module>/<instance>', methods=['DELETE'])
def delete_instance(module, instance):
    item = Item(module, instance)
    locked_instance = get_instance_or_404(item)
    with locked_instance.lock:
        STORE.pop(item)
    return jsonify(True)


@app.route('/ping')
def ping():
    return jsonify('pong')


@app.route('/shutdown', methods=['PUT'])
def shutdown():
    # do some clean shutdown logic for coverage
    request.environ.get('werkzeug.server.shutdown')()
    return jsonify(True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
