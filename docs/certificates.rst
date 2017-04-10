Certificates
~~~~~~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.certificates import CertificatesAPI
  from mbed_cloud.certificates import CertificateType

  api = CertificatesAPI()
  # Create a new developer certificate
  print("Creating new developer certificate...")
  certificate = {
    "name": "my_dev_certificate",
    "type": CertificateType.developer
  }
  new_certificate = api.add_certificate(**certificate)
  print("Successfully created developer certificate with id: %r" % new_certificate.id)

  # Update certificate
  updated_certificate = api.update_certificate(new_certificate.id,
                                             description="my updated certificate")
  # Delete the certificate
  print("Attempting to delete certificate...")
  api.delete_certificate(updated_certificate.id)
  print("Successfully deleted certificate (ID: %r)" % updated_certificate.id)

More examples
-------------

See full listing of examples `in the examples directory`_.

.. _in the examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples/certificates

Reference
---------

.. autoclass:: mbed_cloud.certificates.CertificatesAPI
  :members:

.. autoclass:: mbed_cloud.certificates.Certificate
  :members:
  :inherited-members:
  :exclude-members: etag, object, to_dict, to_str
