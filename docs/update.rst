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

.. autoclass:: mbed_cloud.update.UpdateAPI
  :members:

.. autoclass:: mbed_cloud.update.Firmware
  :members:
  :inherited-members:
  :exclude-members: object, etag, to_str, to_dict, image_id

.. autoclass:: mbed_cloud.update.Manifest
  :members:
  :inherited-members:
  :exclude-members: object, etag, to_str, to_dict, manifest_id

.. autoclass:: mbed_cloud.update.UpdateCampaign
  :members:
  :inherited-members:
  :exclude-members: object, etag, to_str, to_dict, campaign_id
