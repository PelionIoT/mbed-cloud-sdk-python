"""
.. warning::
    Enums should not be imported directly from this module as the organisation of categories may change in
    the future, please use the :mod:`mbed_cloud.foundation.enums` module to import enums.

Accounts Enums
==============

This module contains all Enums used by Foundation Entities in the Accounts category:

- :class:`AccountMfaStatusEnum`
- :class:`AccountOrderEnum`
- :class:`AccountReferenceEnum`
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
    from mbed_cloud.foundation.enums import AccountReferenceEnum
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


class AccountReferenceEnum(BaseEnum):
    """Represents expected values of `AccountReferenceEnum`

    This is used by Entities in the "accounts" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    BRAND_LOGO_EMAIL = "brand_logo_email"
    BRAND_LOGO_LANDSCAPE = "brand_logo_landscape"
    BRAND_LOGO_PORTRAIT = "brand_logo_portrait"
    BRAND_LOGO_SQUARE = "brand_logo_square"
    CAROUSEL_IMAGE_LANDSCAPE_0 = "carousel_image_landscape_0"
    CAROUSEL_IMAGE_LANDSCAPE_1 = "carousel_image_landscape_1"
    CAROUSEL_IMAGE_LANDSCAPE_2 = "carousel_image_landscape_2"
    CAROUSEL_IMAGE_LANDSCAPE_3 = "carousel_image_landscape_3"
    CAROUSEL_IMAGE_LANDSCAPE_4 = "carousel_image_landscape_4"
    CAROUSEL_IMAGE_LANDSCAPE_5 = "carousel_image_landscape_5"
    CAROUSEL_IMAGE_LANDSCAPE_6 = "carousel_image_landscape_6"
    CAROUSEL_IMAGE_LANDSCAPE_7 = "carousel_image_landscape_7"
    CAROUSEL_IMAGE_LANDSCAPE_8 = "carousel_image_landscape_8"
    CAROUSEL_IMAGE_LANDSCAPE_9 = "carousel_image_landscape_9"
    CAROUSEL_IMAGE_PORTRAIT_0 = "carousel_image_portrait_0"
    CAROUSEL_IMAGE_PORTRAIT_1 = "carousel_image_portrait_1"
    CAROUSEL_IMAGE_PORTRAIT_2 = "carousel_image_portrait_2"
    CAROUSEL_IMAGE_PORTRAIT_3 = "carousel_image_portrait_3"
    CAROUSEL_IMAGE_PORTRAIT_4 = "carousel_image_portrait_4"
    CAROUSEL_IMAGE_PORTRAIT_5 = "carousel_image_portrait_5"
    CAROUSEL_IMAGE_PORTRAIT_6 = "carousel_image_portrait_6"
    CAROUSEL_IMAGE_PORTRAIT_7 = "carousel_image_portrait_7"
    CAROUSEL_IMAGE_PORTRAIT_8 = "carousel_image_portrait_8"
    CAROUSEL_IMAGE_PORTRAIT_9 = "carousel_image_portrait_9"
    CAROUSEL_IMAGE_SQUARE_0 = "carousel_image_square_0"
    CAROUSEL_IMAGE_SQUARE_1 = "carousel_image_square_1"
    CAROUSEL_IMAGE_SQUARE_2 = "carousel_image_square_2"
    CAROUSEL_IMAGE_SQUARE_3 = "carousel_image_square_3"
    CAROUSEL_IMAGE_SQUARE_4 = "carousel_image_square_4"
    CAROUSEL_IMAGE_SQUARE_5 = "carousel_image_square_5"
    CAROUSEL_IMAGE_SQUARE_6 = "carousel_image_square_6"
    CAROUSEL_IMAGE_SQUARE_7 = "carousel_image_square_7"
    CAROUSEL_IMAGE_SQUARE_8 = "carousel_image_square_8"
    CAROUSEL_IMAGE_SQUARE_9 = "carousel_image_square_9"
    DESKTOP_BACKGROUND_LANDSCAPE = "desktop_background_landscape"
    DESKTOP_BACKGROUND_PORTRAIT = "desktop_background_portrait"
    DESKTOP_BACKGROUND_SQUARE = "desktop_background_square"

    values = frozenset(
        (
            "brand_logo_email",
            "brand_logo_landscape",
            "brand_logo_portrait",
            "brand_logo_square",
            "carousel_image_landscape_0",
            "carousel_image_landscape_1",
            "carousel_image_landscape_2",
            "carousel_image_landscape_3",
            "carousel_image_landscape_4",
            "carousel_image_landscape_5",
            "carousel_image_landscape_6",
            "carousel_image_landscape_7",
            "carousel_image_landscape_8",
            "carousel_image_landscape_9",
            "carousel_image_portrait_0",
            "carousel_image_portrait_1",
            "carousel_image_portrait_2",
            "carousel_image_portrait_3",
            "carousel_image_portrait_4",
            "carousel_image_portrait_5",
            "carousel_image_portrait_6",
            "carousel_image_portrait_7",
            "carousel_image_portrait_8",
            "carousel_image_portrait_9",
            "carousel_image_square_0",
            "carousel_image_square_1",
            "carousel_image_square_2",
            "carousel_image_square_3",
            "carousel_image_square_4",
            "carousel_image_square_5",
            "carousel_image_square_6",
            "carousel_image_square_7",
            "carousel_image_square_8",
            "carousel_image_square_9",
            "desktop_background_landscape",
            "desktop_background_portrait",
            "desktop_background_square",
        )
    )


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
