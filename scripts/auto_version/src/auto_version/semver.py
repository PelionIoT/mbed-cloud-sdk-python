from auto_version.definitions import SemVer
from auto_version.definitions import SemVerSigFig
from auto_version.config import AutoVersionConfig as config


def get_current_semver(data):
    """Given a dictionary of all version data available, determine the current version"""
    # get the not-none values from data
    known = {key: data.get(alias) for key, alias in config.semver_aliases.items() if data.get(alias) is not None}

    inferred_semver = None
    parts = (known.pop(config.VERSION_FIELD) or '').split('.')[:3]
    if len(parts) == 3:
        inferred_semver = SemVer(*parts)

    explicit_semver = None
    if len(known) == 3:
        explicit_semver = SemVer(**known)

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
