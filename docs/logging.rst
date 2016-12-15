Logging
~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.logging import LoggingAPI
  api = LoggingAPI()

  # 5 most recent device logs
  most_recent = api.list_device_logs(limit=5)

  # Next 5 device logs
  api.list_device_logs(limit=5, after=most_recent[-1].device_log_id)

  # 10 oldest device logs
  api.list_device_logs(order='asc')

  # 10 most recent logs for a specific device
  filters = {
    'device_id': '01588c0460c002420a012c0400000000',
  }
  api.list_device_logs(limit=10, filters=filters)

  # Specific log
  api.get_device_log("0158b997cf7102420a013f0800000000")

Reference
---------

.. automodule:: mbed_cloud.logging
  :members:

