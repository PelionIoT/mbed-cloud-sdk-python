"""
.. warning::
    Policy should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: Policy
=========================

The Policy entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    policys = pelion_dm_sdk.foundation.policy()

How to import Policy directly:

.. code-block:: python
    
    from mbed_cloud.foundation import Policy

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class Policy(Entity):
    """Represents the `Policy` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["action", "allow", "feature", "inherited", "resource"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, action=None, allow=None, feature=None, inherited=None, resource=None):
        """Creates a local `Policy` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param action: Comma-separated list of actions, empty string represents all
            actions.
        :type action: str
        :param allow: True or false controlling whether an action is allowed or not.
        :type allow: bool
        :param feature: Feature name corresponding to this policy.
        :type feature: str
        :param inherited: Flag indicating whether this feature is inherited or overwritten
            specifically.
        :type inherited: bool
        :param resource: Resource that is protected by this policy.
        :type resource: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._action = fields.StringField(value=action)
        self._allow = fields.BooleanField(value=allow)
        self._feature = fields.StringField(value=feature)
        self._inherited = fields.BooleanField(value=inherited)
        self._resource = fields.StringField(value=resource)

    @property
    def action(self):
        """Comma-separated list of actions, empty string represents all actions.
        
        api example: 'GET'
        
        :rtype: str
        """

        return self._action.value

    @property
    def allow(self):
        """True or false controlling whether an action is allowed or not.
        
        api example: True
        
        :rtype: bool
        """

        return self._allow.value

    @property
    def feature(self):
        """Feature name corresponding to this policy.
        
        api example: 'update-campaigns'
        
        :rtype: str
        """

        return self._feature.value

    @property
    def inherited(self):
        """Flag indicating whether this feature is inherited or overwritten specifically.
        
        :rtype: bool
        """

        return self._inherited.value

    @property
    def resource(self):
        """Resource that is protected by this policy.
        
        api example: '/v3/update-campaign'
        
        :rtype: str
        """

        return self._resource.value
