..
    This file is autogenerated.
    Only edit this file directly to correct typos.
    See CONTRIBUTING for instructions on adding new entries.

Pelion Device Management SDK for Python
=======================================
This news file contains a log of notable changes to the SDK.

Please see `mbed-cloud-sdk <https://pypi.org/project/mbed-cloud-sdk/#history>`__ for
a list of versions that have been released on PyPI.

..
    begin_release_notes

2.2.0 (2019-06-14)
==================

Features
--------

- Support added for Device Groups. (#1374)

- Support added User Interface Configuration (Branding) i.e. colours, images.
  (#2031)

Improved Documentation
----------------------

- Replace old Campaign update example with new one based on foundation
  interface. (#1955)

- Corrected formatting of `add_device` parameters. (#2069)

- Corrected formatting of `add_query` parameters. (#2070)

- Remove required comment `name` parameter of `add_query`. (#2071)

- Removed out of date FIXME comments from legacy code. (#2125)

- Added examples for resource value and subscription. (#2163)

Misc
----

- #13062019


2.1.0 (2019-05-17)
==================

Features
--------

- First to Claim - to bulk upload for Enrolment Identities added to the
  _Foundation Interface_. (#1162)

- First to Claim - to bulk delete for Enrolment Identities added to the
  _Foundation Interface_. (#1432)

- Certificate entities added to the _Foundation Interface_. (#1438)

- Update Campaigns statistics summary and events added to the _Foundation
  Interface_. (#1467)

- Introduction of the _Foundation Interface_ which adds a new 'Entities' based
  interface. (#1567)

- Addition of server credentials entity to the _Foundation Interface_ including
  ability to get all credentials in a single resource. (#1604)

- Account Management entities to support Aggregators / Sub-Tenant accounts
  added to the _Foundation Interface_. (#1605)

- Device Events entity added to the _Foundation Interface_. (#1768)

- Addition of device entity to the _Foundation SDK_ and support added for
  Certificate Renew. (#1827)

- Pelion Device Management rebranding (previously Mbed Cloud). (#1915)

- Support for Certificate Blacklist (Enrolment Denials) added to the
  _Foundation Interface_. (#1997)

- Device Update support added to the _Foundation Interface_. (#2004)

- Support for filtering list endpoints added to the _Foundation Interface_.
  (#2039)

- Pre-Shared Key (PSK) added to the _Foundation Interface_. (#2339)

Misc
----

- #1615, #1828, #2384


2.0.8 (2019-05-13)
==================

Improved Documentation
----------------------

- Fix callback function name in connect example. (#2014)


2.0.7 (2019-05-13)
==================

Improved Documentation
----------------------

- Keyword for Pelion Device Management added to distributions metedata. (#1931)

- Removed 'trust_class' argument from legacy device_directory SDK. (#2607)

Misc
----

- #2306


2.0.6 (2019-03-05)
==================

Bugfixes
--------

- DeviceDirectoryAPI add_device will now default the device_execution_mode to 0
  when not defined (as per REST API behaviour) (#2068)

- ConnectAPI set_resource_value_async and set_resource_value will now encode
  and send integers, not just strings. (#2133)

- DeviceDirectoryAPI update_query can now be used to change the query name
  without supplying a filter. (#2135)


2.0.5 (2019-02-26)
==================

Bugfixes
--------

- Fixes to subscription patterns and filtering, also a timeout on a blocking
  subscription now raises a CloudTimeoutError not a Queue.empty exception.
  (#2103)

- Errors received in async-responses will now populate the exception `status`
  and `reason` attributes. (#2134)

- Stopping notifications now terminates cleanly without logging an error.
  (#2136)


2.0.4 (2018-11-30)
==================

Bugfixes
--------

- Updated set_resource_value and execute_resource to use the device requests
  API. (#1718)

- Fixed TypeError when devices de-register or expire. (#1871)

- Updated package dependencies (to fix Python 2 build issues in CircleCI)
  (#1921)


2.0.3 (2018-11-07)
==================

Bugfixes
--------

- The signature parameter for the `add_certificate` method is now an optional
  as it has been deprecated in the API. (#1483)


2.0.2 (2018-09-28)
==================

Bugfixes
--------

- Configuration parameters will now be loaded from a .env file in the current
  working directory. (#1762)

- Warnings will no longer be given by the old notification system when using
  new subscription system. (#1763)

- Omitting `device_id` and `resource_path` parameters of `ResourceValues` now
  works as a wildcard match-all (`*`). (#1764)


2.0.1 (2018-09-07)
==================

Bugfixes
--------

- SDK is now Python 3.7 compatible. Changes the underlying codegen module to be
  compatible with Python 3.7 (cannot assign to async: is a reserved keyword).
  (#1459)

- Unless otherwise specified, configuration always explicitly sets a default
  API host. Resolves "The API is only accessible over HTTPS" error when using
  certificate APIs. (#1555)

Improved Documentation
----------------------

- Ensure documentation and changelog is built using the CI release version,
  rather than the dev version. (#1481)


2.0.0 (2018-08-07)
==================

Features
--------

- Change to versioning scheme. Semver `Major.Minor.Patch` scheme now reflects
  state of SDK rather than API. (#1416)

- Settings can now be configured from `.env` files through use of
  https://pypi.org/project/python-dotenv/ (#927)

Bugfixes
--------

- Fix for incorrect month/day parameter being sent to API (billing report
  overview) (billing)

Improved Documentation
----------------------

- This major version increment marks departure from the previous semver
  approach that tracked API major and minor versions. (release)


1.2.10.1235 (2018-07-05)
========================

Features
--------

- Add the Billing module, which provides access to the account's financial
  configurations. (#1210)


1.2.9.1210 (2018-06-27)
=======================

Features
--------

- Remove custom properties from accounts and user entities. (#1362)

- Documentation now includes a full API reference, generated from the source
  code. (#1407)

Bugfixes
--------

- Minor adjustments to TPIP reporting. (#1346)

- Previously, notifications for resource value changes would not be triggered.
  Resource value change subscriptions now use the correct routing keys. The SDK
  now provides the expected values for `device_id` and `resource_path` when
  notifying user code. (#1361)


1.2.8.1183 (2018-06-11)
=======================

Features
--------
- Support List Pre Shared Keys endpoint for Bootstrap API (#631)

- `News` renamed to `Changelog` (#1278)

- PaginatedResponse objects used in API list endpoints now takes `max_results`
  and `page_size` to remove the ambiguity of the `limit` parameter. (#1296)

- Resources channel now receives the full notification rather than just the
  payload. (#1318)

Bugfixes
--------

- Log messages no longer go directly to the root logger (#1091)

- If autostart is disabled, a CloudException is no longer raised when there is
  no long-polling thread (e.g. for the get_resource_value method). This fixes a
  regression that stopped Webhooks from being cleanly enabled. (#1292)


1.2.8.970 (2018-05-22)
======================

Features
--------

- Third Party IP reports are generated according to a common format. (#1008)

- New dockerised CI build system (#1037)

- Client-Lite: Add device bootstrap API. This provides the ability to set
  Pre-Shared Keys for device bring-up. (#1099)

- Adds 'Value Change' subscription channel. This supercedes 'presubscription'
  and 'subscription' behaviours to provide a uniform interface, in line with
  the existing 'Device State' channel. (#1102)

- Add new 'in' and 'not in (nin)' filter operators to enable that functionality
  in the IAM api. (#1225)

- Client-Lite: Manifest upload supports upload of keytable file (#552)

- First to Claim: If a certificate is in enrollment mode, signature is not
  required (#924)

- Configuration can be set using environment variables `MBED_CLOUD_SDK_HOST`
  and `MBED_CLOUD_SDK_API_KEY` (m0)

- All pull requests against the repository should have a news file describing
  the benefit of the work done. (m1)

Bugfixes
--------

- Reduce the number of logs that go directly to the root logger (#1091)

- Online documentation now links back to GitHub for license and contribution
  guidelines (#1097)

- Link to the new location of the online documentation (#1109)


1.2.7.968 (2018-03-27)
======================

Features
--------

- Add subscriptions High Level Abstraction. Provides access to device
  registration status notifications. Sends request to terminate long poll on
  'stop_notifications'. (#722)


1.2.6.852 (2018-03-08)
======================

Features
--------

- Support Connector Enrollment Service API in SDK. Capabilities include:
  Account Admin can upload a list of Device IDs to claim, and can view the
  status of claimed devices. Make a new device claim using:
  `mbed_cloud.EnrollmentAPI().add_enrollment_claim(enrollment_identity=YOUR_CLAIM_TOKEN)`.
  (#627)

- The HTTP header User-Agent is now configured by the SDK and contains version
  and basic platform information, which is passed to the Mbed Cloud. (#634)

Bugfixes
--------

- ConnectAPI: Add a timeout parameter to `set_resource_value` and
  `execute_resource_value` (#1015)

- Fix for list_campaign_device_states using outdated api (#1022)

- ConnectAPI: Use a different api backend for consistency when retrieving
  resource values. `set_resource_value`/`set_resource_value_async` no longer
  execute a resource (use `execute_resource` instead). (#604)

- SDKs now iterate subscriptions in order to delete them. (#733)

- Use correct API for updating campaign objects (#953)


Older releases
==============

.. _section-1:

1.2.5
-----

.. _deliverables-1:

Deliverables
~~~~~~~~~~~~

The application is primarily hosted on pypi at
https://pypi.org/project/mbed-cloud-sdk and can be installed using pip:

::

    $ pip install mbed-cloud-sdk

.. _changes-1:

Changes
~~~~~~~

-  Added ‘claimed_at’ field to Devices
-  Added ‘last_update_time’ to Groups
-  Added ‘device_mode’ to Certificate
-  Renamed ‘owner’ -> ‘owner_id’ on ApiKey
-  Re-implemented PaginatedResponse to match the API spec

   -  Deprecation: No longer uses ‘.data’ attribute
   -  Iterable but not indexable
   -  Ease-of-use functionality such as ``.first()``

-  Improvements to BaseObject data handling
-  Various small improvements to correctness and consistency with other
   SDKs

Known Issues
~~~~~~~~~~~~

-  No new issues

.. _section-2:

1.2.4
-----

.. _deliverables-2:

Deliverables
~~~~~~~~~~~~

The application is primarily hosted on pypi at
https://pypi.org/project/mbed-cloud-sdk and can be installed using pip:

::

    $ pip install mbed-cloud-sdk

.. _changes-2:

Changes
~~~~~~~

-  Filter construction logic reworked
-  Added webhook notification handler
-  AsyncConsumer.wait()
-  Various bugfixes

.. _known-issues-1:

Known Issues
~~~~~~~~~~~~

-  Testing shows that ``get_resource_value`` will fail when the cloud
   service returns a value directly, rather than through an open
   notification channel. This affects all previous versions.
-  The only known workaround at present is to ensure the cloud cache is
   not used by:

   -  Waiting between calls to get_resource_value
   -  Reducing `the configured TTL`_ on the cloud client image on the
      device

.. _section-3:

1.2.3
-----

.. _deliverables-3:

Deliverables
~~~~~~~~~~~~

The application is additionally hosted on pypi at
https://pypi.org/project/mbed-cloud-sdk and can be installed using pip:

::

    $ pip install mbed-cloud-sdk

.. _changes-3:

Changes
~~~~~~~

-  Initial early access release tracking Mbed Cloud 1.2 APIs
-  Added unittests
-  Added coverage collection
-  Python versions supported:

   -  2.7.10+
   -  3.4.3+

-  Examples working with both Python 2.7.10+ and 3.4.3+

1.2.0-alpha
-----------

.. _deliverables-4:

Deliverables
~~~~~~~~~~~~

The application is hosted on GitHub at
https://github.com/ARMmbed/mbed-cloud-sdk-python and can be installed
using pip:

::

    $ pip install ARMmbed/mbed-cloud-sdk-python@1.2.0-alpha

.. _changes-4:

Changes
~~~~~~~

-  Initial early access release tracking Mbed Clou

.. _the configured TTL: https://cloud.mbed.com/docs/latest/collecting/handle-resources.html#working-with-the-server-cache
