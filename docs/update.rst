Update
~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.update import UpdateAPI
  api = UpdateAPI()

  # Get 5 latest firmware images
  images = api.list_firmware_images(limit=5)

Reference
---------

.. automodule:: mbed_cloud.update
  :members:

