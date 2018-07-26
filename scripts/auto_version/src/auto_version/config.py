"""Configuration system for the auto_version tool"""
import os
import logging

import toml

from auto_version.definitions import SemVerSigFig

_LOG = logging.getLogger(__name__)


class Constants(object):
    """Internal - reused strings"""

    # regex groups
    KEY_GROUP = 'KEY'
    VALUE_GROUP = 'VALUE'

    # internal field keys
    VERSION_FIELD = 'VERSION_KEY'
    VERSION_STRICT_FIELD = 'VERSION_KEY_STRICT'
    VERSION_LOCK_FIELD = 'VERSION_LOCK'
    RELEASE_FIELD = 'RELEASE_FIELD'
    COMMIT_COUNT_FIELD = 'COMMIT_COUNT'
    COMMIT_FIELD = 'COMMIT'

    # as used in toml file
    CONFIG_KEY = 'AutoVersionConfig'

    PROJECT_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)))))


class AutoVersionConfig(object):
    """Configuration - can be overridden using a toml config file"""

    CONFIG_NAME = 'DEFAULT'
    RELEASED_VALUE = True
    VERSION_LOCK_VALUE = True
    VERSION_UNLOCK_VALUE = False
    key_aliases = {
        '__version__': Constants.VERSION_FIELD,
        '__strict_version__': Constants.VERSION_STRICT_FIELD,
        'PRODUCTION': Constants.RELEASE_FIELD,
        'SDK_MAJOR': SemVerSigFig.major,
        'SDK_MINOR': SemVerSigFig.minor,
        'SDK_PATCH': SemVerSigFig.patch,
        'VERSION_LOCK': Constants.VERSION_LOCK_FIELD,
        Constants.COMMIT_COUNT_FIELD: Constants.COMMIT_COUNT_FIELD,
        Constants.COMMIT_FIELD: Constants.COMMIT_FIELD,
    }
    _forward_aliases = {}  # autopopulated later - reverse mapping of the above
    targets = [
        os.path.join(
            Constants.PROJECT_ROOT, 'src', 'mbed_cloud', '_version.py'
        ),
        os.path.join(
            Constants.PROJECT_ROOT, 'src', 'mbed_cloud', '_build_info.py'
        ),
    ]
    regexers = {
        '.json':       r"""^\s*[\"]?(?P<KEY>\w+)[\"]?\s*:[\t ]*[\"]?(?P<VALUE>[^\r\n\t\f\v\"',]+)[\"]?,?""",  # noqa
        '.py':         r"""^\s*['\"]?(?P<KEY>\w+)['\"]?\s*[=:]\s*['\"]?(?P<VALUE>[^\r\n\t\f\v\"']+)['\"]?,?""",  # noqa
        '.cs':         r"""^\s*['\"]?(?P<KEY>\w+)['\"]?\s*[=:][\t ]*['\"]?(?P<VALUE>[^\r\n\t\f\v\"']+)['\"]?""",  # noqa
        '.csproj':     r"""^<(?P<KEY>\w+)>(?P<VALUE>\S+)<\/\w+>""",  # noqa
        '.properties': r"""^\s*(?P<KEY>\w+)\s*=[\t ]*(?P<VALUE>[^\r\n\t\f\v\"']+)?""",  # noqa
    }
    trigger_patterns = {
        SemVerSigFig.major: os.path.join(Constants.PROJECT_ROOT, 'docs', 'news', '*.major'),
        SemVerSigFig.minor: os.path.join(Constants.PROJECT_ROOT, 'docs', 'news', '*.feature'),
        SemVerSigFig.patch: os.path.join(Constants.PROJECT_ROOT, 'docs', 'news', '*.bugfix'),
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
            _LOG.debug('loading config from %s', os.path.abspath(path))
            config._inflate(toml.load(fh))
    else:
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            pass
        with open(path, 'w') as fh:
            toml.dump(config._deflate(), fh)
