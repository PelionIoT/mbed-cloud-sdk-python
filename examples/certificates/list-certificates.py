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


def _main():
    api = CertificatesAPI()
    certificates = list(api.list_certificates(limit=10, order='desc'))

    for idx, certificate in enumerate(certificates):
        print(certificate)


if __name__ == "__main__":
    _main()
