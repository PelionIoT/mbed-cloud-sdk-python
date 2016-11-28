from mbed_cloud_sdk.devices.connector import ConnectorAPI

BUTTON_RESOURCE="/3200/0/5501"

def main():
    api = ConnectorAPI()
    api.start_long_polling()
    endpoints = api.list_endpoints()
    if not endpoints:
        raise Exception("No endpoints registered. Aborting")

    # Synchronously get the initial/current value of the resource
    value = api.get_resource_value(endpoints[0].name, BUTTON_RESOURCE, sync=True)

    # Register a subscription for new values
    queue = api.subscribe(endpoints[0].name, BUTTON_RESOURCE)
    while True:
        # Print the current value
        print "Current value: %r" % (value,)

        # Get a new value, using the subscriptions
        value = queue.get(timeout = 30)

if __name__ == "__main__":
    main()
