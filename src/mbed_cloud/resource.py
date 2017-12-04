class Resource(object):
    """Describes resource type from device.

    Example usage:

    .. code-block:: python

        >>> resources = api.list_resources(device_id)
        >>> for r in resources:
                print(r.uri, r.name, r.observable)
        /3/0/1,None,True
        /5/0/2,Update,False
        ...
    """

    def __init__(self, resource_obj):
        """Override __init__ and allow passing in backend object."""
        self._observable = resource_obj.obs
        self._path = resource_obj.uri
        self._type = resource_obj.rt
        self._content_type = resource_obj.type

    @property
    def observable(self):
        """Get the observability of this Resource.

        Whether the resource is observable or not (true/false)

        :return: The observability of this ResourcesData.
        :rtype: bool
        """
        return self._observable

    @property
    def path(self):
        """Get the URI of this Resource.

        :return: The URI of this Resource.
        :rtype: str
        """
        return self._path

    @property
    def type(self):
        """Get the type of this Resource, if set.

        :return: The type of the Resource.
        :rtype: str
        """
        return self._type

    @property
    def content_type(self):
        """The content type of this Resource, if set.

        :return: The content type of the Resource.
        :rtype: str
        """
        return self._content_type

    def to_dict(self):
        """Return dictionary of object."""
        return {
            'observable': self.observable,
            'path': self.path,
            'type': self.type,
            'content_type': self.content_type
        }

    def __repr__(self):
        """For print and pprint."""
        return str(self.to_dict())