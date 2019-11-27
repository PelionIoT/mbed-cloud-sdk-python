"""
Foundation Interface: Enums
===========================

Some attributes of Foundation Interface Entities use enumerations if the API defines a restricted range of values. The
following is a list of all enums in the Foundation Interface ordered by the entity's category:


Accounts
--------

- :class:`mbed_cloud.foundation.entities.accounts.enums.AccountBusinessModelEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.AccountMfaStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.AccountOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.AccountStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.ApiKeyOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.ApiKeyStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.IdentityProviderAlgorithmEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.IdentityProviderOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.IdentityProviderStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.IdentityProviderTypeEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.LoginProfileTypeEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.OidcRequestTokenModeEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.PolicyGroupOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.PolicyInheritedTypeEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantApiKeyOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantApiKeyStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantIdentityProviderAlgorithmEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantIdentityProviderOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantIdentityProviderStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantPolicyGroupOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantUserOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantUserStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.UserInvitationOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.UserOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.UserStatusEnum`

Branding
--------

- :class:`mbed_cloud.foundation.entities.branding.enums.DarkThemeColorReferenceEnum`
- :class:`mbed_cloud.foundation.entities.branding.enums.DarkThemeImageReferenceEnum`
- :class:`mbed_cloud.foundation.entities.branding.enums.LightThemeColorReferenceEnum`
- :class:`mbed_cloud.foundation.entities.branding.enums.LightThemeImageReferenceEnum`
- :class:`mbed_cloud.foundation.entities.branding.enums.SubtenantDarkThemeColorReferenceEnum`
- :class:`mbed_cloud.foundation.entities.branding.enums.SubtenantDarkThemeImageReferenceEnum`
- :class:`mbed_cloud.foundation.entities.branding.enums.SubtenantLightThemeColorReferenceEnum`
- :class:`mbed_cloud.foundation.entities.branding.enums.SubtenantLightThemeImageReferenceEnum`

Device_Update
-------------

- :class:`mbed_cloud.foundation.entities.device_update.enums.CampaignDeviceMetadataDeploymentStateEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.CampaignStatisticsIdEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.CampaignStatisticsSummaryStatusEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.FirmwareImageOrderEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.FirmwareManifestDeliveredPayloadTypeEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.FirmwareManifestOrderEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.FirmwareManifestSchemaVersionEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.UpdateCampaignOrderEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.UpdateCampaignPhaseEnum`
- :class:`mbed_cloud.foundation.entities.device_update.enums.UpdateCampaignStrategyEnum`

Devices
-------

- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceDeployedStateEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceEnrollmentBulkCreateStatusEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceEnrollmentBulkDeleteStatusEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceEnrollmentDenialOrderEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceEnrollmentOrderEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceLifecycleStatusEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceMechanismEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceStateEnum`

Security
--------

- :class:`mbed_cloud.foundation.entities.security.enums.CertificateEnrollmentEnrollResultEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.CertificateEnrollmentEnrollStatusEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.CertificateEnrollmentIncludeEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.CertificateEnrollmentOrderEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.CertificateIssuerTypeEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.SubtenantTrustedCertificateServiceEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.SubtenantTrustedCertificateStatusEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.TrustedCertificateOrderEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.TrustedCertificateServiceEnum`
- :class:`mbed_cloud.foundation.entities.security.enums.TrustedCertificateStatusEnum`

------------

.. note::
    Enums should be imported via this module as the organisation of the categories in which entities are arranged
    may change in the future.

How to import Enums:

.. code-block:: python
    
    from mbed_cloud.foundation.enums import AccountBusinessModelEnum
    from mbed_cloud.foundation.enums import AccountMfaStatusEnum
    from mbed_cloud.foundation.enums import AccountOrderEnum
    from mbed_cloud.foundation.enums import AccountStatusEnum
    from mbed_cloud.foundation.enums import ApiKeyOrderEnum
    from mbed_cloud.foundation.enums import ApiKeyStatusEnum
    from mbed_cloud.foundation.enums import IdentityProviderAlgorithmEnum
    from mbed_cloud.foundation.enums import IdentityProviderOrderEnum
    from mbed_cloud.foundation.enums import IdentityProviderStatusEnum
    from mbed_cloud.foundation.enums import IdentityProviderTypeEnum
    from mbed_cloud.foundation.enums import LoginProfileTypeEnum
    from mbed_cloud.foundation.enums import OidcRequestTokenModeEnum
    from mbed_cloud.foundation.enums import PolicyGroupOrderEnum
    from mbed_cloud.foundation.enums import PolicyInheritedTypeEnum
    from mbed_cloud.foundation.enums import SubtenantApiKeyOrderEnum
    from mbed_cloud.foundation.enums import SubtenantApiKeyStatusEnum
    from mbed_cloud.foundation.enums import SubtenantIdentityProviderAlgorithmEnum
    from mbed_cloud.foundation.enums import SubtenantIdentityProviderOrderEnum
    from mbed_cloud.foundation.enums import SubtenantIdentityProviderStatusEnum
    from mbed_cloud.foundation.enums import SubtenantPolicyGroupOrderEnum
    from mbed_cloud.foundation.enums import SubtenantUserOrderEnum
    from mbed_cloud.foundation.enums import SubtenantUserStatusEnum
    from mbed_cloud.foundation.enums import UserInvitationOrderEnum
    from mbed_cloud.foundation.enums import UserOrderEnum
    from mbed_cloud.foundation.enums import UserStatusEnum
    from mbed_cloud.foundation.enums import DarkThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import DarkThemeImageReferenceEnum
    from mbed_cloud.foundation.enums import LightThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import LightThemeImageReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantDarkThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantDarkThemeImageReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantLightThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantLightThemeImageReferenceEnum
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
    from mbed_cloud.foundation.enums import DeviceDeployedStateEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentBulkCreateStatusEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentBulkDeleteStatusEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentDenialOrderEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentOrderEnum
    from mbed_cloud.foundation.enums import DeviceLifecycleStatusEnum
    from mbed_cloud.foundation.enums import DeviceMechanismEnum
    from mbed_cloud.foundation.enums import DeviceStateEnum
    from mbed_cloud.foundation.enums import CertificateEnrollmentEnrollResultEnum
    from mbed_cloud.foundation.enums import CertificateEnrollmentEnrollStatusEnum
    from mbed_cloud.foundation.enums import CertificateEnrollmentIncludeEnum
    from mbed_cloud.foundation.enums import CertificateEnrollmentOrderEnum
    from mbed_cloud.foundation.enums import CertificateIssuerTypeEnum
    from mbed_cloud.foundation.enums import SubtenantTrustedCertificateServiceEnum
    from mbed_cloud.foundation.enums import SubtenantTrustedCertificateStatusEnum
    from mbed_cloud.foundation.enums import TrustedCertificateOrderEnum
    from mbed_cloud.foundation.enums import TrustedCertificateServiceEnum
    from mbed_cloud.foundation.enums import TrustedCertificateStatusEnum

------------
"""

from mbed_cloud.foundation.entities.accounts.enums import AccountBusinessModelEnum
from mbed_cloud.foundation.entities.accounts.enums import AccountMfaStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import AccountOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import AccountStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import ApiKeyOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import ApiKeyStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import IdentityProviderAlgorithmEnum
from mbed_cloud.foundation.entities.accounts.enums import IdentityProviderOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import IdentityProviderStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import IdentityProviderTypeEnum
from mbed_cloud.foundation.entities.accounts.enums import LoginProfileTypeEnum
from mbed_cloud.foundation.entities.accounts.enums import OidcRequestTokenModeEnum
from mbed_cloud.foundation.entities.accounts.enums import PolicyGroupOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import PolicyInheritedTypeEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantApiKeyOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantApiKeyStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantIdentityProviderAlgorithmEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantIdentityProviderOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantIdentityProviderStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantPolicyGroupOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantUserOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantUserStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import UserInvitationOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import UserOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import UserStatusEnum
from mbed_cloud.foundation.entities.branding.enums import DarkThemeColorReferenceEnum
from mbed_cloud.foundation.entities.branding.enums import DarkThemeImageReferenceEnum
from mbed_cloud.foundation.entities.branding.enums import LightThemeColorReferenceEnum
from mbed_cloud.foundation.entities.branding.enums import LightThemeImageReferenceEnum
from mbed_cloud.foundation.entities.branding.enums import SubtenantDarkThemeColorReferenceEnum
from mbed_cloud.foundation.entities.branding.enums import SubtenantDarkThemeImageReferenceEnum
from mbed_cloud.foundation.entities.branding.enums import SubtenantLightThemeColorReferenceEnum
from mbed_cloud.foundation.entities.branding.enums import SubtenantLightThemeImageReferenceEnum
from mbed_cloud.foundation.entities.device_update.enums import CampaignDeviceMetadataDeploymentStateEnum
from mbed_cloud.foundation.entities.device_update.enums import CampaignStatisticsIdEnum
from mbed_cloud.foundation.entities.device_update.enums import CampaignStatisticsSummaryStatusEnum
from mbed_cloud.foundation.entities.device_update.enums import FirmwareImageOrderEnum
from mbed_cloud.foundation.entities.device_update.enums import FirmwareManifestDeliveredPayloadTypeEnum
from mbed_cloud.foundation.entities.device_update.enums import FirmwareManifestOrderEnum
from mbed_cloud.foundation.entities.device_update.enums import FirmwareManifestSchemaVersionEnum
from mbed_cloud.foundation.entities.device_update.enums import UpdateCampaignOrderEnum
from mbed_cloud.foundation.entities.device_update.enums import UpdateCampaignPhaseEnum
from mbed_cloud.foundation.entities.device_update.enums import UpdateCampaignStrategyEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceDeployedStateEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceEnrollmentBulkCreateStatusEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceEnrollmentBulkDeleteStatusEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceEnrollmentDenialOrderEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceEnrollmentOrderEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceLifecycleStatusEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceMechanismEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceStateEnum
from mbed_cloud.foundation.entities.security.enums import CertificateEnrollmentEnrollResultEnum
from mbed_cloud.foundation.entities.security.enums import CertificateEnrollmentEnrollStatusEnum
from mbed_cloud.foundation.entities.security.enums import CertificateEnrollmentIncludeEnum
from mbed_cloud.foundation.entities.security.enums import CertificateEnrollmentOrderEnum
from mbed_cloud.foundation.entities.security.enums import CertificateIssuerTypeEnum
from mbed_cloud.foundation.entities.security.enums import SubtenantTrustedCertificateServiceEnum
from mbed_cloud.foundation.entities.security.enums import SubtenantTrustedCertificateStatusEnum
from mbed_cloud.foundation.entities.security.enums import TrustedCertificateOrderEnum
from mbed_cloud.foundation.entities.security.enums import TrustedCertificateServiceEnum
from mbed_cloud.foundation.entities.security.enums import TrustedCertificateStatusEnum


__all__ = [
    "AccountBusinessModelEnum",
    "AccountMfaStatusEnum",
    "AccountOrderEnum",
    "AccountStatusEnum",
    "ApiKeyOrderEnum",
    "ApiKeyStatusEnum",
    "IdentityProviderAlgorithmEnum",
    "IdentityProviderOrderEnum",
    "IdentityProviderStatusEnum",
    "IdentityProviderTypeEnum",
    "LoginProfileTypeEnum",
    "OidcRequestTokenModeEnum",
    "PolicyGroupOrderEnum",
    "PolicyInheritedTypeEnum",
    "SubtenantApiKeyOrderEnum",
    "SubtenantApiKeyStatusEnum",
    "SubtenantIdentityProviderAlgorithmEnum",
    "SubtenantIdentityProviderOrderEnum",
    "SubtenantIdentityProviderStatusEnum",
    "SubtenantPolicyGroupOrderEnum",
    "SubtenantUserOrderEnum",
    "SubtenantUserStatusEnum",
    "UserInvitationOrderEnum",
    "UserOrderEnum",
    "UserStatusEnum",
    "DarkThemeColorReferenceEnum",
    "DarkThemeImageReferenceEnum",
    "LightThemeColorReferenceEnum",
    "LightThemeImageReferenceEnum",
    "SubtenantDarkThemeColorReferenceEnum",
    "SubtenantDarkThemeImageReferenceEnum",
    "SubtenantLightThemeColorReferenceEnum",
    "SubtenantLightThemeImageReferenceEnum",
    "CampaignDeviceMetadataDeploymentStateEnum",
    "CampaignStatisticsIdEnum",
    "CampaignStatisticsSummaryStatusEnum",
    "FirmwareImageOrderEnum",
    "FirmwareManifestDeliveredPayloadTypeEnum",
    "FirmwareManifestOrderEnum",
    "FirmwareManifestSchemaVersionEnum",
    "UpdateCampaignOrderEnum",
    "UpdateCampaignPhaseEnum",
    "UpdateCampaignStrategyEnum",
    "DeviceDeployedStateEnum",
    "DeviceEnrollmentBulkCreateStatusEnum",
    "DeviceEnrollmentBulkDeleteStatusEnum",
    "DeviceEnrollmentDenialOrderEnum",
    "DeviceEnrollmentOrderEnum",
    "DeviceLifecycleStatusEnum",
    "DeviceMechanismEnum",
    "DeviceStateEnum",
    "CertificateEnrollmentEnrollResultEnum",
    "CertificateEnrollmentEnrollStatusEnum",
    "CertificateEnrollmentIncludeEnum",
    "CertificateEnrollmentOrderEnum",
    "CertificateIssuerTypeEnum",
    "SubtenantTrustedCertificateServiceEnum",
    "SubtenantTrustedCertificateStatusEnum",
    "TrustedCertificateOrderEnum",
    "TrustedCertificateServiceEnum",
    "TrustedCertificateStatusEnum",
]
