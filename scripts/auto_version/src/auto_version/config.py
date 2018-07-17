import os

import toml

from auto_version.definitions import SemVer


class AutoVersionConfig(object):
    CONFIG_NAME = 'DEFAULT'

    COMMIT_COUNT_FIELD = 'COMMIT_COUNT'
    COMMIT_FIELD = 'COMMIT'
    KEY_GROUP = 'KEY'
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
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


def get_or_create_config(path, config):
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
