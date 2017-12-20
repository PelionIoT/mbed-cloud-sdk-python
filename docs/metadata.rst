Metadata
~~~~~~~~~~

Meta data associated with the last request for given module.

Get meta data
---------------

.. code-block:: python

  >>> from mbed_cloud import CertificatesAPI
  >>> certificatesApi = CertificatesAPI()
  >>> certificates = certificatesApi.list_certificates()
  >>> certificatesApi.get_last_api_metadata()
  {ApiMetadata object}

Reference
---------

.. automodule:: mbed_cloud.core
  :members: ApiMetadata