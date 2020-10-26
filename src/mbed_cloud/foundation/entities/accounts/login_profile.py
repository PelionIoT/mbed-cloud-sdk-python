"""
.. warning::
    LoginProfile should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: LoginProfile
===============================

The LoginProfile entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    login_profiles = pelion_dm_sdk.foundation.login_profile()

How to import LoginProfile directly:

.. code-block:: python
    
    from mbed_cloud.foundation import LoginProfile

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class LoginProfile(Entity):
    """Represents the `LoginProfile` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["foreign_id", "id", "login_profile_type", "name"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {
        "type": "login_profile_type",
    }

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {
        "login_profile_type": "type",
    }

    def __init__(
        self, _client=None, foreign_id=None, id=None, login_profile_type=None, name=None,
    ):
        """Creates a local `LoginProfile` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param foreign_id: The ID of the user in the identity provider's service.
        :type foreign_id: str
        :param id: ID of the identity provider.
        :type id: str
        :param login_profile_type: Identity provider type.
        :type login_profile_type: str
        :param name: Name of the identity provider.
        :type name: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._foreign_id = fields.StringField(value=foreign_id)
        self._id = fields.StringField(value=id)
        self._login_profile_type = fields.StringField(value=login_profile_type, enum=enums.LoginProfileTypeEnum)
        self._name = fields.StringField(value=name)

    @property
    def foreign_id(self):
        """The ID of the user in the identity provider's service.
        
        :rtype: str
        """

        return self._foreign_id.value

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
    def login_profile_type(self):
        """Identity provider type.
        
        :rtype: str
        """

        return self._login_profile_type.value

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
