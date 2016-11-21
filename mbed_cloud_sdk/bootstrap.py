import os, json

class Config(dict):
    def __init__(self):
        CONFIG_FILES = filter(None, [
            # Global config in /etc
            "/etc/mbed_cloud_config.json",
            os.path.join(os.getcwd(), "mbed_cloud_config.json"),
            os.environ.get("MBED_CLOUD_SDK_CONFIG")
        ])

        # Go through in order and override the config
        for f in CONFIG_FILES:
            if os.path.isfile(f):
                with open(f) as fh:
                    c = json.loads(fh.read())
                    self.update(c)
