"""
Foundation Interface
====================

The Foundation Interface consists of a number of Entities which are a representation of resources in the API. Entities
are grouped into categories to aid discovery and indicate associated functionality.

.. note::
    Entities should be imported via this module as the organisation of the categories may change in the future.


Accounts
--------

- :mod:`mbed_cloud.foundation.entities.accounts.account`
- :mod:`mbed_cloud.foundation.entities.accounts.active_session`
- :mod:`mbed_cloud.foundation.entities.accounts.api_key`
- :mod:`mbed_cloud.foundation.entities.accounts.identity_provider`
- :mod:`mbed_cloud.foundation.entities.accounts.identity_provider_public_key`
- :mod:`mbed_cloud.foundation.entities.accounts.login_history`
- :mod:`mbed_cloud.foundation.entities.accounts.login_profile`
- :mod:`mbed_cloud.foundation.entities.accounts.oidc_request`
- :mod:`mbed_cloud.foundation.entities.accounts.oidc_request_claim_mapping`
- :mod:`mbed_cloud.foundation.entities.accounts.parent_account`
- :mod:`mbed_cloud.foundation.entities.accounts.password_policy`
- :mod:`mbed_cloud.foundation.entities.accounts.policy`
- :mod:`mbed_cloud.foundation.entities.accounts.policy_group`
- :mod:`mbed_cloud.foundation.entities.accounts.saml2_request`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_api_key`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_identity_provider`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_policy_group`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_user`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_user_invitation`
- :mod:`mbed_cloud.foundation.entities.accounts.user`
- :mod:`mbed_cloud.foundation.entities.accounts.user_invitation`

Branding
--------

- :mod:`mbed_cloud.foundation.entities.branding.dark_theme_color`
- :mod:`mbed_cloud.foundation.entities.branding.dark_theme_image`
- :mod:`mbed_cloud.foundation.entities.branding.light_theme_color`
- :mod:`mbed_cloud.foundation.entities.branding.light_theme_image`
- :mod:`mbed_cloud.foundation.entities.branding.subtenant_dark_theme_color`
- :mod:`mbed_cloud.foundation.entities.branding.subtenant_dark_theme_image`
- :mod:`mbed_cloud.foundation.entities.branding.subtenant_light_theme_color`
- :mod:`mbed_cloud.foundation.entities.branding.subtenant_light_theme_image`

Device_Update
-------------

- :mod:`mbed_cloud.foundation.entities.device_update.campaign_device_metadata`
- :mod:`mbed_cloud.foundation.entities.device_update.campaign_statistics`
- :mod:`mbed_cloud.foundation.entities.device_update.campaign_statistics_events`
- :mod:`mbed_cloud.foundation.entities.device_update.firmware_image`
- :mod:`mbed_cloud.foundation.entities.device_update.firmware_manifest`
- :mod:`mbed_cloud.foundation.entities.device_update.update_campaign`

Devices
-------

- :mod:`mbed_cloud.foundation.entities.devices.device`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_bulk_create`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_bulk_delete`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_denial`
- :mod:`mbed_cloud.foundation.entities.devices.device_events`
- :mod:`mbed_cloud.foundation.entities.devices.device_group`

Security
--------

- :mod:`mbed_cloud.foundation.entities.security.certificate_enrollment`
- :mod:`mbed_cloud.foundation.entities.security.certificate_issuer`
- :mod:`mbed_cloud.foundation.entities.security.certificate_issuer_config`
- :mod:`mbed_cloud.foundation.entities.security.developer_certificate`
- :mod:`mbed_cloud.foundation.entities.security.pre_shared_key`
- :mod:`mbed_cloud.foundation.entities.security.server_credentials`
- :mod:`mbed_cloud.foundation.entities.security.subtenant_trusted_certificate`
- :mod:`mbed_cloud.foundation.entities.security.trusted_certificate`
- :mod:`mbed_cloud.foundation.entities.security.verification_response`

Enums
-----

Some Foundation Interface Entities have attributes which use enumerations, please see the
:mod:`mbed_cloud.foundation.enums` for more information.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK

    pelion_dm_sdk = SDK()
    
    accounts = pelion_dm_sdk.foundation.account()
    active_sessions = pelion_dm_sdk.foundation.active_session()
    api_keys = pelion_dm_sdk.foundation.api_key()
    identity_providers = pelion_dm_sdk.foundation.identity_provider()
    identity_provider_public_keys = pelion_dm_sdk.foundation.identity_provider_public_key()
    login_historys = pelion_dm_sdk.foundation.login_history()
    login_profiles = pelion_dm_sdk.foundation.login_profile()
    oidc_requests = pelion_dm_sdk.foundation.oidc_request()
    oidc_request_claim_mappings = pelion_dm_sdk.foundation.oidc_request_claim_mapping()
    parent_accounts = pelion_dm_sdk.foundation.parent_account()
    password_policys = pelion_dm_sdk.foundation.password_policy()
    policys = pelion_dm_sdk.foundation.policy()
    policy_groups = pelion_dm_sdk.foundation.policy_group()
    saml2_requests = pelion_dm_sdk.foundation.saml2_request()
    subtenant_api_keys = pelion_dm_sdk.foundation.subtenant_api_key()
    subtenant_identity_providers = pelion_dm_sdk.foundation.subtenant_identity_provider()
    subtenant_policy_groups = pelion_dm_sdk.foundation.subtenant_policy_group()
    subtenant_users = pelion_dm_sdk.foundation.subtenant_user()
    subtenant_user_invitations = pelion_dm_sdk.foundation.subtenant_user_invitation()
    users = pelion_dm_sdk.foundation.user()
    user_invitations = pelion_dm_sdk.foundation.user_invitation()
    dark_theme_colors = pelion_dm_sdk.foundation.dark_theme_color()
    dark_theme_images = pelion_dm_sdk.foundation.dark_theme_image()
    light_theme_colors = pelion_dm_sdk.foundation.light_theme_color()
    light_theme_images = pelion_dm_sdk.foundation.light_theme_image()
    subtenant_dark_theme_colors = pelion_dm_sdk.foundation.subtenant_dark_theme_color()
    subtenant_dark_theme_images = pelion_dm_sdk.foundation.subtenant_dark_theme_image()
    subtenant_light_theme_colors = pelion_dm_sdk.foundation.subtenant_light_theme_color()
    subtenant_light_theme_images = pelion_dm_sdk.foundation.subtenant_light_theme_image()
    campaign_device_metadatas = pelion_dm_sdk.foundation.campaign_device_metadata()
    campaign_statisticss = pelion_dm_sdk.foundation.campaign_statistics()
    campaign_statistics_eventss = pelion_dm_sdk.foundation.campaign_statistics_events()
    firmware_images = pelion_dm_sdk.foundation.firmware_image()
    firmware_manifests = pelion_dm_sdk.foundation.firmware_manifest()
    update_campaigns = pelion_dm_sdk.foundation.update_campaign()
    devices = pelion_dm_sdk.foundation.device()
    device_enrollments = pelion_dm_sdk.foundation.device_enrollment()
    device_enrollment_bulk_creates = pelion_dm_sdk.foundation.device_enrollment_bulk_create()
    device_enrollment_bulk_deletes = pelion_dm_sdk.foundation.device_enrollment_bulk_delete()
    device_enrollment_denials = pelion_dm_sdk.foundation.device_enrollment_denial()
    device_eventss = pelion_dm_sdk.foundation.device_events()
    device_groups = pelion_dm_sdk.foundation.device_group()
    certificate_enrollments = pelion_dm_sdk.foundation.certificate_enrollment()
    certificate_issuers = pelion_dm_sdk.foundation.certificate_issuer()
    certificate_issuer_configs = pelion_dm_sdk.foundation.certificate_issuer_config()
    developer_certificates = pelion_dm_sdk.foundation.developer_certificate()
    pre_shared_keys = pelion_dm_sdk.foundation.pre_shared_key()
    server_credentialss = pelion_dm_sdk.foundation.server_credentials()
    subtenant_trusted_certificates = pelion_dm_sdk.foundation.subtenant_trusted_certificate()
    trusted_certificates = pelion_dm_sdk.foundation.trusted_certificate()
    verification_responses = pelion_dm_sdk.foundation.verification_response()

How to import Entities directly:

.. code-block:: python
    
    from mbed_cloud.foundation import Account
    from mbed_cloud.foundation import ActiveSession
    from mbed_cloud.foundation import ApiKey
    from mbed_cloud.foundation import IdentityProvider
    from mbed_cloud.foundation import IdentityProviderPublicKey
    from mbed_cloud.foundation import LoginHistory
    from mbed_cloud.foundation import LoginProfile
    from mbed_cloud.foundation import OidcRequest
    from mbed_cloud.foundation import OidcRequestClaimMapping
    from mbed_cloud.foundation import ParentAccount
    from mbed_cloud.foundation import PasswordPolicy
    from mbed_cloud.foundation import Policy
    from mbed_cloud.foundation import PolicyGroup
    from mbed_cloud.foundation import Saml2Request
    from mbed_cloud.foundation import SubtenantApiKey
    from mbed_cloud.foundation import SubtenantIdentityProvider
    from mbed_cloud.foundation import SubtenantPolicyGroup
    from mbed_cloud.foundation import SubtenantUser
    from mbed_cloud.foundation import SubtenantUserInvitation
    from mbed_cloud.foundation import User
    from mbed_cloud.foundation import UserInvitation
    from mbed_cloud.foundation import DarkThemeColor
    from mbed_cloud.foundation import DarkThemeImage
    from mbed_cloud.foundation import LightThemeColor
    from mbed_cloud.foundation import LightThemeImage
    from mbed_cloud.foundation import SubtenantDarkThemeColor
    from mbed_cloud.foundation import SubtenantDarkThemeImage
    from mbed_cloud.foundation import SubtenantLightThemeColor
    from mbed_cloud.foundation import SubtenantLightThemeImage
    from mbed_cloud.foundation import CampaignDeviceMetadata
    from mbed_cloud.foundation import CampaignStatistics
    from mbed_cloud.foundation import CampaignStatisticsEvents
    from mbed_cloud.foundation import FirmwareImage
    from mbed_cloud.foundation import FirmwareManifest
    from mbed_cloud.foundation import UpdateCampaign
    from mbed_cloud.foundation import Device
    from mbed_cloud.foundation import DeviceEnrollment
    from mbed_cloud.foundation import DeviceEnrollmentBulkCreate
    from mbed_cloud.foundation import DeviceEnrollmentBulkDelete
    from mbed_cloud.foundation import DeviceEnrollmentDenial
    from mbed_cloud.foundation import DeviceEvents
    from mbed_cloud.foundation import DeviceGroup
    from mbed_cloud.foundation import CertificateEnrollment
    from mbed_cloud.foundation import CertificateIssuer
    from mbed_cloud.foundation import CertificateIssuerConfig
    from mbed_cloud.foundation import DeveloperCertificate
    from mbed_cloud.foundation import PreSharedKey
    from mbed_cloud.foundation import ServerCredentials
    from mbed_cloud.foundation import SubtenantTrustedCertificate
    from mbed_cloud.foundation import TrustedCertificate
    from mbed_cloud.foundation import VerificationResponse

------------
"""

from mbed_cloud.foundation.entities.accounts.account import Account
from mbed_cloud.foundation.entities.accounts.active_session import ActiveSession
from mbed_cloud.foundation.entities.accounts.api_key import ApiKey
from mbed_cloud.foundation.entities.accounts.identity_provider import IdentityProvider
from mbed_cloud.foundation.entities.accounts.identity_provider_public_key import IdentityProviderPublicKey
from mbed_cloud.foundation.entities.accounts.login_history import LoginHistory
from mbed_cloud.foundation.entities.accounts.login_profile import LoginProfile
from mbed_cloud.foundation.entities.accounts.oidc_request import OidcRequest
from mbed_cloud.foundation.entities.accounts.oidc_request_claim_mapping import OidcRequestClaimMapping
from mbed_cloud.foundation.entities.accounts.parent_account import ParentAccount
from mbed_cloud.foundation.entities.accounts.password_policy import PasswordPolicy
from mbed_cloud.foundation.entities.accounts.policy import Policy
from mbed_cloud.foundation.entities.accounts.policy_group import PolicyGroup
from mbed_cloud.foundation.entities.accounts.saml2_request import Saml2Request
from mbed_cloud.foundation.entities.accounts.subtenant_api_key import SubtenantApiKey
from mbed_cloud.foundation.entities.accounts.subtenant_identity_provider import SubtenantIdentityProvider
from mbed_cloud.foundation.entities.accounts.subtenant_policy_group import SubtenantPolicyGroup
from mbed_cloud.foundation.entities.accounts.subtenant_user import SubtenantUser
from mbed_cloud.foundation.entities.accounts.subtenant_user_invitation import SubtenantUserInvitation
from mbed_cloud.foundation.entities.accounts.user import User
from mbed_cloud.foundation.entities.accounts.user_invitation import UserInvitation
from mbed_cloud.foundation.entities.branding.dark_theme_color import DarkThemeColor
from mbed_cloud.foundation.entities.branding.dark_theme_image import DarkThemeImage
from mbed_cloud.foundation.entities.branding.light_theme_color import LightThemeColor
from mbed_cloud.foundation.entities.branding.light_theme_image import LightThemeImage
from mbed_cloud.foundation.entities.branding.subtenant_dark_theme_color import SubtenantDarkThemeColor
from mbed_cloud.foundation.entities.branding.subtenant_dark_theme_image import SubtenantDarkThemeImage
from mbed_cloud.foundation.entities.branding.subtenant_light_theme_color import SubtenantLightThemeColor
from mbed_cloud.foundation.entities.branding.subtenant_light_theme_image import SubtenantLightThemeImage
from mbed_cloud.foundation.entities.device_update.campaign_device_metadata import CampaignDeviceMetadata
from mbed_cloud.foundation.entities.device_update.campaign_statistics import CampaignStatistics
from mbed_cloud.foundation.entities.device_update.campaign_statistics_events import CampaignStatisticsEvents
from mbed_cloud.foundation.entities.device_update.firmware_image import FirmwareImage
from mbed_cloud.foundation.entities.device_update.firmware_manifest import FirmwareManifest
from mbed_cloud.foundation.entities.device_update.update_campaign import UpdateCampaign
from mbed_cloud.foundation.entities.devices.device import Device
from mbed_cloud.foundation.entities.devices.device_enrollment import DeviceEnrollment
from mbed_cloud.foundation.entities.devices.device_enrollment_bulk_create import DeviceEnrollmentBulkCreate
from mbed_cloud.foundation.entities.devices.device_enrollment_bulk_delete import DeviceEnrollmentBulkDelete
from mbed_cloud.foundation.entities.devices.device_enrollment_denial import DeviceEnrollmentDenial
from mbed_cloud.foundation.entities.devices.device_events import DeviceEvents
from mbed_cloud.foundation.entities.devices.device_group import DeviceGroup
from mbed_cloud.foundation.entities.security.certificate_enrollment import CertificateEnrollment
from mbed_cloud.foundation.entities.security.certificate_issuer import CertificateIssuer
from mbed_cloud.foundation.entities.security.certificate_issuer_config import CertificateIssuerConfig
from mbed_cloud.foundation.entities.security.developer_certificate import DeveloperCertificate
from mbed_cloud.foundation.entities.security.pre_shared_key import PreSharedKey
from mbed_cloud.foundation.entities.security.server_credentials import ServerCredentials
from mbed_cloud.foundation.entities.security.subtenant_trusted_certificate import SubtenantTrustedCertificate
from mbed_cloud.foundation.entities.security.trusted_certificate import TrustedCertificate
from mbed_cloud.foundation.entities.security.verification_response import VerificationResponse


__all__ = [
    "Account",
    "ActiveSession",
    "ApiKey",
    "CampaignDeviceMetadata",
    "CampaignStatistics",
    "CampaignStatisticsEvents",
    "CertificateEnrollment",
    "CertificateIssuer",
    "CertificateIssuerConfig",
    "DarkThemeColor",
    "DarkThemeImage",
    "DeveloperCertificate",
    "Device",
    "DeviceEnrollment",
    "DeviceEnrollmentBulkCreate",
    "DeviceEnrollmentBulkDelete",
    "DeviceEnrollmentDenial",
    "DeviceEvents",
    "DeviceGroup",
    "FirmwareImage",
    "FirmwareManifest",
    "IdentityProvider",
    "IdentityProviderPublicKey",
    "LightThemeColor",
    "LightThemeImage",
    "LoginHistory",
    "LoginProfile",
    "OidcRequest",
    "OidcRequestClaimMapping",
    "ParentAccount",
    "PasswordPolicy",
    "Policy",
    "PolicyGroup",
    "PreSharedKey",
    "Saml2Request",
    "ServerCredentials",
    "SubtenantApiKey",
    "SubtenantDarkThemeColor",
    "SubtenantDarkThemeImage",
    "SubtenantIdentityProvider",
    "SubtenantLightThemeColor",
    "SubtenantLightThemeImage",
    "SubtenantPolicyGroup",
    "SubtenantTrustedCertificate",
    "SubtenantUser",
    "SubtenantUserInvitation",
    "TrustedCertificate",
    "UpdateCampaign",
    "User",
    "UserInvitation",
    "VerificationResponse",
]
