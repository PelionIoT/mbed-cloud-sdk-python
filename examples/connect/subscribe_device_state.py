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
"""Example showing basic usage of device state subscriptions."""


def run():
    # an example: subscribing to device state changes
    # creates an Observer listening to device state changes for devices
    # whose id starts with `016`
    from mbed_cloud import ConnectAPI
    api = ConnectAPI()
    # prepare a channel
    channel = api.subscribe.channels.DeviceStateChanges(
        device_id='016*',
        # here, `channel` refers to the filterable device state received from
        # the notification system
        channel=[
            api.subscribe.channels.ChannelIdentifiers.registrations,
            api.subscribe.channels.ChannelIdentifiers.registrations_expired
        ]
    )
    # start listening for updates
    observer = api.subscribe(channel)
    # on the first update for the channel, block for the specified timeout
    print(observer.next().block(timeout=120000))
    # end of example


__name__ == "__main__" and run()
