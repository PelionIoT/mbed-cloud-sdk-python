"""
.. warning::
    LoginHistory should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: LoginHistory
===============================

The LoginHistory entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    login_historys = pelion_dm_sdk.foundation.login_history()

How to import LoginHistory directly:

.. code-block:: python
    
    from mbed_cloud.foundation import LoginHistory

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class LoginHistory(Entity):
    """Represents the `LoginHistory` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["date", "ip_address", "success", "user_agent"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, date=None, ip_address=None, success=None, user_agent=None):
        """Creates a local `LoginHistory` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param date: UTC time RFC3339 for this login attempt.
        :type date: datetime
        :param ip_address: IP address of the client.
        :type ip_address: str
        :param success: Flag indicating whether login attempt was successful or not.
        :type success: bool
        :param user_agent: User Agent header from the login request.
        :type user_agent: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._date = fields.DateTimeField(value=date)
        self._ip_address = fields.StringField(value=ip_address)
        self._success = fields.BooleanField(value=success)
        self._user_agent = fields.StringField(value=user_agent)

    @property
    def date(self):
        """UTC time RFC3339 for this login attempt.
        
        api example: '2018-02-14T17:52:07Z'
        
        :rtype: datetime
        """

        return self._date.value

    @property
    def ip_address(self):
        """IP address of the client.
        
        api example: '127.0.0.1'
        
        :rtype: str
        """

        return self._ip_address.value

    @property
    def success(self):
        """Flag indicating whether login attempt was successful or not.
        
        api example: True
        
        :rtype: bool
        """

        return self._success.value

    @property
    def user_agent(self):
        """User Agent header from the login request.
        
        api example: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML,
            like Gecko) Chrome/41.0.2227.1 Safari/537.36'
        
        :rtype: str
        """

        return self._user_agent.value
