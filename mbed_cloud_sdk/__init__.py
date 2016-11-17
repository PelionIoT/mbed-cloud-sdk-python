import sys

from mbed_cloud_sdk.bootstrap import Config

config = Config()

class BaseAPI(object):
    def __init__(self, user_config={}):
        config.update(user_config)

        if "api_key" not in config:
            sys.stderr.write("api_key not found in config. Please see documentation.\n")
            sys.exit(1)
