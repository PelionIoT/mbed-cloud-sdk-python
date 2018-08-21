from datetime import datetime
from datetime import date

from dateutil.parser import parse


class Field(object):
    base_type = None

    def __init__(self, value, enum=None):
        self._val = None
        self._enum = enum
        self.set(value)

    @property
    def value(self):
        return self._val

    def set(self, value):
        if not isinstance(value, (self.base_type, type(None))):
            raise TypeError("%s is not a %s" % (value, self.base_type))
        if self._enum and value not in self._enum.values:
            raise ValueError("%s must be a value from %s" % (value, self._enum))
        self._val = value
        return self

    def to_json(self):
        return self.value

    def to_api(self):
        return self.value

    def from_api(self, value):
        self.set(value)


class DateTimeField(Field):
    base_type = datetime

    def to_json(self):
        return self.value.isoformat()

    def to_api(self):
        return self.value.isoformat() + "Z"

    def from_api(self, value):
        self.set(parse(value))


class DateField(Field):
    base_type = date


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
