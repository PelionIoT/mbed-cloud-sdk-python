Bootstrap
~~~~~~~~~
For configuring devices using Pre Shared Keys.

Usage
-----

.. code-block:: python

  from mbed_cloud import BootstrapAPI
  api = BootstrapAPI()

  api.add_psk(endpoint_name='your device name here', secret_hex='0123456789ABCDEF')


Reference
---------

.. automodule:: mbed_cloud.bootstrap
  :members: BootstrapAPI, PreSharedKey
