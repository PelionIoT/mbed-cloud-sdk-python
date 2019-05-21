"""
.. warning::
    ParentAccount should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: ParentAccount
================================

The ParentAccount entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    parent_accounts = pelion_dm_sdk.foundation.parent_account()

How to import ParentAccount directly:

.. code-block:: python
    
    from mbed_cloud.foundation import ParentAccount

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class ParentAccount(Entity):
    """Represents the `ParentAccount` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["admin_email", "admin_name", "id"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

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
        :param id: The ID of the parent account.
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

    @property
    def admin_name(self):
        """The name of the admin user who is the contact person of the parent account.
        
        api example: 'J. Doe'
        
        :rtype: str
        """

        return self._admin_name.value

    @property
    def id(self):
        """The ID of the parent account.
        
        api example: '01619571dad80242ac12000600000000'
        
        :rtype: str
        """

        return self._id.value
