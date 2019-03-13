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
- :mod:`mbed_cloud.foundation.entities.accounts.login_history`
- :mod:`mbed_cloud.foundation.entities.accounts.login_profile`
- :mod:`mbed_cloud.foundation.entities.accounts.parent_account`
- :mod:`mbed_cloud.foundation.entities.accounts.password_policy`
- :mod:`mbed_cloud.foundation.entities.accounts.policy`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_user`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_user_invitation`
- :mod:`mbed_cloud.foundation.entities.accounts.user`
- :mod:`mbed_cloud.foundation.entities.accounts.user_invitation`

Devices
-------

- :mod:`mbed_cloud.foundation.entities.devices.device`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_bulk_create`
- :mod:`mbed_cloud.foundation.entities.devices.device_enrollment_bulk_delete`
- :mod:`mbed_cloud.foundation.entities.devices.device_events`

Security
--------

- :mod:`mbed_cloud.foundation.entities.security.certificate_enrollment`
- :mod:`mbed_cloud.foundation.entities.security.certificate_issuer`
- :mod:`mbed_cloud.foundation.entities.security.certificate_issuer_config`
- :mod:`mbed_cloud.foundation.entities.security.developer_certificate`
- :mod:`mbed_cloud.foundation.entities.security.server_credentials`
- :mod:`mbed_cloud.foundation.entities.security.subtenant_trusted_certificate`
- :mod:`mbed_cloud.foundation.entities.security.trusted_certificate`
- :mod:`mbed_cloud.foundation.entities.security.verification_response`


How to import Entities:

.. code-block:: python
    
    from mbed_cloud.foundation import Account
    from mbed_cloud.foundation import ActiveSession
    from mbed_cloud.foundation import ApiKey
    from mbed_cloud.foundation import LoginHistory
    from mbed_cloud.foundation import LoginProfile
    from mbed_cloud.foundation import ParentAccount
    from mbed_cloud.foundation import PasswordPolicy
    from mbed_cloud.foundation import Policy
    from mbed_cloud.foundation import SubtenantUser
    from mbed_cloud.foundation import SubtenantUserInvitation
    from mbed_cloud.foundation import User
    from mbed_cloud.foundation import UserInvitation
    from mbed_cloud.foundation import Device
    from mbed_cloud.foundation import DeviceEnrollment
    from mbed_cloud.foundation import DeviceEnrollmentBulkCreate
    from mbed_cloud.foundation import DeviceEnrollmentBulkDelete
    from mbed_cloud.foundation import DeviceEvents
    from mbed_cloud.foundation import CertificateEnrollment
    from mbed_cloud.foundation import CertificateIssuer
    from mbed_cloud.foundation import CertificateIssuerConfig
    from mbed_cloud.foundation import DeveloperCertificate
    from mbed_cloud.foundation import ServerCredentials
    from mbed_cloud.foundation import SubtenantTrustedCertificate
    from mbed_cloud.foundation import TrustedCertificate
    from mbed_cloud.foundation import VerificationResponse

"""

from mbed_cloud.foundation.entities.accounts.account import Account
from mbed_cloud.foundation.entities.accounts.active_session import ActiveSession
from mbed_cloud.foundation.entities.accounts.api_key import ApiKey
from mbed_cloud.foundation.entities.accounts.login_history import LoginHistory
from mbed_cloud.foundation.entities.accounts.login_profile import LoginProfile
from mbed_cloud.foundation.entities.accounts.parent_account import ParentAccount
from mbed_cloud.foundation.entities.accounts.password_policy import PasswordPolicy
from mbed_cloud.foundation.entities.accounts.policy import Policy
from mbed_cloud.foundation.entities.accounts.subtenant_user import SubtenantUser
from mbed_cloud.foundation.entities.accounts.subtenant_user_invitation import (
    SubtenantUserInvitation,
)
from mbed_cloud.foundation.entities.accounts.user import User
from mbed_cloud.foundation.entities.accounts.user_invitation import UserInvitation
from mbed_cloud.foundation.entities.devices.device import Device
from mbed_cloud.foundation.entities.devices.device_enrollment import DeviceEnrollment
from mbed_cloud.foundation.entities.devices.device_enrollment_bulk_create import (
    DeviceEnrollmentBulkCreate,
)
from mbed_cloud.foundation.entities.devices.device_enrollment_bulk_delete import (
    DeviceEnrollmentBulkDelete,
)
from mbed_cloud.foundation.entities.devices.device_events import DeviceEvents
from mbed_cloud.foundation.entities.security.certificate_enrollment import (
    CertificateEnrollment,
)
from mbed_cloud.foundation.entities.security.certificate_issuer import CertificateIssuer
from mbed_cloud.foundation.entities.security.certificate_issuer_config import (
    CertificateIssuerConfig,
)
from mbed_cloud.foundation.entities.security.developer_certificate import (
    DeveloperCertificate,
)
from mbed_cloud.foundation.entities.security.server_credentials import ServerCredentials
from mbed_cloud.foundation.entities.security.subtenant_trusted_certificate import (
    SubtenantTrustedCertificate,
)
from mbed_cloud.foundation.entities.security.trusted_certificate import TrustedCertificate
from mbed_cloud.foundation.entities.security.verification_response import (
    VerificationResponse,
)


__all__ = [
    "Account",
    "ActiveSession",
    "ApiKey",
    "CertificateEnrollment",
    "CertificateIssuer",
    "CertificateIssuerConfig",
    "DeveloperCertificate",
    "Device",
    "DeviceEnrollment",
    "DeviceEnrollmentBulkCreate",
    "DeviceEnrollmentBulkDelete",
    "DeviceEvents",
    "LoginHistory",
    "LoginProfile",
    "ParentAccount",
    "PasswordPolicy",
    "Policy",
    "ServerCredentials",
    "SubtenantTrustedCertificate",
    "SubtenantUser",
    "SubtenantUserInvitation",
    "TrustedCertificate",
    "User",
    "UserInvitation",
    "VerificationResponse",
]
