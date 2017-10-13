#!/usr/bin/python

# ---------------------------------------------------------------------------
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
import os

from setuptools import find_packages
from setuptools import setup
from mbed_cloud.__version__ import VERSION

# To install, run:
# pip install .

# To install in dev mode, run:
# pip install .[dev]

# Render the README in reST
# http://stackoverflow.com/a/26737672
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace('\r', '')
except(OSError, IOError, ImportError):
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fh:
        long_description = fh.readlines()

NAME = 'mbed-cloud-sdk'

with open(os.path.join(os.path.dirname(__file__), 'dependencies.txt')) as fh:
    dependencies = fh.readlines()

with open(os.path.join(os.path.dirname(__file__), 'requirements.dev.txt')) as fh:
    dev_requirements = fh.readlines()

setup(
    name=NAME,
    version=VERSION,
    description="Mbed Cloud Python SDK",
    author="Arkadiusz Zaluski, Herman Schistad",
    author_email="arkadiusz.zaluski@arm.com",
    url="https://github.com/ARMmbed/mbed-cloud-sdk-python",
    install_requires=dependencies,
    extras_require={
        'dev': dev_requirements
    },
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description
)
