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

import subprocess
import os


def main():
    """Tags the current repository

    and commits changes to news files
    """
    # see:
    # https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi
    # nb. to test locally, switch back to an HTTPS url:
    # git remote set-url origin https://${GITHUB_TOKEN}@github.com/ARMmbed/mbed-cloud-sdk-python-private.git
    print('tagging and releasing to %s as %s' % (
        os.getenv('TWINE_REPOSITORY_URL', os.getenv('TWINE_REPOSITORY')),
        os.getenv('TWINE_USERNAME')
    ))

    version = subprocess.check_output(['python', 'setup.py', '--version']).decode().strip()
    if 'dev' in version:
        raise Exception('cannot release unversioned project: %s' % version)

    subprocess.check_call(['apk', 'update'])
    subprocess.check_call(['apk', 'add', 'git'])
    subprocess.check_call(['apk', 'add', 'openssh'])
    subprocess.check_call(['git', 'tag', version])
    subprocess.check_call(['git', 'push', '--tags'])
    subprocess.check_call(['git', 'add', 'NEWS.rst' 'docs/news/*'])
    subprocess.check_call(['git', 'commit', '-m', ':newspaper: Update changelog [skip ci]'])
    subprocess.check_call(['git', 'push'])
    subprocess.check_call(['twine', 'upload', 'dist/*'])


if __name__ == '__main__':
    main()
