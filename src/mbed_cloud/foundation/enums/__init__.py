"""
Foundation Interface: Enums
===========================

Some attributes of Foundation Interface Entities use enumerations and the API has a restricted range of values. The
following is a list of all enums in the Foundation Interface ordered by the entity's category:


Accounts
--------

- :class:`mbed_cloud.foundation.entities.accounts.enums.AccountMfaStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.AccountOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.AccountStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.ApiKeyOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.ApiKeyStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.SubtenantUserStatusEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.UserInvitationOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.UserOrderEnum`
- :class:`mbed_cloud.foundation.entities.accounts.enums.UserStatusEnum`

Devices
-------

- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceDeployedStateEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceEnrollmentBulkCreateStatusEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceEnrollmentBulkDeleteStatusEnum`
- :class:`mbed_cloud.foundation.entities.devices.enums.DeviceEnrollmentOrderEnum`
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
    
    from mbed_cloud.foundation.enums import AccountMfaStatusEnum
    from mbed_cloud.foundation.enums import AccountOrderEnum
    from mbed_cloud.foundation.enums import AccountStatusEnum
    from mbed_cloud.foundation.enums import ApiKeyOrderEnum
    from mbed_cloud.foundation.enums import ApiKeyStatusEnum
    from mbed_cloud.foundation.enums import SubtenantUserStatusEnum
    from mbed_cloud.foundation.enums import UserInvitationOrderEnum
    from mbed_cloud.foundation.enums import UserOrderEnum
    from mbed_cloud.foundation.enums import UserStatusEnum
    from mbed_cloud.foundation.enums import DeviceDeployedStateEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentBulkCreateStatusEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentBulkDeleteStatusEnum
    from mbed_cloud.foundation.enums import DeviceEnrollmentOrderEnum
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

from mbed_cloud.foundation.entities.accounts.enums import AccountMfaStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import AccountOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import AccountStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import ApiKeyOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import ApiKeyStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import SubtenantUserStatusEnum
from mbed_cloud.foundation.entities.accounts.enums import UserInvitationOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import UserOrderEnum
from mbed_cloud.foundation.entities.accounts.enums import UserStatusEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceDeployedStateEnum
from mbed_cloud.foundation.entities.devices.enums import (
    DeviceEnrollmentBulkCreateStatusEnum,
)
from mbed_cloud.foundation.entities.devices.enums import (
    DeviceEnrollmentBulkDeleteStatusEnum,
)
from mbed_cloud.foundation.entities.devices.enums import DeviceEnrollmentOrderEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceMechanismEnum
from mbed_cloud.foundation.entities.devices.enums import DeviceStateEnum
from mbed_cloud.foundation.entities.security.enums import (
    CertificateEnrollmentEnrollResultEnum,
)
from mbed_cloud.foundation.entities.security.enums import (
    CertificateEnrollmentEnrollStatusEnum,
)
from mbed_cloud.foundation.entities.security.enums import CertificateEnrollmentIncludeEnum
from mbed_cloud.foundation.entities.security.enums import CertificateEnrollmentOrderEnum
from mbed_cloud.foundation.entities.security.enums import CertificateIssuerTypeEnum
from mbed_cloud.foundation.entities.security.enums import (
    SubtenantTrustedCertificateServiceEnum,
)
from mbed_cloud.foundation.entities.security.enums import (
    SubtenantTrustedCertificateStatusEnum,
)
from mbed_cloud.foundation.entities.security.enums import TrustedCertificateOrderEnum
from mbed_cloud.foundation.entities.security.enums import TrustedCertificateServiceEnum
from mbed_cloud.foundation.entities.security.enums import TrustedCertificateStatusEnum


__all__ = [
    "AccountMfaStatusEnum",
    "AccountOrderEnum",
    "AccountStatusEnum",
    "ApiKeyOrderEnum",
    "ApiKeyStatusEnum",
    "SubtenantUserStatusEnum",
    "UserInvitationOrderEnum",
    "UserOrderEnum",
    "UserStatusEnum",
    "DeviceDeployedStateEnum",
    "DeviceEnrollmentBulkCreateStatusEnum",
    "DeviceEnrollmentBulkDeleteStatusEnum",
    "DeviceEnrollmentOrderEnum",
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
