"""Configuration system for the auto_version tool"""
import os

import toml

from auto_version.definitions import SemVerSigFig


class Constants(object):
    """Internal - reused strings"""

    # regex groups
    KEY_GROUP = 'KEY'
    VALUE_GROUP = 'VALUE'

    # internal field keys
    VERSION_FIELD = 'VERSION_KEY'
    VERSION_LOCK_FIELD = 'VERSION_LOCK'
    RELEASE_FIELD = 'RELEASE_FIELD'
    COMMIT_COUNT_FIELD = 'COMMIT_COUNT'
    COMMIT_FIELD = 'COMMIT'

    # as used in toml file
    CONFIG_KEY = 'AutoVersionConfig'


class AutoVersionConfig(object):
    """Configuration - can be overridden using a toml config file"""

    CONFIG_NAME = 'DEFAULT'
    PROJECT_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)))))
    RELEASED_VALUE = True
    VERSION_LOCK_VALUE = True
    VERSION_UNLOCK_VALUE = False
    key_aliases = {
        SemVerSigFig.major: 'SDK_MAJOR',
        SemVerSigFig.minor: 'SDK_MINOR',
        SemVerSigFig.patch: 'SDK_PATCH',
        Constants.VERSION_FIELD: '__version__',
        Constants.VERSION_LOCK_FIELD: 'VERSION_LOCK',
        Constants.RELEASE_FIELD: 'PRODUCTION',
        Constants.COMMIT_COUNT_FIELD: Constants.COMMIT_COUNT_FIELD,
        Constants.COMMIT_FIELD: Constants.COMMIT_FIELD,
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
        '.properties': r"""(?P<KEY>\w+)\s*[=:]\s*(?P<VALUE>[\w\.\-_]+)""",
    }
    trigger_patterns = {
        SemVerSigFig.major: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.major'),
        SemVerSigFig.minor: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.feature'),
        SemVerSigFig.patch: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.bugfix'),
    }
    DEVMODE_TEMPLATE = '{version}.dev{count}'

    @classmethod
    def _deflate(cls):
        """Prepare for serialisation - returns a dictionary"""
        data = {k: v for k, v in vars(cls).items() if not k.startswith('_')}
        return {Constants.CONFIG_KEY: data}

    @classmethod
    def _inflate(cls, data):
        """Update config by deserialising input dictionary"""
        for k, v in data[Constants.CONFIG_KEY].items():
            setattr(cls, k, v)
        return cls._deflate()


def get_or_create_config(path, config):
    """Using TOML format, load config from given path, or write out example based on defaults"""
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
