"""Regex substitution handler"""
from auto_version.config import Constants


class ReplacementHandler(object):
    """Tool used by regex when performing substitutions

    We store state so that we consume our parameters as we make each replacement
    """

    def __init__(self, **params):
        """New handler instance

        :param params: mapping of <key to match> <value to replace with>
        """
        self.params = params
        self.missing = set(params.keys())

    def __call__(self, match):
        """Given a regex Match Object, return the entire replacement string"""
        original = match.string.strip('\r\n')
        key = match.group(Constants.KEY_GROUP)
        replacement = self.params.get(key)
        if replacement is None:  # if this isn't a key we are interested in replacing
            replaced = original
        else:
            start, end = match.span(Constants.VALUE_GROUP)
            if start < 0:
                start = end = len(original)
            self.missing.remove(key)
            replaced = ''.join([
                original[:start],
                str(replacement),
                original[end:],
            ])
        return replaced
