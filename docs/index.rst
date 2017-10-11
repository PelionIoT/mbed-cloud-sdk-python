Mbed Cloud SDK
==============

The Mbed Cloud SDK gives developers access to the full Mbed suite using Python.

Components
----------

.. toctree::
  :maxdepth: 1

  account_management
  certificates
  connect
  device_directory
  update

Concepts
--------

.. toctree::
  :maxdepth: 1

  configuration
  exceptions
  pagination
  metadata

Prerequisites
----------

Python 2.7.10+ / Python 3.4.3+

Quickstart
----------

You can install the SDK by cloning this repository and then run the following
commands. Note that setting up a virtual environment is optional.

.. code-block:: shell

  pip install git+https://github.com/ARMmbed/mbed-cloud-sdk-python.git

Next you will need to create an API key. You can do this logging in to the
`Cloud Portal`. Subsequently, create a new file `.mbed_cloud_config.json`
with the following content:

.. code-block:: shell

  $ cat .mbed_cloud_config.json
  {
    "api_key": "ak_your_api_key_here"
  }

This file will automatically be picked up during API instatiation.
See :doc:`configuration` for more information. You're
now ready to use the API.

.. code-block:: python

  >>> from mbed_cloud.connect import ConnectAPI
  >>> connect_api = ConnectAPI()
  >>> connect_api.list_connected_devices().data[0]
  {
    "id": "Device #1",
    "state": "registered",
    ...
  }
  >>> from mbed_cloud.account_management import AccountManagementAPI
  >>> account_api = AccountManagementAPI()
  >>> list(account_api.list_users())[0]
  {
    "email": "username@example.org",
    "full_name": "Mrs Example",
    ...
  }

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

    python examples/connect/list-connected-devices.py

.. _Cloud Portal: https://portal.us-east-1.mbedcloud.com/login
.. _examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples
