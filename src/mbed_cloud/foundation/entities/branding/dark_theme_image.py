"""
.. warning::
    DarkThemeImage should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DarkThemeImage
=================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DarkThemeImage.delete`
- :meth:`DarkThemeImage.list`
- :meth:`DarkThemeImage.read`
- :meth:`DarkThemeImage.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    dark_theme_images = pelion_dm_sdk.foundation.dark_theme_image()

How to import DarkThemeImage directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DarkThemeImage

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


class DarkThemeImage(Entity):
    """Represents the `DarkThemeImage` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["reference", "static_uri", "updated_at"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, reference=None, static_uri=None, updated_at=None):
        """Creates a local `DarkThemeImage` instance

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
        self._reference = fields.StringField(value=reference, enum=enums.DarkThemeImageReferenceEnum)
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

    def delete(self):
        """Revert an image to dark theme default.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-images/dark/{reference}/clear>`_.
        
        :rtype: DarkThemeImage
        """

        return self._client.call_api(
            method="post",
            path="/v3/branding-images/dark/{reference}/clear",
            content_type="application/json",
            path_params={"reference": self._reference.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get metadata of all dark theme images.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-images/dark>`_.
        
        :param filter: Filtering when listing entities is not supported by the API for this
            entity.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, ASC or DESC. Default
            value is ASC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return for each page.
        :type page_size: int
        
        :param include: Comma separated additional data to return.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(DarkThemeImage)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import DarkThemeImage
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=DarkThemeImage._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = DarkThemeImage._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=DarkThemeImage,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get metadata of all dark theme images.
        
        :param after: Not supported by the API.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Not supported by the API.
        :type order: str
        
        :param limit: Not supported by the API.
        :type limit: int
        
        :param include: Not supported by the API.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters

        return self._client.call_api(
            method="get", path="/v3/branding-images/dark", content_type="application/json", unpack=False
        )

    def read(self):
        """Get metadata of a dark theme image.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-images/dark/{reference}>`_.
        
        :rtype: DarkThemeImage
        """

        return self._client.call_api(
            method="get",
            path="/v3/branding-images/dark/{reference}",
            content_type="application/json",
            path_params={"reference": self._reference.to_api()},
            unpack=self,
        )

    def update(self, image):
        """Upload a dark theme image.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-images/dark/{reference}/upload-multipart>`_.
        
        :param image: The image in PNG or JPEG format as multipart form data. Files can be
            provided as a file object or a path to an existing file on disk.
        :type image: file
        
        :rtype: DarkThemeImage
        """

        auto_close_image = False

        # If image is a string rather than a file, treat as a path and attempt to open the file.
        if image and isinstance(image, six.string_types):
            image = open(image, "rb")
            auto_close_image = True

        try:

            return self._client.call_api(
                method="post",
                path="/v3/branding-images/dark/{reference}/upload-multipart",
                stream_params={"image": ("image.png", image, "image/png")},
                path_params={"reference": self._reference.to_api()},
                unpack=self,
            )
        finally:
            # Calling the API may result in an exception being raised so close the files in a finally statement.
            # Note: Files are only closed if they were opened by the method.
            if auto_close_image:
                image.close()
