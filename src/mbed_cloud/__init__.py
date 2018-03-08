# --------------------------------------------------------------------------
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
"""Exposes the primary interfaces for the SDK."""


from mbed_cloud._version import __version__  # noqa

from mbed_cloud.account_management import AccountManagementAPI
from mbed_cloud.certificates import CertificatesAPI
from mbed_cloud.connect import ConnectAPI
from mbed_cloud.device_directory import DeviceDirectoryAPI
from mbed_cloud.enrollment import EnrollmentAPI
from mbed_cloud.update import UpdateAPI
