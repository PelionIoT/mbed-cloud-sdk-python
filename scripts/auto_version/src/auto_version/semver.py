"""Functions for manipulating SemVer objects (Major.Minor.Patch)"""
import logging
import re

from auto_version.config import AutoVersionConfig as config
from auto_version.config import Constants
from auto_version.definitions import SemVer
from auto_version.definitions import SemVerSigFig

_LOG = logging.getLogger(__file__)

re_semver = re.compile(r"""(?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)(?P<tail>.*)""")


def get_current_semver(data):
    """Given a dictionary of all version data available, determine the current version"""
    # get the not-none values from data
    known = {
        key: data.get(alias)
        for key, alias in config._forward_aliases.items()
        if data.get(alias) is not None
    }

    # prefer the strict field, if available
    potentials = [
        known.pop(Constants.VERSION_STRICT_FIELD, None),
        known.pop(Constants.VERSION_FIELD, None),
    ]

    from_components = [known.get(k) for k in SemVerSigFig._fields if k in known]
    if len(from_components) == 3:
        potentials.append('.'.join(from_components))

    versions = set()
    for potential in potentials:
        if not potential:
            continue
        match = re_semver.match(potential)
        if match:
            parts = match.groupdict()
            parts.pop('tail')
            versions.add(SemVer(**parts))

    if len(versions) > 1:
        raise ValueError('conflicting versions within project: %s' % versions)

    if not versions:
        _LOG.debug('key pairs found: \n%r', known)
        raise ValueError('could not find existing semver')
    return versions.pop()


def make_new_semver(current_semver, all_triggers):
    """Defines how to increment semver based on which significant figure is triggered"""
    new_semver = {}
    bumped = False
    for sig_fig in SemVerSigFig:  # iterate sig figs in order of significance
        value = getattr(current_semver, sig_fig)
        if bumped:
            new_semver[sig_fig] = '0'
        elif sig_fig in all_triggers:
            new_semver[sig_fig] = str(int(value) + 1)
            bumped = True
        else:
            new_semver[sig_fig] = value
    return SemVer(**new_semver)
