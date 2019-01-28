from mbed_cloud.sdk.common import fields


class Entity(object):
    _fieldnames = []
    _renames = {}

    def __init__(self, _client, **kwargs):
        """Create a new Entity

        :param client:
        :type client: Client
        :param kwargs:
        """
        if _client is None:
            from mbed_cloud.sdk.common.sdk import get_or_create_global_sdk_instance

            _client = get_or_create_global_sdk_instance().client
        self._client = _client
        self._logger = self._client.config.logger.getChild(self.__class__.__name__)

    def __str__(self):
        """Human readable short format text"""
        friendly = "?"
        for name in (
            getattr(self, f, None)
            for f in ["full_name", "name", "id"] + self._fieldnames
        ):
            if name is not None:
                friendly = name
                break
        return "<%s %s>" % (self.__class__.__name__, friendly)

    def __repr__(self):
        """Long format text (object might be re-instantiatable from this)"""
        return repr(self.to_dict())

    def _repr_pretty_(self, p, cycle):
        """Defining repr_pretty helps control output in IPython:

        https://ipython.readthedocs.io/en/stable/api/generated/IPython.lib.pretty.html
        """
        p.text(str(self))

    def __eq__(self, other):
        """Equality comparison"""
        # TODO: 'primary key' behaviour
        return (
            # very fast - they are the same instance
            (self is other)
            or
            # fast - they are at least the same class
            isinstance(other, self.__class__)
            and (
                # pretty fast - they have the same id [state may be different though ...]
                (
                    getattr(self, "id", None) is not None
                    and getattr(self, "id", None) == getattr(other, "id", None)
                )
                or
                # much slower - deep comparison of dictionaries
                (
                    getattr(self, "id", None) is None
                    and getattr(other, "id", None) is None
                    and self.to_dict() == other.to_dict()
                )
            )
        )

    def to_literal(self):
        """Return all fields from object in a format suitable for serialisation"""
        return {
            field: getattr(self, "_" + field).to_literal() for field in self._fieldnames
        }

    def to_dict(self):
        """Return all fields as key-value pairs"""
        return {field: getattr(self, field) for field in self._fieldnames}

    def to_api(self):
        """Return all fields in API format"""
        return {
            self._renames.get(sdk_field, sdk_field): getattr(self, "_" + sdk_field).to_api()
            for sdk_field in self._fieldnames
        }

    def from_literal(self, **kwargs):
        """Load values into object from pure literals"""
        for field_name, value in kwargs.items():
            field = getattr(self, "_" + field_name, None)
            try:
                field and field.from_literal(value)
            except Exception:
                # we don't care why loading the field fails. maybe it's bad data? log it.
                self._logger.exception(
                    "unable to deserialise literal field: %s %s %s",
                    self,
                    field_name,
                    value,
                )
        return self

    def from_dict(self, *args, **kwargs):
        """Load values into object from a dictionary

        Equivalent to a dictionary update method
        Ignores unknown keys
        """
        for arg in args:
            self.from_dict(**arg)
        for field_name, value in kwargs.items():
            field = getattr(self, "_" + field_name, None)
            if isinstance(field, fields.Field):
                field.set(value)
        return self

    def from_api(self, **kwargs):
        """Load values into object from an API response"""
        for api_field_name, value in kwargs.items():
            field = getattr(
                self, "_" + self._renames.get(api_field_name, api_field_name), None
            )
            try:
                field and field.from_api(value)
            except Exception:  # noqa
                # we don't care why loading the field fails. maybe the API changed? log it.
                self._logger.exception(
                    "unable to deserialise received field: %s %s %r",
                    self,
                    api_field_name,
                    value,
                )
        return self
