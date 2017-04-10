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
"""Example showing basic usage of Access API."""
from mbed_cloud.access import AccessAPI


def _main():
    api = AccessAPI()

    header = "List all groups in Organisation"
    print("%s\n%s" % (header, len(header) * "-"))
    groups = api.list_groups(limit=5, order='desc')
    for idx, group in enumerate(groups):
        print("\t- %s" % (group.name))

        header = "\nAll registered API keys in Group: %s" % group.name
        keys = api.list_group_api_keys(group.id)
        print("%s \n%s" % (header, len(header) * "-"))
        for idx, k in enumerate(keys):
            print("\t- %s" % (k.name))

        # list users from single group
        header = "\nAll registered Users in Group: %s" % group.name
        users = api.list_group_users(group.id)
        print("%s \n%s" % (header, len(header) * "-"))
        for idx, u in enumerate(users):
            print("\t- %s (%s - %s)" % (u.full_name, u.email, u.username))


if __name__ == "__main__":
    _main()
