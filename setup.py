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

# To install, run:
# pip install .

# To install in dev mode, run:
# pip install .[dev]

import os

from setuptools import find_packages
from setuptools import setup

NAME = 'mbed-cloud-sdk'
__version__ = None

repository_dir = os.path.dirname(__file__)

# single source for version information without side effects
with open(os.path.join(repository_dir, 'src', 'mbed_cloud', '_version.py')) as fh:
    exec(fh.read())

# Render the README in reST
# http://stackoverflow.com/a/26737672
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace('\r', '')
except(OSError, IOError, ImportError):
    with open(os.path.join(repository_dir, 'README.md')) as fh:
        long_description = fh.read()

with open(os.path.join(repository_dir, 'dependencies.txt')) as fh:
    dependencies = fh.readlines()

with open(os.path.join(repository_dir, 'requirements.dev.txt')) as fh:
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
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    long_description=long_description,
    python_requires='>=2.7.10, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.0, !=3.4.1, !=3.4.2, <4',
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    )
)
