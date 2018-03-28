Configuration
-------------
Configuration parameters can be set in the following ways:

- In JSON file(s)
- Directly when instantiating a new API object

Configuration parameters
========================

You can configure the SDK with the following parameters:

- `api_key`: The API key created in https://portal.us-east-1.mbedcloud.com/ (Required)
- `host`: The fully qualified hostname (schema, host, port) of the api server (Optional)

Configuration files
==========================
The file should be named `.mbed_cloud_config.json` and contain JSON describing configuration options

.. code-block:: text

  $ cat .mbed_cloud_config.json
  {
    "api_key": "ak_*********"
  }

In case of multiple configs, precedence for conflicting parameters is given to the more specific config.
In order of increasing specificity, config file(s) should be placed in one of the following directories:

- `/etc/`
- current user home
- current working directory
- the path specified by the environment variable: `MBED_CLOUD_SDK_CONFIG`


Configuration on instantiation
==============================

Configuration on a per-object basis takes precedence over any other configuration source:

.. code-block:: python

  from mbed_cloud import AccountManagementAPI
  config = { "api_key": "ak_*********" }
  api = AccountManagementAPI(config)
