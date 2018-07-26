Configuration
-------------
Individual parameters can be set in the following ways:

- Directly when instantiating a new API object
- Through environment variables
- Through environment variables configured in *.env* files

Configuration on instantiation
==============================

Configuration on a per-object basis takes precedence over any other configuration source:

.. code-block:: python

  from mbed_cloud import AccountManagementAPI
  config = { "api_key": "ak_*********" }
  api = AccountManagementAPI(config)

Production deployment
=====================
Many CI and production server providers allow direct configuration of environment variables
in a secure manner, to the equivalent of:

``export MBED_CLOUD_SDK_API_KEY=ak_abcdef123``

Local development
=================
When developing locally, a `.env` file excluded from version control can be used to
configure the SDK without modifying your system's environment:

*(in file: "/path/to/my/project/.env")*

``MBED_CLOUD_SDK_API_KEY=ak_abcdef123``

The file should be named `.env` and placed at any level on your directory tree between
your project's working directory and the root.
Files closer to the working directory, and any variables in the system environment, take priority.

Configuration parameters
========================

You can configure the SDK with the following parameters:

=========== ========================== =================================================================== ========
parameter   env var                    description                                                         optional
=========== ========================== =================================================================== ========
``api_key`` ``MBED_CLOUD_SDK_HOST``    The API key created in the portal                                   Required
``host``    ``MBED_CLOUD_SDK_API_KEY`` The fully qualified hostname (scheme, host, port) of the api server Optional
=========== ========================== =================================================================== ========
