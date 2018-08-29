from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk.common.sdk import get_or_create_global_sdk_instance


class Entity(object):
    _fieldnames = []
    _renames = {}

    def __init__(self, client, **kwargs):
        """Create a new Entity

        :param client:
        :type client: Client
        :param kwargs:
        """
        if client is None:
            client = get_or_create_global_sdk_instance().client
        self._client = client

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
        """Possibly instantiatable long format text"""
        return repr({field: getattr(self, field) for field in self._fieldnames})

    def to_literal(self):
        """Return all fields from object in a format suitable for serialisation"""
        return {
            field: getattr(self, "_" + field).to_literal() for field in self._fieldnames
        }

    def _from_api(self, **kwargs):
        """Load values into object from an API response"""
        for k, v in kwargs.items():
            field = getattr(self, "_" + self._renames.get(k, k), None)
            if field:
                if isinstance(field, fields.Field):
                    field.from_api(v)
                else:
                    print(repr(field))
                    print(v)
        return self
