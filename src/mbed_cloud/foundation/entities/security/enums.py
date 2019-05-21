"""
.. warning::
    Enums should not be imported directly from this module as the organisation of categories may change in
    the future, please use the :mod:`mbed_cloud.foundation.enums` module to import enums.

Security Enums
==============

This module contains all Enums used by Foundation Entities in the Security category:

- :class:`CertificateEnrollmentEnrollResultEnum`
- :class:`CertificateEnrollmentEnrollStatusEnum`
- :class:`CertificateEnrollmentIncludeEnum`
- :class:`CertificateEnrollmentOrderEnum`
- :class:`CertificateIssuerTypeEnum`
- :class:`SubtenantTrustedCertificateServiceEnum`
- :class:`SubtenantTrustedCertificateStatusEnum`
- :class:`TrustedCertificateOrderEnum`
- :class:`TrustedCertificateServiceEnum`
- :class:`TrustedCertificateStatusEnum`

------------

How to import Enums:

.. code-block:: python
    
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

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.foundation.common.enum_base import BaseEnum


class CertificateEnrollmentEnrollResultEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentEnrollResultEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    FAILURE = "failure"
    SUCCESS = "success"

    values = frozenset(("failure", "success"))


class CertificateEnrollmentEnrollStatusEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentEnrollStatusEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    COMPLETED = "completed"
    NEW = "new"

    values = frozenset(("completed", "new"))


class CertificateEnrollmentIncludeEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentIncludeEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    TOTAL_COUNT = "total_count"

    values = frozenset(("total_count",))


class CertificateEnrollmentOrderEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentOrderEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class CertificateIssuerTypeEnum(BaseEnum):
    """Represents expected values of `CertificateIssuerTypeEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    CFSSL_AUTH = "CFSSL_AUTH"
    GLOBAL_SIGN = "GLOBAL_SIGN"

    values = frozenset(("CFSSL_AUTH", "GLOBAL_SIGN"))


class SubtenantTrustedCertificateServiceEnum(BaseEnum):
    """Represents expected values of `SubtenantTrustedCertificateServiceEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    BOOTSTRAP = "bootstrap"
    LWM2M = "lwm2m"

    values = frozenset(("bootstrap", "lwm2m"))


class SubtenantTrustedCertificateStatusEnum(BaseEnum):
    """Represents expected values of `SubtenantTrustedCertificateStatusEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))


class TrustedCertificateOrderEnum(BaseEnum):
    """Represents expected values of `TrustedCertificateOrderEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class TrustedCertificateServiceEnum(BaseEnum):
    """Represents expected values of `TrustedCertificateServiceEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    BOOTSTRAP = "bootstrap"
    LWM2M = "lwm2m"

    values = frozenset(("bootstrap", "lwm2m"))


class TrustedCertificateStatusEnum(BaseEnum):
    """Represents expected values of `TrustedCertificateStatusEnum`

    This is used by Entities in the "security" category.

    .. note::
        If new values are added to the enum in the API they will be passed through unchanged by the SDK,
        but will not be on this list. If this occurs please update the SDK to the most recent version.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))
