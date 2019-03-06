"""Custom methods for security entities."""


def is_developer_certificate_setter(self, field, value):
    """Set whether this certificate is a developer certificate or not

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.TrustedCertificate
    :param field: Name of the field which is this is a setter method.
    :type field: str
    :param value: Set to True if a developer certificate
    :type value: bool
    """

    self._device_execution_mode = 1 if value else 0


def is_developer_certificate_getter(self, field):
    """Return whether this certificate is a developer certificate or not.

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.sdk.entities.TrustedCertificate
    :param field: Name of the field which is this is a setter method.
    :type field: str

    :rtype: bool - True if a developer certificate, False otherwise.
    """

    return self._device_execution_mode.value == 1
