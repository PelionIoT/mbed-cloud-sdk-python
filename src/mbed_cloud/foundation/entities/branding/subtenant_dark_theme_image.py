"""
.. warning::
    SubtenantDarkThemeImage should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: SubtenantDarkThemeImage
==========================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`SubtenantDarkThemeImage.delete`
- :meth:`SubtenantDarkThemeImage.read`
- :meth:`SubtenantDarkThemeImage.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    subtenant_dark_theme_images = pelion_dm_sdk.foundation.subtenant_dark_theme_image()

How to import SubtenantDarkThemeImage directly:

.. code-block:: python
    
    from mbed_cloud.foundation import SubtenantDarkThemeImage

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super
import six

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class SubtenantDarkThemeImage(Entity):
    """Represents the `SubtenantDarkThemeImage` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["reference", "static_uri", "updated_at"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, reference=None, static_uri=None, updated_at=None):
        """Creates a local `SubtenantDarkThemeImage` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param reference: Name of the image.
        :type reference: str
        :param static_uri: The static link to the image.
        :type static_uri: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._reference = fields.StringField(value=reference, enum=enums.SubtenantDarkThemeImageReferenceEnum)
        self._static_uri = fields.StringField(value=static_uri)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def reference(self):
        """Name of the image.
        
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
    def static_uri(self):
        """The static link to the image.
        
        api example: 'https://static.mbed.com/123456789.jpg'
        
        :rtype: str
        """

        return self._static_uri.value

    @property
    def updated_at(self):
        """Last update time in UTC.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def delete(self, account_id):
        """Revert an image to dark theme default.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/branding-images/dark/{reference}/clear>`_.
        
        :param account_id: Account ID.
        :type account_id: str
        
        :rtype: SubtenantDarkThemeImage
        """

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account_id}/branding-images/dark/{reference}/clear",
            content_type="application/json",
            path_params={"account_id": fields.StringField(account_id).to_api(), "reference": self._reference.to_api()},
            unpack=self,
        )

    def read(self, account_id):
        """Get metadata of a dark theme image.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/branding-images/dark/{reference}>`_.
        
        :param account_id: Account ID.
        :type account_id: str
        
        :rtype: SubtenantDarkThemeImage
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/branding-images/dark/{reference}",
            content_type="application/json",
            path_params={"account_id": fields.StringField(account_id).to_api(), "reference": self._reference.to_api()},
            unpack=self,
        )

    def update(self, account_id, image):
        """Upload a dark theme image.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/branding-images/dark/{reference}/upload-multipart>`_.
        
        :param account_id: Account ID.
        :type account_id: str
        
        :param image: The image in PNG or JPEG format as multipart form data. Files can be
            provided as a file object or a path to an existing file on disk.
        :type image: file
        
        :rtype: SubtenantDarkThemeImage
        """

        auto_close_image = False

        # If image is a string rather than a file, treat as a path and attempt to open the file.
        if image and isinstance(image, six.string_types):
            image = open(image, "rb")
            auto_close_image = True

        try:

            return self._client.call_api(
                method="post",
                path="/v3/accounts/{account_id}/branding-images/dark/{reference}/upload-multipart",
                path_params={
                    "account_id": fields.StringField(account_id).to_api(),
                    "reference": self._reference.to_api(),
                },
                stream_params={"image": ("image.png", image, "image/png")},
                unpack=self,
            )
        finally:
            # Calling the API may result in an exception being raised so close the files in a finally statement.
            # Note: Files are only closed if they were opened by the method.
            if auto_close_image:
                image.close()
