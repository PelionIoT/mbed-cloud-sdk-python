"""Load cli options"""
import argparse
import ast

from auto_version.config import AutoVersionConfig as config
from auto_version.definitions import SemVerSigFig


def get_cli():
    """Load cli options"""
    parser = argparse.ArgumentParser(description='controls version number of releases')
    parser.add_argument(
        '--target',
        action='append',
        default=[],
        help='Files containing version info. '
             'Assumes unique variable names between files. (default: %s).' % (config.targets,),
    )
    parser.add_argument(
        '--bump',
        choices=SemVerSigFig,
        help='Bumps the specified part of SemVer string. '
             'Use this locally to correctly modify the version file.',
    )
    parser.add_argument(
        '--news', '--file-triggers',
        action='store_true',
        dest='file_triggers',
        help='Detects need to bump based on presence of files (as specified in config).',
    )
    parser.add_argument(
        '--set',
        help='Set the SemVer string. Use this locally to set the project version explicitly.',
    )
    parser.add_argument(
        '--lock',
        action='store_true',
        help='Locks the SemVer string. '
             'Lock will remain for another call to autoversion before being cleared.',
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
        print('unpacking %r = %r' % (k, v))
        updates[k.strip()] = ast.literal_eval(v.strip())

    return args, updates
