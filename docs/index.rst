mbed Cloud SDK
==============

The mbed Cloud SDK gives developers access to the full mbed suite using Python.

Components
----------

.. toctree::
  :maxdepth: 1

  devices
  access
  development
  manufacturing 
  logging 
  update 

Concepts
--------

.. toctree::
  :maxdepth: 1

  pagination
  configuration

Quickstart
----------

You can install the SDK by cloning this repository and then run the following
commands. Note that setting up a virtual environment is optional.

.. code-block:: shell

  pip install mbed-cloud-sdk

Next you will need to create an API key. You can do this logging in to the
`Cloud Portal`_. Subsequently, create a new file `.mbed_cloud_configuration.json`
with the following content:

.. code-block:: shell

  $ cat .mbed_cloud_configuration.json
  {
    "api_key": "ak_your_api_key_here"
  }
  
This file will automatically be picked up during API instatiation (take a look
at the :doc:`configuration` overview, for more details on this topic). You're
now ready to use the API.

.. code-block:: python

  >>> from mbed_cloud.devices import DeviceAPI
  >>> device_api = DeviceAPI()
  >>> device_api.list_connected_devices().as_list()[0]
  {
    "name": "Device #1",
    "state": "unenrolled",
    ...
  }
  >>> from mbed_cloud.access import AccessAPI
  >>> access_api = AccessAPI()
  >>> access_api.list_users().as_list()[0]
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

    python examples/devices/list-devices.py

Running examples using integration lab
--------------------------------------

Get an API key using the `cloud portal integration environment`_ and enter it
into `api_key` in the `mbed_cloud_config_integration.json` file. See
:doc:`configuration` for more information.

Run the following command to list accounts in the organisation:

.. code-block:: shell

  export MBED_CLOUD_SDK_CONFIG=$PWD/mbed_cloud_config_integration.json
  python examples/access/list-details.py

.. _cloud portal integration environment: https://lab.mbedcloudintegration.net
.. _Cloud Portal: https://portal.mbedcloud.com
.. _examples directory: https://github.com/ARMmbed/mbed-cloud-sdk-python/tree/master/examples
