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
from operator import itemgetter
import jinja2

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

# The required parameters for a paginator
PAGINATOR_PARAMETERS = {
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
    # Swagger formats (specialisation of types)
    "string": "StringField",
    "date-time": "DateTimeField",
    "date": "DateField",
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
    "date-time": "datetime",
    "date": "date",
}


def map_python_field_types(fields):
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
def to_snake_case(name):
    """Converts string to snake_case

    we don't use title because that forces lowercase for the word, whereas we want:
    PSK -> psk
    api key -> api_key
    user -> user
    """
    return name.replace(" ", "_").lower()


def sort_parg_kwarg(items):
    """Very specific sort ordering for ensuring pargs, kwargs are in the correct order"""
    return sorted(items, key=lambda x: not bool(x.get('required')))


class GenModule:
    """Container for 'modules' (aka groups from the intermediate file)"""

    def __init__(self, name=None, data=None, root=None, target=None):
        """Init

        :param name: name of the module
        :param data: data to render using template
        :param root: file path containing this module
        """
        self.name = name
        self.data = data or {}
        self.root = root
        self.target = target


class FileMap:
    """Container for matching rendering of templates into directories

    Includes iteration over a list of GenModules
    """

    def __init__(self, jinja_env, output_dir, template, target=None, per_module=None):
        """Init

        :param jinja_env:
        :param output_dir:
        :param template:
        :param target:
        :param per_module:
        """
        self.jinja_env = jinja_env
        self.output_dir = output_dir
        self.target = target or template.replace('jinja2', 'py')
        self.template = self.jinja_env.get_template(template)
        self.per_module = per_module or [GenModule()]

    def run(self, config):
        """Use self.template to write a file in each GenModule directory

        using self.output_dir as a starting point
        and self.target as the name of the destination file
        """
        for gen_module in self.per_module:
            output_dir = os.path.join(*[
                p for p in (self.output_dir, gen_module.root, gen_module.name) if p
            ])

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            output = os.path.join(output_dir, gen_module.target or self.target)

            logger.info("Rendering '%s' to '%s'", self.template, output)

            rendered = self.template.render(gen_module.data or config)

            with open(output, 'w') as fh:
                fh.write(rendered)


def render_foundation_sdk(python_sdk_def_dict, output_dir):
    """Render the Foundation SDK using the jinja templates

    :param dict python_sdk_def_dict: SDK definitions dictionary post processed for Python
    :param str output_dir: Directory in which the SDK generation should be written.
    :return:
    """

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR)
    )
    jinja_env.filters['repr'] = repr
    jinja_env.filters['pargs_kwargs'] = sort_parg_kwarg
    jinja_env.filters.update(dict(
        repr=repr,
        sort_parg_kwarg=sort_parg_kwarg,
        to_snake=to_snake_case,
        to_pascal=to_pascal_case,
    ))

    generation_root = '_modules'
    generation_dir = os.path.join(output_dir, generation_root)

    sub_modules = [
        GenModule(name=to_snake_case(group['_key']), root=generation_root, data=group) for group in python_sdk_def_dict.get('groups')
    ]
    entity_modules = [
        GenModule(name=None, root=os.path.join(generation_root, to_snake_case(e['group_id'])), data=e) for e in python_sdk_def_dict.get('entities')
    ]
    src_entity_modules = [
        GenModule(name=None, root=os.path.join(generation_root, to_snake_case(e['group_id'])), data={'entities': [e]}, target=to_snake_case(e['_key']) + '.py') for e in python_sdk_def_dict.get('entities')
    ]
    enum_modules = [
        GenModule(
            # name='enums',
            root=os.path.join(generation_root, to_snake_case(g['_key'])),
            data=dict(
              enums=[e for e in python_sdk_def_dict.get('enums') if e['group_id'] == g['_key']]
            )
        ) for g in python_sdk_def_dict.get('groups')
    ]

    enum_dir = os.path.join(output_dir, 'enums')
    entities_dir = os.path.join(output_dir, 'entities')

    file_maps = [
        FileMap(jinja_env, generation_dir, 'factory.jinja2', '_factory.py'),
        FileMap(jinja_env, enum_dir, 'enums__init__.jinja2', '__init__.py'),
        FileMap(jinja_env, entities_dir, 'entities__init__.jinja2', '__init__.py'),

        # layed out in the module structure
        FileMap(jinja_env, output_dir, 'entity.jinja2', per_module=src_entity_modules),
        FileMap(jinja_env, output_dir, 'enum.jinja2', 'enums.py', per_module=enum_modules),
        FileMap(jinja_env, output_dir, '__init__.jinja2', per_module=sub_modules),
        FileMap(jinja_env, output_dir, '__init__.jinja2', per_module=entity_modules),
    ]

    for file_map in file_maps:
        file_map.run(python_sdk_def_dict)


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

        # Fill in any missing list parameters so there is a consistent interface
        required_fields = list(PAGINATOR_PARAMETERS.keys())
        for field in private["fields"]:
            # If the field is already present it can be removed from the list
            if field["_key"] in required_fields:
                required_fields.remove(field["_key"])
        # If there are any required fields add in a standard definition
        for required_field in required_fields:
            private["fields"].append(PAGINATOR_PARAMETERS[required_field])
        # Sort the list by the name of the field so the parameter order is consistent
        if required_fields:
            private["fields"].sort(key=itemgetter("_key"))
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
                        help="Delete all files in the output subdirectories before writing files.")
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
    if arguments.clean_output_dir and os.path.exists(arguments.output_dir):
        logger.info("Removing directory '%s'", arguments.output_dir)
        shutil.rmtree(arguments.output_dir)
    # Create output directory if it doesn't exist
    if not os.path.exists(arguments.output_dir):
        logger.info("Creating directory '%s'", arguments.output_dir)
        os.makedirs(arguments.output_dir)

    # Process the generic SDK definition file to create the specialised Python specifiv definition file
    python_sdk_def_dict = post_process_definition_file(arguments.sdk_def_file)

    if arguments.python_sdk_def_file:
        write_intermediate_file(arguments.python_sdk_def_file, python_sdk_def_dict)

    render_foundation_sdk(python_sdk_def_dict, arguments.output_dir)

    logger.info("Reformatting generated source files in directory '%s'", arguments.output_dir)
    subprocess.run(['black', arguments.output_dir, '--fast'])

    return 0


if __name__ == "__main__":
    sys.exit(main())
