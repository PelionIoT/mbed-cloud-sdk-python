# --------------------------------------------------------------------------
# Pelion Device Management SDK
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
"""Some shared utilities"""
import datetime
import logging
import platform
import uuid

from mbed_cloud import __version__
from mbed_cloud.exceptions import CloudValueError

LOG = logging.getLogger(__name__)
USERAGENT = None


def logging_check():
    """As an Pelion Device Management sub-module, iterate and log at each verbosity level"""
    text = 'logging check "%s"'
    for level in ['debug', 'info', 'warning', 'critical']:
        getattr(LOG, level)(text, level)


def ensure_listable(obj):
    """Ensures obj is a list-like container type"""
    return obj if isinstance(obj, (list, tuple, set)) else [obj]


def force_utc(time, name='field', precision=6):
    """Appending 'Z' to isoformatted time - explicit timezone is required for most APIs"""
    if not isinstance(time, datetime.datetime):
        raise CloudValueError("%s should be of type datetime" % (name,))
    clip = 6 - precision
    timestring = time.isoformat()
    if clip:
        timestring = timestring[:-clip]
    return timestring + "Z"


def new_async_id():
    """A source of new client-side async ids"""
    return str(uuid.uuid4())


def get_user_agent():
    """Common method for obtaining user agent"""
    global USERAGENT
    if not USERAGENT:
        USERAGENT = "mbed-cloud-sdk-python/{sdk_ver} ({pfm}) Python/{py_ver}".format(
            sdk_ver=__version__,
            pfm=platform.platform(),
            py_ver=platform.python_version()
        )
    return USERAGENT
