"""Sends release notifications to interested parties

Currently this is an arm-internal slack channel.
"""

import os

from slackclient import SlackClient

import mbed_cloud


def run():
    # 1. assumes you've set a token for an authorised slack user/bot.
    # 2. assumes said user/bot is already in channel.
    #    otherwise: https://github.com/slackapi/python-slackclient#joining-a-channel
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
