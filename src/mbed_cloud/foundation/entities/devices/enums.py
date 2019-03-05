"""
Enum module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.sdk.common.enum import BaseEnum


class DeviceDeployedStateEnum(BaseEnum):
    """Represents expected values of `DeviceDeployedStateEnum`

    This is used by Mbed Cloud "devices" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    DEVELOPMENT = "development"
    PRODUCTION = "production"

    values = frozenset(("development", "production"))


class DeviceEnrollmentBulkCreateStatusEnum(BaseEnum):
    """Represents expected values of `DeviceEnrollmentBulkCreateStatusEnum`

    This is used by Mbed Cloud "devices" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    COMPLETED = "completed"
    NEW = "new"
    PROCESSING = "processing"

    values = frozenset(("completed", "new", "processing"))


class DeviceEnrollmentBulkDeleteStatusEnum(BaseEnum):
    """Represents expected values of `DeviceEnrollmentBulkDeleteStatusEnum`

    This is used by Mbed Cloud "devices" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    COMPLETED = "completed"
    NEW = "new"
    PROCESSING = "processing"

    values = frozenset(("completed", "new", "processing"))


class DeviceEnrollmentOrderEnum(BaseEnum):
    """Represents expected values of `DeviceEnrollmentOrderEnum`

    This is used by Mbed Cloud "devices" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class DeviceMechanismEnum(BaseEnum):
    """Represents expected values of `DeviceMechanismEnum`

    This is used by Mbed Cloud "devices" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    CONNECTOR = "connector"
    DIRECT = "direct"

    values = frozenset(("connector", "direct"))


class DeviceStateEnum(BaseEnum):
    """Represents expected values of `DeviceStateEnum`

    This is used by Mbed Cloud "devices" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    BOOTSTRAPPED = "bootstrapped"
    CLOUD_ENROLLING = "cloud_enrolling"
    DEREGISTERED = "deregistered"
    REGISTERED = "registered"
    UNENROLLED = "unenrolled"

    values = frozenset(
        ("bootstrapped", "cloud_enrolling", "deregistered", "registered", "unenrolled")
    )
