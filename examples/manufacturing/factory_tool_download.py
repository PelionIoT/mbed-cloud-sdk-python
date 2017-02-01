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
"""Example showing basic usage of manufacturing API / factory tool download."""
from mbed_cloud.manufacturing import ManufacturingAPI

import tempfile


def _main():
    api = ManufacturingAPI()

    print("Operating systems:")
    versions = api.factory_tool_versions().to_dict()
    for v in versions.itervalues():
        print("\t- %s (%s)[%s MB]" % (v["os"], v["filename"], v["size"]))

    resp = api.factory_tool_download("Linux")
    fh = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
    fh.write(resp)

    print("Downloaded %r to %s" % (versions["lin_archive_info"]["filename"], fh.name))

if __name__ == "__main__":
    _main()
