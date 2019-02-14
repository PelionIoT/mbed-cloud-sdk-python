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


class PasswordPolicy(Entity):
    """Represents the `PasswordPolicy` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = ["minimum_length"]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(self, _client=None, minimum_length=None):
        """Creates a local `PasswordPolicy` instance

        :param minimum_length: Minimum length for the password. A number between 8 and 512.
        :type minimum_length: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._minimum_length = fields.StringField(value=minimum_length)

    @property
    def minimum_length(self):
        """Minimum length for the password. A number between 8 and 512.
        
        api example: '8'
        
        :rtype: str
        """

        return self._minimum_length.value

    @minimum_length.setter
    def minimum_length(self, value):
        """Set value of `minimum_length`

        :param value: value to set
        :type value: str
        """

        self._minimum_length.set(value)
