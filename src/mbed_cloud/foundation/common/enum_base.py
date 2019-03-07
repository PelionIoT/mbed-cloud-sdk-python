# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object


class BaseEnum(object):
    values = frozenset()

    def __setattr__(self, name, value):
        raise Exception("enum container values cannot be modified")
