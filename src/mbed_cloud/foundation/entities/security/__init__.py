"""
.. warning::
    Entities should not be imported via this module as the organisation may change in the future, please use the
    :mod:`mbed_cloud.foundation` module to import entities.

Security Foundation Entities
============================

This module contains the Foundation Entities that are grouped together under the Security category:

- :mod:`mbed_cloud.foundation.entities.security.certificate_enrollment`
- :mod:`mbed_cloud.foundation.entities.security.certificate_issuer`
- :mod:`mbed_cloud.foundation.entities.security.certificate_issuer_config`
- :mod:`mbed_cloud.foundation.entities.security.developer_certificate`
- :mod:`mbed_cloud.foundation.entities.security.pre_shared_key`
- :mod:`mbed_cloud.foundation.entities.security.server_credentials`
- :mod:`mbed_cloud.foundation.entities.security.subtenant_trusted_certificate`
- :mod:`mbed_cloud.foundation.entities.security.trusted_certificate`
- :mod:`mbed_cloud.foundation.entities.security.verification_response`

------------

How to import Security Entities:

.. code-block:: python
    
    from mbed_cloud.foundation import CertificateEnrollment
    from mbed_cloud.foundation import CertificateIssuer
    from mbed_cloud.foundation import CertificateIssuerConfig
    from mbed_cloud.foundation import DeveloperCertificate
    from mbed_cloud.foundation import PreSharedKey
    from mbed_cloud.foundation import ServerCredentials
    from mbed_cloud.foundation import SubtenantTrustedCertificate
    from mbed_cloud.foundation import TrustedCertificate
    from mbed_cloud.foundation import VerificationResponse

------------
"""
