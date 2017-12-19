Mbed Cloud SDK for Python
=========================

The ``mbed-cloud-sdk`` gives developers access to the full `Arm
Mbed <https://docs.mbed.com/>`__ suite using Python.

.. common_content_anchor

Prerequisites
-------------

Python 2.7.10+ / Python 3.4.3+, built with SSL support.

Use of `virtual
environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`__
or *pipenv* is recommended to manage python versions and dependencies.

Installation
------------

.. code:: bash

    pip install mbed-cloud-sdk

Usage
-----

These instructions can also be found in the `official
documentation <https://cloud.mbed.com/docs/v1.2/mbed-cloud-sdk-python/>`__:

1. Create an API key in the `Mbed Cloud
   Portal <https://portal.us-east-1.mbedcloud.com/>`__.

2. Create a configuration file in your ``$HOME`` or project directory
   (``.mbed_cloud_config.json``):

   .. code:: javascript

       {
           "api_key": "your_api_key_here"
       }

3. Import the library and you're ready to go.

   .. code:: python

       from mbed_cloud import ConnectAPI
       connect_api = ConnectAPI()
       connect_api.list_connected_devices().data[0]
       {
         "id": "Device #1",
         "state": "unenrolled",
         ...
       }

   .. code:: python

       from mbed_cloud import AccountManagementAPI
       api = AccountManagementAPI()
       list(api.list_users())[0]
       {
         "email": "username@example.org",
         "full_name": "A.N. Individual",
         ...
       }

Documentation and examples
--------------------------

The full documentation and API reference is hosted here:
https://cloud.mbed.com/docs/v1.2/mbed-cloud-sdk-python/.

.. _examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples
See the `examples directory`_ for a collection of use-cases of this API, e.g.:

    .. code:: python

       python examples/connect/list-connected-devices.py


Contributing
------------

Mbed Cloud SDK for Python is open source and we would like your help; there
is a brief guide on how to get started in `CONTRIBUTING.md <CONTRIBUTING.md>`__.

Licence
-------

Mbed Cloud SDK for Python is free to use and licensed under the Apache
License 2.0. See `LICENCE <LICENCE>`__ for more information.

Troubleshooting
---------------
Suggestions for issues that have been reported when using the SDK.

- SSL version / :code:`SSLV3_ALERT_HANDSHAKE_FAILURE`
    .. code:: python

      urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.us-east-1.mbedcloud.com', port=443):
      Max retries exceeded with url: /v3/firmware-images/
      (Caused by SSLError(SSLError(1, u'[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:590)'),))

    This probably means the Python interpreter being used has an old version of SSL. The recommended minimum version for the SDK is
    :code:`1.0.2`,
    however security best practice is to use the latest available version of SSL, which can be found here:
    https://www.openssl.org.
    It is recommended to upgrade/rebuild the Python interpreter with the latest available SSL library.
    The SSL version currently in use by the Python interpreter can be found using
    :code:`python -c "import ssl; print(ssl.OPENSSL_VERSION)"`
