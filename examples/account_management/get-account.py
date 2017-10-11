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
"""Example showing basic usage of AccountManagement API."""
from mbed_cloud.account_management import AccountManagementAPI


def _main():
    api = AccountManagementAPI()

    header = "Account details"
    print("%s\n%s" % (header, len(header) * "-"))
    account = api.get_account()
    print(account)


if __name__ == "__main__":
    _main()
