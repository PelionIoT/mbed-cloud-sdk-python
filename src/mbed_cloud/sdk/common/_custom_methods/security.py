# from mbed_cloud.sdk.enums import CertificateCertificateTypeEnum
#
#
def developer_certificate_setter(self, field, value):
    """Logic for determining whether this certificate is LWM2M, BOOTSTRAP or DEVELOPER

    :param self:
    :type self: mbed_cloud.sdk.entities.Certificate
    """

    self._device_execution_mode = True if value == 1 else False


def developer_certificate_getter(self, field):
    """Logic for determining whether this certificate is LWM2M, BOOTSTRAP or DEVELOPER

    :param self:
    :type self: mbed_cloud.sdk.entities.Certificate
    """

    return self._device_execution_mode == 1
