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
- :class:`SubtenantApiKeyStatusEnum`
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
    from mbed_cloud.foundation.enums import SubtenantApiKeyStatusEnum
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
