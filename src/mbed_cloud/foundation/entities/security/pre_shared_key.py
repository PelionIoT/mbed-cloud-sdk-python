"""
.. warning::
    PreSharedKey should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: PreSharedKey
===============================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`PreSharedKey.create`
- :meth:`PreSharedKey.delete`
- :meth:`PreSharedKey.list`
- :meth:`PreSharedKey.read`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    pre_shared_keys = pelion_dm_sdk.foundation.pre_shared_key()

How to import PreSharedKey directly:

.. code-block:: python
    
    from mbed_cloud.foundation import PreSharedKey

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class PreSharedKey(Entity):
    """Represents the `PreSharedKey` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = ["created_at", "endpoint_name", "id"]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(self, _client=None, created_at=None, endpoint_name=None, id=None):
        """Creates a local `PreSharedKey` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param created_at: The date-time (RFC3339) when this PSK was uploaded to Device
            Management.
        :type created_at: datetime
        :param endpoint_name: The unique endpoint identifier that this PSK applies to. 16-64 [pr
            intable](https://en.wikipedia.org/wiki/ASCII#Printable_characters)
            (non-control) ASCII characters.
        :type endpoint_name: str
        :param id: The Id of the pre_shared_key, shadows the endpoint_name
        :type id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._created_at = fields.DateTimeField(value=created_at)
        self._endpoint_name = fields.StringField(value=endpoint_name)
        self._id = fields.StringField(value=id)

    @property
    def created_at(self):
        """The date-time (RFC3339) when this PSK was uploaded to Device Management.
        
        api example: '2017-07-21T17:32:28.012Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def endpoint_name(self):
        """The unique endpoint identifier that this PSK applies to. 16-64
        [printable](https://en.wikipedia.org/wiki/ASCII#Printable_characters) (non-
        control) ASCII characters.
        
        api example: 'my-endpoint-0001'
        
        :rtype: str
        """

        from mbed_cloud.foundation._custom_methods import pre_shared_key_id_getter

        return pre_shared_key_id_getter(self=self)

    @endpoint_name.setter
    def endpoint_name(self, value):
        """Set value of `endpoint_name`

        :param value: value to set
        :type value: str
        """

        from mbed_cloud.foundation._custom_methods import pre_shared_key_id_setter

        pre_shared_key_id_setter(self=self, value=value)

    @property
    def id(self):
        """The Id of the pre_shared_key, shadows the endpoint_name
        
        :rtype: str
        """

        from mbed_cloud.foundation._custom_methods import pre_shared_key_id_getter

        return pre_shared_key_id_getter(self=self)

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        from mbed_cloud.foundation._custom_methods import pre_shared_key_id_setter

        pre_shared_key_id_setter(self=self, value=value)

    def create(self, secret_hex):
        """Upload a PSK to Pelion Device Management.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v2/device-shared-keys>`_.
        
        :param secret_hex: The secret of the PSK in hexadecimal. It is not case sensitive; 4a is
            same as 4A, and it is allowed with or without 0x in the beginning. The
            minimum length of the secret is 128 bits and maximum 256 bits.
        :type secret_hex: str
        
        :rtype: PreSharedKey
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._id.value_set:
            body_params["endpoint_name"] = self._id.to_api()
        # Method parameters are unconditionally sent even if set to None
        body_params["secret_hex"] = fields.StringField(secret_hex).to_api()

        return self._client.call_api(
            method="post",
            path="/v2/device-shared-keys",
            content_type="application/json",
            body_params=body_params,
            unpack=self,
        )

    def delete(self):
        """Remove a PSK.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v2/device-shared-keys/{endpoint_name}>`_.
        
        :rtype: PreSharedKey
        """

        return self._client.call_api(
            method="delete",
            path="/v2/device-shared-keys/{endpoint_name}",
            content_type="application/json",
            path_params={"endpoint_name": self._id.to_api()},
            unpack=self,
        )

    def list(self, filter=None, order=None, max_results=None, page_size=None, include=None):
        """List PSKs.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v2/device-shared-keys>`_.
        
        :param filter: Filtering when listing entities is not supported by the API for this
            entity.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: The order of the records based on creation time, ASC or DESC. Default
            value is ASC
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of entries per page.
        :type page_size: int
        
        :param include: Comma separated additional data to return.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(PreSharedKey)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import PreSharedKey
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=PreSharedKey._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = PreSharedKey._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=PreSharedKey,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, filter=None, order=None, limit=None, include=None):
        """List PSKs.
        
        :param after: An offset token for fetching a specific page. Provided by the server.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Not supported by the API.
        :type order: str
        
        :param limit: The number of entries per page.
        :type limit: int
        
        :param include: Not supported by the API.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v2/device-shared-keys",
            content_type="application/json",
            query_params=query_params,
            unpack=False,
        )

    def read(self):
        """Get a PSK.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v2/device-shared-keys/{endpoint_name}>`_.
        
        :rtype: PreSharedKey
        """

        return self._client.call_api(
            method="get",
            path="/v2/device-shared-keys/{endpoint_name}",
            content_type="application/json",
            path_params={"endpoint_name": self._id.to_api()},
            unpack=self,
        )
