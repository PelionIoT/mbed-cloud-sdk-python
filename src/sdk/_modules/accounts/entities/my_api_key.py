"""
Entity module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class MyApiKey(Entity):
    """Represents the `MyApiKey` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "created_at",
        "creation_time",
        "group_ids",
        "id",
        "key",
        "last_login_time",
        "name",
        "owner",
        "status",
        "updated_at",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {"groups": "group_ids"}

    def __init__(
        self,
        _client=None,
        created_at=None,
        creation_time=None,
        group_ids=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `MyApiKey` instance

        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: The timestamp of the API key creation in the storage, in
            milliseconds.
        :type creation_time: int
        :param group_ids: A list of group IDs this API key belongs to.
        :type group_ids: list
        :param id: The UUID of the API key.
        :type id: str
        :param key: The API key.
        :type key: str
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: int
        :param name: The display name for the API key.
        :type name: str
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: str
        :param status: The status of the API key.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._created_at = fields.DateTimeField(value=created_at)
        self._creation_time = fields.IntegerField(value=creation_time)
        self._group_ids = fields.ListField(value=group_ids)
        self._id = fields.StringField(value=id)
        self._key = fields.StringField(value=key)
        self._last_login_time = fields.IntegerField(value=last_login_time)
        self._name = fields.StringField(value=name)
        self._owner = fields.StringField(value=owner)
        self._status = fields.StringField(value=status, enum=enums.MyApiKeyStatusEnum)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """
        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """Set value of `created_at`

        :param value: value to set
        :type value: datetime
        """
        self._created_at.set(value)

    @property
    def creation_time(self):
        """The timestamp of the API key creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """
        return self._creation_time.value

    @creation_time.setter
    def creation_time(self, value):
        """Set value of `creation_time`

        :param value: value to set
        :type value: int
        """
        self._creation_time.set(value)

    @property
    def group_ids(self):
        """A list of group IDs this API key belongs to.
        
        :rtype: list
        """
        return self._group_ids.value

    @group_ids.setter
    def group_ids(self, value):
        """Set value of `group_ids`

        :param value: value to set
        :type value: list
        """
        self._group_ids.set(value)

    @property
    def id(self):
        """The UUID of the API key.
        
        api example: '01619571f7020242ac12000600000000'
        
        :rtype: str
        """
        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """
        self._id.set(value)

    @property
    def key(self):
        """The API key.
        
        api example: 'ak_1MDE2MTk1NzFmNmU4MDI0MmFjMTIwMDA2MDAwMDAwMDA01619571f7020242ac120006000000
            00'
        
        :rtype: str
        """
        return self._key.value

    @key.setter
    def key(self, value):
        """Set value of `key`

        :param value: value to set
        :type value: str
        """
        self._key.set(value)

    @property
    def last_login_time(self):
        """The timestamp of the latest API key usage, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """
        return self._last_login_time.value

    @last_login_time.setter
    def last_login_time(self, value):
        """Set value of `last_login_time`

        :param value: value to set
        :type value: int
        """
        self._last_login_time.set(value)

    @property
    def name(self):
        """The display name for the API key.
        
        api example: 'API key gorgon'
        
        :rtype: str
        """
        return self._name.value

    @name.setter
    def name(self, value):
        """Set value of `name`

        :param value: value to set
        :type value: str
        """
        self._name.set(value)

    @property
    def owner(self):
        """The owner of this API key, who is the creator by default.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """
        return self._owner.value

    @owner.setter
    def owner(self, value):
        """Set value of `owner`

        :param value: value to set
        :type value: str
        """
        self._owner.set(value)

    @property
    def status(self):
        """The status of the API key.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """
        return self._status.value

    @status.setter
    def status(self, value):
        """Set value of `status`

        :param value: value to set
        :type value: str
        """
        self._status.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """
        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """Set value of `updated_at`

        :param value: value to set
        :type value: datetime
        """
        self._updated_at.set(value)
