"""Custom decorator functions used in mbed_cloud_sdk."""
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
        CONFIG_FILES = filter(None, [
            # Global config in /etc
            "/etc/mbed_cloud_config.json",

            # Config file in home directory
            os.path.join(os.path.expanduser("~"), ".mbed_cloud_config.json"),

            # Config file in current directory
            os.path.join(os.getcwd(), ".mbed_cloud_config.json"),

            # Config file specified using environment variable
            os.environ.get("MBED_CLOUD_SDK_CONFIG")
        ])

        # Go through in order and override the config
        for f in CONFIG_FILES:
            if os.path.isfile(f):
                with open(f) as fh:
                    c = json.loads(fh.read())
                    self.update(c)
