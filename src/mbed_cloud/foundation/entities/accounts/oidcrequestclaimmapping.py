"""
.. warning::
    OIDCRequestClaimMapping should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: OIDCRequestClaimMapping
==========================================

The OIDCRequestClaimMapping entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    oidcrequestclaimmappings = pelion_dm_sdk.foundation.oidcrequestclaimmapping()

How to import OIDCRequestClaimMapping directly:

.. code-block:: python
    
    from mbed_cloud.foundation import OIDCRequestClaimMapping

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class OIDCRequestClaimMapping(Entity):
    """Represents the `OIDCRequestClaimMapping` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "email",
        "email_verified",
        "family_name",
        "given_name",
        "name",
        "phone_number",
        "sub",
        "updated_at",
        "updated_at_pattern",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        email=None,
        email_verified=None,
        family_name=None,
        given_name=None,
        name=None,
        phone_number=None,
        sub=None,
        updated_at=None,
        updated_at_pattern=None,
    ):
        """Creates a local `OIDCRequestClaimMapping` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param email: Custom claim name for 'email'.
        :type email: str
        :param email_verified: Custom claim name for 'email_verified'.
        :type email_verified: str
        :param family_name: Custom claim name for 'family_name'.
        :type family_name: str
        :param given_name: Custom claim name for 'given_name'.
        :type given_name: str
        :param name: Custom claim name for 'name'.
        :type name: str
        :param phone_number: Custom claim name for 'phone_number'.
        :type phone_number: str
        :param sub: Custom claim name for 'sub'.
        :type sub: str
        :param updated_at: Custom claim name for 'updated_at'.
        :type updated_at: str
        :param updated_at_pattern: Custom pattern for claim 'updated_at' as defined by the Java
            SimpleDateFormat class.
        :type updated_at_pattern: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._email = fields.StringField(value=email)
        self._email_verified = fields.StringField(value=email_verified)
        self._family_name = fields.StringField(value=family_name)
        self._given_name = fields.StringField(value=given_name)
        self._name = fields.StringField(value=name)
        self._phone_number = fields.StringField(value=phone_number)
        self._sub = fields.StringField(value=sub)
        self._updated_at = fields.StringField(value=updated_at)
        self._updated_at_pattern = fields.StringField(value=updated_at_pattern)

    @property
    def email(self):
        """Custom claim name for 'email'.
        
        api example: 'email_address'
        
        :rtype: str
        """

        return self._email.value

    @property
    def email_verified(self):
        """Custom claim name for 'email_verified'.
        
        :rtype: str
        """

        return self._email_verified.value

    @property
    def family_name(self):
        """Custom claim name for 'family_name'.
        
        :rtype: str
        """

        return self._family_name.value

    @property
    def given_name(self):
        """Custom claim name for 'given_name'.
        
        :rtype: str
        """

        return self._given_name.value

    @property
    def name(self):
        """Custom claim name for 'name'.
        
        :rtype: str
        """

        return self._name.value

    @property
    def phone_number(self):
        """Custom claim name for 'phone_number'.
        
        :rtype: str
        """

        return self._phone_number.value

    @property
    def sub(self):
        """Custom claim name for 'sub'.
        
        :rtype: str
        """

        return self._sub.value

    @property
    def updated_at(self):
        """Custom claim name for 'updated_at'.
        
        :rtype: str
        """

        return self._updated_at.value

    @property
    def updated_at_pattern(self):
        """Custom pattern for claim 'updated_at' as defined by the Java SimpleDateFormat
        class.
        
        api example: "yyyy-MM-dd'T'HH:mm:ssXXX"
        
        :rtype: str
        """

        return self._updated_at_pattern.value
