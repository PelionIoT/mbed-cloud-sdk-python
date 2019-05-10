# Python 2 compatibility
from __future__ import unicode_literals
from builtins import int
from builtins import object
from builtins import super

from datetime import datetime
from datetime import date
from dateutil.parser import parse
from io import BufferedIOBase
import json
import six
import pytz

import logging

LOG = logging.getLogger(__name__)


class Field(object):
    base_type = None

    def __init__(self, value, enum=None, entity=None):
        self._val = None
        self._enum = enum
        self._entity = entity
        self.value_set = False

        # Work out the valid valid types that the set method can use
        if self._entity:
            self._valid_types = (self.base_type, self._entity, type(None))
        else:
            self._valid_types = (self.base_type, type(None))

        self.set(value)

        # If the initial value provided was not None and was accepted then flag that the value has been set.
        if self._val is None:
            self.value_set = False

    @property
    def value(self):
        return self._val

    def set(self, value):
        if not isinstance(value, self._valid_types):
            raise TypeError("%r is not one of the valid types %s" % (value, self._valid_types))
        if value is not None and self._enum and value not in self._enum.values:
            LOG.warning("Unknown enum value '%s' received from API for %s", value, self._enum)
        self._val = value
        self.value_set = True
        return self

    def to_literal(self):
        return self.value

    def to_api(self):
        return self.value.to_api() if self.value and self._entity else self.value

    def from_api(self, value):
        if value and self._entity:
            new_entity = self._entity().from_api(**value)
            return self.set(new_entity)
        else:
            return self.set(value)

    def from_literal(self, value):
        return self.set(self._entity().from_literal(**value)) if value and self._entity else self.set(value)

    def to_query_param(self):
        """Generate a format which is appropriate to representing a a query param

        Note: This will not URL encode as this will be performed by the `requests` library
        """
        return json.dumps(self.value) if self.value is None else self.to_api()


class DateTimeField(Field):
    base_type = datetime

    def set(self, value):
        """Set the date/time using a datetime object or a date/time like string."""
        if isinstance(value, six.string_types):
            # Use dateutil.parser to accept various input
            self._val = parse(value)
            self.value_set = True
        else:
            return super().set(value)
        return self

    def to_literal(self):
        return self.value.isoformat() if self.value else None

    def to_api(self):
        if self.value:
            if self.value.tzinfo:
                # Convert to UTC timezone and clear the timezone so isoformat renders with offset
                naive_datetime = self.value.astimezone(pytz.utc).replace(tzinfo=None)
            else:
                naive_datetime = self.value
            # Render date, manually appending `Z` UTC indicator
            return naive_datetime.isoformat() + "Z"
        else:
            return None

    def from_api(self, value):
        return self.set(value)

    from_literal = from_api


class DateField(DateTimeField):
    base_type = date

    def to_api(self):
        # ISO dates do not have a trailing Z
        return self.value.isoformat() if self.value else None

    def set(self, value):
        """Set the date using a date object or a date/time like string."""
        super().set(value)
        # Use dateutil.parser to accept various input if a string is passed in but then convert to a date object
        if isinstance(self._val, datetime):
            self._val = self._val.date()
            self.value_set = True
        return self


class DictField(Field):
    base_type = dict

    def to_query_param(self):
        """Generate a format which is appropriate to representing a a query param

        Note: This will not URL encode as this will be performed by the `requests` library
        """
        return json.dumps(self.value)

    def set(self, value):
        """Handle entities being provided as dictionaries."""
        # If this is an entity field, the type is valid then handle being given a value which is not an entity
        if self._entity and isinstance(value, self._valid_types) and not isinstance(value, self._entity):
            # Pass the dict to the entity as kwargs for create a blank entity if the value is None
            new_entity = self._entity(**value) if value else self._entity()
            return super().set(new_entity)
        # Revert to default behaviour if not handling an entity
        return super().set(value)


class IntegerField(Field):
    base_type = int

    def set(self, value):
        """Attempt to convert to an integer if not already."""
        try:
            int_value = int(value)
        except TypeError:
            int_value = value
        return super().set(int_value)


class FloatField(Field):
    base_type = float

    def set(self, value):
        """Attempt to convert to a float if not already."""
        try:
            float_value = float(value)
        except TypeError:
            float_value = value
        return super().set(float_value)


class StringField(Field):
    # Python 2 and 3 compatible string type
    base_type = six.string_types


class BinaryField(Field):
    # Python 2 and 3 compatible binary type
    base_type = six.binary_type


class BooleanField(Field):
    base_type = bool

    def to_query_param(self):
        """Generate a format which is appropriate to representing a a query param

        Note: This will not URL encode as this will be performed by the `requests` library
        """
        return json.dumps(self.value)


class ListField(Field):
    base_type = list

    def set(self, value):
        if isinstance(value, list) and self._entity:
            # Convert a list of dictionaries into a list of entities
            self._val = [self._entity(**item) if isinstance(item, dict) else item for item in value]
            self.value_set = True
        else:
            return super().set(value)
        return self

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
            return self.set([self._entity().from_api(**item) for item in value] if value else None)
        else:
            return super().from_api(value)

    def from_literal(self, value):
        if self._entity:
            return self.set([self._entity().from_literal(**item) for item in value] if value else None)
        else:
            return super().from_api(value)

    def to_query_param(self):
        """Generate a format which is appropriate to representing a a query param

        Note: This will not URL encode as this will be performed by the `requests` library
        """
        return ",".join(self.value)


class FileField(Field):
    """A file object

    nb. potential to provide some overloaded behaviours here
    e.g. use a stream/file object, otherwise if user provides a string,
    we can either open that as a file if it exists,
    or, finally, treat it as raw data to pass in (StringIO)
    """

    base_type = BufferedIOBase
