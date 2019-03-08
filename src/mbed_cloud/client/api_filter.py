"""API Filter Builder

The API allows the user to filter when retrieving a list of resource via query parameters. The ApiFilter class builds
the query parameters from a simple dictionary definition.
"""

from mbed_cloud.foundation.common import fields


# A list of Foundation Interface field types that could be filter values
_valid_value_types = [
    fields.StringField,
    # Must check for bool before int as `isinstance(True, int)` evaluates to true
    fields.BooleanField,
    fields.IntegerField,
    fields.FloatField,
    fields.DateTimeField,
    fields.DateField,
    fields.ListField,
    fields.DictField,
]


def _to_query_param(sdk_value):
    """Convert a standard Python value to a value suitable for a query parameter value.

    Note: This will not URL encode as this will be performed by the `requests` library

    :param sdk_value: filter value
    :return Value suitable for the query string
    """
    for value_type in _valid_value_types:
        if isinstance(sdk_value, value_type.base_type):
            return value_type(sdk_value).to_query_param()
    # Default to a string field - this will happen for None values
    return fields.StringField(sdk_value).to_query_param()


class ApiFilter(object):
    """Filter Builder for listing resource from the API."""

    def __init__(self, filter_definition=None, field_renames=None):
        """Create an instance of an API filter.

        The recommended usage is to use the `add_filter` method to create API filters:

        .. code-block:: python

            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("created_at", "gte", datetime(2019, 1, 1))
            api_filter.add_filter("created_at", "lte", datetime(2019, 12, 31))

        Alternatively a filter can be defined by providing a filter definition as a dict when the class is instantiated:

       .. code-block:: python

            from mbed_cloud import ApiFilter

            my_filter = {
                "created_at": {
                    "gte": datetime(2019, 1, 1),
                    "lte": datetime(2019, 12, 31)
                }
            }
            api_filter = ApiFilter(filter_definition=my_filter)

        *Note: Filters are not supported by the API for all entities and fields, please see the entity for details.*

        :param filter_definition: A optional definition of the fields on which to filter along with the operators and
            values. `{<Field Name>: {"<Filter Operator>": "<Compassion Value>"}`
        :type filter_definition: dict
        :param field_renames: An optional definition of renames performed in the Foundation Interface (not required if
            using with the Client interface. `{<SDK Name>: <API Name>}`
        :type field_renames: dict
        """
        self.filter_definition = filter_definition if filter_definition else {}
        self.field_renames = field_renames if field_renames else {}

    def add_filter(self, field, operator, value):
        """Add a new API filter.

        *Note: Filters are not supported by the API for all entities and fields, please see the entity for details.*

        :param field: Name of the field on which to filter
        :type field: str
        :param operator: The filter operator, one of `eq`, `neq`, `lte`, `gte`, `in`, `nin` and `like`.
        :type operator: str
        :param value: The comparison value e.g. `True`, `7`, `"hello world"`, `["open", "closed"]`
        """
        self.filter_definition.setdefault(field, {}).update({operator: value})

    def to_api(self):
        """Generate filters suitable to being sent to the API as a filter.

        This method will only need to be called explicitly when the Client Interface is being used.
        """
        api_filter = {}

        for sdk_field, sdk_operator_value in self.filter_definition.items():
            # If a rename dictionary has been provided then rename the field, otherwise leave as it is
            api_field = self.field_renames.get(sdk_field, sdk_field)
            try:
                # The filter definition should contain a dictionary if filter operators and values
                for sdk_operator, sdk_value in sdk_operator_value.items():
                    # The dictionary may contain multiple filters, process each one
                    api_value = _to_query_param(sdk_value)
                    api_filter[api_field + "__" + sdk_operator] = api_value
            except AttributeError:
                # Default to equality if a filter operator was not provided
                api_value = _to_query_param(sdk_operator_value)
                api_filter[api_field + "__eq"] = api_value

        return api_filter
