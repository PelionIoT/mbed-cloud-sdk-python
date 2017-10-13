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

# Version number is composed based on API backend version and SDK version.
# Breaking changes in SDK will increment major version number.
# API version number will follow Mbed release schedule (~quarterly releases).
API_VERSION = "1.2"
SDK_MAJOR_MINOR = "2"
SDK_SUFFIX = ""
VERSION = "%s.%s%s" % (API_VERSION, SDK_MAJOR_MINOR, SDK_SUFFIX)
