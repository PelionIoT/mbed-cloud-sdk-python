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
import glob
import os
import re
import pprint
import shlex
import subprocess

# TODO: move these items into a configuration system
KEY_GROUP = 'KEY'
VALUE_GROUP = 'VALUE'
VERSION_FIELD = '__version__'
SemVerFields = namedtuple('SemVerFields', ['major', 'minor', 'patch'])
SemVer = SemVerFields(*SemVerFields._fields)
SemVerAliases = {
    SemVer.major: 'SDK_MAJOR',
    SemVer.minor: 'SDK_MINOR',
    SemVer.patch: 'SDK_PATCH',
    VERSION_FIELD: '__version__',
}

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

re_assignment_detector = re.compile(r"""(?P<KEY>\w+)\s?[=:]\s?['\"]?(?P<VALUE>[\w\.\-_]+)['\"]?""")
use_xml = {'.csproj'}
re_assignment_detector_xml = re.compile(r"""<(?P<KEY>\w+)>(?P<VALUE>\S+)<\/\w+>""")
trigger_patterns = {
    SemVer.major: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.major'),
    SemVer.minor: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.feature'),
}


class ReplacementHandler(object):
    """Tool used by regex when performing substitutions

    We store state so that we consume our parameters as we make each replacement
    """
    def __init__(self, **params):
        self.params = params
        self.missing = set(params.keys())

    def __call__(self, match):
        """Given a regex Match Object, return the entire replacement string"""
        original = match.string.strip('\r\n')
        key = match.group(KEY_GROUP)
        replacement = self.params.get(key)
        if replacement is None:  # if this isn't a key we are interested in replacing
            replaced = original
        else:
            self.missing.remove(key)
            replaced = ''.join([
                original[:match.start(VALUE_GROUP)],
                replacement,
                original[match.end(VALUE_GROUP):],
            ])
        return replaced


def write_out(targets, **params):
    """Writes version info into version file inline"""
    handler = ReplacementHandler(**params)
    for target, regexer in regexer_for_targets(targets):
        fh = fileinput.FileInput(target, inplace=True)
        try:
            for line in fh:
                # printing to stdout writes to the file
                print(regexer.sub(handler, line).rstrip())
        finally:
            fh.close()
    if handler.missing:
        raise Exception('Failed to complete all expected replacements: %r' % handler.missing)


def regexer_for_targets(targets):
    """Pairs up target files with their correct regex"""
    for target in targets:
        path, file_ext = os.path.splitext(target)
        regexer = re_assignment_detector_xml if file_ext in use_xml else re_assignment_detector
        yield target, regexer


def read(targets):
    """Reads generic key-value pairs from input files"""
    results = {}
    for target, regexer in regexer_for_targets(targets):
        with open(target) as fh:
            for line in fh:
                match = regexer.match(line.strip())
                if not match:
                    continue
                k_v = match.groupdict()
                results[k_v[KEY_GROUP]] = k_v[VALUE_GROUP]
    return results


def detect_file_triggers(trigger_patterns):
    """The existence of files matching configured globs will trigger a version bump"""
    triggered = set()
    for trigger, pattern in trigger_patterns.items():
        if glob.glob(pattern):
            triggered.add(trigger)
    return triggered


def get_current_semver(data):
    """Given a dictionary of all version data available, determine the current version"""
    # get the not-none values from data
    known = {key: data.get(alias) for key, alias in SemVerAliases.items() if data.get(alias) is not None}

    inferred_semver = None
    parts = (known.pop(VERSION_FIELD) or '').split('.')[:3]
    if len(parts) == 3:
        inferred_semver = SemVerFields(*parts)

    explicit_semver = None
    if len(known) == 3:
        explicit_semver = SemVerFields(**known)

    if inferred_semver and explicit_semver and (explicit_semver != inferred_semver):
        raise ValueError('conflicting versions within project: %s %s' % (inferred_semver, explicit_semver))

    using_existing = inferred_semver or explicit_semver
    if not using_existing:
        raise ValueError('could not find existing semver')
    return using_existing


def make_new_semver(current_semver, all_triggers):
    """defines how to increment semver based on which significant figure is triggered"""
    all_triggers = all_triggers or {SemVer.patch}  # minimum increment is patch
    new_semver = {}
    bumped = False
    for sig_fig in SemVer:  # iterate sig figs in order of significance
        value = getattr(current_semver, sig_fig)
        if bumped:
            new_semver[sig_fig] = '0'
        elif sig_fig in all_triggers:
            new_semver[sig_fig] = str(int(value) + 1)
            bumped = True
        else:
            new_semver[sig_fig] = value
    return SemVerFields(**new_semver)


def main():
    # load cli
    # load config file
    # load git extras
    targets = [
        os.path.join(
            PROJECT_ROOT, 'src', 'mbed_cloud', '_version.py'
        ),
        os.path.join(
            PROJECT_ROOT, 'src', 'mbed_cloud', '_build_info.py'
        ),
    ]
    triggered = detect_file_triggers(trigger_patterns)
    all_data = read(targets)
    current_semver = get_current_semver(all_data)
    new_semver = make_new_semver(current_semver, triggered)
    updates = {}
    # if available, write back to any aliases
    for k, v in SemVerAliases.items():
        updates[v] = getattr(new_semver, k, '.'.join(new_semver))
    print(current_semver)
    print(new_semver)
    pprint.pprint(updates)
    write_out(targets, **updates)


__name__ == '__main__' and main()
