"""
Entity module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class ParentAccount(Entity):
    """Represents the `ParentAccount` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = ["admin_email", "admin_name", "id"]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, admin_email=None, admin_name=None, id=None):
        """Creates a local `ParentAccount` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param admin_email: The email address of the admin user who is the contact person of
            the parent account.
        :type admin_email: str
        :param admin_name: The name of the admin user who is the contact person of the parent
            account.
        :type admin_name: str
        :param id: The ID of the parent account
        :type id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._admin_email = fields.StringField(value=admin_email)
        self._admin_name = fields.StringField(value=admin_name)
        self._id = fields.StringField(value=id)

    @property
    def admin_email(self):
        """The email address of the admin user who is the contact person of the parent
        account.
        
        api example: 'info@arm.com'
        
        :rtype: str
        """

        return self._admin_email.value

    @admin_email.setter
    def admin_email(self, value):
        """Set value of `admin_email`

        :param value: value to set
        :type value: str
        """

        self._admin_email.set(value)

    @property
    def admin_name(self):
        """The name of the admin user who is the contact person of the parent account.
        
        api example: 'J. Doe'
        
        :rtype: str
        """

        return self._admin_name.value

    @admin_name.setter
    def admin_name(self, value):
        """Set value of `admin_name`

        :param value: value to set
        :type value: str
        """

        self._admin_name.set(value)

    @property
    def id(self):
        """The ID of the parent account
        
        api example: '01619571dad80242ac12000600000000'
        
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
