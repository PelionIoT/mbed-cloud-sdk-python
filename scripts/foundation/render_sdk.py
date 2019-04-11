#!/usr/bin/env python3
"""Generate Foundation SDK code from the SDK Foundation Definition file."""

import sys
import argparse
import os
import shutil
import yaml
import logging
import copy
import functools
import subprocess
import re
from collections import defaultdict
import jinja2

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

SUPPORTED_FILTER_OPERATORS = ["eq", "neq", "gte", "lte", "in", "nin", "like"]

# The required parameters for a paginator
PRIVATE_PAGINATOR_PARAMETERS = {
    "after": {
        '_key': 'after',
        'api_fieldname': 'after',
        'description': 'Not supported by the API.',
        'entity_fieldname': 'after',
        'external_param': True,
        'in': 'query',
        'name': 'after',
        'parameter_fieldname': 'after',
        'required': False,
        'type': 'string',
        'python_type': 'str',
        'python_field': 'StringField',
        'default': None
    },
    "include": {
        '_key': 'include',
        'api_fieldname': 'include',
        'description': 'Not supported by the API.',
        'entity_fieldname': 'include',
        'external_param': True,
        'in': 'query',
        'name': 'include',
        'parameter_fieldname': 'include',
        'required': False,
        'type': 'string',
        'python_type': 'str',
        'python_field': 'StringField',
        'default': None
    },
    "limit": {
        '_key': 'limit',
        'api_fieldname': 'limit',
        'default': None,
        'description': 'Not supported by the API.',
        'entity_fieldname': 'limit',
        'external_param': True,
        'format': 'int32',
        'in': 'query',
        'name': 'limit',
        'parameter_fieldname': 'limit',
        'required': False,
        'type': 'integer',
        'python_type': 'int',
        'python_field': 'IntegerField'
    },
    "order": {
        '_key': 'order',
        'api_fieldname': 'order',
        'default': None,
        'description': 'Not supported by the API.',
        'entity_fieldname': 'order',
        'external_param': True,
        'in': 'query',
        'name': 'order',
        'parameter_fieldname': 'order',
        'required': False,
        'type': 'string',
        'python_type': 'str',
        'python_field': 'StringField'
    },
    "filter": {
        '_key': 'filter',
        'api_fieldname': 'filter',
        'default': None,
        'description': 'Optional API filter for listing resources.',
        'entity_fieldname': 'filter',
        'external_param': True,
        'in': 'special_query',
        'name': 'filter',
        'parameter_fieldname': 'filter',
        'required': False,
        'type': 'mbed_cloud.client.api_filter.ApiFilter',
        'python_type': 'mbed_cloud.client.api_filter.ApiFilter',
        'python_field': 'mbed_cloud.client.api_filter.ApiFilter'
    },
}

PUBLIC_PAGINATOR_PARAMETERS = {
    'filter': {
        '_key': 'filter',
        'api_fieldname': 'filter',
        'default': None,
        'description': 'Filtering when listing entities is not supported by the API for this entity.',
        'entity_fieldname': 'filter',
        'external_param': True,
        'in': 'query',
        'name': 'after',
        'parameter_fieldname': 'filter',
        'python_field': 'mbed_cloud.client.api_filter.ApiFilter',
        'python_type': 'mbed_cloud.client.api_filter.ApiFilter',
        'required': False,
        'type': 'mbed_cloud.client.api_filter.ApiFilter',
        '_sort_order': "e",
    },
    'include': {
        '_key': 'include',
        'api_fieldname': 'include',
        'default': None,
        'description': 'Comma separated additional data to return.',
        'entity_fieldname': 'include',
        'external_param': True,
        'in': 'query',
        'name': 'include',
        'parameter_fieldname': 'include',
        'python_field': 'StringField',
        'python_type': 'str',
        'required': False,
        'type': 'string',
        '_sort_order': "a",
    },
    'page_size': {
        '_key': 'page_size',
        'api_fieldname': 'page_size',
        'default': None,
        'description': 'The number of results to return for each page.',
        'entity_fieldname': 'page_size',
        'external_param': True,
        'format': 'int32',
        'in': 'query',
        'name': 'page_size',
        'parameter_fieldname': 'page_size',
        'python_field': 'IntegerField',
        'python_type': 'int',
        'required': False,
        'type': 'integer',
        '_sort_order': "c",
    },
    'order': {
        '_key': 'order',
        'api_fieldname': 'order',
        'default': None,
        'description': 'The order of the records based on creation time, ASC or DESC. Default value is ASC',
        'entity_fieldname': 'order',
        'enum': ['ASC', 'DESC'],
        'external_param': True,
        'in': 'query',
        'name': 'order',
        'parameter_fieldname': 'order',
        'python_field': 'StringField',
        'python_type': 'str',
        'required': False,
        'type': 'string',
        '_sort_order': "d",
    },
    'max_results': {
        '_key': 'max_results',
        'api_fieldname': 'max_results',
        'default': None,
        'description': 'Total maximum number of results to retrieve',
        'entity_fieldname': 'max_results',
        'external_param': True,
        'format': 'int32',
        'in': 'query',
        'name': 'max_results',
        'parameter_fieldname': 'max_results',
        'python_field': 'IntegerField',
        'python_type': 'int',
        'required': False,
        'type': 'integer',
        '_sort_order': "b",
    },
}

# Define a sort order so that method for listing methods appear in a fixed sort order before any endpoint specific
# parameters
SORT_ORDER = {
    "after": "1",
    "filter": "2",
    "order": "3",
    "limit": "4",
    "max_results": "5",
    "page_size": "6",
    "include": "7",
}

# Map from Swagger Types / Formats to Foundation field types
SWAGGER_FIELD_MAP = {
    # Swagger types
    "array": "ListField",
    "boolean": "BooleanField",
    "integer": "IntegerField",
    "number": "FloatField",
    "object": "DictField",
    "file": "FileField",
    "string": "StringField",
    # Swagger formats (specialisation of types)
    "byte": "BinaryField",
    "binary": "BinaryField",
    "date-time": "DateTimeField",
    "date": "DateField",
    # Custom filter field is stored as a dictionary
    "filter": "DictField",
}

# Map from Swagger Types / Formats to native Python types
SWAGGER_TYPE_MAP = {
    # Swagger types
    "array": "list",
    "boolean": "bool",
    "integer": "int",
    "number": "float",
    "object": "dict",
    "string": "str",
    "file": "file",
    # Swagger formats (specialisation of types)
    "byte": "bytes",
    "binary": "bytes",
    "date-time": "datetime",
    "date": "date",
    # Custom filter field is used the standard API filter builder
    "filter": "mbed_cloud.client.api_filter.ApiFilter",
}


def map_python_field_types(fields):
    """Add Python types and Foundation field types to definition file."""
    for field in fields:
        swagger_type = field.get("type")
        swagger_format = field.get("format")
        field["python_type"] = SWAGGER_TYPE_MAP.get(swagger_format) or SWAGGER_TYPE_MAP.get(swagger_type)
        field["python_field"] = SWAGGER_FIELD_MAP.get(swagger_format) or SWAGGER_FIELD_MAP.get(swagger_type)


@functools.lru_cache()
def to_pascal_case(string):
    """Convert from snake_case to PascalCase

    Using the standard library `title` doesn't help as it changes everything after the first letter to lowercase, we
    want the following:
    - API -> API
    - api_key -> ApiKey
    - user -> User
    - paginated_response(account) -> PaginatedResponse(Account)

    :param str string: String to reformat.
    :returns: Reformatted string.
    :rtype: str
    """
    string = string.replace(" ", "_")
    string = string.replace("__", "_")
    string = string.replace("(", "(_")
    return string and "".join(n[0].upper() + n[1:] for n in string.split("_") if n)


@functools.lru_cache()
def to_snake_case(string):
    """Converts string to snake_case

    we don't use title because that forces lowercase for the word, whereas we want:
    PSK -> psk
    api key -> api_key
    content-length -> content_length
    user -> user
    """
    return re.sub("[ -]", "_", string).lower()


def to_singular_name(name):
    """Convert to snake case and remove and trailing `s` if present"""
    return to_snake_case(name).rstrip('s')


def sort_parg_kwarg(items):
    """Very specific sort ordering for ensuring pargs, kwargs are in the correct order"""
    return sorted(items, key=lambda x: not bool(x.get('required')))


class TemplateRenderer(object):
    """Foundation Interface Template Renderer for jinja2"""

    def __init__(self, output_root_dir):
        """Setup the jinja2 environment

        :param str output_root_dir: Root directory in which to write the Foundation interface.
        """
        self.output_root_dir = output_root_dir

        self.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
        self.jinja_env.filters['repr'] = repr
        self.jinja_env.filters['pargs_kwargs'] = sort_parg_kwarg
        self.jinja_env.filters.update(dict(
            repr=repr,
            sort_parg_kwarg=sort_parg_kwarg,
            to_snake=to_snake_case,
            to_pascal=to_pascal_case,
            to_singular_name=to_singular_name,
        ))

    def render_template(self, template_filename, group="group", entity="entity", template_data=None):
        """Render one or more jinja2 templates.

        The output filename is relative to the `output_root_dir` defined in the class instance but is also defined by
        the `template_filename`. The `template_filename` should be interspersed with `.` to indicate subdirectories.

        Two place holders are also supported in the template filename:
        - `group`: which will be replaced by the `group` parameter
        - `entity`: which will be replaced by the `entity` parameter

        :param str template_filename: name of template to render, this also defines the output path and filename.
        :param str group: This should be supplied when the template filename contains `group` .
        :param str entity: This should be supplied when the template filename contains `entity`.
        :param dict template_data: Data to pass to the template.
        """
        template = self.jinja_env.get_template(template_filename)

        # Remove template extension (we'll append .py later).
        output_path = template_filename.replace(".jinja2", "")

        # Covert the template filename to a path (which will be relative to the output_root_dir).
        output_path = output_path.replace(".", os.path.sep)

        # If `group` or `entity` exist in the path name replace them with the provided group and entity parameters
        output_path = output_path.replace("group", to_snake_case(group))
        output_path = output_path.replace("entity", to_snake_case(entity))

        # Combine the root directory with the directory defined by the template filename
        output_path = os.path.join(self.output_root_dir, output_path) + ".py"

        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            logger.info("Creating subdirectory '%s'", output_dir)
            os.makedirs(output_dir)

        logger.info("Rendering template from '%s' to '%s'", template_filename, output_path)
        rendered = template.render(template_data)
        with open(output_path, "w") as output_fh:
            output_fh.write(rendered)


def render_foundation_sdk(python_sdk_def_dict, output_dir):
    """Render the Foundation interface using the jinja templates

    :param dict python_sdk_def_dict: SDK definitions dictionary post processed for Python
    :param str output_dir: Directory in which the SDK generation should be written.
    """
    renderer = TemplateRenderer(output_dir)

    # Create a python file for each entity
    for entity in python_sdk_def_dict.get("entities", []):
        renderer.render_template("entities.group.entity.jinja2",
                                 group=entity['group_id'],
                                 entity=entity['_key'],
                                 template_data={'entities': [entity]})

    # Create a init file for each group of entities
    for group in python_sdk_def_dict.get("groups", []):
        renderer.render_template("entities.group.__init__.jinja2", group=group['_key'], template_data=group)

    # Create a init file at the group level
    renderer.render_template("entities.__init__.jinja2", template_data=python_sdk_def_dict)

    # Create a init file to allow an entity to be imported without defining the group
    renderer.render_template("__init__.jinja2", template_data=python_sdk_def_dict)

    # Collect the enum definitions in a list per group
    enum_data = defaultdict(list)
    for enum in python_sdk_def_dict.get("enums", []):
        enum_data[enum['group_id']].append(enum)

    # Create an enum definition file for each group of entities
    for group, enum_list in enum_data.items():
        renderer.render_template("entities.group.enums.jinja2", group=group, template_data={"enums": enum_list})

    # Create a init file to allow an enum to be imported without defining the group
    renderer.render_template("enums.__init__.jinja2", template_data={"enums": enum_data})

    # Create the factory which is used by the SDK instance to create entity instances
    renderer.render_template("entities.entity_factory.jinja2", template_data=python_sdk_def_dict)


def count_param_in(fields):
    """We need to know whether to even render any given 'in' parameter group, and to do this we have to count them...

    :param fields:
    :return:
    """
    params_in = {}
    for field in fields:
        field_in = field.get("in")
        # If the field `in` is defined then add to the parameter request
        # otherwise it isn't used in the API request. For example a custom
        # field will not have an `in` defined.
        if field_in:
            is_file = field.get("type") == "file"
            if is_file:
                field_in = "stream"
            params_in.setdefault(field_in, 0)
            params_in[field_in] += 1
    return params_in


def add_required_parameters(method, parameters):
    """Add any missing parameters to the method definition.

    If the parameter is not present then add the definition, otherwise leave the existing definition (along with the
    documentation) unchanged.

    :param method: The method to which to add the parameters.
    :param parameters: The required parameters.
    """
    # Deepcopy the parameters so any later changes to not impact the base definition.
    required_parameters = copy.deepcopy(parameters)
    # Fill in any missing list parameters so there is a consistent interface
    required_fields = list(required_parameters.keys())
    for field in method["fields"]:
        # If the field is already present it can be removed from the list
        if field["_key"] in required_fields:
            required_fields.remove(field["_key"])
    # If there are any required fields which were missing, add in a standard definition
    for required_field in required_fields:
        method["fields"].append(required_parameters[required_field])
    # Sort the list in a predefined sort order so common parameters come first followed by endpoint specific parameters
    method["fields"].sort(key=lambda field: SORT_ORDER.get(field["_key"], field["_key"]))


def create_filter_table(x_filter):
    """Render the filter table for insertion into the documentation

    It is difficult to render the table with variable field lengths as the table formatting has strict requirements.

    :param x_filter: The x_filter definition from the method.
    """
    field_column_title = "Field"
    # Find the maximum length of the field names in this table
    field_name_max_length = max([len(field_name) for field_name in x_filter.keys()] + [len(field_column_title)])
    # Find the maximum length of the filter operators in this table
    operator_max_length = max([len(filter_operator) for filter_operator in SUPPORTED_FILTER_OPERATORS])
    # How many columuns are there for filter operators
    num_supported_filters = len(SUPPORTED_FILTER_OPERATORS)

    row_separator = "+-%s-+" % ("-" * field_name_max_length)
    row_separator += ("-%s-+" % ("-" * operator_max_length) * num_supported_filters)
    row_separator += "\n"

    title_separator = "+=%s=+" % ("=" * field_name_max_length)
    title_separator += ("=%s=+" % ("=" * operator_max_length) * num_supported_filters)
    title_separator += "\n"

    title_row = "| %-*s |" % (field_name_max_length, field_column_title)
    title_row += "".join([" %-*s |" % (operator_max_length, operator) for operator in SUPPORTED_FILTER_OPERATORS])
    title_row += "\n"

    # Table heading
    filter_table = row_separator
    filter_table += title_row
    filter_table += title_separator

    for field_name, field_filters in x_filter.items():
        field_row = "| %-*s |" % (field_name_max_length, field_name)
        for supported_filter_operator in SUPPORTED_FILTER_OPERATORS:
            if supported_filter_operator in field_filters:
                field_row += " %-*s |" % (operator_max_length, "Y")
            else:
                field_row += " %-*s |" % (operator_max_length, " ")
        filter_table += field_row + "\n"
        filter_table += row_separator

    return filter_table


def create_custom_methods(entity, method):
    """Create paginator methods for iterating over list resources

    There is a public facing iterator method and a private method with makes the API inside a paginator. These both
    need to be defined from the base resource description.

    The custom method is currently called 'paginate'

    :param entity: The entity being processed, this will be modified if a paginator is found.
    :param method: The current method being processed.
    """
    if method.get("pagination"):
        internal_paginator = copy.deepcopy(method)
        internal_paginator["private_method"] = True
        internal_paginator["_key"] = f"paginate_{method['_key']}"
        internal_paginator["internal_paginator_method"] = True
        method["custom_method"] = "paginate"
        method["paginate_target"] = internal_paginator["_key"]
        method["public_paginator_method"] = True

        add_required_parameters(internal_paginator, PRIVATE_PAGINATOR_PARAMETERS)

        # Rename the API `limit` to `page_size` and drop `after`
        adjusted_fields = []
        for field in method["fields"]:
            field_name = field["_key"]
            if field_name == "after":
                continue
            if field_name == "limit":
                new_field = {}
                for key, value in field.items():
                    if value == "limit":
                        value = "page_size"
                    new_field[key] = value
                adjusted_fields.append(new_field)
            else:
                adjusted_fields.append(field)
        method["fields"] = adjusted_fields
        add_required_parameters(method, PUBLIC_PAGINATOR_PARAMETERS)

        x_filter = method.get("x_filter")
        if x_filter:
            method["x_filter_table"] = create_filter_table(x_filter)
            # Replace the "not supported" description for the filter field if x_filter is defined
            for field in method["fields"]:
                if field["_key"] == "filter":
                    field["description"] = "An optional filter to apply when listing entities, please see the above " \
                                            "**API Filters** table for supported filters."

        entity["methods"].append(internal_paginator)


def post_process_definition_file(sdk_def_filename):
    """Post-process SDK Definition file to add Python specific information.

    :param str sdk_def_filename: Path to SDK Definition file.
    :returns: Dictionary containing modified SDK Definitions
    :rtype: dict
    """
    with open(sdk_def_filename, "r") as sdk_def_file_handle:
        # Open the SDK Definition file and load the YAML
        sdk_gen_dict = yaml.load(sdk_def_file_handle)
        # The SDK generation file is organised around SDK entities
        for entity in sdk_gen_dict["entities"]:
            map_python_field_types(entity["fields"])

            # Convert a reference to an SDK Entity to a Python code reference
            # devices.device.list -> mbed_cloud.foundation.entities.devices.device.Device.list
            for field in entity["fields"]:
                foundation_reference = field.get("foundation_reference")
                if foundation_reference:
                    reference_segments = foundation_reference.split(".")
                    # E.g. mbed_cloud.foundation.entities.devices
                    python_reference = "mbed_cloud.foundation.entities." + to_snake_case(reference_segments[0])
                    if len(reference_segments) > 1:
                        # E.g. mbed_cloud.foundation.entities.devices.device.Device
                        python_reference += ".%s.%s" %(to_snake_case(reference_segments[1]), to_pascal_case(reference_segments[1]))
                    if len(reference_segments) > 2:
                        # E.g. mbed_cloud.foundation.entities.devices.device.Device.list
                        python_reference += ".%s" % to_snake_case(reference_segments[2])
                    field["foundation_reference"] = python_reference

            for method in entity["methods"][:]:
                map_python_field_types(method["fields"])
                method["python_params_in"] = count_param_in(method["fields"])
                [f.setdefault("default", None) for f in method["fields"]]
                create_custom_methods(entity, method)
                # Convert the return type to a Python type or assume it is an entity if not known
                return_type = method["return_type"]
                method["python_return_type"] = SWAGGER_TYPE_MAP.get(return_type, to_pascal_case(return_type))

    return sdk_gen_dict


def write_intermediate_file(output_filename, python_sdk_def_dict):
    """Write the post processed file to defined location as YAML.

    :param str output_filename: Name of file to which to write the file.
    :param dict python_sdk_def_dict: SDK definitions dictionary post processed for Python
    """
    logger.info("Writing post processed file to '%s'.", output_filename)
    with open(output_filename, "w+") as output_file_handle:
        yaml.safe_dump(python_sdk_def_dict, output_file_handle, default_flow_style=False)


def main():
    """Argument handling and main entry point."""
    parser = argparse.ArgumentParser(description="""
        Generate Foundation SDK code from the SDK Foundation Definition file (required Python 3).
        """)

    parser.add_argument("sdk_def_file", type=str, metavar="SDK Foundation Definition File",
                        help='SDK Foundation Definition filename and path e.g. sdk_foundation_definition.yaml')
    parser.add_argument("-o", "--output-dir", type=str, default=".",
                        help="The output directory, generated source files will be written to this directory")
    parser.add_argument("-p", "--python-sdk-def-file", type=str,
                        help="Provide an file path to save the post processed Python specific definition file as YAML.")
    parser.add_argument("--clean-output-dir", action='store_true',
                        help="Delete all files in the entity subdirectory to ensure old files are purged.")
    parser.add_argument("-v", "--verbose", action='count', default=0,
                        help="Logging verbosity, by default only errors are logged.")

    if sys.version_info[0] < 3:
        raise parser.error("This script must be executed using Python 3")

    arguments = parser.parse_args()

    if arguments.verbose > 2:
        logger.setLevel(logging.DEBUG)
    elif arguments.verbose > 1:
        logger.setLevel(logging.INFO)
    elif arguments.verbose > 0:
        logger.setLevel(logging.WARNING)
    else:
        logger.setLevel(logging.ERROR)

    if arguments.clean_output_dir and arguments.output_dir == ".":
        raise parser.error("The current directory cannot be cleaned, please specify a different output directory.")

    # Clean output directory if requested and it is needed
    entity_dir = os.path.join(arguments.output_dir, "entities")
    if arguments.clean_output_dir and os.path.exists(entity_dir):
        logger.info("Removing directory '%s'", entity_dir)
        shutil.rmtree(entity_dir)

    # Process the generic SDK definition file to create the specialised Python specifiv definition file
    python_sdk_def_dict = post_process_definition_file(arguments.sdk_def_file)

    if arguments.python_sdk_def_file:
        write_intermediate_file(arguments.python_sdk_def_file, python_sdk_def_dict)

    render_foundation_sdk(python_sdk_def_dict, arguments.output_dir)

    logger.info("Reformatting generated source files in directory '%s'", arguments.output_dir)
    subprocess.run(['black', arguments.output_dir, '--fast', '--line-length=92'])

    return 0


if __name__ == "__main__":
    sys.exit(main())
