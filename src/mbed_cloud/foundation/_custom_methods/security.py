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


def pre_shared_key_id_setter(self, value):
    """Set both the endpoint_name and ID fields

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.foundation.PreSharedKey
    :param value: endpoint_name / ID of entity
    :type value: str
    """
    self._endpoint_name.set(value)
    # Also set the ID here as this is used when creating the URI
    self._id.set(value)


def pre_shared_key_id_getter(self):
    """Return the ID field / endpoint_name field

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.foundation.PreSharedKey

    :return: Entity ID (which shadows the endpoint name)
    :rtype: str
    """
    # The underlying value of endpoint name will set by the REST API, so use this in preference to the id
    return self._endpoint_name.value
