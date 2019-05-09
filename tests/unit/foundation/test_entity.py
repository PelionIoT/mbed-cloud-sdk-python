
# Python 2 compatibility
from __future__ import unicode_literals

import datetime

from tests.common import BaseCase

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields


class SimpleEntity(Entity):
    """Represents the `User` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "a_simple_field",
        "a_renamed_field",
        "a_datetime_field",
        "a_date_field",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {
        "badly_named_field": "a_renamed_field",
    }

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
            self,
            _client=None,
            a_simple_field=None,
            a_renamed_field=None,
            a_datetime_field=None,
            a_date_field=None,
    ):
        super(SimpleEntity, self).__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._a_simple_field = fields.StringField(value=a_simple_field)
        self._a_renamed_field = fields.StringField(value=a_renamed_field)
        self._a_datetime_field = fields.DateTimeField(value=a_datetime_field)
        self._a_date_field = fields.DateField(value=a_date_field)

    @property
    def a_simple_field(self):
        return self._a_simple_field.value

    @a_simple_field.setter
    def a_simple_field(self, value):
        self._a_simple_field.set(value)

    @property
    def a_renamed_field(self):
        return self._a_renamed_field.value

    @a_renamed_field.setter
    def a_renamed_field(self, value):
        self._a_renamed_field.set(value)

    @property
    def a_datetime_field(self):
        return self._a_datetime_field.value

    @a_datetime_field.setter
    def a_datetime_field(self, value):
        self._a_datetime_field.set(value)

    @property
    def a_date_field(self):
        return self._a_date_field.value

    @a_date_field.setter
    def a_date_field(self, value):
        self._a_date_field.set(value)


class TestEntity(BaseCase):

    def test_to_api(self):
        entity_fields = {
            "a_simple_field": "hello",
            "a_renamed_field": "world",
            "a_datetime_field": datetime.datetime(2019, 3, 28, 23, 58, 0),
            "a_date_field": datetime.date(2019, 3, 29),
        }
        my_entity = SimpleEntity(**entity_fields)
        entity_fields.update({
            "a_datetime_field": "2019-03-28T23:58:00Z",
            "a_date_field": "2019-03-29",
        })
        self.assertEqual(my_entity.to_api(), entity_fields)
