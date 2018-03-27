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
"""This test server is executed by CI test runs with a common"""

import os

from slackclient import SlackClient

import mbed_cloud


def run():
    """Sends release notifications to interested parties

    Currently this is an arm-internal slack channel.

     1. assumes you've set a token for an authorised slack user/bot.
     2. assumes said user/bot is already in channel.
     otherwise: https://github.com/slackapi/python-slackclient#joining-a-channel
    """
    slack_token = os.environ.get('SLACK_API_TOKEN')
    if not slack_token:
        print('no slack token')
        return

    channel_id = '#mbed-cloud-sdk'
    payload = (
        ':checkered_flag: New version of :snake: Python SDK released: *{v}* '
        '(<https://pypi.org/project/mbed-cloud-sdk/{v}/|PyPI>)'
    ).format(v=mbed_cloud.__version__)

    print('notifying slack channel %s with payload:\n%s' % (channel_id, payload))

    sc = SlackClient(slack_token)
    sc.api_call(
        'chat.postMessage',
        channel=os.environ.get('SLACK_CHANNEL', channel_id),
        text=payload,
    )


if __name__ == '__main__':
    run()
