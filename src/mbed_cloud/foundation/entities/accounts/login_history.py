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


class LoginHistory(Entity):
    """Represents the `LoginHistory` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = ["date", "ip_address", "success", "user_agent"]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(
        self, _client=None, date=None, ip_address=None, success=None, user_agent=None
    ):
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

    @date.setter
    def date(self, value):
        """Set value of `date`

        :param value: value to set
        :type value: datetime
        """

        self._date.set(value)

    @property
    def ip_address(self):
        """IP address of the client.
        
        api example: '127.0.0.1'
        
        :rtype: str
        """

        return self._ip_address.value

    @ip_address.setter
    def ip_address(self, value):
        """Set value of `ip_address`

        :param value: value to set
        :type value: str
        """

        self._ip_address.set(value)

    @property
    def success(self):
        """Flag indicating whether login attempt was successful or not.
        
        api example: True
        
        :rtype: bool
        """

        return self._success.value

    @success.setter
    def success(self, value):
        """Set value of `success`

        :param value: value to set
        :type value: bool
        """

        self._success.set(value)

    @property
    def user_agent(self):
        """User Agent header from the login request.
        
        api example: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML,
            like Gecko) Chrome/41.0.2227.1 Safari/537.36'
        
        :rtype: str
        """

        return self._user_agent.value

    @user_agent.setter
    def user_agent(self, value):
        """Set value of `user_agent`

        :param value: value to set
        :type value: str
        """

        self._user_agent.set(value)
