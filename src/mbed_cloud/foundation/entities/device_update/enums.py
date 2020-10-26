"""
.. warning::
    Enums should not be imported directly from this module as the organisation of categories may change in
    the future, please use the :mod:`mbed_cloud.foundation.enums` module to import enums.

DeviceUpdate Enums
==================

This module contains all Enums used by Foundation Entities in the DeviceUpdate category:

- :class:`CampaignDeviceMetadataDeploymentStateEnum`
- :class:`CampaignStatisticsIdEnum`
- :class:`CampaignStatisticsSummaryStatusEnum`
- :class:`FirmwareImageOrderEnum`
- :class:`FirmwareManifestDeliveredPayloadTypeEnum`
- :class:`FirmwareManifestOrderEnum`
- :class:`FirmwareManifestSchemaVersionEnum`
- :class:`UpdateCampaignOrderEnum`
- :class:`UpdateCampaignPhaseEnum`
- :class:`UpdateCampaignStrategyEnum`

------------

How to import Enums:

.. code-block:: python
    
    from mbed_cloud.foundation.enums import CampaignDeviceMetadataDeploymentStateEnum
    from mbed_cloud.foundation.enums import CampaignStatisticsIdEnum
    from mbed_cloud.foundation.enums import CampaignStatisticsSummaryStatusEnum
    from mbed_cloud.foundation.enums import FirmwareImageOrderEnum
    from mbed_cloud.foundation.enums import FirmwareManifestDeliveredPayloadTypeEnum
    from mbed_cloud.foundation.enums import FirmwareManifestOrderEnum
    from mbed_cloud.foundation.enums import FirmwareManifestSchemaVersionEnum
    from mbed_cloud.foundation.enums import UpdateCampaignOrderEnum
    from mbed_cloud.foundation.enums import UpdateCampaignPhaseEnum
    from mbed_cloud.foundation.enums import UpdateCampaignStrategyEnum

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.foundation.common.enum_base import BaseEnum


class CampaignDeviceMetadataDeploymentStateEnum(BaseEnum):
    """Represents expected values of `CampaignDeviceMetadataDeploymentStateEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    DEPLOYED = "deployed"
    DEREGISTERED = "deregistered"
    FAILED_CONNECTOR_CHANNEL_UPDATE = "failed_connector_channel_update"
    MANIFESTREMOVED = "manifestremoved"
    PENDING = "pending"
    UPDATED_CONNECTOR_CHANNEL = "updated_connector_channel"

    values = frozenset(
        (
            "deployed",
            "deregistered",
            "failed_connector_channel_update",
            "manifestremoved",
            "pending",
            "updated_connector_channel",
        )
    )


class CampaignStatisticsIdEnum(BaseEnum):
    """Represents expected values of `CampaignStatisticsIdEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    FAIL = "fail"
    INFO = "info"
    SKIPPED = "skipped"
    SUCCESS = "success"

    values = frozenset(("fail", "info", "skipped", "success",))


class CampaignStatisticsSummaryStatusEnum(BaseEnum):
    """Represents expected values of `CampaignStatisticsSummaryStatusEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    FAIL = "FAIL"
    INFO = "INFO"
    SKIPPED = "SKIPPED"
    SUCCESS = "SUCCESS"

    values = frozenset(("FAIL", "INFO", "SKIPPED", "SUCCESS",))


class FirmwareImageOrderEnum(BaseEnum):
    """Represents expected values of `FirmwareImageOrderEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC",))


class FirmwareManifestDeliveredPayloadTypeEnum(BaseEnum):
    """Represents expected values of `FirmwareManifestDeliveredPayloadTypeEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    DELTA = "delta"
    FULL = "full"

    values = frozenset(("delta", "full",))


class FirmwareManifestOrderEnum(BaseEnum):
    """Represents expected values of `FirmwareManifestOrderEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC",))


class FirmwareManifestSchemaVersionEnum(BaseEnum):
    """Represents expected values of `FirmwareManifestSchemaVersionEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    1 = "1"
    3 = "3"

    values = frozenset(("1", "3",))


class UpdateCampaignOrderEnum(BaseEnum):
    """Represents expected values of `UpdateCampaignOrderEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC",))


class UpdateCampaignPhaseEnum(BaseEnum):
    """Represents expected values of `UpdateCampaignPhaseEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "active"
    ARCHIVED = "archived"
    AWAITING_APPROVAL = "awaiting_approval"
    DELETED = "deleted"
    DRAFT = "draft"
    STARTING = "starting"
    STOPPED = "stopped"
    STOPPING = "stopping"
    TIMED = "timed"

    values = frozenset(
        ("active", "archived", "awaiting_approval", "deleted", "draft", "starting", "stopped", "stopping", "timed",)
    )


class UpdateCampaignStrategyEnum(BaseEnum):
    """Represents expected values of `UpdateCampaignStrategyEnum`

    This is used by Entities in the "device_update" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    CONTINUOUS = "continuous"
    ONE - SHOT = "one-shot"

    values = frozenset(("continuous", "one-shot",))
