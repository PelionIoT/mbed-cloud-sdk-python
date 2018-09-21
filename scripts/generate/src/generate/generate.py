# --------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

"""Generates the Foundation API for the Python SDK

You'll be wanting to use Python 3 for this.
"""

import logging
import os
import subprocess

import jinja2
import yaml

from generate.cli import get_cli

_LOG = logging.getLogger(__file__)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


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
            _LOG.info('rendering %s', self.template)
            rendered = self.template.render(gen_module.data or config)

            output_dir = os.path.join(*[
                p for p in (self.output_dir, gen_module.root, gen_module.name) if p
            ])

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            output = os.path.join(output_dir, gen_module.target or self.target)
            with open(output, 'w') as fh:
                _LOG.info('writing %s', output)
                fh.write(rendered)


def sort_parg_kwarg(items):
    """Very specific sort ordering for ensuring pargs, kwargs are in the correct order"""
    return sorted(items, key=lambda x: not bool(x.get('required')))


def main(input_file, output_dir):
    """Bulk of the generation work

    :param input_file: The 'inter.yaml' intermediate yaml configuration / specification file
    :param output_dir: Directory to generate the SDK in to
    :return:
    """
    _LOG.info('loading %s', input_file)
    with open(input_file, encoding='utf8') as fh:
        config = yaml.safe_load(fh)

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR)
    )
    jinja_env.filters['repr'] = repr
    jinja_env.filters['pargs_kwargs'] = sort_parg_kwarg

    generation_root = '_modules'
    generation_dir = os.path.join(output_dir, generation_root)

    sub_modules = [
        GenModule(name=g['_key']['snake'], root=generation_root, data=g) for g in config.get('groups')
    ]
    entity_modules = [
        GenModule(name='entities', root=os.path.join(generation_root, e['group_id']['snake']), data=e['group_id']) for e in config.get('entities')
    ]
    src_entity_modules = [
        GenModule(name='entities', root=os.path.join(generation_root, e['group_id']['snake']), data={'entities': [e]}, target=e['_key']['snake']+'.py') for e in config.get('entities')
    ]
    enum_modules = [
        GenModule(
            # name='enums',
            root=os.path.join(generation_root, g['_key']['snake']),
            data=dict(
              enums=[e for e in config.get('enums') if e['group_id']['name']==g['_key']['name']]
            )
        ) for g in config.get('groups')
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
        file_map.run(config)

    _LOG.info('post-formatting %s', output_dir)
    subprocess.run(['black', output_dir, '--fast'])


def main_from_cli():
    r"""Generate the SDK

    example cmd from sdk top level directory:
    python -m generate
     --source=C:\coding\mbed-cloud-api-contract\out\sdk_generation_cache.yaml.python.yaml
     --output=src\mbed_cloud\sdk\common
    """
    args = get_cli()
    params = vars(args)
    verbosity = params.pop('verbosity')
    log_level = max(logging.WARNING - 10 * verbosity, 1)
    logging.basicConfig(level=log_level, format='%(module)s %(levelname)8s %(message)s')
    main(**params)


__name__ == '__main__' and main_from_cli()
