from datetime import datetime
from datetime import date

from dateutil.parser import parse


class Field(object):
    base_type = None

    def __init__(self, value):
        self._val = None
        self.set(value)

    @property
    def value(self):
        return self._val

    def set(self, value):
        if not isinstance(value, (self.base_type, type(None))):
            raise TypeError("%s is not a %s" % (value, self.base_type))
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
