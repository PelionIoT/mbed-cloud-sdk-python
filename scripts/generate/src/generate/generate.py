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

import chevron
import yaml

from generate.cli import get_cli

_LOG = logging.getLogger(__file__)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


def main(input_file, output_dir):
    with open(input_file, encoding='utf8') as fh:
        config = yaml.safe_load(fh)

    template = os.path.join(TEMPLATE_DIR, 'api.mustache')
    with open(template) as tpl:
        _LOG.info('rendering %s', template)
        rendered = chevron.render(tpl, config)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output = os.path.join(output_dir, 'api.py')
    with open(output, 'w') as fh:
        _LOG.info('writing %s', output)
        fh.write(rendered)


def main_from_cli():
    """Generate the SDK
    """
    args = get_cli()
    params = vars(args)
    verbosity = params.pop('verbosity')
    log_level = max(logging.WARNING - 10 * verbosity, 1)
    logging.basicConfig(level=log_level, format='%(module)s %(levelname)8s %(message)s')
    main(**params)


__name__ == '__main__' and main_from_cli()
