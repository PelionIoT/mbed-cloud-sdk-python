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
import datetime
from mbed_cloud.account_management import AccountManagementAPI


def _main():
    api = AccountManagementAPI()

    header = "All registered users in Organisation"
    print("%s\n%s" % (header, len(header) * "-"))
    for idx, u in enumerate(api.list_users()):
        print("\t- %s (%s - %s)" % (u.full_name, u.email, u.username))

    header = "\nAll registered API keys in Organisation"
    presp = api.list_api_keys(limit=2)
    print("%s \n%s" % (header, len(header) * "-"))
    for idx, k in enumerate(presp):
        last_used = "Never"
        if k.last_login_time > 0:
            last_used = datetime.datetime.fromtimestamp(k.last_login_time / 1000).strftime('%c')
        print("\t- %s (Last used: %s)" % (k.name, last_used))


if __name__ == "__main__":
    _main()
