#!/usr/bin/env python3
"""Generate Foundation SDK code from the SDK Foundation Definition file."""

import sys
import argparse
import os
import shutil
import yaml
import logging
import copy
from collections import defaultdict
from jinja2 import Environment, PackageLoader, select_autoescape

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

env = Environment(
    loader=PackageLoader('render_sdk', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Dictionary to temporarily override fields that we have found may be null
NULLABLE_FIELDS = {
    # "Entity": ["field_name1", ""field_name2"]
    "User": ["address", "password", "phone_number", "username", "login_profiles"],
    "UserInvitation": ["login_profiles"],
}

MARSHMALLOW_STRING = "fields.String"
MARSHMALLOW_DATETIME = "fields.DateTime"
MARSHMALLOW_DATE = "fields.Date"
MARSHMALLOW_INTEGER = "fields.Integer"
MARSHMALLOW_NUMBER = "fields.Float"
MARSHMALLOW_BOOL = "fields.Boolean"
MARSHMALLOW_LIST = "fields.List"
MARSHMALLOW_DICT = "fields.Dict"
MARSHMALLOW_NESTED = "fields.Nested"

SCHEMA_FOLDER = "_schemas"
DEFINITIONS_FOLDER = "_definitions"
ENTITY_TESTS_FOLDER = "_entity_tests"


swagger_field_map = {
    # types...
    "array": "ListField",
    "boolean": "BooleanField",
    "integer": "IntegerField",
    "number": "FloatField",
    "object": "DictField",
    "string": "StringField",
    "date-time": "DateTimeField",
    "date": "DateField",
    "file": "FileField",
}
swagger_type_map = {
    # formats ...
    "array": "list",
    "boolean": "bool",
    "integer": "int",
    "number": "float",
    "object": "dict",
    "string": "str",
    "date-time": "datetime",
    "date": "date",
    "file": "file",
}


# Lookup table for marshmallow types based on OpenAPI types and formats
PYTHON_TYPE_LOOKUP = {
    "string": {
        "base_type": MARSHMALLOW_STRING,
        "formats": {
            "date-time": MARSHMALLOW_DATETIME,
            "date": MARSHMALLOW_DATE,
            "byte": MARSHMALLOW_STRING,
            "binary": MARSHMALLOW_STRING,
            "password": MARSHMALLOW_STRING,
        }
    },
    "integer": {
        "base_type": MARSHMALLOW_INTEGER,
        "formats": {
            "int32": MARSHMALLOW_INTEGER,
            "int64": MARSHMALLOW_INTEGER,
        }
    },
    "number": {
        "base_type": MARSHMALLOW_NUMBER,
        "formats": {
            "float": MARSHMALLOW_NUMBER,
            "double": MARSHMALLOW_NUMBER,
        }
    },
    "boolean": {
        "base_type": MARSHMALLOW_BOOL,
        "formats": {}
    },
    "array": {
        "base_type": MARSHMALLOW_LIST,
        "formats": {}
    },
    "object": {
        "base_type": MARSHMALLOW_DICT,
        "formats": {}
    },
}


def to_pascalcase(string):
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


# def lookup_type(entity_name, field_name, field):
#     """Lookup marshmallow type from swagger type and format information.
#
#     :param str entity_name: Name of SDK entity.
#     :param str field_name: Name of field in SDK entity.
#     :param str field: Field defintion from the API.
#     :returns: Marshmallow schema type.
#     :rtype: str
#     """
#     open_api_type = field.get("type")
#     open_api_format = field.get("format")
#
#     try:
#         marshmallow_info = MARSHMALLOW_TYPE_LOOKUP[open_api_type]
#     except KeyError:
#         marshmallow_type = None
#         logger.error("%s:%s - Marshmallow type has not been defined for OpenAPI type '%s'.", entity_name, field_name,
#                      open_api_type)
#     else:
#         marshmallow_type = marshmallow_info["base_type"]
#         if open_api_format is not None:
#             try:
#                 marshmallow_type = marshmallow_info["formats"][open_api_format]
#             except KeyError:
#                 logger.warning("%s:%s - Unexpected OpenAPI format '%s', defaulting to '%s'.", entity_name, field_name,
#                                open_api_format, marshmallow_type)
#     return marshmallow_type


def map_python_field_types(fields):
    for field in fields:
        kind = field.get("type")
        format = field.get("format")
        field["python_type"] = swagger_type_map.get(format) or swagger_type_map.get(
            kind
        )
        field["python_field"] = swagger_field_map.get(
            format
        ) or swagger_field_map.get(kind)


def count_param_in(fields):
    """
    we need to know whether to even render any given 'in' parameter group,
    and to do this we have to count them...
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


def paginators_as_custom_methods(entity, method):
    """
    Sets up a custom method whenever we come across a paginator

    The custom method is currently called 'paginate'
    :param entity:
    :param method:
    :return:
    """

    paginated = method.get("pagination")
    if paginated:
        private = copy.deepcopy(method)
        private["private_method"] = True
        private["_key"] = f"paginate_{method['_key']}"
        method["custom_method"] = "paginate"
        method["paginate_target"] = private["_key"]
        entity["methods"].append(private)


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
            for method in entity["methods"][:]:
                map_python_field_types(method["fields"])
                method["python_params_in"] = count_param_in(method["fields"])
                [f.setdefault("default", None) for f in method["fields"]]
                paginators_as_custom_methods(entity, method)
                # Convert the return type to a Python type or assume it is an entity if not known
                return_type = method["return_type"]
                method["python_return_type"] = swagger_type_map.get(return_type, to_pascalcase(return_type))

    return sdk_gen_dict


# def write_entity_files(output_dir, definition_info, template):
#     """Write definition files to defined output directory.
#
#     - <output_dir>/
#       - <group>.py - class per entity
#
#     :param str output_dir: Output directory to which to write the Marshmallow schemas.
#     :param str definition_info: definition information created from SDK definition.
#     :param str template: jinja template to render
#     """
#     logger.info("Loading template '%s'.", template)
#     template = env.get_template(template)
#
#     for group, entities in definition_info.items():
#         output_filename = os.path.join(output_dir, group) + ".py"
#
#         rendered = template.render(group=group, entities=entities)
#
#         logger.info("Writing to '%s'.", output_filename)
#         with open(output_filename, "w+") as output_file_handle:
#             output_file_handle.write(rendered)


def write_intermediate_file(output_filename, python_sdk_gen_dict):
    """Write the post processed file to defined location as YAML.

    - <output_dir>/
      - __init__.py

    :param str output_filename: Name of file to which to write the file.
    :param str python_sdk_gen_dict: SDK Generation post processed for Python
    """
    logger.info("Writing post processed file to '%s'.", output_filename)
    with open(output_filename, "w+") as output_file_handle:
        yaml.safe_dump(python_sdk_gen_dict, output_file_handle, default_flow_style=False)


def main():
    """Argument handling and main entry point."""
    parser = argparse.ArgumentParser(description="""
        Generate Foundation SDK code from the SDK Foundation Definition file.
        """)

    parser.add_argument("sdk_def_file", type=str, metavar="SDK Foundation Definition File",
                        help='SDK Foundation Definition filename and path e.g. sdk_foundation_definition.yaml')
    parser.add_argument("-o", "--output-dir", type=str, default=".",
                        help="The output directory, generated source files will be written to this directory")
    parser.add_argument("-p", "--python-sdk-def-file", type=str,
                        help="Provide an file path to save the post processed Python specific definition file as YAML.")
    parser.add_argument("--clean-output-dir", action='store_true',
                        help="Delete all files in the output subdirectories before writing files.")
    parser.add_argument("-v", "--verbose", action='count', default=0,
                        help="Logging verbosity, by default only errors are logged.")

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
    if arguments.clean_output_dir and os.path.exists(arguments.output_dir):
        logger.info("Removing directory '%s'", arguments.output_dir)
        shutil.rmtree(arguments.output_dir)
    # Create output directory if it doesn't exist
    if not os.path.exists(arguments.output_dir):
        logger.info("Creating directory '%s'", arguments.output_dir)
        os.makedirs(arguments.output_dir)

    # Process the generic SDK definition file to create the specialised Python specifiv definition file
    python_sdk_gen_dict = post_process_definition_file(arguments.sdk_def_file)

    if arguments.python_sdk_def_file:
        write_intermediate_file(arguments.python_sdk_def_file, python_sdk_gen_dict)

    # logger.info("Reformatting generated source files in directory '%s'", arguments.output_dir)
    # subprocess.run(['black', arguments.output_dir, '--fast'])

    return 0


if __name__ == "__main__":
    sys.exit(main())
