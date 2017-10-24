Mbed Cloud SDK for Python
=========================

The ``mbed-cloud-sdk`` gives developers access to the full `Arm
Mbed <https://docs.mbed.com/>`__ suite using Python.

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

       from mbed_cloud.connect import ConnectAPI
       connect_api = ConnectAPI()
       connect_api.list_connected_devices().data[0]
       {
         "id": "Device #1",
         "state": "unenrolled",
         ...
       }

   .. code:: python

       from mbed_cloud.account_management import AccountManagementAPI
       api = AccountManagementAPI()
       list(api.list_users())[0]
       {
         "email": "username@example.org",
         "full_name": "A.N. Individual",
         ...
       }

Documentation and examples
--------------------------

See the full documentation and API reference at
https://cloud.mbed.com/docs/v1.2/mbed-cloud-sdk-python/.

Licence
-------

Mbed Cloud SDK for Python is free to use and licensed under the Apache
License 2.0. See LICENCE for more information.
