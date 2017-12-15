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
"""Collects results from CI run"""
import json
import os
from xml.etree import ElementTree


def main():
    """Collects results from CI run"""
    source_files = (
        ('integration', r'results/rpc/results.xml'),
        ('unittests', r'results/unittests.xml'),
        ('coverage', r'results/coverage.xml')
    )

    parsed = {k: ElementTree.parse(v).getroot().attrib for k, v in source_files}

    with open(os.path.expanduser('results/summary.json'), 'w') as fh:
        json.dump(parsed, fh)


if __name__ == '__main__':
    main()
