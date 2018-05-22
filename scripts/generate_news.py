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
"""Handles usage of towncrier for automated changelog generation

a) abstracts configuration and execution for this project
b) prepares for usage in CI environment to stop from generating
   entries for every minor patch version

However, when deploying to production, we always want a changelog
"""
import os
import subprocess

from distutils.version import LooseVersion

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
news_dir = os.path.join(PROJECT_ROOT, 'docs', 'news')
metafile = os.path.join(news_dir, 'last_built.meta')


def main():
    """Writes out newsfile if significant version bump"""
    last_known = '0'
    if os.path.isfile(metafile):
        with open(metafile) as fh:
            last_known = fh.read()

    import mbed_cloud
    current = mbed_cloud.__version__

    # how significant a change in version scheme should trigger a new changelog entry
    # (api major, api minor, sdk major, sdk minor, sdk patch)
    sigfigs = 4
    current_version = LooseVersion(current).version
    last_known_version = LooseVersion(last_known).version

    should_towncrier = current_version[:sigfigs] != last_known_version[:sigfigs]

    print('%s -- %s :: current vs previous changelog build' % (current, last_known))
    if should_towncrier:
        print('%s >> %s :: running changelog build' % (current, last_known))
        subprocess.check_call(
            ['towncrier', '--yes'],
            cwd=os.path.join(PROJECT_ROOT, 'docs', 'changelog')
        )
        with open(metafile, 'w') as fh:
            fh.write(current)


if __name__ == '__main__':
    main()
