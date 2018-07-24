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

from auto_version.cli import get_cli
from auto_version.config import AutoVersionConfig as config
from auto_version.config import get_or_create_config
from auto_version.config import Constants
import auto_version.definitions
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
                results[k_v[Constants.KEY_GROUP]] = k_v[Constants.VALUE_GROUP]
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
    return {Constants.COMMIT_FIELD: commit, Constants.COMMIT_COUNT_FIELD: commit_count}


def main(
    set_to=None, release=None, bump=None, lock=None, file_triggers=None,
    config_path=None, **extra_updates
):
    """Main workflow.

    Load config from cli and file
    Detect "bump triggers" - things that cause a version increment
    Find the current version
    Create a new version
    Write out new version and any other requested variables

    :param set_to: explicitly set semver to this version string
    :param release: marks with a production flag
                just sets a single flag as per config
    :param bump: string indicating major/minor/patch
                more significant bumps will zero the less significant ones
    :param lock: locks the version string for the next call to autoversion
                lock only removed if a version bump would have occurred
    :param file_triggers: whether to enable bumping based on file triggers
                bumping occurs once if any file(s) exist that match the config
    :param config_path: path to config file
    :param extra_updates:
    :return:
    """
    updates = {}
    updates.update(get_dvcs_info())
    if config_path:
        get_or_create_config(config_path, config)

    for k, v in config.regexers.items():
        config.regexers[k] = re.compile(v)

    # a forward-mapping of the configured aliases
    # giving <our config param> : <the configured value>
    # if a value occurs multiple times, we take the last set value
    for k, v in config.key_aliases.items():
        config._forward_aliases[v] = k

    triggers = set()
    if file_triggers:
        triggers = triggers.union(detect_file_triggers(config.trigger_patterns))

    if bump:
        triggers.add(bump)

    all_data = read_targets(config.targets)

    # binary state lock protects from version increments if set
    lock_key = config._forward_aliases.get(Constants.VERSION_LOCK_FIELD)
    if triggers and lock_key and str(all_data.get(lock_key)) == str(config.VERSION_LOCK_VALUE):
        triggers.clear()
        updates[Constants.VERSION_LOCK_FIELD] = config.VERSION_UNLOCK_VALUE

    current_semver = semver.get_current_semver(all_data)
    new_semver = (
        auto_version.definitions.SemVer(*set_to.split('.'))
        if set_to else
        semver.make_new_semver(current_semver, triggers)
    )

    version_string = '.'.join(new_semver)

    if release:
        # in production, we have something like `1.2.3`, as well as a flag e.g. PRODUCTION=True
        updates[Constants.RELEASE_FIELD] = config.RELEASED_VALUE
    else:
        # in dev mode, we have a dev marker e.g. `1.2.3.dev678`
        version_string = config.DEVMODE_TEMPLATE.format(
            version=version_string,
            count=updates.get(Constants.COMMIT_COUNT_FIELD, 0)
        )

    # make available all components of the semantic version including the full string
    updates[Constants.VERSION_FIELD] = version_string
    for part in semver.SemVerSigFig:
        updates[part] = getattr(new_semver, part)

    # if we are explicitly setting or locking the version, then set the lock field
    if set_to or lock:
        updates[Constants.VERSION_LOCK_FIELD] = config.VERSION_LOCK_VALUE

    # only rewrite field the user has specified in the configuration
    native_updates = {
        native: updates.get(key)
        for native, key in config.key_aliases.items()
        if updates.get(key) is not None
    }

    # finally, add in commandline overrides
    native_updates.update(extra_updates)

    write_targets(config.targets, **native_updates)

    return current_semver, new_semver, native_updates


def main_from_cli():
    """Main workflow.

    Load config from cli and file
    Detect "bump triggers" - things that cause a version increment
    Find the current version
    Create a new version
    Write out new version and any other requested variables
    """
    args, command_line_updates = get_cli()
    old, new, updates = main(
        set_to=args.set,
        lock=args.lock,
        release=args.release,
        bump=args.bump,
        file_triggers=args.file_triggers,
        config_path=args.config,
        **command_line_updates
    )
    print(old)
    print(new)
    pprint.pprint(updates)


__name__ == '__main__' and main_from_cli()
