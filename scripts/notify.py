# --------------------------------------------------------------------------
# Pelion Device Management Python SDK
# (C) COPYRIGHT 2017,2019 Arm Limited
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
"""Part of the CI process"""

import os

from slackclient import SlackClient


def main():
    """Sends release notifications to interested parties

    Currently this is an arm-internal slack channel.

     1. assumes you've set a token for an authorised slack user/bot.
     2. assumes said user/bot is already in channel.
     otherwise: https://github.com/slackapi/python-slackclient#joining-a-channel
    """
    slack_token = os.environ.get('SLACK_API_TOKEN')
    channel_id = os.environ.get('SLACK_CHANNEL', '#isg-dm-sdk')
    message = os.environ.get('SLACK_MESSAGE', (
        ':checkered_flag: New version of :snake: Python SDK released: *{version}* '
        '(<https://pypi.org/project/mbed-cloud-sdk/{version}/|PyPI>)'
    ))

    if not slack_token:
        print('no slack token')
        return

    version = os.environ.get('SLACK_NOTIFY_VERSION')
    if not version:
        try:
            import mbed_cloud
        except ImportError:
            pass
        else:
            version = mbed_cloud.__version__

    payload = message.format(version=version) if version else message

    print('notifying slack channel %s with payload:\n%s' % (channel_id, payload))

    sc = SlackClient(slack_token)
    sc.api_call(
        'chat.postMessage',
        channel=channel_id,
        text=payload,
    )


if __name__ == '__main__':
    main()
