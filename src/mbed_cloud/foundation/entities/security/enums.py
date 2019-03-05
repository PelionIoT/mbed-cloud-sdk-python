"""
Enum module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.sdk.common.enum import BaseEnum


class CertificateEnrollmentEnrollResultEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentEnrollResultEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    FAILURE = "failure"
    FORBIDDEN = "forbidden"
    NOT_FOUND = "not_found"
    SUCCESS = "success"

    values = frozenset(("failure", "forbidden", "not_found", "success"))


class CertificateEnrollmentEnrollStatusEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentEnrollStatusEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    COMPLETED = "completed"
    NEW = "new"

    values = frozenset(("completed", "new"))


class CertificateEnrollmentIncludeEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentIncludeEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    TOTAL_COUNT = "total_count"

    values = frozenset(("total_count",))


class CertificateEnrollmentOrderEnum(BaseEnum):
    """Represents expected values of `CertificateEnrollmentOrderEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class CertificateIssuerTypeEnum(BaseEnum):
    """Represents expected values of `CertificateIssuerTypeEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    CFSSL_AUTH = "CFSSL_AUTH"
    GLOBAL_SIGN = "GLOBAL_SIGN"

    values = frozenset(("CFSSL_AUTH", "GLOBAL_SIGN"))


class SubtenantTrustedCertificateServiceEnum(BaseEnum):
    """Represents expected values of `SubtenantTrustedCertificateServiceEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    BOOTSTRAP = "bootstrap"
    LWM2M = "lwm2m"

    values = frozenset(("bootstrap", "lwm2m"))


class SubtenantTrustedCertificateStatusEnum(BaseEnum):
    """Represents expected values of `SubtenantTrustedCertificateStatusEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))


class TrustedCertificateOrderEnum(BaseEnum):
    """Represents expected values of `TrustedCertificateOrderEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class TrustedCertificateServiceEnum(BaseEnum):
    """Represents expected values of `TrustedCertificateServiceEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    BOOTSTRAP = "bootstrap"
    LWM2M = "lwm2m"

    values = frozenset(("bootstrap", "lwm2m"))


class TrustedCertificateStatusEnum(BaseEnum):
    """Represents expected values of `TrustedCertificateStatusEnum`

    This is used by Mbed Cloud "security" functionality

    Note: If new values are added to the enum in the API they will be passed through unchanged by
    the SDK, but will not be on this list. If this occurs please update the SDK to the most recent
    version.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))
