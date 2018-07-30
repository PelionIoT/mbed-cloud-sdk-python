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
import glob
import logging
import os
import pprint
import re
import shlex
import subprocess
import warnings

from auto_version.cli import get_cli
from auto_version.config import AutoVersionConfig as config
from auto_version.config import get_or_create_config
from auto_version.config import Constants
import auto_version.definitions
from auto_version.replacement_handler import ReplacementHandler

from auto_version import semver

_LOG = logging.getLogger(__file__)


def replace_lines(regexer, handler, lines):
    """Uses replacement handler to perform replacements on lines of text

    First we strip off all whitespace
    We run the replacement on a clean 'content' string
    Finally we replace the original content with the replaced version
    This ensures that we retain the correct whitespace from the original line
    """
    result = []
    for line in lines:
        content = line.strip()
        replaced = regexer.sub(handler, content)
        result.append(line.replace(content, replaced, 1))
    return result


def write_targets(targets, **params):
    """Writes version info into version file"""
    handler = ReplacementHandler(**params)
    for target, regexer in regexer_for_targets(targets):
        with open(target) as fh:
            lines = fh.readlines()
        lines = replace_lines(regexer, handler, lines)
        with open(target, 'w') as fh:
            fh.writelines(lines)
    if handler.missing:
        raise Exception('Failed to complete all expected replacements: %r' % handler.missing)


def regexer_for_targets(targets):
    """Pairs up target files with their correct regex"""
    for target in targets:
        path, file_ext = os.path.splitext(target)
        regexer = config.regexers[file_ext]
        yield target, regexer


def extract_keypairs(lines, regexer):
    """Given some lines of text, extract key-value pairs from them"""
    updates = {}
    for line in lines:
        # for consistency we must match the replacer and strip whitespace / newlines
        match = regexer.match(line.strip())
        if not match:
            continue
        k_v = match.groupdict()
        updates[k_v[Constants.KEY_GROUP]] = k_v[Constants.VALUE_GROUP]
    return updates


def read_targets(targets):
    """Reads generic key-value pairs from input files"""
    results = {}
    for target, regexer in regexer_for_targets(targets):
        with open(target) as fh:
            results.update(extract_keypairs(fh.readlines(), regexer))
    return results


def detect_file_triggers(trigger_patterns):
    """The existence of files matching configured globs will trigger a version bump"""
    triggers = set()
    for trigger, pattern in trigger_patterns.items():
        matches = glob.glob(pattern)
        if matches:
            _LOG.debug('trigger: %s bump from %r\n\t%s', trigger, pattern, matches)
            triggers.add(trigger)
        else:
            _LOG.debug('trigger: no match on %r', pattern)
    return triggers


def get_all_triggers(bump, file_triggers):
    """Aggregated set of significant figures to bump"""
    triggers = set()
    if file_triggers:
        triggers = triggers.union(detect_file_triggers(config.trigger_patterns))
    if bump:
        _LOG.debug('trigger: %s bump requested', bump)
        triggers.add(bump)
    return triggers


def get_lock_behaviour(triggers, all_data, lock):
    """Binary state lock protects from version increments if set"""
    updates = {}
    lock_key = config._forward_aliases.get(Constants.VERSION_LOCK_FIELD)
    # if we are explicitly setting or locking the version, then set the lock field True anyway
    if lock:
        updates[Constants.VERSION_LOCK_FIELD] = config.VERSION_LOCK_VALUE
    elif triggers and lock_key and str(all_data.get(lock_key)) == str(config.VERSION_LOCK_VALUE):
        triggers.clear()
        updates[Constants.VERSION_LOCK_FIELD] = config.VERSION_UNLOCK_VALUE
    return updates


def get_final_version_string(release_mode, semver, commit_count=0):
    """Generates update dictionary entries for the version string"""
    version_string = '.'.join(semver)
    maybe_dev_version_string = version_string
    updates = {}
    if release_mode:
        # in production, we have something like `1.2.3`, as well as a flag e.g. PRODUCTION=True
        updates[Constants.RELEASE_FIELD] = config.RELEASED_VALUE
    else:
        # in dev mode, we have a dev marker e.g. `1.2.3.dev678`
        maybe_dev_version_string = config.DEVMODE_TEMPLATE.format(
            version=version_string,
            count=commit_count
        )

    # make available all components of the semantic version including the full string
    updates[Constants.VERSION_FIELD] = maybe_dev_version_string
    updates[Constants.VERSION_STRICT_FIELD] = version_string
    return updates


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

    if config_path:
        get_or_create_config(config_path, config)

    for k, v in config.regexers.items():
        config.regexers[k] = re.compile(v)

    # a forward-mapping of the configured aliases
    # giving <our config param> : <the configured value>
    # if a value occurs multiple times, we take the last set value
    for k, v in config.key_aliases.items():
        config._forward_aliases[v] = k

    all_data = read_targets(config.targets)
    current_semver = semver.get_current_semver(all_data)

    triggers = get_all_triggers(bump, file_triggers)
    updates.update(get_lock_behaviour(triggers, all_data, lock))
    updates.update(get_dvcs_info())

    if set_to:
        new_semver = auto_version.definitions.SemVer(*set_to.split('.'))
        if not lock:
            warnings.warn(
                'After setting version manually, does it need locking for a CI flow?',
                UserWarning
            )
    else:
        new_semver = semver.make_new_semver(current_semver, triggers)

    updates.update(get_final_version_string(
        release_mode=release,
        semver=new_semver,
        commit_count=updates.get(Constants.COMMIT_COUNT_FIELD, 0)
    ))

    for part in semver.SemVerSigFig:
        updates[part] = getattr(new_semver, part)

    # only rewrite a field that the user has specified in the configuration
    native_updates = {
        native: updates[key]
        for native, key in config.key_aliases.items()
        if key in updates
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
    log_level = logging.WARNING - 10 * args.verbosity
    logging.basicConfig(level=log_level, format='%(module)s %(levelname)8s %(message)s')
    old, new, updates = main(
        set_to=args.set,
        lock=args.lock,
        release=args.release,
        bump=args.bump,
        file_triggers=args.file_triggers,
        config_path=args.config,
        **command_line_updates
    )
    _LOG.info('previously: %s', old)
    _LOG.info('currently:  %s', new)
    _LOG.debug('updates:\n%s', pprint.pformat(updates))
    print(
        updates.get(config._forward_aliases.get(Constants.VERSION_FIELD)) or
        updates.get(config._forward_aliases.get(Constants.VERSION_STRICT_FIELD))
    )


__name__ == '__main__' and main_from_cli()
