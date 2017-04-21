Connect
~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.connect import ConnectAPI
  api = ConnectAPI()

  # List all endpoints connected
  devices = list(api.list_connected_devices())

  # Get resources of the first connected endpoint
  resources = api.list_resources(devices[0].id)

  # Get resources which are observable
  observable = filter(lambda r: r.observable, resources)

  # Subscribe to observable resource
  api.subscribe(endpoints[0].name, observable[0].path)

  # Register a webhook to send all updates to
  api.update_webhook(WEBHOOK_URL)

  # Remove webhook, and now use long-polling instead
  api.delete_webhook()
  api.start_notifications()

  # Read the current resource value by blocking
  resource_value = api.get_resource_value(devices[0].id, observable[0].path)

  # Get next one, but do it async waiting for it to finish
  async_handler = api.get_resource_value_async(devices[0].id, observable[0].path)
  while not async_handler.is_done:
    time.sleep(1)
  if async_handler.error:
    raise Exception("Something went wrong: %s" % (async_handler.error)
  resource_value = async_handler.value

.. code-block:: python

  from mbed_cloud.connect import ConnectAPI
  api = ConnectAPI()

  # Get Metrics from the last 30 days grouped in 1 day interval
  for metric in api.get_metrics(interval="1d", period="30d"):
      print(metric)


More examples
-------------

See full listing of examples `in the examples directory`_.

.. _in the examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples/connect

Reference
---------

.. automodule:: mbed_cloud.connect
  :members: ConnectAPI, AsyncConsumer

.. autoclass:: mbed_cloud.connect.ConnectedDevice
  :members:
  :inherited-members:
  :exclude-members: to_dict, to_str

.. autoclass:: mbed_cloud.connect.Metric
  :members:
  :inherited-members:
  :exclude-members: object, etag, to_str, to_dict

.. autoclass:: mbed_cloud.connect.Resource
  :members:

.. autoclass:: mbed_cloud.connect.Webhook
  :members:
  :inherited-members:
  :exclude-members: to_dict, to_str
