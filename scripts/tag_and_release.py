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


def git_url_ssh_to_https(url):
    """Convert a git url

    url will look like
    https://github.com/ARMmbed/mbed-cloud-sdk-python.git
    or
    git@github.com:ARMmbed/mbed-cloud-sdk-python.git
    we want:
    https://${GITHUB_TOKEN}@github.com/ARMmbed/mbed-cloud-sdk-python-private.git
    """
    path = url.split('github.com', 1)[1][1:].strip()
    new = 'https://{GITHUB_TOKEN}@github.com/%s' % path
    print('rewriting git url to: %s' % new)
    return new.format(GITHUB_TOKEN=os.getenv('GITHUB_TOKEN'))


def main():
    """Tags the current repository

    and commits changes to news files
    """
    # see:
    # https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi
    twine_repo = os.getenv('TWINE_REPOSITORY_URL') or os.getenv('TWINE_REPOSITORY')
    print('tagging and releasing to %s as %s' % (
        twine_repo,
        os.getenv('TWINE_USERNAME')
    ))

    if not twine_repo:
        raise Exception('cannot release to implicit pypi repository. explicitly set the repo/url.')

    version = subprocess.check_output(['python', 'setup.py', '--version']).decode().strip()
    if 'dev' in version:
        raise Exception('cannot release unversioned project: %s' % version)

    print('python - preparing environment')
    subprocess.check_call(['apk', 'update'])
    subprocess.check_call(['apk', 'add', 'git'])
    subprocess.check_call(['pip', 'install', 'twine'])
    url = subprocess.check_output(['git', 'remote', 'get-url', 'origin'])
    new_url = git_url_ssh_to_https(url.decode())
    subprocess.check_call(['git', 'remote', 'set-url', 'origin', new_url])
    branch_spec = 'origin/%s' % os.getenv('CIRCLE_BRANCH')
    subprocess.check_call(['git', 'branch', '--set-upstream-to', branch_spec])
    print('git - pushing tags')
    subprocess.check_call(['git', 'tag', '-a', version, '-m', 'release %s' % version])
    subprocess.check_call(['git', 'tag', '-f', 'latest'])
    subprocess.check_call(['git', 'push', '-f', 'origin', '--tags'])
    print('git - add changes')
    subprocess.check_call(['git', 'add', 'src/mbed_cloud/_version.py'])
    subprocess.check_call(['git', 'add', 'CHANGELOG.rst'])
    subprocess.check_call(['git', 'add', 'docs/news/*'])
    print('git - commit changes')
    subprocess.check_call(['git', 'commit', '-m', ':checkered_flag: :newspaper: releasing version %s\n[skip ci]' % version])
    print('git - pushing commits')
    subprocess.check_call(['git', 'push', 'origin'])
    print('pypi - uploading')
    subprocess.check_call(['python', '-m', 'twine', 'upload', 'release-dist/*'])
    print('pypi - uploading successful')


if __name__ == '__main__':
    main()
