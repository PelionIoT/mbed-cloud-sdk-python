"""
.. warning::
    Enums should not be imported directly from this module as the organisation of categories may change in
    the future, please use the :mod:`mbed_cloud.foundation.enums` module to import enums.

Accounts Enums
==============

This module contains all Enums used by Foundation Entities in the Accounts category:

- :class:`AccountMfaStatusEnum`
- :class:`AccountOrderEnum`
- :class:`AccountStatusEnum`
- :class:`ApiKeyOrderEnum`
- :class:`ApiKeyStatusEnum`
- :class:`IdentityProviderAlgorithmEnum`
- :class:`IdentityProviderOrderEnum`
- :class:`IdentityProviderStatusEnum`
- :class:`OidcRequestTokenModeEnum`
- :class:`PolicyGroupOrderEnum`
- :class:`PolicyInheritedTypeEnum`
- :class:`SubtenantApiKeyOrderEnum`
- :class:`SubtenantApiKeyStatusEnum`
- :class:`SubtenantIdentityProviderAlgorithmEnum`
- :class:`SubtenantIdentityProviderOrderEnum`
- :class:`SubtenantIdentityProviderStatusEnum`
- :class:`SubtenantPolicyGroupOrderEnum`
- :class:`SubtenantUserOrderEnum`
- :class:`SubtenantUserStatusEnum`
- :class:`UserInvitationOrderEnum`
- :class:`UserOrderEnum`
- :class:`UserStatusEnum`

------------

How to import Enums:

.. code-block:: python
    
    from mbed_cloud.foundation.enums import AccountMfaStatusEnum
    from mbed_cloud.foundation.enums import AccountOrderEnum
    from mbed_cloud.foundation.enums import AccountStatusEnum
    from mbed_cloud.foundation.enums import ApiKeyOrderEnum
    from mbed_cloud.foundation.enums import ApiKeyStatusEnum
    from mbed_cloud.foundation.enums import IdentityProviderAlgorithmEnum
    from mbed_cloud.foundation.enums import IdentityProviderOrderEnum
    from mbed_cloud.foundation.enums import IdentityProviderStatusEnum
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

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.foundation.common.enum_base import BaseEnum


class AccountMfaStatusEnum(BaseEnum):
    """Represents expected values of `AccountMfaStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ENFORCED = "enforced"
    OPTIONAL = "optional"

    values = frozenset(("enforced", "optional"))


class AccountOrderEnum(BaseEnum):
    """Represents expected values of `AccountOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class AccountStatusEnum(BaseEnum):
    """Represents expected values of `AccountStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    ENROLLING = "ENROLLING"
    RESTRICTED = "RESTRICTED"
    SUSPENDED = "SUSPENDED"

    values = frozenset(("ACTIVE", "ENROLLING", "RESTRICTED", "SUSPENDED"))


class ApiKeyOrderEnum(BaseEnum):
    """Represents expected values of `ApiKeyOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class ApiKeyStatusEnum(BaseEnum):
    """Represents expected values of `ApiKeyStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))


class IdentityProviderAlgorithmEnum(BaseEnum):
    """Represents expected values of `IdentityProviderAlgorithmEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    EC224 = "EC224"
    EC256 = "EC256"
    EC384 = "EC384"
    EC521 = "EC521"
    ECDSA224 = "ECDSA224"
    ECDSA256 = "ECDSA256"
    ECDSA384 = "ECDSA384"
    ECDSA521 = "ECDSA521"
    RSA2048 = "RSA2048"
    RSA3072 = "RSA3072"

    values = frozenset(
        ("EC224", "EC256", "EC384", "EC521", "ECDSA224", "ECDSA256", "ECDSA384", "ECDSA521", "RSA2048", "RSA3072")
    )


class IdentityProviderOrderEnum(BaseEnum):
    """Represents expected values of `IdentityProviderOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class IdentityProviderStatusEnum(BaseEnum):
    """Represents expected values of `IdentityProviderStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"

    values = frozenset(("ACTIVE", "SUSPENDED"))


class OidcRequestTokenModeEnum(BaseEnum):
    """Represents expected values of `OidcRequestTokenModeEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    GET = "GET"
    POST = "POST"

    values = frozenset(("GET", "POST"))


class PolicyGroupOrderEnum(BaseEnum):
    """Represents expected values of `PolicyGroupOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class PolicyInheritedTypeEnum(BaseEnum):
    """Represents expected values of `PolicyInheritedTypeEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACCOUNT = "account"
    TEMPLATE = "template"
    TIER_TEMPLATE = "tier_template"

    values = frozenset(("account", "template", "tier_template"))


class SubtenantApiKeyOrderEnum(BaseEnum):
    """Represents expected values of `SubtenantApiKeyOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class SubtenantApiKeyStatusEnum(BaseEnum):
    """Represents expected values of `SubtenantApiKeyStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))


class SubtenantIdentityProviderAlgorithmEnum(BaseEnum):
    """Represents expected values of `SubtenantIdentityProviderAlgorithmEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    EC224 = "EC224"
    EC256 = "EC256"
    EC384 = "EC384"
    EC521 = "EC521"
    ECDSA224 = "ECDSA224"
    ECDSA256 = "ECDSA256"
    ECDSA384 = "ECDSA384"
    ECDSA521 = "ECDSA521"
    RSA2048 = "RSA2048"
    RSA3072 = "RSA3072"

    values = frozenset(
        ("EC224", "EC256", "EC384", "EC521", "ECDSA224", "ECDSA256", "ECDSA384", "ECDSA521", "RSA2048", "RSA3072")
    )


class SubtenantIdentityProviderOrderEnum(BaseEnum):
    """Represents expected values of `SubtenantIdentityProviderOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class SubtenantIdentityProviderStatusEnum(BaseEnum):
    """Represents expected values of `SubtenantIdentityProviderStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"

    values = frozenset(("ACTIVE", "SUSPENDED"))


class SubtenantPolicyGroupOrderEnum(BaseEnum):
    """Represents expected values of `SubtenantPolicyGroupOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class SubtenantUserOrderEnum(BaseEnum):
    """Represents expected values of `SubtenantUserOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class SubtenantUserStatusEnum(BaseEnum):
    """Represents expected values of `SubtenantUserStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    ENROLLING = "ENROLLING"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"
    RESET = "RESET"

    values = frozenset(("ACTIVE", "ENROLLING", "INACTIVE", "INVITED", "RESET"))


class UserInvitationOrderEnum(BaseEnum):
    """Represents expected values of `UserInvitationOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class UserOrderEnum(BaseEnum):
    """Represents expected values of `UserOrderEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class UserStatusEnum(BaseEnum):
    """Represents expected values of `UserStatusEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    ENROLLING = "ENROLLING"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"
    RESET = "RESET"

    values = frozenset(("ACTIVE", "ENROLLING", "INACTIVE", "INVITED", "RESET"))
