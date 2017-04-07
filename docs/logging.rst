Logging
~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.logging import LoggingAPI
  api = LoggingAPI()

  # List device logs
  for d in api.list_device_logs():
    print(d.device_log_id)

  # 10 oldest device logs
  list(api.list_device_logs(order='asc'))[:10]

  # 10 most recent logs for a specific device
  filters = {
    'device_id': '01588c0460c002420a012c0400000000',
  }
  api.list_device_logs(limit=10, filters=filters)

  # Specific log
  api.get_device_log("0158b997cf7102420a013f0800000000")

Reference
---------

.. autoclass:: mbed_cloud.logging.LoggingAPI
  :members:

.. autoclass:: mbed_cloud.logging.DeviceLog
  :members:
  :inherited-members:
  :exclude-members: to_dict, to_str
