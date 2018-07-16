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

SemVerFields = namedtuple('SemVerFields', ['major', 'minor', 'patch'])
SemVer = SemVerFields(*SemVerFields._fields)
NewsVer = SemVerFields('.major', '.feature', None)


def get_current_value(text_line):
    """Parses a line, returns the current value"""
    return ast.literal_eval(text_line.split('=')[-1].strip())


def increment(text_line):
    """Given a text line, increment the assigned value"""
    val = int(get_current_value(text_line))
    val += 1
    return str(val)


def get_in_files(targets, key):
    """Finds a line in a file containing an assignment"""
    for target in targets:
        with open(target) as fh:
            for line in fh.readlines():
                if line.startswith(key):
                    return get_current_value(line)


def is_bump_locked(targets):
    """Whether the version is currently undergoing a X.X.0 release and should not be bumped"""
    return get_in_files(targets, 'RESET_PATCH')


def write_out(targets, template, **params):
    """Writes version info into version file inline - primarily used in CI

    (imports during setup.py are fraught with peril)
    """
    for target in targets:
        fh = fileinput.FileInput(target, inplace=True)
        try:
            for line in fh:
                for k, v in params.items():
                    parts = line.split('=')
                    if len(parts) == 2 and parts[0].strip() == k:
                        if hasattr(v, '__call__'):
                            # pass value through a filter before rendering
                            v = v(line)
                        print(template % dict(key=k, value=v, script=__file__))
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
    default_filepaths = [
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'src', 'mbed_cloud', '_version.py'
        ),
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'src', 'mbed_cloud', '_semver.py'
        ),
    ]
    default_template = '%(key)s = %(value)r  # auto (see %(script)s)'
    parser = argparse.ArgumentParser(description="controls version number of releases")
    parser.add_argument(
        '--target',
        action='append',
        default=[],
        help='The target version file (default: %s).' % (default_filepaths,),
    )
    parser.add_argument(
        '--bump',
        choices=SemVer,
        help='Bumps the specified part of SemVer string. Use this locally to correctly modify the version file.',
    )
    parser.add_argument(
        '--release',
        action='store_true',
        help='Marks as a release build, which flags the build as released.',
    )
    parser.add_argument(
        '--template',
        default=default_template,
        help='Template for re-writing lines (default).',
    )
    parser.add_argument(
        '--exists',
        help='Specify filepath to automatically bump version based on existence of '
             'files with extensions: %s.' % (NewsVer,),
    )
    args, others = parser.parse_known_args()
    targets = args.target or default_filepaths

    if os.getenv('CI') and args.bump != SemVer.prod:
        raise ValueError('should be building production version numbers in CI')

    replacements = get_release_info()
    replacement_defaults = {
        SemVer.major: dict(
            SDK_MAJOR=increment,
            SDK_MINOR='0',
            SDK_PATCH='0',
        ),
        SemVer.minor: dict(
            SDK_MINOR=increment,
            SDK_PATCH='0',
        ),
        SemVer.patch: dict(
            SDK_PATCH=increment,
        ),
    }

    # apply the conditional kwargs based on SemVer mode
    replacements.update(replacement_defaults.get(args.bump, {}))

    if args.release:
        replacements.update(RELEASE=True)

    # pull extra kwargs from commandline
    for kwargs in others:
        k, v = kwargs.split('=')
        replacements[k.strip()] = ast.literal_eval(v.strip())

    # unless we're bump locked
    if is_bump_locked(targets):
        # if version is a X.X.0 release, then remove the bump lock (for next time) and do not bump patch
        replacements.pop('SDK_PATCH')
        replacements.setdefault('RESET_PATCH', False)

    # pure semver
    LAST_RELEASE = get_in_files(targets, 'LAST_RELEASE')
    MAJOR, MINOR, PATCH = LAST_RELEASE.split('.')[:3]
    print(LAST_RELEASE)
    LAST_RELEASE = '.'.join([
        replacements.get('SDK_MAJOR', MAJOR),
        replacements.get('SDK_MINOR', MINOR),
        replacements.get('SDK_PATCH', PATCH)
    ])
    print(LAST_RELEASE)

    write_out(targets, args.template, **replacements)


__name__ == '__main__' and main()
