Development
~~~~~~~~~~~

Viewing and creating new developer certificates
-----------------------------------------------

Note that the first couple commands are to create a new private/public key
using OpenSSL. The API accepts a base64 encoded NIST P-256 Elliptic Curve
public key.

.. code-block:: shell

  $ openssl ecparam -out key.pem -name prime256v1 -genkey
  $ openssl ec -text -in key.pem -pubout
  read EC key
  Private-Key: (256 bit)
  priv:
      00:ad:3e:dc:9c:49:46:af:ea:2c:b9:31:9f:6f:65:
      62:75:1e:91:f9:9e:f1:a1:90:09:45:2b:7a:cd:9a:
      98:3c:83
  pub:
      04:33:6c:95:45:86:70:6c:e8:3f:86:2c:eb:42:73:
      24:42:bb:0d:cd:f1:33:bc:70:82:b2:30:11:ba:2b:
      ee:79:14:da:30:cd:bc:8b:01:3a:06:c6:67:c5:da:
      a6:0a:6f:d1:8d:c2:81:ce:a6:43:48:62:17:0b:01:
      36:92:e0:76:97
  ASN1 OID: prime256v1
  writing EC key
  -----BEGIN PUBLIC KEY-----
  MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEM2yVRYZwbOg/hizrQnMkQrsNzfEz
  vHCCsjARuivueRTaMM28iwE6BsZnxdqmCm/RjcKBzqZDSGIXCwE2kuB2lw==
  -----END PUBLIC KEY-----


.. code-block:: python

  >>> from mbed_cloud_sdk.development.certificate import CertificateAPI
  >>> api = CertificateAPI()
  >>> pub_key = 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEM2yVRYZwbOg/hizrQnMkQrsNzfEz.....'
  >>> cert = api.create_certificate(pub_key)
  >>> print "%r" % (cert.created_at)
  '2016-10-18T10:46:03Z'

Reference
---------

.. automodule:: mbed_cloud_sdk.development
  :members:

