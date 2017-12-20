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
"""Example showing extended usage of the webhook functionality.

Prerequisites

Two third party tools are used in this example:
    hug - a simple python3 webserver
    ngrok - a tool to tunnel public http requests to localhost

Install python libraries:
    pip install ngrok hug
Install ngrok from https://ngrok.com/
Follow the ngrok instructions to configure a tunnel
Set the resulting tunnel url in the variable below
Run the example with:
   hug -f examples/webhook_ngrok.py
Finally, visit 127.0.0.1:8000 in your browser to initiate the sequence
"""
from mbed_cloud.connect import ConnectAPI

import hug

import threading
import traceback

api = ConnectAPI()
ngrok_url = 'https://8b5e7ff1.ngrok.io'
resource_path = "/3/0"


def blocking_code(api):
    """The bulk of this example

    Registers a webhook with mbed cloud services, waits for data to arrive.
    """
    device = api.list_connected_devices().data[0]
    print('using device #', device.id)
    api.delete_device_subscriptions(device.id)

    try:
        print('setting webhook url to:', ngrok_url)
        api.update_webhook(ngrok_url)
        print('requesting resource value for:', resource_path)
        deferred = api.get_resource_value_async(device_id=device.id, resource_path=resource_path)
        print('waiting for async #', deferred.async_id)
        result = deferred.wait(15)
        print('webhook sent us:', result)
        return result
    except Exception:
        print(traceback.format_exc())
    finally:
        api.delete_webhook()
        print("Deregistered and unsubscribed from all resources. Exiting.")


@hug.put('/', parse_body=False)
def webhook_handler(request):
    """Receives the webhook from mbed cloud services

    Passes the raw http body directly to mbed sdk, to notify that a webhook was received
    """
    body = request.stream.read().decode('utf8')
    print('webhook handler saw:', body)
    api.notify_webhook_received(payload=body)
    print('keys handler', api._db.keys())


@hug.get('/')
def main():
    """Does something with our device

    We must do this in the same process to be certain we are sharing the api instance
    (ideally in future the async id database will be capable of being more than
    just a dictionary)
    """
    print('doing something!...')
    t = threading.Thread(target=blocking_code, kwargs=dict(api=api))
    t.daemon = True
    t.start()
    return 'ok'
