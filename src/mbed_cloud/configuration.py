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


class Config(dict):
    """Create configuration dict, reading config file(s) on initialisation."""

    logger = logging.getLogger(__name__)

    def __init__(self, updates=None):
        """Go through list of directories in priority order and add to config.

        For each file which is found and valid, we extend/overwrite the existing
        config dictionary.

        Of highest priority is using the `MBED_CLOUD_SDK_CONFIG` environment
        variable, to specify a config JSON file.
        """
        logging.basicConfig(level=logging.INFO)
        self._using_paths = []

        try:
            self.load(updates=updates)
        except Exception:
            raise Exception(
                "There was a problem loading the SDK configuration file.\n"
                "Paths attempted, in priority order: \n\t%s\n"
                "The original traceback is recorded below:\n"
                "\n%s"
                % (',\n\t'.join(self._using_paths), traceback.format_exc())
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
            os.environ.get("MBED_CLOUD_SDK_CONFIG")
        ]

    def load(self, updates):
        """Load configuration data"""
        paths = self.paths()

        # Go through in order and override the config
        for path in paths:
            if not path:
                continue
            abs_path = os.path.abspath(os.path.expanduser(path))
            if not os.path.isfile(abs_path):
                self._using_paths.append('missing: %s' % abs_path)
                continue
            self._using_paths.append(' exists: %s' % abs_path)
            with open(abs_path) as fh:
                self.update(json.load(fh))
        if updates:
            self.update(updates)
        self.validate()

    def validate(self):
        """Validate / fix up the current config"""
        if not self.get('api_key'):
            raise ValueError("api_key not found in config. Please see documentation.")
        host = self.get('host')
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
