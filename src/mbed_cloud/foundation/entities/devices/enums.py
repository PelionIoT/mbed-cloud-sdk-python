"""
.. warning::
    Enums should not be imported directly from this module as the organisation of categories may change in
    the future, please use the :mod:`mbed_cloud.foundation.enums` module to import enums.

Devices Enums
=============

This module contains all Enums used by Foundation Entities in the Devices category:

- :class:`DeviceDeployedStateEnum`
- :class:`DeviceEnrollmentBulkCreateStatusEnum`
- :class:`DeviceEnrollmentBulkDeleteStatusEnum`
- :class:`DeviceEnrollmentDenialOrderEnum`
- :class:`DeviceEnrollmentOrderEnum`
- :class:`DeviceMechanismEnum`
- :class:`DeviceStateEnum`

------------

How to import Enums:

.. code-block:: python
    
    from mbed_cloud.foundation.enums import DeviceDeployedStateEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentBulkCreateStatusEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentBulkDeleteStatusEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentDenialOrderEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentOrderEnum
    from mbed_cloud.foundation.enums import DeviceMechanismEnum
    from mbed_cloud.foundation.enums import DeviceStateEnum

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.foundation.common.enum_base import BaseEnum


class DeviceDeployedStateEnum(BaseEnum):
    """Represents expected values of `DeviceDeployedStateEnum`

    This is used by Entities in the "devices" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    DEVELOPMENT = "development"
    PRODUCTION = "production"

    values = frozenset(("development", "production"))


class DeviceEnrollmentBulkCreateStatusEnum(BaseEnum):
    """Represents expected values of `DeviceEnrollmentBulkCreateStatusEnum`

    This is used by Entities in the "devices" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    COMPLETED = "completed"
    NEW = "new"
    PROCESSING = "processing"

    values = frozenset(("completed", "new", "processing"))


class DeviceEnrollmentBulkDeleteStatusEnum(BaseEnum):
    """Represents expected values of `DeviceEnrollmentBulkDeleteStatusEnum`

    This is used by Entities in the "devices" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    COMPLETED = "completed"
    NEW = "new"
    PROCESSING = "processing"

    values = frozenset(("completed", "new", "processing"))


class DeviceEnrollmentDenialOrderEnum(BaseEnum):
    """Represents expected values of `DeviceEnrollmentDenialOrderEnum`

    This is used by Entities in the "devices" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class DeviceEnrollmentOrderEnum(BaseEnum):
    """Represents expected values of `DeviceEnrollmentOrderEnum`

    This is used by Entities in the "devices" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class DeviceMechanismEnum(BaseEnum):
    """Represents expected values of `DeviceMechanismEnum`

    This is used by Entities in the "devices" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    CONNECTOR = "connector"
    DIRECT = "direct"

    values = frozenset(("connector", "direct"))


class DeviceStateEnum(BaseEnum):
    """Represents expected values of `DeviceStateEnum`

    This is used by Entities in the "devices" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    BOOTSTRAPPED = "bootstrapped"
    CLOUD_ENROLLING = "cloud_enrolling"
    DEREGISTERED = "deregistered"
    REGISTERED = "registered"
    UNENROLLED = "unenrolled"

    values = frozenset(("bootstrapped", "cloud_enrolling", "deregistered", "registered", "unenrolled"))
