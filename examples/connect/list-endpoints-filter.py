# ---------------------------------------------------------------------------
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
"""Example: listing endpoints and filter them by type using Connect API."""
import datetime
from mbed_cloud import ConnectAPI


def _main():
    api = ConnectAPI()

    # Print devices that matches filter
    filters = {
        'created_at': {'$gte': datetime.datetime(2017, 1, 1),
                       '$lte': datetime.datetime(2017, 12, 31)
                       }
    }
    devices = api.list_connected_devices(order='asc', filters=filters)
    for idx, device in enumerate(devices):
        print(device)


if __name__ == "__main__":
    _main()
