"""Tests for entities in the account module."""

from datetime import datetime, date
from tests.common import BaseCase
from mbed_cloud import ApiFilter
from mbed_cloud.foundation import User


class TestApiFilter(BaseCase):
    """Test creation of API filters."""
    
    def test_string_type(self):
        filter_definition = {"name": {"eq": "Badger"}}
        expected_filter = {"name__eq": "Badger"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_integer_type(self):
        filter_definition = {"name": {"neq": -50}}
        expected_filter = {"name__neq": -50}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_float_type(self):
        filter_definition = {"name": {"gte": -1.7}}
        expected_filter = {"name__gte": -1.7}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_boolean_type(self):
        filter_definition = {"name": {"like": True}}
        expected_filter = {"name__like": "true"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_datetime_type(self):
        filter_definition = {"name": {"eq": datetime(2019, 3, 7, 13, 33, 47)}}
        expected_filter = {"name__eq": "2019-03-07T13:33:47Z"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_date_type(self):
        filter_definition = {"name": {"eq": date(2019, 3, 7)}}
        expected_filter = {"name__eq": "2019-03-07"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_list_type(self):
        filter_definition = {"name": {"in": ["Badger", "Gopher"]}}
        expected_filter = {"name__in": "Badger,Gopher"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_dict_type(self):
        filter_definition = {"name": {"nin": {"Animal": "Badger"}}}
        expected_filter = {"name__nin": '{"Animal": "Badger"}'}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_none(self):
        filter_definition = {"name": {"eq": None}}
        expected_filter = {"name__eq": "null"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_entity(self):
        my_user = User(id="my_user_id")
        filter_definition = {"sub_entity": {"eq": my_user}}
        expected_filter = {"sub_entity__eq": "my_user_id"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_missing_operator(self):
        filter_definition = {"name": date(2019, 3, 7)}
        expected_filter = {"name__eq": "2019-03-07"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_rename(self):
        filter_definition = {"SDK_name": {"eq": "Badger"}}
        renames = {"SDK_name": "API_name"}
        expected_filter = {"API_name__eq": "Badger"}

        api_filter = ApiFilter(filter_definition, renames)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_add_filter(self):
        api_filter = ApiFilter()
        self.assertEqual({}, api_filter.to_api())

        api_filter.add_filter("created_at", "gte", datetime(2019, 1, 1))
        expected_filter = {"created_at__gte": "2019-01-01T00:00:00Z"}
        self.assertEqual(expected_filter, api_filter.to_api())

        api_filter.add_filter("created_at", "lte", date(2019, 12, 31))
        expected_filter = {"created_at__gte": "2019-01-01T00:00:00Z", "created_at__lte": "2019-12-31"}
        self.assertEqual(expected_filter, api_filter.to_api())

        api_filter.add_filter("status", "eq", True)
        expected_filter = {
            "created_at__gte": "2019-01-01T00:00:00Z",
            "created_at__lte": "2019-12-31",
            "status__eq": "true"
        }
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_single_list_filter(self):
        filter_definition = {"name": {"in": ["Gopher"]}}
        expected_filter = {"name__in": "Gopher"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_compound_list_filter(self):
        filter_definition = {"name": {"in": ["Badger", 17, 20.5, True, date(2019, 12, 31), datetime(2019, 1, 1), None]}}
        expected_filter = {"name__in": "Badger,17,20.5,true,2019-12-31,2019-01-01T00:00:00Z,null"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_nested_list_filter(self):
        filter_definition = {"name": {"in": ["Badger", [17, 20.5], True, datetime(2019, 1, 1), None]}}
        expected_filter = {"name__in": "Badger,17,20.5,true,2019-01-01T00:00:00Z,null"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_list_of_entities_filter(self):
        user_one = User(id="user1")
        user_two = User(id="user2")
        filter_definition = {"sub_entity": {"in": [user_one, user_two]}}
        expected_filter = {"sub_entity__in": "user1,user2"}

        api_filter = ApiFilter(filter_definition)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_compound_filter(self):
        filter_definition = {
            "created_at": {
                "gte": datetime(2019, 1, 1),
                "lte": date(2019, 12, 31),
            },
            "colour": {"like": "purple"},
            "integer": {"neq": 42},
            "float": {"neq": 13.98},
            "state": {"in": ["OPEN", "CLOSED"]},
            "city": {"nin": ["Cambridge", "London"]},
            "strange": {"eq": {"hello": "world"}},
            "done": False,
            "firmware_checksum": None,
        }
        renames = {
            "colour": "API_colour",
            "state": "API_state",
            "strange": "API_strange",
            "firmware_checksum": "API_fw_csum",
        }
        expected_filter = {
            "created_at__gte": "2019-01-01T00:00:00Z",
            "created_at__lte": "2019-12-31",
            "API_colour__like": "purple",

            "integer__neq": 42,
            "float__neq": 13.98,
            "API_state__in": "OPEN,CLOSED",
            "city__nin": "Cambridge,London",
            "API_strange__eq": '{"hello": "world"}',
            "done__eq": "false",
            "API_fw_csum__eq": "null"}

        api_filter = ApiFilter(filter_definition, renames)
        self.assertEqual(expected_filter, api_filter.to_api())

    def test_legacy_filter(self):
        filter_definition = {
            "created_at": {
                "$gte": datetime(2019, 1, 1),
                "$lte": date(2019, 12, 31),
            },
            "colour": {"$like": "purple"},
            "integer": {"$neq": 42},
            "float": {"$neq": 13.98},
            "state": {"$in": ["OPEN", "CLOSED"]},
            "city": {"$nin": ["Cambridge", "London"]},
            "strange": {"$eq": {"hello": "world"}},
            "done": False,
            "firmware_checksum": None,
        }
        renames = {
            "colour": "API_colour",
            "state": "API_state",
            "strange": "API_strange",
            "firmware_checksum": "API_fw_csum",
        }
        expected_filter = {
            "created_at__gte": "2019-01-01T00:00:00Z",
            "created_at__lte": "2019-12-31",
            "API_colour__like": "purple",

            "integer__neq": 42,
            "float__neq": 13.98,
            "API_state__in": "OPEN,CLOSED",
            "city__nin": "Cambridge,London",
            "API_strange__eq": '{"hello": "world"}',
            "done__eq": "false",
            "API_fw_csum__eq": "null"}

        api_filter = ApiFilter(filter_definition, renames)
        self.assertEqual(expected_filter, api_filter.to_api())
