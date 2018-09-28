# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Custom decorator functions used in mbed_cloud."""
from __future__ import unicode_literals
import json
import logging
import os
import traceback

from dotenv import load_dotenv
from dotenv import find_dotenv

ENVVAR_API_HOST = 'MBED_CLOUD_SDK_HOST'
ENVVAR_API_KEY = 'MBED_CLOUD_SDK_API_KEY'
DEFAULT_CLOUD_HOST = 'https://api.us-east-1.mbedcloud.com'

LOG = logging.getLogger(__name__)


class Config(dict):
    """Create configuration dict, reading config file(s) on initialisation."""

    path_from_env_key = 'MBED_CLOUD_SDK_CONFIG'

    def __init__(self, updates=None):
        """Go through list of directories in priority order and add to config.

        For each file which is found and valid, we extend/overwrite the existing
        config dictionary.

        Of highest priority is using the `MBED_CLOUD_SDK_CONFIG` environment
        variable, to specify a config JSON file.
        """
        # if no root logger is defined yet, configure a default stream handler
        logging.basicConfig(level=logging.INFO)

        self._using_paths = []

        try:
            self.load(updates=updates)
        except Exception:
            raise Exception(
                "There was a problem loading the SDK configuration file.\n"
                "Paths attempted, in priority order: \n\t%s\n"
                "Config file can be set using env key: `%s`\n"
                "The original traceback is recorded below:\n"
                "\n%s"
                % (',\n\t'.join(self._using_paths), self.path_from_env_key, traceback.format_exc())
            )

    def paths(self):
        """Get list of paths to look in for configuration data"""
        filename = '.mbed_cloud_config.json'
        return [
            # Global config in /etc for *nix users
            "/etc/%s" % filename,

            # Config file in home directory
            os.path.join(os.path.expanduser("~"), filename),

            # Config file in current directory
            os.path.join(os.getcwd(), filename),

            # Config file specified using environment variable
            os.environ.get(self.path_from_env_key)
        ]

    def load(self, updates):
        """Load configuration data"""
        # Go through in order and override the config (`.mbed_cloud_config.json` loader)
        for path in self.paths():
            if not path:
                continue
            abs_path = os.path.abspath(os.path.expanduser(path))
            if not os.path.isfile(abs_path):
                self._using_paths.append('missing: %s' % abs_path)
                continue
            self._using_paths.append(' exists: %s' % abs_path)
            with open(abs_path) as fh:
                self.update(json.load(fh))

        # New dotenv loader - requires explicit instructions to use current working directory
        load_dotenv(find_dotenv(usecwd=True))

        # Pluck config values out of the environment
        for env_var, key in {ENVVAR_API_HOST: 'host', ENVVAR_API_KEY: 'api_key'}.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                self[key] = env_value
        if updates:
            self.update(updates)
        self.validate()

    def validate(self):
        """Validate / fix up the current config"""
        if not self.get('api_key'):
            raise ValueError("api_key not found in config. Please see documentation.")
        host = self.get('host') or DEFAULT_CLOUD_HOST
        if host:
            # remove extraneous slashes and force to byte string
            # otherwise msg += message_body in httplib will fail in python2
            # when message_body contains binary data, and url is unicode

            # remaining failure modes include at least:
            # passing bytes in python3 will fail as we try to strip unicode '/' characters
            # passing unicode code points in python2 will fail due to httplib host.encode('ascii')
            host = host.strip('/')
            if not isinstance(host, str):
                host = host.encode('utf-8')
            self['host'] = host

        self.setdefault('autostart_notification_thread', True)
