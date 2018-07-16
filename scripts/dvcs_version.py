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
"""Generates DVCS version information

see also:
https://git-scm.com/docs/git-shortlog
https://www.python.org/dev/peps/pep-0440/
https://pypi.python.org/pypi/semver
https://pypi.python.org/pypi/bumpversion
https://github.com/warner/python-versioneer

"""
import ast
import fileinput
import os
import shlex
import sys
import subprocess


def increment(text_line):
    """Given a text line, increment the assigned value"""
    current = ast.literal_eval(text_line.split('=')[-1].strip())
    val = int(current)
    val += 1
    return str(val)


def write_out(**params):
    """Writes version info into version file inline - only used in CI

    (imports during setup.py are fraught with peril)
    """
    target = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 'src', 'mbed_cloud', '_version.py'
    )
    fh = fileinput.FileInput(target, inplace=True)
    try:
        for line in fh:
            for k, v in params.items():
                if line.split('=')[0].strip() == k:
                    if hasattr(v, '__call__'):
                        v = v(line)
                    print('%s = %r  # auto (see %s)' % (k, v, __file__))
                    params.pop(k)
                    break
            else:
                print(line.rstrip())
    finally:
        fh.close()
    if params:
        raise Exception('Failed to complete all replacements: %r' % params)


def main(**replacements):
    """Generates DVCS version information"""
    cmd = 'git rev-list --count HEAD'
    commit_count = str(int(subprocess.check_output(shlex.split(cmd)).strip()))
    cmd = 'git rev-parse HEAD'
    commit = subprocess.check_output(shlex.split(cmd)).strip().decode()
    replacement_params = dict(COMMIT=commit, COMMIT_COUNT=commit_count, SDK_MAJOR=increment)
    replacement_params.update(replacements)
    write_out(**replacement_params)


if __name__ == '__main__':
    replacements = {}
    for kwargs in sys.argv[1:]:
        k, v = kwargs.split('=')
        replacements[k.strip()] = ast.literal_eval(v.strip())
    main(**replacements)
