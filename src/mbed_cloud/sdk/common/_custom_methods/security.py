from mbed_cloud.sdk.enums import CertificateCertificateTypeEnum


def certificate_type_setter(self, field, value):
    """Logic for determining whether this certificate is LWM2M, BOOTSTRAP or DEVELOPER

    :param self:
    :type self: mbed_cloud.sdk.entities.Certificate
    """

    # this is always computed
    if value == CertificateCertificateTypeEnum.DEVELOPER:
        self.device_execution_mode = 1
        self.service = CertificateCertificateTypeEnum.BOOTSTRAP.lower()
    elif value == CertificateCertificateTypeEnum.BOOTSTRAP:
        self.device_execution_mode = 0
        self.service = CertificateCertificateTypeEnum.BOOTSTRAP.lower()
    elif value == CertificateCertificateTypeEnum.LWM2M:
        self.device_execution_mode = 0
        self.service = CertificateCertificateTypeEnum.LWM2M.lower()
    else:
        raise ValueError(
            "not a valid certificate type, must be one of %s"
            % CertificateCertificateTypeEnum.values
        )
    return value


def certificate_type_getter(self, field):
    """Logic for determining whether this certificate is LWM2M, BOOTSTRAP or DEVELOPER

    :param self:
    :type self: mbed_cloud.sdk.entities.Certificate
    """

    # this is always computed
    current_type = CertificateCertificateTypeEnum.DEVELOPER
    if not self.device_execution_mode:
        for cert_type in CertificateCertificateTypeEnum.values:
            if self.service and self.service.upper() == cert_type:
                current_type = cert_type
                break
    return current_type
