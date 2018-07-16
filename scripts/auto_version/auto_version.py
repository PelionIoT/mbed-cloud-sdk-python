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
import argparse
import ast
import fileinput
import glob
import os
import pprint
import re
import shlex
import subprocess

from collections import namedtuple

import toml

SemVerFields = namedtuple('SemVerFields', ['major', 'minor', 'patch'])
SemVer = SemVerFields(*SemVerFields._fields)


class AutoVersionConfig(object):
    CONFIG_NAME = 'DEFAULT'

    COMMIT_COUNT_FIELD = 'COMMIT_COUNT'
    COMMIT_FIELD = 'COMMIT'
    KEY_GROUP = 'KEY'
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    RELEASED_FIELD = 'PRODUCTION'
    RELEASED_VALUE = True
    VALUE_GROUP = 'VALUE'
    VERSION_FIELD = '__version__'
    semver_aliases = {
        SemVer.major: 'SDK_MAJOR',
        SemVer.minor: 'SDK_MINOR',
        SemVer.patch: 'SDK_PATCH',
        VERSION_FIELD: '__version__',
    }
    targets = [
        os.path.join(
            PROJECT_ROOT, 'src', 'mbed_cloud', '_version.py'
        ),
        os.path.join(
            PROJECT_ROOT, 'src', 'mbed_cloud', '_build_info.py'
        ),
    ]
    regexers = {
        '.json': r"""(?P<KEY>\w+)\s?[=:]\s?['\"]?(?P<VALUE>[\w\.\-_]+)['\"]?""",
        '.py': r"""(?P<KEY>\w+)\s?[=:]\s?['\"]?(?P<VALUE>[\w\.\-_]+)['\"]?""",
        '.csproj': r"""<(?P<KEY>\w+)>(?P<VALUE>\S+)<\/\w+>""",
    }
    trigger_patterns = {
        SemVer.major: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.major'),
        SemVer.minor: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.feature'),
    }
    DEVMODE_TEMPLATE = '{version}.dev{count}'

    _config_key = 'AutoVersionConfig'

    @classmethod
    def _deflate(cls):
        data = {k: v for k, v in vars(cls).items() if not k.startswith('_')}
        return {cls._config_key: data}

    @classmethod
    def _inflate(cls, data):
        for k, v in data[cls._config_key].items():
            if isinstance(v, dict):
                getattr(cls, k).update(v)
            else:
                setattr(cls, k, v)
        return cls._deflate()


config = AutoVersionConfig


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
        key = match.group(config.KEY_GROUP)
        replacement = self.params.get(key)
        if replacement is None:  # if this isn't a key we are interested in replacing
            replaced = original
        else:
            self.missing.remove(key)
            replaced = ''.join([
                original[:match.start(config.VALUE_GROUP)],
                str(replacement),
                original[match.end(config.VALUE_GROUP):],
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
        regexer = config.regexers[file_ext]
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
                results[k_v[config.KEY_GROUP]] = k_v[config.VALUE_GROUP]
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
    known = {key: data.get(alias) for key, alias in config.semver_aliases.items() if data.get(alias) is not None}

    inferred_semver = None
    parts = (known.pop(config.VERSION_FIELD) or '').split('.')[:3]
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


def get_dvcs_info():
    """Gets current repository info from git"""
    cmd = 'git rev-list --count HEAD'
    commit_count = str(int(subprocess.check_output(shlex.split(cmd)).decode('utf8').strip()))
    cmd = 'git rev-parse HEAD'
    commit = str(subprocess.check_output(shlex.split(cmd)).decode('utf8').strip())
    return {config.COMMIT_FIELD: commit, config.COMMIT_COUNT_FIELD: commit_count}


def get_cli():
    parser = argparse.ArgumentParser(description='controls version number of releases')
    parser.add_argument(
        '--target',
        action='append',
        default=[],
        help='Files containing version info. Assumes unique variable names between files. (default: %s).' % (
        config.targets,),
    )
    parser.add_argument(
        '--bump',
        choices=SemVer,
        help='Bumps the specified part of SemVer string. Use this locally to correctly modify the version file.',
    )
    parser.add_argument(
        '--set',
        help='Set the SemVer string. Use this locally to set the project version explicitly.',
    )
    parser.add_argument(
        '--release',
        action='store_true',
        default=False,
        help='Marks as a release build, which flags the build as released.',
    )
    parser.add_argument(
        '--config',
        help='Configuration file path.',
    )
    args, others = parser.parse_known_args()

    # pull extra kwargs from commandline, e.g. TESTRUNNER_VERSION
    updates = {}
    for kwargs in others:
        k, v = kwargs.split('=')
        updates[k.strip()] = ast.literal_eval(v.strip())

    return args, updates


def get_or_create_config(path):
    if os.path.isfile(path):
        with open(path) as fh:
            print('loading config from %s' % path)
            config._inflate(toml.load(fh))
    else:
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            pass
        with open(path, 'w') as fh:
            toml.dump(config._deflate(), fh)


def main():
    args, updates = get_cli()

    if args.config:
        get_or_create_config(args.config)
    print('using config: %r' % config.CONFIG_NAME)

    for k, v in config.regexers.items():
        config.regexers[k] = re.compile(v)

    triggered = detect_file_triggers(config.trigger_patterns)
    if args.bump:
        triggered.add(args.bump)
    all_data = read(config.targets)
    current_semver = get_current_semver(all_data)
    new_semver = SemVerFields(*args.set.split('.')) if args.set else make_new_semver(current_semver, triggered)

    if args.release:
        updates[config.RELEASED_FIELD] = config.RELEASED_VALUE

    updates.update(get_dvcs_info())

    # where possible, write back any other aliases based on the semver
    for k, v in config.semver_aliases.items():
        updates[v] = getattr(new_semver, k, '.'.join(new_semver))

    print(current_semver)
    print(new_semver)
    pprint.pprint(updates)
    write_out(config.targets, **updates)


__name__ == '__main__' and main()
