Devices
~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.devices import DeviceAPI
  api = DeviceAPI()

  # List all endpoints connected
  devices = list(api.list_connected_devices())

  # Get resources of the first connected endpoint
  resources = api.list_resources(devices[0].id)

  # Get resources which are observable
  observable = filter(lambda r: r.observable, resources)

  # Subscribe to observable resource
  api.subscribe(endpoints[0].name, observable[0].path)

  # Register a webhook to send all updates to
  api.add_webhook(WEBHOOK_URL)

  # Remove webhook, and now use long-polling instead
  api.delete_webhook()
  api.start_long_polling()

  # Read the current resource value by blocking
  resource_value = api.get_resource_value(observable[0].id, observable[0].uri)

  # Get next one, but do it async waiting for it to finish
  async_handler = api.get_resource_value_async(observable[0].id, observable[0].uri)
  while not async_handler.is_done:
    time.sleep(1)
  if async_handler.error:
    raise Exception("Something went wrong: %s" % (async_handler.error)
  resource_value = async_handler.value

  # 5 most recent devices from catalog, which are registered
  filters = { 'state': 'registered' }
  reg_devices = list(api.list_devices(limit=10, order='desc', filters=filters))

  # Get details about specific (registered) device
  api.get_device(reg_devices[0].id)

More examples
-------------

See full listing of examples `in the examples directory`_.

.. _in the examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples/devices

Reference
---------

.. automodule:: mbed_cloud.devices
  :members: DeviceAPI, AsyncConsumer

.. autoclass:: mbed_cloud.devices.DeviceDetail
  :members:
  :inherited-members:
  :exclude-members: etag, object, to_dict, to_str

.. autoclass:: mbed_cloud.devices.Filter
  :members:
  :inherited-members:
  :exclude-members: etag, object, to_dict, to_str

.. autoclass:: mbed_cloud.devices.Resource
  :members:
