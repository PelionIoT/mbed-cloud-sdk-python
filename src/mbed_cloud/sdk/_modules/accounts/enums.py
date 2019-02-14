"""
Enum module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.sdk.common.enum import BaseEnum


class AccountMfaStatusEnum(BaseEnum):
    """Represents expected values of `AccountMfaStatusEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ENFORCED = "enforced"
    OPTIONAL = "optional"

    values = frozenset(("enforced", "optional"))


class AccountOrderEnum(BaseEnum):
    """Represents expected values of `AccountOrderEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class AccountStatusEnum(BaseEnum):
    """Represents expected values of `AccountStatusEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ACTIVE = "ACTIVE"
    ENROLLING = "ENROLLING"
    RESTRICTED = "RESTRICTED"
    SUSPENDED = "SUSPENDED"

    values = frozenset(("ACTIVE", "ENROLLING", "RESTRICTED", "SUSPENDED"))


class ApiKeyOrderEnum(BaseEnum):
    """Represents expected values of `ApiKeyOrderEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class ApiKeyStatusEnum(BaseEnum):
    """Represents expected values of `ApiKeyStatusEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))


class SubtenantUserStatusEnum(BaseEnum):
    """Represents expected values of `SubtenantUserStatusEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ACTIVE = "ACTIVE"
    ENROLLING = "ENROLLING"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"
    RESET = "RESET"

    values = frozenset(("ACTIVE", "ENROLLING", "INACTIVE", "INVITED", "RESET"))


class UserInvitationOrderEnum(BaseEnum):
    """Represents expected values of `UserInvitationOrderEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class UserOrderEnum(BaseEnum):
    """Represents expected values of `UserOrderEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class UserStatusEnum(BaseEnum):
    """Represents expected values of `UserStatusEnum`

    This is used by Mbed Cloud "accounts" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ACTIVE = "ACTIVE"
    ENROLLING = "ENROLLING"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"
    RESET = "RESET"

    values = frozenset(("ACTIVE", "ENROLLING", "INACTIVE", "INVITED", "RESET"))
