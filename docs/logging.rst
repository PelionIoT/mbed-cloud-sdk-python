Logging
~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud_sdk.logging import LoggingAPI
  api = LoggingAPI()

  # Get the 5 most recent device logs
  most_recent = api.list_device_logs(limit=5)

  # Get the next 5 device logs
  api.list_device_logs(limit=5, after=most_recent[-1].device_log_id)

  # Get the 10 oldest device logs
  api.list_device_logs(order='asc')

  # Get the 10 most recent logs for a specific device
  filters = {
    'device_id': '01588c0460c002420a012c0400000000',
  }
  api.list_device_logs(limit=10, filters=filters)

Reference
---------

.. automodule:: mbed_cloud_sdk.logging
  :members:

