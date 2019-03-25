# ---------------------------------------------------------------------------
# Pelion Device Management Python SDK
# (C) COPYRIGHT 2017,2019 Arm Limited
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

NAME = 'mbed-cloud-sdk'
__version__ = None

repository_dir = os.path.dirname(__file__)

# single source for project version information without side effects
with open(os.path.join(repository_dir, 'src', 'mbed_cloud', '_version.py')) as fh:
    exec(fh.read())

# .rst readme needed for pypi
with open(os.path.join(repository_dir, 'README.rst')) as fh:
    long_description = fh.read()

# some of the dependencies are inherited from swagger-codegen
# https://github.com/swagger-api/swagger-codegen/blob/master/modules/swagger-codegen/src/main/resources/python/setup.mustache#L18
with open(os.path.join(repository_dir, 'requirements.txt')) as fh:
    requirements = fh.readlines()

setup(
    author="Arkadiusz Zaluski, David Hyman, Herman Schistad",
    author_email="support@mbed.com",
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Object Brokering',
    ),
    description="Pelion Device Management Python SDK",
    include_package_data=True,
    install_requires=requirements,
    license='Apache 2.0',
    long_description=long_description,
    name=NAME,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires='>=2.7.10, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.0, !=3.4.1, !=3.4.2, <4',
    url="https://github.com/ARMmbed/mbed-cloud-sdk-python",
    version=__version__,
)
