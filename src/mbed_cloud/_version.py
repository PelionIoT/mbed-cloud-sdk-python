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
"""The version number is based on SemVer.

Breaking changes in SDK will increment the major version number.

references:
- https://semver.org/
- https://www.python.org/dev/peps/pep-0440/

Validate with:
python -c "from mbed_cloud import __version__; print(__version__)"

This file is autogenerated, do not modify by hand (see auto_version.py)
"""
from ._build_info import COMMIT_COUNT
from ._build_info import PRODUCTION

SDK_MAJOR = '2'
SDK_MINOR = '0'
SDK_PATCH = '0'
__version__ = '2.0.0'

if not PRODUCTION:
    __version__ += '.dev%s' % (COMMIT_COUNT or 0)
