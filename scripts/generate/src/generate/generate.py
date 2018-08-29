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

import logging
import os
import subprocess
import operator
import pathlib

import jinja2
import yaml

from generate.cli import get_cli

_LOG = logging.getLogger(__file__)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


class GenModule:
    def __init__(self, name=None, data=None, root=None):
        self.name = name
        self.data = data or {}
        self.root = root


class FileMap:
    def __init__(self, jinja_env, output_dir, template, target=None, per_module=None):
        self.jinja_env = jinja_env
        self.output_dir = output_dir
        self.target = target or template.replace('jinja2', 'py')
        self.template = self.jinja_env.get_template(template)
        self.per_module = per_module or [GenModule()]

    def run(self, config):
        for gen_module in self.per_module:
            _LOG.info('rendering %s', self.template)
            module_config = {'gen_module': gen_module.data}
            module_config.update(config)
            rendered = self.template.render(module_config)
            output_dir = os.path.join(*[p for p in (self.output_dir, gen_module.root, gen_module.name) if p])

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            output = os.path.join(output_dir, self.target)
            with open(output, 'w') as fh:
                _LOG.info('writing %s', output)
                fh.write(rendered)


def sort_parg_kwarg(items):
    return sorted(items, key=lambda x: not bool(x.get('required')))


def main(input_file, output_dir):
    _LOG.info('loading %s', input_file)
    with open(input_file, encoding='utf8') as fh:
        config = yaml.safe_load(fh)

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR)
    )
    jinja_env.filters['repr'] = repr
    jinja_env.filters['pargs_kwargs'] = sort_parg_kwarg

    sub_modules = [
        GenModule(name=g['_key']['snake'], root='modules', data=g) for g in config.get('groups')
    ]

    common_dir = os.path.join(output_dir, 'common')

    file_maps = [
        FileMap(jinja_env, common_dir, 'entities.jinja2', '_entities.py'),
        FileMap(jinja_env, common_dir, 'enums.jinja2', '_enums.py'),
        FileMap(jinja_env, output_dir, '__init__.jinja2', per_module=sub_modules),
    ]

    for file_map in file_maps:
        file_map.run(config)

    # write a blank __init__
    _LOG.info('writing supplementary files')
    with open(os.path.join(output_dir, '__init__.py'), 'a'):
        pass
    with open(os.path.join(output_dir, 'modules', '__init__.py'), 'a'):
        pass

    _LOG.info('post-formatting %s', output_dir)
    subprocess.run(['black', output_dir])


def main_from_cli():
    """Generate the SDK

    example cmd from sdk top level directory:
    python -m generate --source=C:\coding\mbed-cloud-api-contract\out\sdk_generation_cache.yaml.python.yaml --output=src\mbed_cloud\sdk\common
    """
    args = get_cli()
    params = vars(args)
    verbosity = params.pop('verbosity')
    log_level = max(logging.WARNING - 10 * verbosity, 1)
    logging.basicConfig(level=log_level, format='%(module)s %(levelname)8s %(message)s')
    main(**params)


__name__ == '__main__' and main_from_cli()
