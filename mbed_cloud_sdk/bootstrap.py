import os, json

class Config(dict):
    def __init__(self):
        CONFIG_FILES = [
            # Environment variable or global config in /etc
            os.environ.get("MBED_CLOUD_SDK_CONFIG", "/etc/mbed_cloud_config.json"),
            os.path.join(os.getcwd(), "mbed_cloud_config.json")
        ]

        # Go through in order and override the config
        for f in CONFIG_FILES:
            if os.path.isfile(f):
                with open(f) as fh:
                    c = json.loads(fh.read())
                    self.update(c)
