"""
.. warning::
    Enums should not be imported directly from this module as the organisation of categories may change in
    the future, please use the :mod:`mbed_cloud.foundation.enums` module to import enums.

Branding Enums
==============

This module contains all Enums used by Foundation Entities in the Branding category:

- :class:`DarkThemeColorReferenceEnum`
- :class:`DarkThemeImageReferenceEnum`
- :class:`LightThemeColorReferenceEnum`
- :class:`LightThemeImageReferenceEnum`
- :class:`SubtenantDarkThemeColorReferenceEnum`
- :class:`SubtenantDarkThemeImageReferenceEnum`
- :class:`SubtenantLightThemeColorReferenceEnum`
- :class:`SubtenantLightThemeImageReferenceEnum`

------------

How to import Enums:

.. code-block:: python
    
    from mbed_cloud.foundation.enums import DarkThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import DarkThemeImageReferenceEnum
    from mbed_cloud.foundation.enums import LightThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import LightThemeImageReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantDarkThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantDarkThemeImageReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantLightThemeColorReferenceEnum
    from mbed_cloud.foundation.enums import SubtenantLightThemeImageReferenceEnum

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.foundation.common.enum_base import BaseEnum


class DarkThemeColorReferenceEnum(BaseEnum):
    """Represents expected values of `DarkThemeColorReferenceEnum`

    This is used by Entities in the "branding" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    CANVAS_BACKGROUND = "canvas_background"
    CANVAS_BACKGROUND_FONT_COLOR = "canvas_background_font_color"
    ERROR_COLOR = "error_color"
    ERROR_FONT_COLOR = "error_font_color"
    INFO_COLOR = "info_color"
    INFO_FONT_COLOR = "info_font_color"
    PRIMARY = "primary"
    PRIMARY_FONT_COLOR = "primary_font_color"
    SECONDARY = "secondary"
    SECONDARY_FONT_COLOR = "secondary_font_color"
    SUCCESS_COLOR = "success_color"
    SUCCESS_FONT_COLOR = "success_font_color"
    WARNING_COLOR = "warning_color"
    WARNING_FONT_COLOR = "warning_font_color"
    WORKSPACE_BACKGROUND = "workspace_background"
    WORKSPACE_BACKGROUND_FONT_COLOR = "workspace_background_font_color"

    values = frozenset(
        (
            "canvas_background",
            "canvas_background_font_color",
            "error_color",
            "error_font_color",
            "info_color",
            "info_font_color",
            "primary",
            "primary_font_color",
            "secondary",
            "secondary_font_color",
            "success_color",
            "success_font_color",
            "warning_color",
            "warning_font_color",
            "workspace_background",
            "workspace_background_font_color",
        )
    )


class DarkThemeImageReferenceEnum(BaseEnum):
    """Represents expected values of `DarkThemeImageReferenceEnum`

    This is used by Entities in the "branding" category.

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


class LightThemeColorReferenceEnum(BaseEnum):
    """Represents expected values of `LightThemeColorReferenceEnum`

    This is used by Entities in the "branding" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    CANVAS_BACKGROUND = "canvas_background"
    CANVAS_BACKGROUND_FONT_COLOR = "canvas_background_font_color"
    ERROR_COLOR = "error_color"
    ERROR_FONT_COLOR = "error_font_color"
    INFO_COLOR = "info_color"
    INFO_FONT_COLOR = "info_font_color"
    PRIMARY = "primary"
    PRIMARY_FONT_COLOR = "primary_font_color"
    SECONDARY = "secondary"
    SECONDARY_FONT_COLOR = "secondary_font_color"
    SUCCESS_COLOR = "success_color"
    SUCCESS_FONT_COLOR = "success_font_color"
    WARNING_COLOR = "warning_color"
    WARNING_FONT_COLOR = "warning_font_color"
    WORKSPACE_BACKGROUND = "workspace_background"
    WORKSPACE_BACKGROUND_FONT_COLOR = "workspace_background_font_color"

    values = frozenset(
        (
            "canvas_background",
            "canvas_background_font_color",
            "error_color",
            "error_font_color",
            "info_color",
            "info_font_color",
            "primary",
            "primary_font_color",
            "secondary",
            "secondary_font_color",
            "success_color",
            "success_font_color",
            "warning_color",
            "warning_font_color",
            "workspace_background",
            "workspace_background_font_color",
        )
    )


class LightThemeImageReferenceEnum(BaseEnum):
    """Represents expected values of `LightThemeImageReferenceEnum`

    This is used by Entities in the "branding" category.

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


class SubtenantDarkThemeColorReferenceEnum(BaseEnum):
    """Represents expected values of `SubtenantDarkThemeColorReferenceEnum`

    This is used by Entities in the "branding" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    CANVAS_BACKGROUND = "canvas_background"
    CANVAS_BACKGROUND_FONT_COLOR = "canvas_background_font_color"
    ERROR_COLOR = "error_color"
    ERROR_FONT_COLOR = "error_font_color"
    INFO_COLOR = "info_color"
    INFO_FONT_COLOR = "info_font_color"
    PRIMARY = "primary"
    PRIMARY_FONT_COLOR = "primary_font_color"
    SECONDARY = "secondary"
    SECONDARY_FONT_COLOR = "secondary_font_color"
    SUCCESS_COLOR = "success_color"
    SUCCESS_FONT_COLOR = "success_font_color"
    WARNING_COLOR = "warning_color"
    WARNING_FONT_COLOR = "warning_font_color"
    WORKSPACE_BACKGROUND = "workspace_background"
    WORKSPACE_BACKGROUND_FONT_COLOR = "workspace_background_font_color"

    values = frozenset(
        (
            "canvas_background",
            "canvas_background_font_color",
            "error_color",
            "error_font_color",
            "info_color",
            "info_font_color",
            "primary",
            "primary_font_color",
            "secondary",
            "secondary_font_color",
            "success_color",
            "success_font_color",
            "warning_color",
            "warning_font_color",
            "workspace_background",
            "workspace_background_font_color",
        )
    )


class SubtenantDarkThemeImageReferenceEnum(BaseEnum):
    """Represents expected values of `SubtenantDarkThemeImageReferenceEnum`

    This is used by Entities in the "branding" category.

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


class SubtenantLightThemeColorReferenceEnum(BaseEnum):
    """Represents expected values of `SubtenantLightThemeColorReferenceEnum`

    This is used by Entities in the "branding" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    CANVAS_BACKGROUND = "canvas_background"
    CANVAS_BACKGROUND_FONT_COLOR = "canvas_background_font_color"
    ERROR_COLOR = "error_color"
    ERROR_FONT_COLOR = "error_font_color"
    INFO_COLOR = "info_color"
    INFO_FONT_COLOR = "info_font_color"
    PRIMARY = "primary"
    PRIMARY_FONT_COLOR = "primary_font_color"
    SECONDARY = "secondary"
    SECONDARY_FONT_COLOR = "secondary_font_color"
    SUCCESS_COLOR = "success_color"
    SUCCESS_FONT_COLOR = "success_font_color"
    WARNING_COLOR = "warning_color"
    WARNING_FONT_COLOR = "warning_font_color"
    WORKSPACE_BACKGROUND = "workspace_background"
    WORKSPACE_BACKGROUND_FONT_COLOR = "workspace_background_font_color"

    values = frozenset(
        (
            "canvas_background",
            "canvas_background_font_color",
            "error_color",
            "error_font_color",
            "info_color",
            "info_font_color",
            "primary",
            "primary_font_color",
            "secondary",
            "secondary_font_color",
            "success_color",
            "success_font_color",
            "warning_color",
            "warning_font_color",
            "workspace_background",
            "workspace_background_font_color",
        )
    )


class SubtenantLightThemeImageReferenceEnum(BaseEnum):
    """Represents expected values of `SubtenantLightThemeImageReferenceEnum`

    This is used by Entities in the "branding" category.

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
