Devices
~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud_sdk.devices.connector import ConnectorAPI
  api = ConnectorAPI()

  # List all endpoints connected
  endpoints = api.list_endpoints()

  # Get resources of the first connected endpoint
  resources = api.list_resources(endpoints[0].name)

  # Get resources which are observable
  observable = filter(lambda r: r.obs, resources)

  # Subscribe to observable resource
  api.subscribe(endpoints[0].name, observable[0].path)

  # Register a webhook to send all updates to
  api.register_webhook(WEBHOOK_URL)
  
  # Remove webhook, and now use long-polling instead
  api.deregister_webhook()
  api.start_long_polling()

  # Read the current resource value by blocking
  resource_value = api.get_resource_value(endpoints[0].name, observable[0].path, sync=True)

  # Get next one, but do it async waiting for it to finish
  async_handler = api.get_resource_value(endpoints[0].name, observable[0].path)
  while not async_handler.is_done():
    time.sleep(1)
  if async_handler.error():
    raise Exception("Something went wrong: %s" % (async_handler.error())
  resource_value = async_handler.get_value()

  # 5 most recent devices from catalog, which are registered
  filters = { 'state': 'registered' }
  reg_devices = api.list_devices(limit=10, order='desc', filters=filters)

  # Get details about specific (registered) device
  api.get_device(reg_devices[0].device_id)

More examples
-------------

See full listing of examples `in the examples directory`_.

.. _in the examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples/devices

Reference
---------

.. automodule:: mbed_cloud_sdk.devices
  :members: DeviceAPI, AsyncConsumer
