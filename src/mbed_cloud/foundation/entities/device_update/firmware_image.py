"""
.. warning::
    FirmwareImage should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: FirmwareImage
================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`FirmwareImage.create`
- :meth:`FirmwareImage.delete`
- :meth:`FirmwareImage.list`
- :meth:`FirmwareImage.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    firmware_images = pelion_dm_sdk.foundation.firmware_image()

How to import FirmwareImage directly:

.. code-block:: python
    
    from mbed_cloud.foundation import FirmwareImage

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


class FirmwareImage(Entity):
    """Represents the `FirmwareImage` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "created_at",
        "datafile_checksum",
        "datafile_size",
        "datafile_url",
        "description",
        "id",
        "name",
        "updated_at",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {"datafile": "datafile_url"}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {"datafile_url": "datafile"}

    def __init__(
        self,
        _client=None,
        created_at=None,
        datafile_checksum=None,
        datafile_size=None,
        datafile_url=None,
        description=None,
        id=None,
        name=None,
        updated_at=None,
    ):
        """Creates a local `FirmwareImage` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param created_at: The time the object was created
        :type created_at: datetime
        :param datafile_checksum: The checksum (sha256) generated for the datafile
        :type datafile_checksum: str
        :param datafile_size: The size of the datafile in bytes
        :type datafile_size: int
        :param datafile_url: The firmware image file URL
        :type datafile_url: str
        :param description: The description of the object
        :type description: str
        :param id: (Required) The firmware image ID
        :type id: str
        :param name: The firmware image name
        :type name: str
        :param updated_at: The time the object was updated
        :type updated_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._created_at = fields.DateTimeField(value=created_at)
        self._datafile_checksum = fields.StringField(value=datafile_checksum)
        self._datafile_size = fields.IntegerField(value=datafile_size)
        self._datafile_url = fields.StringField(value=datafile_url)
        self._description = fields.StringField(value=description)
        self._id = fields.StringField(value=id)
        self._name = fields.StringField(value=name)
        self._updated_at = fields.DateTimeField(value=updated_at)

    @property
    def created_at(self):
        """The time the object was created
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def datafile_checksum(self):
        """The checksum (sha256) generated for the datafile
        
        api example: '0000000000000000000000000000000000000000000000000000000000000000'
        
        :rtype: str
        """

        return self._datafile_checksum.value

    @property
    def datafile_size(self):
        """The size of the datafile in bytes
        
        :rtype: int
        """

        return self._datafile_size.value

    @property
    def datafile_url(self):
        """The firmware image file URL
        
        api example: 'http://example.com/00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._datafile_url.value

    @property
    def description(self):
        """The description of the object
        
        :rtype: str
        """

        return self._description.value

    @description.setter
    def description(self, value):
        """Set value of `description`

        :param value: value to set
        :type value: str
        """

        self._description.set(value)

    @property
    def id(self):
        """The firmware image ID

        This field must be set when updating or deleting an existing FirmwareImage Entity.
        
        api example: '00000000000000000000000000000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        self._id.set(value)

    @property
    def name(self):
        """The firmware image name
        
        :rtype: str
        """

        return self._name.value

    @name.setter
    def name(self, value):
        """Set value of `name`

        :param value: value to set
        :type value: str
        """

        self._name.set(value)

    @property
    def updated_at(self):
        """The time the object was updated
        
        api example: '2017-05-22T12:37:55.576563Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    def create(self, firmware_image_file):
        """Create an image

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/firmware-images/>`_.
        
        :param firmware_image_file: The firmware image file to upload Files can be provided as a file
            object or a path to an existing file on disk.
        :type firmware_image_file: file
        
        :rtype: FirmwareImage
        """

        auto_close_firmware_image_file = False

        # If firmware_image_file is a string rather than a file, treat as a path and attempt to open the file.
        if firmware_image_file and isinstance(firmware_image_file, six.string_types):
            firmware_image_file = open(firmware_image_file, "rb")
            auto_close_firmware_image_file = True

        try:

            return self._client.call_api(
                method="post",
                path="/v3/firmware-images/",
                stream_params={
                    "description": (None, self._description.to_api(), "text/plain"),
                    "datafile": ("firmware_image_file.bin", firmware_image_file, "application/octet-stream"),
                    "name": (None, self._name.to_api(), "text/plain"),
                },
                unpack=self,
            )
        finally:
            # Calling the API may result in an exception being raised so close the files in a finally statement.
            # Note: Files are only closed if they were opened by the method.
            if auto_close_firmware_image_file:
                firmware_image_file.close()

    def delete(self):
        """Delete an image

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/firmware-images/{image_id}/>`_.
        
        :rtype: FirmwareImage
        """

        return self._client.call_api(
            method="delete",
            path="/v3/firmware-images/{image_id}/",
            content_type="application/json",
            path_params={"image_id": self._id.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """List all images

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/firmware-images/>`_.

        **API Filters**

        The following filters are supported by the API when listing FirmwareImage entities:

        +-------------------+------+------+------+------+------+------+------+
        | Field             | eq   | neq  | gte  | lte  | in   | nin  | like |
        +===================+======+======+======+======+======+======+======+
        | created_at        |      |      | Y    | Y    | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+
        | datafile_checksum | Y    | Y    |      |      | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+
        | datafile_size     | Y    | Y    |      |      | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+
        | datafile_url      | Y    | Y    |      |      | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+
        | description       | Y    | Y    |      |      | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+
        | id                | Y    | Y    |      |      | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+
        | name              | Y    | Y    |      |      | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+
        | updated_at        |      |      | Y    | Y    | Y    | Y    |      |
        +-------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import FirmwareImage
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("created_at", "in", <filter value>)
            for firmware_image in FirmwareImage().list(filter=api_filter):
                print(firmware_image.created_at)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: ASC or DESC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type page_size: int
        
        :param include: A comma-separated list of data fields to return. Currently supported:
            total_count
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(FirmwareImage)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import FirmwareImage
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=FirmwareImage._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = FirmwareImage._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=FirmwareImage,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """List all images
        
        :param after: The ID of the the item after which to retrieve the next page
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: ASC or DESC
        :type order: str
        
        :param limit: How many objects to retrieve in the page. The minimum limit is 2 and
            the maximum is 1000. Limit values outside of this range are set to the
            closest limit.
        :type limit: int
        
        :param include: A comma-separated list of data fields to return. Currently supported:
            total_count
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.FirmwareImageOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/firmware-images/",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get an image

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/firmware-images/{image_id}/>`_.
        
        :rtype: FirmwareImage
        """

        return self._client.call_api(
            method="get",
            path="/v3/firmware-images/{image_id}/",
            content_type="application/json",
            path_params={"image_id": self._id.to_api()},
            unpack=self,
        )
