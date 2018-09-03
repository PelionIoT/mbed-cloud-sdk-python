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
"""Example: Basic configuration of the API"""


def run():
    # an example: configuring the SDK
    from mbed_cloud import AccountManagementAPI
    config = dict(api_key='ak_1234abc')
    # alternatively, configuration can be loaded from json files or environment variables
    # if the host is not the default Mbed Cloud, it needs to be specified
    config['host'] = 'https://custom-mbed-cloud-host.com'
    # create an instance of one of the SDK modules
    api = AccountManagementAPI(params=config)
    # do something with the SDK
    print(api.get_account())
    # end of example


__name__ == "__main__" and run()
