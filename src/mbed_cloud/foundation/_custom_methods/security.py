"""Custom methods for security entities."""


def is_developer_certificate_setter(self, value):
    """Set whether this certificate is a developer certificate or not

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.foundation.TrustedCertificate
    :param value: Set to True if a developer certificate
    :type value: bool
    """
    self._device_execution_mode = 1 if value else 0


def is_developer_certificate_getter(self):
    """Return whether this certificate is a developer certificate or not.

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.foundation.TrustedCertificate

    :return: True if a developer certificate, False otherwise.
    :rtype: bool
    """
    return self._device_execution_mode.value == 1
