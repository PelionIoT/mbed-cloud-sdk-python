# ---------------------------------------------------------------------------
# Pelion Device Management SDK
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

== What's happening here?

This example implements the following sequence:
(each column is a thread of control)

|app thread|            |server thread|        |mbed cloud|
register webhook
                                                webhook created
request resource value
                                                value requested
                        asyncid stored
wait for value
    -                       -                       -
                                                a value appears!
                                                trigger webhook
                        webhook received
                        notify SDK
value received


== Prerequisites

Two third-party tools are used in this example:
- hug: a simple python3 webserver
- ngrok: a tool to tunnel public http requests to localhost
        (because webhook urls must be on the public internet
        and presumably your development machine isn't...)
        Other providers are available, such as https://localtunnel.github.io


== Instructions

- Install python libraries: `pip install ngrok hug`
- Install ngrok from https://ngrok.com/
    - Follow the ngrok documentation to configure a tunnel:
    - `ngrok http 8000`
- Run this Python SDK example in a terminal with the following command:
    - `hug -f examples/webhook_ngrok.py https://YOUR_NGROK_ID_GOES_HERE.ngrok.io`
- Visit `https://YOUR_NGROK_ID_GOES_HERE.ngrok.io/start` to initiate the sequence
  (use a GET request or point your web browser at this url)
- View the result of the application in the terminal

"""

# an example: using a webhook for handling notifications from mbed cloud
from mbed_cloud.connect import ConnectAPI

import hug

import os
import sys
import threading
import traceback

# we must disable automatic creation of a long-poll thread
# as webhooks and long polling are mutually exclusive on mbed cloud
api = ConnectAPI(dict(autostart_notification_thread=False))
ngrok_url = sys.argv[-1] if len(sys.argv) == 4 else (
    os.environ.get('NGROK_URL') or
    'https://YOUR_NGROK_ID_GOES_HERE.ngrok.io'
)
os.environ['NGROK_URL'] = ngrok_url
resource_path = "/3/0/2"


def my_application(api):
    """An example application.

    - Registers a webhook with mbed cloud services
    - Requests the value of a resource
    - Prints the value when it arrives
    """
    device = api.list_connected_devices().first()
    print('using device #', device.id)
    api.delete_device_subscriptions(device.id)

    try:
        print('setting webhook url to:', ngrok_url)
        api.update_webhook(ngrok_url)
        print('requesting resource value for:', resource_path)
        deferred = api.get_resource_value_async(device_id=device.id, resource_path=resource_path)
        print('waiting for async #', deferred.async_id)
        result = deferred.wait(15)
        print('webhook sent us this payload value:', repr(result))
        return result
    except Exception:
        print(traceback.format_exc())
    finally:
        api.delete_webhook()
        print("Deregistered and unsubscribed from all resources. Exiting.")
        exit(1)


@hug.put('/', parse_body=False)
def webhook_handler(request):
    """Receives the webhook from mbed cloud services

    Passes the raw http body directly to mbed sdk, to notify that a webhook was received
    """
    body = request.stream.read().decode('utf8')
    print('webhook handler saw:', body)
    api.notify_webhook_received(payload=body)

    # nb. protected references are not part of the API.
    # this is just to demonstrate that the asyncid is stored
    print('key store contains:', api._db.keys())


@hug.get('/start')
def start_sequence():
    """Start the demo sequence

    We must start this thread in the same process as the webserver to be certain
    we are sharing the api instance in memory.

    (ideally in future the async id database will be capable of being more than
    just a dictionary)
    """
    print('getting started!...')
    t = threading.Thread(target=my_application, kwargs=dict(api=api))
    t.daemon = True
    t.start()
    return 'ok, starting webhook to: %s' % (ngrok_url,)

# end of example
