# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Example showing basic usage of developer certificates."""
from mbed_cloud.certificates import CertificatesAPI
from mbed_cloud.certificates import CertificateType


def _main():
    api = CertificatesAPI()
    # Create a new developer certificate
    print("Creating new developer certificate...")
    certificate = {
        "name": "my_dev_certificate",
        "type": CertificateType.developer
    }
    new_certificate = api.add_certificate(**certificate)
    print("Successfully created developer certificate with id: %r" % new_certificate.id)

    # Update certificate
    updated_certificate = api.update_certificate(new_certificate.id,
                                                 description="my updated certificate")

    # Delete the device
    print("Attempting to delete certificate...")
    api.delete_certificate(updated_certificate.id)
    print("Successfully deleted certificate (ID: %r)" % updated_certificate.id)


if __name__ == "__main__":
    _main()
