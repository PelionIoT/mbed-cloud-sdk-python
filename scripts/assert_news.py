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
"""Part of the CI process"""

import os
import subprocess
import sys


def main(news_dir=None):
    """Checks for existence of a new newsfile"""
    if news_dir is None:
        from generate_news import news_dir
    news_dir = os.path.abspath(news_dir)

    # assume the name of the remote alias is just 'origin'
    remote_alias = 'origin'

    # figure out what the 'default branch' for the origin is
    origin_stats = subprocess.check_output(
        ['git', 'remote', 'show', remote_alias],
        cwd=news_dir
    ).decode()

    # the output of the git command looks like:
    # '  HEAD branch: master'
    origin_branch = 'master'  # unless we prove otherwise
    for line in origin_stats.splitlines():
        if 'head branch:' in line.lower():
            origin_branch = line.split(':', 1)[-1].strip()
            break

    origin = '%s/%s' % (remote_alias, origin_branch)

    # figure out the current branch
    current_branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
        cwd=news_dir
    ).decode().strip()

    print(':: Finding news in `%s` to add to remote `%s`' % (current_branch, origin))
    diff_command = ['git', 'diff', '%s...%s' % (origin, current_branch), '--name-status', news_dir]
    file_diff = subprocess.check_output(
        diff_command,
        cwd=news_dir
    ).decode()

    # the output of the git command looks like:
    # 'A       docs/news/789.feature'

    # [optional] ensure we have an addition, rather than just modify/delete
    added_news = [line for line in file_diff.splitlines() if line.lower().strip().startswith('a')]

    # pass or fail
    if not added_news:
        print(
            '! Error: Uh-oh, did not find any news files!\n'
            '! Please add a news file to `%s`\n'
            '+ File diff:\n%s\n'
            '{} Git diff command:\n`%s`\n' % (
                news_dir,
                file_diff.strip(),
                subprocess.list2cmdline(diff_command)
            )
        )
        exit(1)  # exit with an error status, no need for a traceback
    print(':: %s new files in `%s`' % (len(added_news), news_dir))


if __name__ == '__main__':
    news_dir = sys.argv[1] if len(sys.argv) > 1 else None
    main(news_dir)
