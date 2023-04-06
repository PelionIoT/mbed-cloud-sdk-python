Pelion Device Management SDK for Python
=======================================

.. image:: http://unmaintained.tech/badge.svg

----

    Due to a redirected focus onto future development of the Pelion Device Management APIs, this SDK Is no longer actively supported and there is no commitment for future maintenance releases.

    The open source project and corresponding packages for this SDK remain publicly available. 

    Existing applications developed using the SDK will continue to operate against existing Pelion Device Management REST APIs (assuming that those APIs are not subject to the deprecation process for commercial customers). New APIs supported by Pelion Device Management will only be available through the REST APIs. 

    It is recommended that for ongoing development, applications which previously used the SDK should be migrated over time to access the Pelion Device Management REST APIs directly. 

    Please see this  `page <https://www.pelion.com/docs/device-management/current/mbed-cloud-sdk-references/moving-from-the-pelion-device-management-sdks-to-the-apis.html>`_, which provides additional information on using the REST APIs. By following this guide, you will learn how to build a web application using the REST APIs directly. 

----

The ``mbed-cloud-sdk`` gives developers access to `Pelion Device Management <https://cloud.mbed.com/>`__ API using
Python.

.. image:: https://img.shields.io/pypi/l/mbed-cloud-sdk.svg
    :target: https://github.com/PelionIoT/mbed-cloud-sdk-python/blob/master/LICENCE

.. image:: https://img.shields.io/pypi/v/mbed-cloud-sdk.svg
    :target: https://pypi.org/project/mbed-cloud-sdk/

.. image:: https://img.shields.io/pypi/pyversions/mbed-cloud-sdk.svg
    :target: https://pypi.org/project/mbed-cloud-sdk/

.. image:: https://img.shields.io/pypi/status/mbed-cloud-sdk.svg
    :target: https://pypi.org/project/mbed-cloud-sdk/

.. image:: https://img.shields.io/circleci/project/github/ARMmbed/mbed-cloud-sdk-python/master.svg?label=circleci
    :target: https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/tree/master

.. image:: https://codecov.io/gh/ARMmbed/mbed-cloud-sdk-python/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/PelionIoT/mbed-cloud-sdk-python

.. common_content_anchor

Prerequisites
-------------

Python 2.7.10+ / Python 3.4.3, built with SSL support.

Use of `virtual
environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`__
or `pipenv <https://docs.pipenv.org/>`__ is recommended to manage python versions and dependencies.

Installation
------------

.. code:: bash

    pip install mbed-cloud-sdk

Usage
-----

These instructions can also be found in the `official
documentation <https://cloud.mbed.com/docs/latest/mbed-cloud-sdk-python/>`__:

1. Create a configuration file ``.env`` in your ``$HOME`` or project
   directory, and add your API key from the portal:

   .. code:: bash

        MBED_CLOUD_SDK_API_KEY="your_api_key_here"

2. Import the library and you're ready to go.

   .. code:: python

        from mbed_cloud.foundation import Device

        # List the first 10 devices on your Pelion Device Management account.
        for device in Device().list(max_results=10):
            print("Hello device %s" % device.name)

Documentation and examples
--------------------------

The SDK guide and examples are available at `GitHub <https://PelionIoT.github.io/mbed-cloud-sdk-documentation/#introduction>`__.

The documentation contains many examples covering various Use Cases that you may have. In each
case you can compare the python implementation with alternatives in languages
supported by the other Pelion Device Management SDKs.

Contributing
------------

The Pelion Device Management SDK for Python is open source and we would like your help; there
is a brief guide on how to get started in `CONTRIBUTING.md <https://github.com/PelionIoT/mbed-cloud-sdk-python/tree/master/CONTRIBUTING.md>`__.

Licence
-------

The Pelion Device Management SDK for Python is free to use and is licensed under the Apache
License 2.0. See `LICENCE <https://github.com/PelionIoT/mbed-cloud-sdk-python/tree/master/LICENCE>`__ for more information.

Versioning
----------

The current version scheme used by the SDK follows PEP440:

:code:`<SDK major>.<SDK minor>.<SDK patch>`

Troubleshooting
---------------
Suggestions for issues that have been reported when using the SDK.

- SSL version / :code:`SSLV3_ALERT_HANDSHAKE_FAILURE`
    .. code:: python

        urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.mbedcloud.com', port=443):
        Max retries exceeded with url: /v3/firmware-images/
        (Caused by SSLError(SSLError(1, u'[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:590)'),))

    This probably means the Python interpreter being used has an old version of SSL. The recommended minimum version for the SDK is
    :code:`1.0.2`,
    however security best practice is to use the latest available version of SSL, which can be found here:
    https://www.openssl.org.
    It is recommended to upgrade/rebuild the Python interpreter with the latest available SSL library.
    The SSL version currently in use by the Python interpreter can be found using
    :code:`python -c "import ssl; print(ssl.OPENSSL_VERSION)"`
