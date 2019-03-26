"""
.. warning::
    Entities should not be imported via this module as the organisation may change in the future, please use the
    :mod:`mbed_cloud.foundation` module to import entities.

Devices Foundation Entities
===========================

This module contains the Foundation Entities that are grouped together under the Devices category:

- :mod:`mbed_cloud.foundation.entities.devices.device`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_bulk_create`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_bulk_delete`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_denial`
- :mod:`mbed_cloud.foundation.entities.devices.device_events`

------------

How to import Devices Entities:

.. code-block:: python
    
    from mbed_cloud.foundation import Device
    from mbed_cloud.foundation import DeviceEnrollment
    from mbed_cloud.foundation import DeviceEnrollmentBulkCreate
    from mbed_cloud.foundation import DeviceEnrollmentBulkDelete
    from mbed_cloud.foundation import DeviceEnrollmentDenial
    from mbed_cloud.foundation import DeviceEvents

------------
"""
