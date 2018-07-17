from auto_version.config import AutoVersionConfig as config


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
