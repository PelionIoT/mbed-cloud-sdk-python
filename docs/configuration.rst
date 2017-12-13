Configuration
-------------
Configuration parameters can be set in the following ways:
- In json file(s)
- Directly when instantiating a new API object

Configuration parameters
========================

Set the following configuration parameters:
- `api_key`: The API key created in https://portal.us-east-1.mbedcloud.com/ (Required)

Configuration files
==========================
The file should be named `.mbed_cloud_config.json` and placed in any of the following directories, with
more specific directories taking precedence for conflicting parameters. In order of specificity:
- on unix: `/etc/`
- current user home
- current working directory
- the path specified by the environment variable: `MBED_CLOUD_SDK_CONFIG`

.. code-block:: text

  $ cat .mbed_cloud_config.json
  {
    "api_key": "ak_*********"
  }

Configuration on instantiation
==============================

Configuration on a per-object basis takes precedence over any other configuration source:

.. code-block:: python

  from mbed_cloud import AccountManagementAPI
  config = { "api_key": "ak_*********" }
  api = AccountManagementAPI(config)
