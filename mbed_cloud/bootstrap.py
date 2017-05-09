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
"""Custom decorator functions used in mbed_cloud."""
from __future__ import unicode_literals
import json
import os


class Config(dict):
    """Create configuration dict, reading config file(s) on initialisation."""

    def __init__(self):
        """Go through list of directories in priority order and add to config.

        For each file which is found and valid, we extend/overwrite the existing
        config dictionary.

        Of highest priority is using the `MBED_CLOUD_SDK_CONFIG` environment
        variable, to specify a config JSON file.
        """
        CONFIG_FILES = [_f for _f in [
            # Global config in /etc
            "/etc/mbed_cloud_config.json",

            # Config file in home directory
            os.path.join(os.path.expanduser("~"), ".mbed_cloud_config.json"),

            # Config file in current directory
            os.path.join(os.getcwd(), ".mbed_cloud_config.json"),

            # Config file specified using environment variable
            os.environ.get("MBED_CLOUD_SDK_CONFIG")
        ] if _f]

        # Go through in order and override the config
        for f in CONFIG_FILES:
            if os.path.isfile(f):
                with open(f) as fh:
                    c = json.loads(fh.read())
                    self.update(c)
