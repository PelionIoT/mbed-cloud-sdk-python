"""
.. warning::
    SubtenantDarkThemeColor should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SubtenantDarkThemeColor
==========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`SubtenantDarkThemeColor.delete`
- :meth:`SubtenantDarkThemeColor.read`
- :meth:`SubtenantDarkThemeColor.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    subtenant_dark_theme_colors = pelion_dm_sdk.foundation.subtenant_dark_theme_color()

How to import SubtenantDarkThemeColor directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SubtenantDarkThemeColor

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SubtenantDarkThemeColor(Entity):
    """Represents the `SubtenantDarkThemeColor` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["color", "reference", "updated_at"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, color=None, reference=None, updated_at=None):
        """Creates a local `SubtenantDarkThemeColor` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param color: The color given as name (purple) or as a hex code.
        :type color: str
        :param reference: Color name.
        :type reference: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._color = fields.StringField(value=color)
        self._reference = fields.StringField(value=reference, enum=enums.SubtenantDarkThemeColorReferenceEnum)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def color(self):
        """The color given as name (purple) or as a hex code.
        
        api example: '#f3f93e'
        
        :rtype: str
        """

        return self._color.value

    @color.setter
    def color(self, value):
        """Set value of `color`

        :param value: value to set
        :type value: str
        """

        self._color.set(value)

    @property
    def reference(self):
        """Color name.
        
        :rtype: str
        """

        return self._reference.value

    @reference.setter
    def reference(self, value):
        """Set value of `reference`

        :param value: value to set
        :type value: str
        """

        self._reference.set(value)

    @property
    def updated_at(self):
        """Last update time in UTC.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def delete(self, account_id):
        """Reset branding color to default.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/branding-colors/dark/{reference}>`_.
        
        :param account_id: Account ID.
        :type account_id: str
        
        :rtype: 
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account_id}/branding-colors/dark/{reference}",
            content_type="application/json",
            path_params={"account_id": fields.StringField(account_id).to_api(), "reference": self._reference.to_api()},
            unpack=self,
        )

    def read(self, account_id):
        """Get dark theme branding color.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/branding-colors/dark/{reference}>`_.
        
        :param account_id: Account ID.
        :type account_id: str
        
        :rtype: SubtenantDarkThemeColor
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/branding-colors/dark/{reference}",
            content_type="application/json",
            path_params={"account_id": fields.StringField(account_id).to_api(), "reference": self._reference.to_api()},
            unpack=self,
        )

    def update(self, account_id):
        """Updates a dark theme branding color.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/branding-colors/dark/{reference}>`_.
        
        :param account_id: Account ID.
        :type account_id: str
        
        :rtype: SubtenantDarkThemeColor
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._color.value_set:
            body_params["color"] = self._color.to_api()
        if self._updated_at.value_set:
            body_params["updated_at"] = self._updated_at.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/accounts/{account_id}/branding-colors/dark/{reference}",
            content_type="application/json",
            path_params={"account_id": fields.StringField(account_id).to_api(), "reference": self._reference.to_api()},
            body_params=body_params,
            unpack=self,
        )
