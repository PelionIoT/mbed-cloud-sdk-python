# Python 2 compatibility
from __future__ import unicode_literals
from builtins import int
from builtins import object
from builtins import str
from builtins import super

from datetime import datetime
from datetime import date

from dateutil.parser import parse

from io import BufferedIOBase

import logging

LOG = logging.getLogger(__name__)


class Field(object):
    base_type = None

    def __init__(self, value, enum=None, entity=None):
        self._val = None
        self._enum = enum
        self._entity = entity
        self.set(value)

    @property
    def value(self):
        return self._val

    def set(self, value):
        if not isinstance(value, (self.base_type, type(None))):
            raise TypeError("%r is not a %s" % (value, self.base_type))
        if value is not None and self._enum and value not in self._enum.values:
            LOG.warning(
                "Unknown enum value '%s' received from API for %s", value, self._enum
            )
        self._val = value
        return self

    def to_literal(self):
        return self.value

    def to_api(self):
        return self.value.to_api() if self.value and self._entity else self.value

    def from_api(self, value):
        return (
            self.set(self._entity().from_api(**value))
            if value and self._entity
            else self.set(value)
        )

    def from_literal(self, value):
        return (
            self.set(self._entity().from_literal(**value))
            if value and self._entity
            else self.set(value)
        )


class DateTimeField(Field):
    base_type = datetime

    def to_literal(self):
        return self.value.isoformat() if self.value else None

    def to_api(self):
        return self.value.isoformat() + "Z" if self.value else None

    def from_api(self, value):
        return self.set(parse(value) if value else value)

    from_literal = from_api


class DateField(DateTimeField):
    base_type = date


class DictField(Field):
    base_type = dict


class IntegerField(Field):
    base_type = int


class FloatField(Field):
    base_type = float


class StringField(Field):
    base_type = str


class BooleanField(Field):
    base_type = bool


class ListField(Field):
    base_type = list

    def to_literal(self):
        if self._entity:
            return [item.to_literal() for item in self._val] if self._val else None
        else:
            return super().to_literal()

    def to_api(self):
        if self._entity:
            return [item.to_api() for item in self._val] if self._val else None
        else:
            return super().to_api()

    def from_api(self, value):
        if self._entity:
            return self.set(
                [self._entity().from_api(**item) for item in value] if value else None
            )
        else:
            return super().from_api(value)

    def from_literal(self, value):
        if self._entity:
            return self.set(
                [self._entity().from_literal(**item) for item in value]
                if value
                else None
            )
        else:
            return super().from_api(value)


class FileField(Field):
    """A file object

    nb. potential to provide some overloaded behaviours here
    e.g. use a stream/file object, otherwise if user provides a string,
    we can either open that as a file if it exists,
    or, finally, treat it as raw data to pass in (StringIO)
    """

    base_type = BufferedIOBase
