"""
Entity module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class LoginProfile(Entity):
    """Represents the `LoginProfile` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = ["id", "name"]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(self, _client=None, id=None, name=None):
        """Creates a local `LoginProfile` instance

        :param id: ID of the identity provider.
        :type id: str
        :param name: Name of the identity provider.
        :type name: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._id = fields.StringField(value=id)
        self._name = fields.StringField(value=name)

    @property
    def id(self):
        """ID of the identity provider.
        
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
    def name(self):
        """Name of the identity provider.
        
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
