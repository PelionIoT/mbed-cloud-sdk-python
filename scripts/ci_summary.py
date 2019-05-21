# --------------------------------------------------------------------------
# Pelion Device Management Python SDK
# (C) COPYRIGHT 2017, 2019 Arm Limited
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
"""Collects results from CI run"""
import argparse
import json
import traceback
from xml.etree import ElementTree


def main():
    """Collects results from CI run"""
    source_files = (
        ('integration', r'results/results.xml'),
        ('unittests', r'results/unittests.xml'),
        ('coverage', r'results/coverage.xml')
    )

    parsed = {k: ElementTree.parse(v).getroot().attrib for k, v in source_files}

    with open(r'results/summary.json', 'w') as fh:
        json.dump(parsed, fh)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--noblock', action='store_true', help='always passes')
    opts = parser.parse_args()
    try:
        main()
    except Exception:
        if opts.noblock:
            traceback.print_exc()
        else:
            raise
