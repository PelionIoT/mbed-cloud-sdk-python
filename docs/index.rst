mbed Cloud SDK
==============

The mbed Cloud SDK gives developers access to the full mbed suite using Python.

Components
----------

.. toctree::
  :maxdepth: 1

  devices
  access

Quickstart
----------

You can install the SDK by cloning this repository and then run the following
commands. Note that setting up a virtual environment is optional.

.. code-block:: shell

  virtualenv venv/ && source venv/bin/activate
  python setup.py install

You're now ready to use the API. Let's explore some of the APIs and their
capabilities.

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

Listing users and groups in team/organisation
---------------------------------------------

.. code-block:: python

  >>> from mbed_cloud_sdk.access.accounts import AccountsAPI
  >>> api = AccountsAPI()
  >>> first_user = api.list_users()[0]
  >>> print "%s (%s)" % (first_user.full_name, first_user.email)
  David Bowie (david.bowie@example.org)
  >>> print len(api.list_groups())
  13

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

More examples
-------------

See `examples directory`_ for a collection of use-cases of this API.

To run the examples, you would need to setup your environment by installing the
dependencies in the `requirements.txt` file. This can be easily done using
virtualenv:

.. code-block:: shell

    virtualenv venv/
    source venv/bin/activate
    pip install -r requirements.txt

.. _examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples

Running examples using integration lab
--------------------------------------

Get an API key using the `cloud portal`_ and enter it into :code:`api_key` in
the :code:`mbed_cloud_config_integration.json` file.

Run the following command to list accounts in the organisation:

.. code-block:: shell

  export MBED_CLOUD_SDK_CONFIG=$PWD/mbed_cloud_config_integration.json
  python examples/access/list-details.py

.. _cloud portal: https://lab.mbedcloudintegration.net
