Device Directory
~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.device_directory import DeviceDirectoryAPI
  api = DeviceDirectoryAPI()

  # 5 most recent devices from catalog, which are registered
  filters = { 'state': 'registered' }
  reg_devices = list(api.list_devices(limit=10, order='desc', filters=filters))

  # Get details about specific (registered) device
  api.get_device(reg_devices[0].id)

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

More examples
-------------

See full listing of examples `in the examples directory`_.

.. _in the examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples/device_directory

Reference
---------

.. automodule:: mbed_cloud.device_directory
  :members: DeviceDirectoryAPI

.. autoclass:: mbed_cloud.device_directory.Device
  :members:
  :inherited-members:
  :exclude-members: to_dict, to_str

.. autoclass:: mbed_cloud.device_directory.DeviceLog
  :members:
  :inherited-members:
  :exclude-members: to_dict, to_str

.. autoclass:: mbed_cloud.device_directory.Query
  :members:
  :inherited-members:
  :exclude-members: to_dict, to_str
