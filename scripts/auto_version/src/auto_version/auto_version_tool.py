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
import fileinput
import glob
import os
import pprint
import re
import shlex
import subprocess

import auto_version.definitions
from auto_version.cli import get_cli
from auto_version.config import AutoVersionConfig as config
from auto_version.config import get_or_create_config
from auto_version.replacement_handler import ReplacementHandler

from auto_version import semver


def write_targets(targets, **params):
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
        regexer = config.regexers[file_ext]
        yield target, regexer


def read_targets(targets):
    """Reads generic key-value pairs from input files"""
    results = {}
    for target, regexer in regexer_for_targets(targets):
        with open(target) as fh:
            for line in fh:
                match = regexer.match(line.strip())
                if not match:
                    continue
                k_v = match.groupdict()
                results[k_v[config.KEY_GROUP]] = k_v[config.VALUE_GROUP]
    return results


def detect_file_triggers(trigger_patterns):
    """The existence of files matching configured globs will trigger a version bump"""
    triggered = set()
    for trigger, pattern in trigger_patterns.items():
        if glob.glob(pattern):
            triggered.add(trigger)
    return triggered


def get_dvcs_info():
    """Gets current repository info from git"""
    cmd = 'git rev-list --count HEAD'
    commit_count = str(int(subprocess.check_output(shlex.split(cmd)).decode('utf8').strip()))
    cmd = 'git rev-parse HEAD'
    commit = str(subprocess.check_output(shlex.split(cmd)).decode('utf8').strip())
    return {config.COMMIT_FIELD: commit, config.COMMIT_COUNT_FIELD: commit_count}


def main():
    args, updates = get_cli()

    if args.config:
        get_or_create_config(args.config, config)
    print('using config: %r' % config.CONFIG_NAME)

    for k, v in config.regexers.items():
        config.regexers[k] = re.compile(v)

    triggered = detect_file_triggers(config.trigger_patterns)
    if args.bump:
        triggered.add(args.bump)
    all_data = read_targets(config.targets)
    current_semver = semver.get_current_semver(all_data)
    new_semver = auto_version.definitions.SemVerFields(*args.set.split('.')) if args.set else semver.make_new_semver(current_semver, triggered)

    version_string = '.'.join(new_semver)

    if args.release:
        # in production, we have something like `1.2.3`, as well as a flag e.g. PRODUCTION=True
        updates[config.RELEASED_FIELD] = config.RELEASED_VALUE
    else:
        # in dev mode, we have a dev marker e.g. `1.2.3.dev678`
        version_string = config.DEVMODE_TEMPLATE.format(
            version=version_string,
            count=updates.get(config.COMMIT_COUNT_FIELD, 0)
        )

    updates.update(get_dvcs_info())

    # where possible, write back any other aliases based on the semver
    for k, v in config.semver_aliases.items():
        updates[v] = getattr(new_semver, k, version_string)

    print(current_semver)
    print(new_semver)
    pprint.pprint(updates)
    write_targets(config.targets, **updates)


__name__ == '__main__' and main()
