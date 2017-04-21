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
"""Example showing basic usage of AccountManagement API."""
from mbed_cloud.account_management import AccountManagementAPI


def _main():
    api = AccountManagementAPI()

    header = "Account details"
    print("%s\n%s" % (header, len(header) * "-"))
    account = api.get_account()
    print(account)


if __name__ == "__main__":
    _main()
