"""
.. warning::
    DarkThemeColor should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: DarkThemeColor
=================================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`DarkThemeColor.delete`
- :meth:`DarkThemeColor.list`
- :meth:`DarkThemeColor.read`
- :meth:`DarkThemeColor.update`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    dark_theme_colors = pelion_dm_sdk.foundation.dark_theme_color()

How to import DarkThemeColor directly:

.. code-block:: python
    
    from mbed_cloud.foundation import DarkThemeColor

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class DarkThemeColor(Entity):
    """Represents the `DarkThemeColor` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["color", "reference", "updated_at"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, color=None, reference=None, updated_at=None):
        """Creates a local `DarkThemeColor` instance

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
        self._reference = fields.StringField(value=reference, enum=enums.DarkThemeColorReferenceEnum)
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

    def delete(self):
        """Reset branding color to default.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-colors/dark/{reference}>`_.
        
        :rtype: 
        """

        return self._client.call_api(
            method="delete",
            path="/v3/branding-colors/dark/{reference}",
            content_type="application/json",
            path_params={"reference": self._reference.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """Get dark theme branding colors.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-colors/dark>`_.
        
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
        :rtype: mbed_cloud.pagination.PaginatedResponse(DarkThemeColor)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import DarkThemeColor
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=DarkThemeColor._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = DarkThemeColor._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=DarkThemeColor,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """Get dark theme branding colors.
        
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
            method="get", path="/v3/branding-colors/dark", content_type="application/json", unpack=False
        )

    def read(self):
        """Get dark theme branding color.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-colors/dark/{reference}>`_.
        
        :rtype: DarkThemeColor
        """

        return self._client.call_api(
            method="get",
            path="/v3/branding-colors/dark/{reference}",
            content_type="application/json",
            path_params={"reference": self._reference.to_api()},
            unpack=self,
        )

    def update(self):
        """Updates a dark theme branding color.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/branding-colors/dark/{reference}>`_.
        
        :rtype: DarkThemeColor
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
            path="/v3/branding-colors/dark/{reference}",
            content_type="application/json",
            body_params=body_params,
            path_params={"reference": self._reference.to_api()},
            unpack=self,
        )
