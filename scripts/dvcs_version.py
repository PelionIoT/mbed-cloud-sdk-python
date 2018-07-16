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
from collections import namedtuple
import argparse
import ast
import fileinput
import os
import shlex
import subprocess

SemVer = namedtuple('SemVer', ['major', 'minor', 'patch', 'beta', 'release'])
SemVer = SemVer(*SemVer._fields)


def get_current_value(text_line):
    """Parses a line, returns the current value"""
    return ast.literal_eval(text_line.split('=')[-1].strip())


def increment(text_line):
    """Given a text line, increment the assigned value"""
    val = int(get_current_value(text_line))
    val += 1
    return str(val)


def is_bump_locked(target):
    """Whether the version is currently undergoing a X.X.0 release and should not be bumped"""
    with open(target) as fh:
        for line in fh.readlines():
            if line.startswith('RESET_PATCH'):
                return get_current_value(line)


def write_out(target, **params):
    """Writes version info into version file inline - primarily used in CI

    (imports during setup.py are fraught with peril)
    """
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


def get_release_info():
    """Gets info from git"""
    cmd = 'git rev-list --count HEAD'
    commit_count = str(int(subprocess.check_output(shlex.split(cmd)).decode('utf8').strip()))
    cmd = 'git rev-parse HEAD'
    commit = subprocess.check_output(shlex.split(cmd)).decode('utf8').strip()
    return dict(COMMIT=commit, COMMIT_COUNT=commit_count, SDK_PATCH=increment)


def main():
    """Generates DVCS version information"""
    parser = argparse.ArgumentParser(description="controls version number of releases")
    parser.add_argument(
        'target',
        nargs='?',
        default=os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'src', 'mbed_cloud', '_version.py'
        ),
        help='The target version file.',
    )
    parser.add_argument(
        '--bump',
        choices=SemVer,
        help='Bumps the specified part of SemVer string. Use this locally to correctly modify the version file.',
    )
    args, others = parser.parse_known_args()

    if os.getenv('CI') and args.bump != SemVer.prod:
        raise ValueError('should be building production version numbers in CI')

    replacements = dict(
        BETA=False,
    )

    replacement_defaults = {
        SemVer.major: dict(
            RESET_PATCH=True,
            SDK_MAJOR=increment,
            SDK_MINOR='0',
            SDK_PATCH='0',
        ),
        SemVer.minor: dict(
            RESET_PATCH=True,
            SDK_MINOR=increment,
            SDK_PATCH='0',
        ),
        SemVer.patch: dict(
            SDK_PATCH=increment,
        ),
        SemVer.beta: dict(
            BETA=True
        ),
        SemVer.release: get_release_info(),
    }

    # apply the conditional kwargs based on SemVer mode
    replacements.update(replacement_defaults.get(args.bump, {}))

    # pull extra kwargs from commandline
    for kwargs in others:
        k, v = kwargs.split('=')
        replacements[k.strip()] = ast.literal_eval(v.strip())

    # unless we're bump locked
    if is_bump_locked(args.target):
        # if version is a X.X.0 release, then remove the bump lock (for next time) and do not bump patch
        replacements.pop('SDK_PATCH')
        replacements['RESET_PATCH'] = False

    write_out(args.target, **replacements)


__name__ == '__main__' and main()
