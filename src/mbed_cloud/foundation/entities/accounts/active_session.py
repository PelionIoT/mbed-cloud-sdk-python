"""
Foundation Entity: ActiveSession
================================

The ActiveSession entity does not have any methods, reading or updating ActiveSession must be performed via
the encapsulating entity.

.. warning::
    ActiveSession should not be imported directly from this module as the
    organisation may change in the future, please use the top level foundation module to import entities.

How to import ActiveSession:

.. code-block:: python
    
    from mbed_cloud.foundation import ActiveSession
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class ActiveSession(Entity):
    """Represents the `ActiveSession` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "ip_address",
        "login_time",
        "reference_token",
        "user_agent",
    ]

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        ip_address=None,
        login_time=None,
        reference_token=None,
        user_agent=None,
    ):
        """Creates a local `ActiveSession` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: The UUID of the account.
        :type account_id: str
        :param ip_address: IP address of the client.
        :type ip_address: str
        :param login_time: The login time of the user.
        :type login_time: datetime
        :param reference_token: The reference token.
        :type reference_token: str
        :param user_agent: User Agent header from the login request.
        :type user_agent: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._ip_address = fields.StringField(value=ip_address)
        self._login_time = fields.DateTimeField(value=login_time)
        self._reference_token = fields.StringField(value=reference_token)
        self._user_agent = fields.StringField(value=user_agent)

    @property
    def account_id(self):
        """The UUID of the account.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """Set value of `account_id`

        :param value: value to set
        :type value: str
        """

        self._account_id.set(value)

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
    def login_time(self):
        """The login time of the user.
        
        api example: '2018-02-14T17:52:07Z'
        
        :rtype: datetime
        """

        return self._login_time.value

    @login_time.setter
    def login_time(self, value):
        """Set value of `login_time`

        :param value: value to set
        :type value: datetime
        """

        self._login_time.set(value)

    @property
    def reference_token(self):
        """The reference token.
        
        api example: 'rt_CI6+5hS8p9DrCmkRyS6u4doUdiXr71dX7MqD+g0327hYQthEkYTxMMnCwHyf1rDdk'
        
        :rtype: str
        """

        return self._reference_token.value

    @reference_token.setter
    def reference_token(self, value):
        """Set value of `reference_token`

        :param value: value to set
        :type value: str
        """

        self._reference_token.set(value)

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
