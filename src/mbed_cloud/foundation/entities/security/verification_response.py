"""
.. warning::
    VerificationResponse should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: VerificationResponse
=======================================

The VerificationResponse entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    verification_responses = pelion_dm_sdk.foundation.verification_response()

How to import VerificationResponse directly:

.. code-block:: python
    
    from mbed_cloud.foundation import VerificationResponse

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class VerificationResponse(Entity):
    """Represents the `VerificationResponse` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["message", "successful"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, message=None, successful=None):
        """Creates a local `VerificationResponse` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param message: Provides details in case of failure.
        :type message: str
        :param successful: Indicates whether the certificate issuer was verified
            successfully.
        :type successful: bool
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._message = fields.StringField(value=message)
        self._successful = fields.BooleanField(value=successful)

    @property
    def message(self):
        """Provides details in case of failure.
        
        api example: 'message describing the verification failure'
        
        :rtype: str
        """

        return self._message.value

    @property
    def successful(self):
        """Indicates whether the certificate issuer was verified successfully.
        
        :rtype: bool
        """

        return self._successful.value
