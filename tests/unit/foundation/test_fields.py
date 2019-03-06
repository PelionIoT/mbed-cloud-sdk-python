
# Python 2 compatibility
from __future__ import unicode_literals

import datetime

from tests.common import BaseCase

# Units under test
from mbed_cloud.foundation.common import fields


class TZ(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(minutes=-120)


class TestDateTimeField(BaseCase):
    def test_datetime_object(self):
        field = fields.DateTimeField(value=datetime.datetime(2019, 3, 28, 23, 58, 0))
        self.assertEqual(field.to_api(), "2019-03-28T23:58:00Z")
        self.assertEqual(field.to_literal(), "2019-03-28T23:58:00")

    def test_datetime_object_with_tz(self):
        field = fields.DateTimeField(value=datetime.datetime(2019, 3, 28, 23, 58, 0, tzinfo=TZ()))
        self.assertEqual(field.to_api(), "2019-03-28T23:58:00-02:00")
        self.assertEqual(field.to_literal(), "2019-03-28T23:58:00-02:00")

    def test_datetime_string(self):
        field = fields.DateTimeField(value="2019-03-28T23:58:00")
        self.assertEqual(field.to_api(), "2019-03-28T23:58:00Z")
        self.assertEqual(field.to_literal(), "2019-03-28T23:58:00")

    def test_datetime_string_with_tz(self):
        field = fields.DateTimeField(value="2019-03-28T23:58:00Z")
        self.assertEqual(field.to_api(), "2019-03-28T23:58:00+00:00")
        self.assertEqual(field.to_literal(), "2019-03-28T23:58:00+00:00")

    def test_datetime_string_with_offset(self):
        field = fields.DateTimeField(value="2019-03-28T23:58:00-02:00")
        self.assertEqual(field.to_api(), "2019-03-28T23:58:00-02:00")
        self.assertEqual(field.to_literal(), "2019-03-28T23:58:00-02:00")


class TestDateField(BaseCase):

    def test_date_object(self):
        field = fields.DateField(value=datetime.date(2019, 3, 29))
        self.assertEqual(field.to_api(), "2019-03-29")
        self.assertEqual(field.to_literal(), "2019-03-29")

    def test_datetime_string(self):
        field = fields.DateField(value="2019-03-28T23:58:00")
        self.assertEqual(field.to_api(), "2019-03-28")
        self.assertEqual(field.to_literal(), "2019-03-28")

    def test_date_string(self):
        field = fields.DateField(value="2019-03-29")
        self.assertEqual(field.to_api(), "2019-03-29")
        self.assertEqual(field.to_literal(), "2019-03-29")
