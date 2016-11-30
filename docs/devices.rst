Devices
~~~~~~~

Listing current devices and resources
-------------------------------------

.. code-block:: python

  >>> from mbed_cloud_sdk.devices.connector import ConnectorAPI
  >>> api = ConnectorAPI()
  >>> api.list_endpoints()
  [{'name': '0158685a40aa02420a014c0600000000',
    'q': None,
    'status': 'ACTIVE',
    'type': 'default'}]
  >>> api.list_resources('0158685a40aa02420a014c0600000000')
  [{'obs': False, 'rt': 'Blink', 'type': '', 'uri': '/3201/0/5850'},
   {'obs': False, 'rt': 'Pattern', 'type': '', 'uri': '/3201/0/5853'},
   {'obs': True, 'rt': 'Button', 'type': '', 'uri': '/3200/0/5501'},
   {'obs': False, 'rt': None, 'type': '', 'uri': '/3/0'}]

More examples
-------------

See full listing of examples `in the examples directory`_.

.. _in the examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples/devices

Reference
---------

.. automodule:: mbed_cloud_sdk.devices
  :members: DeviceAPI, AsyncConsumer
