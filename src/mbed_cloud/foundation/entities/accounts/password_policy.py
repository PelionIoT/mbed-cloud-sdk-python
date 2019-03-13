"""
Foundation Entity: PasswordPolicy
==============================


.. warning::
    PasswordPolicy should not be imported directly froma this module as the
    organisation may change in the future, please use the top level foundation module to import entities.

How to import PasswordPolicy:

.. code-block:: python
    
    from mbed_cloud.foundation import PasswordPolicy
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class PasswordPolicy(Entity):
    """Represents the `PasswordPolicy` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = ["minimum_length"]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, minimum_length=None):
        """Creates a local `PasswordPolicy` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

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
