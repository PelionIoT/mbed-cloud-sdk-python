"""Example showing basic usage of the webhook functionality."""
from mbed_cloud.devices import DeviceAPI
import time

BUTTON_RESOURCE = "/3200/0/5501"


def _main():
    api = DeviceAPI()
    endpoints = api.list_endpoints()
    if not endpoints:
        raise Exception("No endpints registered. Aborting")

    # First register to one webhook
    api.register_webhook("http://api.webhookinbox.com/i/JIYNNcZA/in/")
    time.sleep(2)

    # Then register to another one
    api.register_webhook("http://api.webhookinbox.com/i/qlo8pHTA/in/")
    api.subscribe(endpoints[0].name, BUTTON_RESOURCE)
    while True:
        print("Webhook registered. Listening to button updates...")

        time.sleep(10)
        break

    api.deregister_webhook()
    print("Deregistered and ubsubscribed to all resourced. Exiting.")

if __name__ == '__main__':
    _main()
