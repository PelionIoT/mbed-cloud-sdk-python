import os
import re

from collections.__init__ import namedtuple

KEY_GROUP = 'KEY'
VALUE_GROUP = 'VALUE'
VERSION_FIELD = '__version__'
RELEASED_FIELD = 'PRODUCTION'
COMMIT_FIELD = 'COMMIT'
COMMIT_COUNT_FIELD = 'COMMIT_COUNT'
SemVerFields = namedtuple('SemVerFields', ['major', 'minor', 'patch'])
SemVer = SemVerFields(*SemVerFields._fields)
SemVerAliases = {
    SemVer.major: 'SDK_MAJOR',
    SemVer.minor: 'SDK_MINOR',
    SemVer.patch: 'SDK_PATCH',
    VERSION_FIELD: '__version__',
}
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
targets = [
    os.path.join(
        PROJECT_ROOT, 'src', 'mbed_cloud', '_version.py'
    ),
    os.path.join(
        PROJECT_ROOT, 'src', 'mbed_cloud', '_build_info.py'
    ),
]
re_assignment_detector = re.compile(r"""(?P<KEY>\w+)\s?[=:]\s?['\"]?(?P<VALUE>[\w\.\-_]+)['\"]?""")
use_xml = {'.csproj'}
re_assignment_detector_xml = re.compile(r"""<(?P<KEY>\w+)>(?P<VALUE>\S+)<\/\w+>""")
trigger_patterns = {
    SemVer.major: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.major'),
    SemVer.minor: os.path.join(PROJECT_ROOT, 'docs', 'news', '*.feature'),
}
devmode_template = '{version}.dev{count}'


class AutoVersionConfig(object):
    pass
