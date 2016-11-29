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
  assets 
  logging 
  update 

Quickstart
----------

You can install the SDK by cloning this repository and then run the following
commands. Note that setting up a virtual environment is optional.

.. code-block:: shell

  virtualenv venv/ && source venv/bin/activate
  python setup.py install

You're now ready to use the API. Let's explore some of the APIs and their
capabilities.


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
