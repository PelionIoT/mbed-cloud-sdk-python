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
import datetime

from mbed_cloud.accounts.account_management import AccountManagementAPI


def _main():
    api = AccountManagementAPI()

    header = "All registered users in Organisation"
    print("%s\n%s" % (header, len(header) * "-"))
    for idx, u in enumerate(api.list_users()):
        print("\t- %s (%s - %s)" % (u.full_name, u.email, u.username))

    header = "\nAll registered API keys in Organisation"
    presp = api.list_api_keys(limit=2)
    print("%s \n%s" % (header, len(header) * "-"))
    for idx, k in enumerate(presp):
        last_used = "Never"
        if k.last_login_time > 0:
            last_used = datetime.datetime.fromtimestamp(k.last_login_time / 1000).strftime('%c')
        print("\t- %s (Last used: %s)" % (k.name, last_used))


if __name__ == "__main__":
    _main()
